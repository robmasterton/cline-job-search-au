---
name: job-application-assistant
description: >
  Assists with job applications: evaluating job postings, tailoring CVs, writing cover letters,
  and preparing for interviews. Triggers on keywords like: job posting, job application, CV,
  cover letter, resume, interview prep, job fit, career, application, apply, SEEK
# (Cline ignores allowed-tools metadata - manage via VS Code settings)
---

# Job Application Assistant

---

## Workflow

This skill helps you with job application steps. The full "Apply Workflow" is defined in `CLAUDE.md`, which covers:

- **Step 0: Parse Input** - How to handle URLs (SEEK, LinkedIn, other) or pasted text, and extract key job details.
- **Step 1: Evaluate Fit** - Using `04-job-evaluation.md` and `01-candidate-profile.md` to assess the job and optionally incorporate salary benchmarks from `salary_lookup.py`.
- **Step 2: Draft CV + Cover Letter** - Tailoring a CV (`cv/main_<company>.tex`) and cover letter (`cover_letters/cover_<company>_<role>.tex`) based on `03-writing-style.md`, `05-cv-templates.md`, and `06-cover-letter-templates.md`.
- **Step 3: Review & Critique** - Performing an inline review of the drafts, researching the company, and providing structured edits and narrative suggestions.
- **Step 4: Revise Based on Feedback** - Applying the suggested edits and revisions.
- **Step 5: Compile & Inspect PDFs (MANDATORY)** - Compiling the LaTeX documents (`lualatex` for CV, `xelatex` for cover letter) and visually verifying the PDF output for layout, page count, and formatting.
- **Step 6: Present Final Output** - Running a final verification checklist, summarizing tailoring decisions, and listing created files.

For interview preparation, refer to the details in `07-interview-prep.md`.

If you want to perform individual steps, you can ask for:
- "Evaluate this job posting" - Focus on Step 1 only
- "Write a CV for [company]" - Focus on drafting the CV (part of Step 2)
- "Write a cover letter for [role] at [company]" - Focus on drafting the cover letter (part of Step 2)
- "Help me prepare for an interview at [company]" - Focus on interview preparation (Step 4 from the old structure, now part of the overall guidance).
- "What jobs should I look for?" - Career strategy discussion using profile + evaluation framework.

---

## Reference Files

| File | Purpose |
|------|---------|
| `01-candidate-profile.md` | Education, experience, skills, publications, awards |
| `02-behavioral-profile.md` | Behavioral assessment, strengths, ideal environments |
| `03-writing-style.md` | Tone, structure, do's and don'ts |
| `04-job-evaluation.md` | Scoring framework for job fit |
| `05-cv-templates.md` | LaTeX CV structure and tailoring rules |
| `06-cover-letter-templates.md` | LaTeX cover letter structure and tailoring rules |
| `07-interview-prep.md` | STAR examples, tough questions, roleplay guidelines |

---


