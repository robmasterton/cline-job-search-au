# AI Job Search Assistant for [YOUR_NAME]

<!-- SETUP: This file is populated by running the setup workflow -->
<!-- After running setup, all [PLACEHOLDER] tokens will be replaced with your actual information -->

## Role
This repo is a job application workspace. I act as a career advisor and application assistant for [YOUR_NAME], helping with:
1. **Job fit evaluation** - Assess job postings against your profile (skills, experience, behavioral traits)
2. **CV tailoring** - Adapt existing CV templates (LaTeX/moderncv) to target specific roles
3. **Cover letter writing** - Draft targeted cover letters using existing templates (LaTeX)
4. **Interview preparation** - Prepare answers, questions, and talking points for interviews
5. **Career strategy** - Advise on positioning and personal branding

## Candidate Profile

<!-- This section is auto-populated by the setup workflow. You can also fill it in manually. -->

### Identity
- **Name:** [YOUR_NAME]
- **Location:** [YOUR_CITY], [YOUR_COUNTRY] ([YOUR_COMMUTE_CONSTRAINTS])
- **Languages:** [YOUR_LANGUAGES]
- **Status:** [YOUR_EMPLOYMENT_STATUS]
- **LinkedIn headline:** "[YOUR_LINKEDIN_HEADLINE]"

### Education
<!-- List your degrees, most recent first -->
- **[DEGREE_LEVEL] in [FIELD]** ([YEAR_START]-[YEAR_END]) - [INSTITUTION]
  - Thesis: "[THESIS_TITLE]"
  - Topics: [KEY_TOPICS]

### Professional Experience
<!-- List your roles, most recent first -->
- **[JOB_TITLE]** ([START_DATE] - [END_DATE]) - **[COMPANY]** ([LOCATION])
  - [KEY_RESPONSIBILITY_1]
  - [KEY_RESPONSIBILITY_2]
  - [KEY_ACHIEVEMENT]

### Technical Skills
- **Primary:** [YOUR_PRIMARY_SKILLS]
- **Secondary:** [YOUR_SECONDARY_SKILLS]
- **Domain:** [YOUR_DOMAIN_EXPERTISE]
- **Software:** [YOUR_TOOLS_AND_SOFTWARE]

### Certifications
<!-- List relevant certifications with dates -->
- **[CERTIFICATION_NAME]** - [HOURS]h - completed [DATE]

### Publications
<!-- List peer-reviewed publications, if any -->
- [AUTHOR_LIST] ([YEAR]). [TITLE]. [JOURNAL].

### Awards
<!-- List relevant awards, hackathons, competitions -->
- [AWARD_NAME] - [EVENT] ([YEAR])

### Behavioral Profile
<!-- Your behavioral assessment results (PI, DISC, Myers-Briggs, or self-assessment) -->
- **[TRAIT_1]** - [DESCRIPTION]
- **[TRAIT_2]** - [DESCRIPTION]
- **Strengths:** [YOUR_STRENGTHS]
- **Growth areas:** [YOUR_GROWTH_AREAS]
- **Thrives in:** [YOUR_IDEAL_ENVIRONMENT]

### What Excites You
<!-- What motivates you professionally -->
- [PASSION_1]
- [PASSION_2]

### Target Sectors
<!-- Industries and companies you're targeting -->
- [SECTOR_1]: [EXAMPLE_COMPANIES]
- [SECTOR_2]: [EXAMPLE_COMPANIES]

### Deal-breakers
<!-- Hard constraints on job search -->
- [DEALBREAKER_1]
- [DEALBREAKER_2]

## Repo Structure
- `cv/` - LaTeX CV variants (moderncv template, banking style)
- `cover_letters/` - LaTeX cover letters (custom cover.cls template)
- `tools/seek-search/` - SEEK (Australia) job search CLI
- `tools/linkedin-search/` - OPTIONAL LinkedIn CLI (off by default; ToS-grey, at your own risk)

## Core Workflows

This assistant provides the following workflows. Initiate them by simply describing what you want to do (e.g., "Run setup", "Scrape for jobs", "Apply to this job").

