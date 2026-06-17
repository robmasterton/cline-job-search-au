#!/usr/bin/env python3
"""
linkedin-search — OPTIONAL LinkedIn job search CLI (Australian market).

⚠️  USE AT YOUR OWN RISK — READ THIS FIRST  ⚠️
LinkedIn's User Agreement prohibits automated access / scraping. This tool uses
LinkedIn's *guest* endpoints (the same ones logged-out users' browsers hit), with no
login and no API key, but automating them is still against LinkedIn's terms and can get
your IP rate-limited or temporarily blocked. It is DISABLED by default in /scrape and is
provided for personal, low-volume use only. Prefer SEEK (tools/seek-search), which is the
primary, supported source. If in doubt, don't use this — paste a LinkedIn posting into
/apply manually instead.

Endpoints (guest, no auth):
  search: /jobs-guest/jobs/api/seeMoreJobPostings/search   -> job cards (10/page)
  detail: /jobs-guest/jobs/api/jobPosting/<id>             -> full description

Usage:
  python3 linkedin_search.py --keywords "AI Engineer" --where "Australia" --pages 2
  python3 linkedin_search.py --keywords "Senior Full Stack" --where "Brisbane, Queensland, Australia" --remote
  python3 linkedin_search.py --detail https://www.linkedin.com/jobs/view/4417422377

Output: JSON array on stdout (default), or a human table with --table.
"""

import argparse
import json
import re
import sys
import time
from html import unescape
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

SEARCH = "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search"
DETAIL = "https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/"
VIEW = "https://www.linkedin.com/jobs/view/"
UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Safari/605.1.15"
)
PER_PAGE = 10
_TOS = (
    "[linkedin-search] NOTE: LinkedIn's terms prohibit automated access. This uses guest "
    "endpoints for personal, low-volume use only and may get your IP rate-limited. "
    "SEEK (tools/seek-search) is the primary, supported source."
)


def _get(url):
    req = Request(url, headers={"User-Agent": UA, "Accept": "text/html"})
    with urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", "replace")


def _clean(s):
    return re.sub(r"\s+", " ", unescape(re.sub(r"<[^>]+>", "", s or ""))).strip()


def extract_job_id(value):
    value = value.strip()
    if value.isdigit():
        return value
    m = re.search(r"urn:li:jobPosting:(\d+)", value) or re.search(r"/jobs/view/(?:[a-z0-9-]*?-)?(\d{6,})", value)
    return m.group(1) if m else None


def parse_cards(doc):
    rows = []
    for c in re.split(r"<li>", doc):
        tid = re.search(r"urn:li:jobPosting:(\d+)", c) or re.search(r"/jobs/view/[a-z0-9-]*?(\d{8,})", c)
        title = re.search(r"base-search-card__title[^>]*>(.*?)</h3>", c, re.S)
        if not (tid and title):
            continue
        comp = re.search(r"(?:hidden-nested-link|base-search-card__subtitle)[^>]*>\s*(?:<a[^>]*>)?(.*?)(?:</a>|</h4>)", c, re.S)
        loc = re.search(r"job-search-card__location[^>]*>(.*?)</span>", c, re.S)
        date = re.search(r'datetime="([^"]+)"', c)
        jid = tid.group(1)
        rows.append({
            "id": jid,
            "title": _clean(title.group(1)),
            "company": _clean(comp.group(1)) if comp else "",
            "location": _clean(loc.group(1)) if loc else "",
            "listing_date": date.group(1) if date else "",
            "url": VIEW + jid,
        })
    return rows


def search(keywords, where, pages, remote, days):
    seen, out = set(), []
    for page in range(pages):
        params = {"keywords": keywords, "location": where, "start": page * PER_PAGE}
        if remote:
            params["f_WT"] = 2          # remote
        if days:
            params["f_TPR"] = f"r{int(days) * 86400}"
        try:
            doc = _get(f"{SEARCH}?{urlencode(params)}")
        except HTTPError as e:
            print(f"[linkedin-search] HTTP {e.code} on page {page} (likely rate-limited)", file=sys.stderr)
            break
        except URLError as e:
            print(f"[linkedin-search] network error: {e.reason}", file=sys.stderr)
            break
        rows = parse_cards(doc)
        if not rows:
            break
        for r in rows:
            if r["id"] in seen:
                continue
            seen.add(r["id"])
            r["query"] = keywords
            out.append(r)
        time.sleep(1.0)  # be gentle — LinkedIn rate-limits aggressively
    return out


