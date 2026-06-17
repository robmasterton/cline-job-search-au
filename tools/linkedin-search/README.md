# linkedin-search — OPTIONAL LinkedIn job search CLI

> ## ⚠️ Use at your own risk — read this first
> LinkedIn's [User Agreement](https://www.linkedin.com/legal/user-agreement) **prohibits
> automated access and scraping.** This tool uses LinkedIn's *guest* endpoints (the same
> ones a logged-out browser hits) with **no login and no API key** — but automating them is
> still against LinkedIn's terms and can get your IP **rate-limited or temporarily blocked.**
>
> It is **disabled by default** in `/scrape` and provided for **personal, low-volume use
> only**. **SEEK (`tools/seek-search`) is the primary, supported source** — prefer it. If you
> have any doubt, don't use this: open the LinkedIn posting in your browser and paste it into
> `/apply` instead.
>
> This tool is provided as-is; you are responsible for how you use it.

## Why it's here anyway

LinkedIn lists many AU roles that don't appear on SEEK (especially at global companies). The
guest endpoints return real data with no auth, so it's a useful *optional* supplement — with
the caveat above firmly in mind.

## Requirements

- Python 3.10+. **No pip install, no API key, no login.** Standard library only.

## Usage

```bash
cd tools/linkedin-search

# Search (prints a ToS reminder to stderr each run)
python3 linkedin_search.py --keywords "AI Engineer" --where "Brisbane, Queensland, Australia" --pages 2

# Remote-only, last 14 days
python3 linkedin_search.py --keywords "Senior Full Stack" --where "Australia" --remote --days 14

# One job's FULL description (id or URL) — for /apply
python3 linkedin_search.py --detail https://www.linkedin.com/jobs/view/4417422377
```

### Endpoints (guest, no auth)

| Mode | Endpoint | Returns |
|------|----------|---------|
| Search (`--keywords`) | `/jobs-guest/jobs/api/seeMoreJobPostings/search` | Job cards (10/page): title, company, location, posted date, URL |
| Detail (`--detail`) | `/jobs-guest/jobs/api/jobPosting/<id>` | Full description + seniority, employment type, job function |

### Arguments

| Flag | Default | Meaning |
|------|---------|---------|
| `--keywords` | — | Search terms |
| `--where` | `Australia` | Location string, e.g. `"Brisbane, Queensland, Australia"` |
| `--pages` | `2` | Pages (10 jobs/page) |
| `--remote` | off | Remote-only (`f_WT=2`) |
| `--days` | `30` | Only jobs posted in the last N days (0 = no filter) |
| `--detail` | — | Fetch one job's full description by id or URL |
| `--table` | off | Human table instead of JSON |

## Behaviour & limits

- Sleeps 1s between pages and warns on every run — keep volume low.
- A `429`/HTTP error usually means you've been rate-limited; stop and wait.
- These are unofficial endpoints; if LinkedIn changes them, update the regexes in
  `linkedin_search.py`. Last verified: 2026-06.