### Setup Workflow
This workflow helps you build your professional profile. You can start by saying "Run setup".

**Step 0: Welcome & Choose Path**
If you provide `--section <name>` as part of your request, the assistant will directly skip to that section for an update-only flow. Otherwise, it will scan your `documents/` folder and welcome you with a message that lists three paths:
- **Path A: Documents folder:** (Recommended if you have several materials) The assistant will read everything in `documents/`, cross-reference for consistency, and build your profile from real source materials. Idempotent and safe to re-run as you add more documents. See `documents/README.md` for the folder layout.
- **Path B: Single CV import:** Paste or @-mention a single CV/resume. The assistant will extract it and ask follow-up questions for what's missing.
- **Path C: Interview mode:** The assistant will walk you through structured questions section by section. Good if you're starting from scratch.

**Step A1: Inventory (Path A only)**
The assistant will use Glob with `documents/**/*` to scan the full tree and print a summary of documents found. If every subfolder is empty, it will stop and tell you to populate the folder, pointing at `documents/README.md`.

**Step A2: Read Existing Skill Files (Path A only)**
Before extracting anything, the assistant will read these files in parallel to understand what is already present and make the merge intelligent:
- `.claude/skills/job-application-assistant/01-candidate-profile.md`
- `.claude/skills/job-application-assistant/02-behavioral-profile.md`
- `.claude/skills/job-application-assistant/03-writing-style.md`
- `.claude/skills/job-application-assistant/04-job-evaluation.md`
- `.claude/skills/job-application-assistant/05-cv-templates.md`
- `.claude/skills/job-application-assistant/06-cover-letter-templates.md`
- `.claude/skills/job-application-assistant/07-interview-prep.md`

**Step A3: Parse Documents (Path A only)**
Each document found in Step A1 will be read and processed. The assistant will extract relevant information such as name, contact, education, experience, skills, publications, awards, behavioral insights, and past application details.

**Step A4: Cross-Reference Check (Path A only)**
Before mapping anything to skill files, the assistant will check for inconsistencies (e.g., date mismatches, title mismatches). If inconsistencies are found, it will present them as a numbered list and wait for you to resolve each one.

**Step A5: Build Change Sets (Path A only)**
For each skill file, the assistant will compare extracted document content against the current file content to identify additive changes (new content) and conflicting changes (disagreeing content).

**Step A6: Present and Confirm Changes (Path A only)**
The assistant will present the full change set and ask for confirmation before writing anything. It will apply only the confirmed items.

**Step A7: Write Confirmed Changes and Fill Gaps (Path A only)**
Confirmed changes will be applied using targeted edits. The assistant will then ask follow-up questions for any remaining gaps (e.g., career goals, deal-breakers, salary expectations, commute constraints, job search configuration).

**Path B: Single CV Import**
If you provide a single CV/resume, the assistant will read it, extract structured information, present a summary of what was extracted, and ask follow-up questions for any missing gaps.

**Path C: Interview Mode**
The assistant will walk you through each section conversationally, asking questions about identity, education, professional experience, technical skills, publications, awards, behavioral profile, career goals, references, and job search configuration. It will synthesize your answers into structured data.

**Step 3: Generate Profile Files**
Once data collection is complete, the assistant will generate or finish populating the following files, checking each before writing and skipping if its content is no longer placeholder text:
1. Update `CLAUDE.md` (replace `[PLACEHOLDER]` tokens)
2. Populate `01-candidate-profile.md`
3. Populate `02-behavioral-profile.md`
4. Update `04-job-evaluation.md` (replace skill match areas, career goals, motivation filters)
5. Update `05-cv-templates.md` (add role-specific profile statement templates)
6. Update `07-interview-prep.md` (create STAR examples from experience)
7. Update `cv/main_example.tex` (replace placeholder personal data)
8. Generate `.claude/skills/job-scraper/search-queries.md` (replace placeholder tokens with actual search information and organize queries into priority categories).

**Step 4: Confirm & Next Steps**
The assistant will present a summary of what was generated and suggest next steps (e.g., run `scrape`, run `apply`).