def fetch_detail(job_id):
    doc = _get(DETAIL + str(job_id))
    title = re.search(r"top-card-layout__title[^>]*>(.*?)</h2>", doc, re.S) or re.search(r"topcard__title[^>]*>(.*?)</h1>", doc, re.S)
    comp = re.search(r"topcard__org-name-link[^>]*>(.*?)</a>", doc, re.S) or re.search(r"topcard__flavor[^>]*>(.*?)</span>", doc, re.S)
    loc = re.search(r"topcard__flavor--bullet[^>]*>(.*?)</span>", doc, re.S)
    crit = dict(zip(
        [_clean(h) for h in re.findall(r"description__job-criteria-subheader[^>]*>(.*?)</h3>", doc, re.S)],
        [_clean(v) for v in re.findall(r"description__job-criteria-text[^>]*>(.*?)</span>", doc, re.S)],
    ))
    body = re.search(r"show-more-less-html__markup[^>]*>(.*?)</div>", doc, re.S)
    desc = _html_to_text(body.group(1)) if body else ""
    return {
        "id": str(job_id),
        "title": _clean(title.group(1)) if title else "",
        "company": _clean(comp.group(1)) if comp else "",
        "location": _clean(loc.group(1)) if loc else "",
        "seniority": crit.get("Seniority level", ""),
        "employment_type": crit.get("Employment type", ""),
        "job_function": crit.get("Job function", ""),
        "description": desc,
        "url": VIEW + str(job_id),
    }


def _html_to_text(h):
    t = re.sub(r"(?i)<\s*(br|/p|/li|/ul)\s*>", "\n", h)
    t = re.sub(r"(?i)<\s*li[^>]*>", "\n- ", t)
    t = unescape(re.sub(r"<[^>]+>", "", t))
    return re.sub(r"\n\s*\n\s*\n+", "\n\n", re.sub(r"[ \t]+", " ", t)).strip()


def main():
    ap = argparse.ArgumentParser(description="Search LinkedIn jobs (guest API). Use at your own risk — see header.")
    ap.add_argument("--keywords", help='Search terms, e.g. "AI Engineer"')
    ap.add_argument("--where", default="Australia", help='Location, e.g. "Australia", "Brisbane, Queensland, Australia"')
    ap.add_argument("--pages", type=int, default=2, help="Pages to fetch (10 jobs/page). Default 2.")
    ap.add_argument("--remote", action="store_true", help="Remote-only (LinkedIn f_WT=2).")
    ap.add_argument("--days", type=int, default=30, help="Only jobs posted in the last N days (default 30; 0 = no filter).")
    ap.add_argument("--detail", metavar="ID_OR_URL", help="Fetch ONE job's full description by LinkedIn id or URL.")
    ap.add_argument("--table", action="store_true", help="Human-readable output instead of JSON.")
    args = ap.parse_args()

    print(_TOS, file=sys.stderr)

    if args.detail:
        jid = extract_job_id(args.detail)
        if not jid:
            print(f"[linkedin-search] couldn't extract a job id from '{args.detail}'", file=sys.stderr)
            sys.exit(2)
        try:
            job = fetch_detail(jid)
        except (HTTPError, URLError) as e:
            print(f"[linkedin-search] detail fetch failed for {jid}: {e}", file=sys.stderr)
            sys.exit(1)
        if args.table:
            print(f"{job['title']}  —  {job['company']}")
            print("  ".join(filter(None, [job["location"], job["seniority"], job["employment_type"]])))
            print(f"{job['url']}\n\n{job['description']}")
        else:
            json.dump(job, sys.stdout, indent=2, ensure_ascii=False)
            sys.stdout.write("\n")
        return

    if not args.keywords:
        ap.error("provide --keywords for a search, or --detail <id|url> for one job's full description")

    jobs = search(args.keywords, args.where, args.pages, args.remote, args.days)
    if args.table:
        if not jobs:
            print("No jobs found.")
        for i, j in enumerate(jobs, 1):
            print(f"{i}. {j['title']}  —  {j['company']}")
            print(f"   {j['location']}  ·  posted {j['listing_date']}")
            print(f"   {j['url']}\n")
    else:
        json.dump(jobs, sys.stdout, indent=2, ensure_ascii=False)
        sys.stdout.write("\n")


if __name__ == "__main__":
    main()
