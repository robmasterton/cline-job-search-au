# Setup Guide

Getting AI Job Search AU running. For installing the tools themselves (Python, LaTeX), see
**[INSTALL.md](INSTALL.md)** — this guide assumes they're in place.

> **Note:** When the instructions below refer to `/setup`, `/scrape`, or `/apply` slash
> commands, simply describe what you want to your AI assistant naturally:
> "Run setup", "Scrape for jobs", "Apply to this job https://...". The workflows are
> triggered by natural language, not by slash commands.

## 1. Fork and clone

```bash
gh repo fork <your-username>/ai-job-search-au --clone
cd ai-job-search-au

# Enable the privacy hook — blocks committing profile files filled with your PII
git config core.hooksPath .githooks
```

Or fork on GitHub and clone your fork manually. **Run the `git config` line either way** if
your fork is public — see [INSTALL.md → Keeping your data private](INSTALL.md#keeping-your-data-private).

## 2. Check the SEEK tool works

No install needed (Python stdlib only). Confirm it returns live jobs:

```bash
cd tools/seek-search
python3 seek_search.py --keywords "Software Engineer" --where "All Brisbane QLD" --pages 1 --table
cd ../..
```

## 3. Run the setup interview

Start your AI assistant (e.g., Cline), then describe what you want:

> "Run setup"
> "Set up my profile"

The assistant will offer three paths and auto-detect what you have:

- **Path A — Documents folder:** drop your CV / LinkedIn export / references into `documents/` and let the assistant read them all. Best signal. See `documents/README.md` for the layout.
- **Path B — Single CV import:** paste or `@`-mention one CV; the assistant extracts it and asks follow-ups.
- **Path C — Interview:** the assistant walks you through structured questions.

### What gets populated

| File | Content |
|------|---------|
| `CLAUDE.md` | Your full candidate profile |
| `.claude/skills/job-application-assistant/01-candidate-profile.md` | Structured education, experience, skills |
| `02-behavioral-profile.md` | Behavioral profile |
| `04-job-evaluation.md` | Personalised skill-match areas and career goals |
| `05-cv-templates.md` | Profile-statement templates for your background |
| `07-interview-prep.md` | STAR examples from your experience |
| `cv/main_example.tex` | Your LaTeX CV with real details |
| `.claude/skills/job-scraper/search-queries.md` | Role keywords + AU locations for scraper |

> **Privacy:** several of these files (`CLAUDE.md`, `cv/main_example.tex`, `search-queries.md`,
> and the `01/02/04/05/07` profile files) are tracked by git. If your fork is public, don't push
> your filled-in profile — the `pre-commit` hook from step 1 blocks this automatically once
> enabled. See [INSTALL.md → Keeping your data private](INSTALL.md#keeping-your-data-private).

### Re-running setup

```
Run setup --section skills
Run setup --section experience
Run setup --section search     # reconfigure scraper role keywords & locations
```

## 4. Optional: salary benchmarking

If you have salary data (e.g. a survey or your own research):

```bash
pip install openpyxl
python tools/convert_salary_excel.py path/to/salary-data.xlsx --source "My Salary Data 2026"
```

This creates `salary_data.json`, which the apply workflow uses for benchmarking. Skip it and the
salary step is simply omitted.

## 5. Search and apply

```
Scrape for jobs                                   # ranked SEEK shortlist by fit
Apply to https://www.seek.com.au/job/12345678     # SEEK URL — full description auto-fetched
Apply to [paste a job description]                # or paste any posting text
```

The assistant will: evaluate fit → ask before drafting → tailor a CV + cover letter → run a
review step → compile and visually verify both PDFs → present the finished files.

## 6. Compile manually (if needed)

The apply workflow compiles for you, but to do it by hand:

```bash
cd cv && lualatex main_<company>.tex && cd ..
cd cover_letters && xelatex cover_<company>_<role>.tex && cd ..
```

## Troubleshooting

### `seek_search.py` returns nothing / an HTTP error
SEEK's API is unofficial and occasionally changes. Check `tools/seek-search/README.md` →
"Known limitations". A transient `rate_limited` resolves by spacing out calls.

### Apply on a SEEK URL doesn't fetch the description
SEEK HTML is Cloudflare-blocked — the apply workflow must use the CLI's `--detail` mode (it does this
automatically in Step 0). If it fails, run it yourself:
`cd tools/seek-search && python3 seek_search.py --detail "<url>"`.

### LaTeX compilation errors
- CV uses **lualatex**; cover letter uses **xelatex** (needs `fontspec`).
- "File `X.sty` not found" on TinyTeX → install the package list in
  [INSTALL.md → Option A](INSTALL.md#option-a--tinytex-recommended-no-sudo--admin-password-needed).

### "salary_data.json not found"
Expected if you skipped step 4 — the apply workflow omits the salary step automatically.