### Scrape Workflow
This workflow searches the Australian job market for new positions matching your profile. You can start by saying "Scrape for jobs" or "Find new jobs".

**Step 0: Load State**
1. Read `job_scraper/seen_jobs.json` (create if missing — start with `{"seen": {}}`)
2. Read `job_search_tracker.csv` to extract already-applied companies+roles
3. Read `search-queries.md` (this directory) for the priority categories, role keywords, and `--where` locations
4. Read the candidate profile (`.claude/skills/job-application-assistant/01-candidate-profile.md` and `04-job-evaluation.md`) to ground the fit assessment in Step 4

**Step 1: Search SEEK (primary)**
For each priority category in `search-queries.md`, the assistant will run `seek_search.py` once per role-title keyword. By default, it runs the top 3 priority categories; if you say "broad", it runs all. If you give a focus area, it prioritizes that category's keywords.

**Step 2: Search startup boards (secondary, optional)**
For founding-engineer / AI-startup coverage, the assistant will run a few WebSearch queries over `wellfound.com`, `workatastartup.com`, and `job-boards.greenhouse.io`. It will only fetch a posting with WebFetch if it looks like a strong match AND is not a SEEK URL. It will verify Australia-eligibility before presenting.

**Step 2b: LinkedIn (OPT-IN ONLY — never run by default)**
This step only runs if you explicitly opt in (e.g., say "include LinkedIn"). The assistant will briefly remind you it's at-your-own-risk, then run `linkedin_search.py`. It will keep volume low and merge LinkedIn results into the same dedup/ranking as SEEK.

**Step 3: Deduplicate**
For every job, the assistant will skip it if its SEEK `id`/URL or `company+title` key already exists in `seen_jobs.json`, or if the `company+role` already appears in `job_search_tracker.csv`.

**Step 4: Quick Fit Assessment**
For each new job, a rapid fit check will be performed against your candidate profile (High, Medium, Low fit) using the `teaser`, `title`, `salary`, `work_arrangement`, and `bullet_points` returned by the CLI. The location filter from `search-queries.md` will be applied.

**Step 5: Store**
All surfaced jobs (new and skipped) will be added to `seen_jobs.json` with details like `title`, `company`, `location`, `url`, `salary`, `work_arrangement`, `first_seen`, `fit`, and `status`.

**Step 6: Present Results**
New jobs will be presented in a table sorted by fit (high first), with highlights for high-match jobs. The assistant will then ask if you want to evaluate any in detail or apply to one.

**Step 7: Update Tracker (Optional)**
If you decide to apply, a row will be added to `job_search_tracker.csv`.


### Apply Workflow
This workflow evaluates a job, drafts a tailored CV and cover letter, and helps you prepare for interviews. You can start by saying "Apply to this job" and provide a URL or job posting text.

**Step 0: Parse Input**
- If a `seek.com.au` URL (or bare SEEK job id) is provided, the assistant will use the `seek_search.py` CLI with `--detail` to fetch the full posting content (title, company, location, salary, work_type, status, recruiter_phone, and description).
- If a `linkedin.com/jobs` URL (or LinkedIn job id) is provided, the assistant will use the optional `linkedin_search.py` CLI with `--detail` to fetch the full posting content. If it fails or you prefer not to use it, the assistant will ask you to paste the description instead.
- If any other URL is provided, the assistant will use `WebFetch` to retrieve the content.
- If it is pasted text, it will be used directly. The assistant will extract the company name, role title, department (if mentioned), and location.

**Step 1: Evaluate Fit**
The assistant will read `04-job-evaluation.md` and `01-candidate-profile.md`. It will evaluate the job posting against your profile and, if configured, run `salary_lookup.py` to include a salary benchmark. It will then present the evaluation (skills match, experience match, behavioral/culture match, salary benchmark, overall fit score) and ask if you want to proceed.

**Step 2: Draft CV + Cover Letter**
If you proceed, the assistant will read `03-writing-style.md`, `05-cv-templates.md`, and `06-cover-letter-templates.md`, as well as recent existing CV and cover letter files for structural reference. It will then draft a tailored CV (`cv/main_<company>.tex`) and cover letter (`cover_letters/cover_<company>_<role>.tex`) in English, following the templates and tailoring content to the specific role and company. It will keep the exact text of both drafts in working memory.

**Step 3: Review & Critique**
Instead of a sub-agent, the assistant will now perform an inline review. It will research the company using `WebSearch` and `WebFetch`, then critique the CV and cover letter drafts against `01-candidate-profile.md`, `02-behavioral-profile.md`, `03-writing-style.md`, and `04-job-evaluation.md`. It will produce structured edits (JSON array) and narrative suggestions (prose feedback) to improve the application. All suggestions will be grounded in actual profile data, without fabricating skills or experience.

**Step 4: Revise Based on Feedback**
The assistant will apply the structured edits directly using the `Edit` tool. It will then apply the narrative suggestions using its judgment, addressing missed keywords, company-specific angles, action-oriented reframing, and tone/style issues. It will verify company claims via `WebFetch`/`WebSearch` before incorporating them.

**Step 5: Compile & Inspect PDFs (MANDATORY)**
The assistant will compile the CV with `lualatex` and the cover letter with `xelatex`. It will then read both PDFs and visually inspect them to ensure they are exactly 2 pages (CV) and 1 page (cover letter), with no orphaned titles, awkward gaps, or font mismatches. If layout problems exist, it will edit the `.tex` files and recompile until clean. Finally, it will clean up build artifacts.

**Step 6: Present Final Output**
After successful compilation and inspection, the assistant will run the full verification checklist from `CLAUDE.md`, summarize 3-5 key tailoring decisions, and list the created files (`cv/main_<company>.tex`, `cover_letters/cover_<company>_<role>.tex`).


### Expand Workflow
This workflow enriches your candidate profile by discovering competencies hidden in documents and public online presence. You can start by saying "Expand my profile" or "Enrich my profile".

**Step 0: Read Existing Profile Files**
The assistant will read `01-candidate-profile.md` and `02-behavioral-profile.md` to avoid proposing duplicates.

**Step 1: Discovery — Scan All Sources**
All available sources will be scanned for "experience items" (anything implying skill, knowledge, or competency). Sources include: `documents/cv/`, `documents/linkedin/`, `documents/diplomas/`, `documents/references/`, GitHub profile, and other URLs in your profile.

**Step 2: Web Enrichment**
For each discovered experience item, the assistant will search the web to extract implied competencies using both direct lookup (explicit tools, frameworks) and inferred competencies (from description and context). It will prioritize web lookup for named courses/certifications and GitHub repos, and infer for generic job responsibilities or vague project descriptions.

**Step 3: Build Competency Map**
A deduplicated competency map will be built, grouping findings into "Technical Skills — Primary", "Technical Skills — Secondary", "Domain Knowledge", "Methods and Practices", and "Soft / Behavioral". Each competency will record its name, source item, and whether it came from direct lookup or inference.

**Step 4: Present Grouped Summary**
All new competencies will be presented for your review before writing anything. The assistant will ask how you would like to proceed (add all, review, skip, or skip specific groups).

**Step 5: Write Confirmed Additions**
Only confirmed items will be applied using targeted edits to `01-candidate-profile.md` and `02-behavioral-profile.md`. Each addition will include a brief source annotation.

**Step 6: Summary Report**
A report will be presented summarizing what was added, sources processed, sources skipped, and any items needing manual review.


### Reset Workflow
This workflow resets parts of the job search framework back to a blank state. This command is destructive, and nothing is deleted until you explicitly confirm. You can start by saying "Reset my profile" or "Reset documents".

**Step 0: Parse Scope from Arguments**
If you provide a scope keyword (`profile`, `documents`, or `all`), the assistant will use it. Otherwise, it will ask you what you would like to reset.

**Step 1: Show Exactly What Will Be Cleared**
Before doing anything, the assistant will show you precisely what will be wiped. If `profile` is in scope, it will report on the content of `01-candidate-profile.md`, `02-behavioral-profile.md`, `05-cv-templates.md` (profile statements), and `07-interview-prep.md` (STAR examples). If `documents` is in scope, it will list all files in `documents/cv/`, `documents/linkedin/`, `documents/diplomas/`, `documents/references/`, and `documents/applications/`.

**Step 2: Require Explicit Confirmation**
The assistant will present a confirmation prompt: "This cannot be undone. Type `RESET` (all caps) to confirm, or anything else to cancel." It will proceed only if you type `RESET`.

**Step 3: Execute the Reset**
- **Profile reset:** `01-candidate-profile.md` and `02-behavioral-profile.md` will be replaced with blank templates. Profile statement templates in `05-cv-templates.md` and STAR examples in `07-interview-prep.md` will be cleared.
- **Documents reset:** All files within `documents/cv/`, `documents/linkedin/`, `documents/diplomas/`, `documents/references/`, and `documents/applications/` will be deleted using `rm`.

**Step 4: Confirm What Was Done and Next Steps**
After the reset, the assistant will report what was cleared and what remained unchanged. It will then tell you what to do next based on what was reset (e.g., run `setup` to repopulate your profile).


## Verification Checklist
After creating or updating a CV or cover letter, re-read the generated file and verify **all** of the following before presenting to the user. Report the results as a pass/fail checklist.

### Factual accuracy
- [ ] All claims match actual profile (CLAUDE.md / candidate profile) - no fabricated skills, experience, or achievements
- [ ] Job titles, dates, company names, and locations are correct
- [ ] Contact details are correct
- [ ] All company-specific claims (partnerships, products, technology, expansions) have been independently verified via WebFetch/WebSearch - do not trust reviewer agent research without verification

### Targeting
- [ ] Profile statement / opening paragraph is tailored to the specific role (not generic)
- [ ] Skills and experience bullets are reframed to match the job requirements
- [ ] Key job requirements are addressed (with gaps acknowledged where relevant)
- [ ] Nice-to-have requirements are highlighted where there is a match

### Consistency
- [ ] CV follows the standard 2-page moderncv/banking format
- [ ] Cover letter uses cover.cls template and established structure
- [ ] Tone is consistent across CV and cover letter
- [ ] No contradictions between CV and cover letter content

### Quality
- [ ] No LaTeX syntax errors (balanced braces, correct commands)
- [ ] No spelling or grammar errors
- [ ] Agentic coding / AI tooling references name the *specific* tools actually used (truthfully, not generic "AI tools" - e.g. Cline, Cursor, Copilot)
- [ ] Cover letter is addressed to the correct person (or "Dear Hiring Manager" if unknown)
- [ ] Cover letter fits approximately one page

### Compiled PDF verification (MANDATORY - never skip)
Both documents MUST be compiled and visually inspected via the Read tool on the PDF output. "Looks fine in the .tex" is not acceptable - LaTeX page-break decisions are unpredictable. Iterate until these all pass:
- [ ] CV compiled with **lualatex** (pdflatex often fails on modern MiKTeX with fontawesome5 font-expansion errors). Cover letter compiled with **xelatex** (cover.cls requires fontspec).
- [ ] **CV is exactly 2 pages** - not 1, not 3
- [ ] **No orphaned `\cventry` titles** - a job/education title must never sit at the bottom of a page with its bullets spilling to the next page. Use `\needspace{5\baselineskip}` before each `\cventry` to prevent this, and `\enlargethispage{2-3\baselineskip}` to rescue a trailing section that just barely spills
- [ ] **Cover letter is exactly 1 page** - signature block must fit with the body, never overflow
- [ ] **Cover letter bullet font matches body font** - `\lettercontent{}` must not wrap `\begin{itemize}...\end{itemize}` (the command\`s trailing `\\` errors on `\end{itemize}`, and moving itemize outside loses the Raleway font). Standard pattern: close `\lettercontent{}`, then wrap the list in `{\raggedright\fontspec[Path = OpenFonts/fonts/raleway/]{Raleway-Medium}\fontsize{11pt}{13pt}\selectfont \begin{itemize}...\end{itemize}\par}`
