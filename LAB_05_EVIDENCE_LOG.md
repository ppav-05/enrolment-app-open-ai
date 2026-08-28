# Lab 05 - Evidence Log

Fill in the "Actual Result" and "Pass/Fail" columns as you complete each check below.

## How to Gather Evidence

1. **Environment Verification** — Run version checks and verify `.env` configured.
2. **Workflow Creation** — Create `.github/workflows/lab5-ci.yml` GitHub Actions workflow.
3. **Workflow Trigger** — Push to GitHub, trigger `lab5-ci` workflow via GitHub Actions UI.
4. **Evidence Collection** — Download `lab5-report` artifact from workflow run.
5. **Agentic Loop** — Run `python agentic_loop.py`, choose option 4 (DevOps), capture output.
6. **Improvement Cycle** — Refine one prompt file, rerun DevOps mode, record results.

---

## Evidence Table

| Check | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|
| **Lab 4 Dependencies** |
| `.env` configured | `FLASK_BASE_URL=http://localhost:5001` exists | | |
| Python dependencies installed | `requests` library available | | |
| **GitHub Workflow** |
| Workflow file created | `.github/workflows/lab5-ci.yml` exists in repo root | | |
| Workflow triggered | `workflow_dispatch` executed on main branch | | |
| **CI Pipeline Stages** |
| Build stage passed | `build-images` job completed successfully | | |
| Smoke check passed | `smoke-check` job verified all 3 services (8080, 5001, 5002) | | |
| Evidence pack created | `evidence-pack` job generated reports | | |
| **Evidence Artifacts** |
| report.json generated | Contains workflow_name, run_id, commit_sha, branch, timestamp | | |
| report.md generated | Contains workflow summary | | |
| run-view.md generated | Contains run details and GitHub Actions URL | | |
| Artifact uploaded | `lab5-report` artifact available for download | | |
| **Agentic Loop Extension** |
| devops_collector.py added | Module exists at `agentic_loop/collectors/devops_collector.py` | | |
| devops_pipeline.py added | Module exists at `agentic_loop/pipelines/devops_pipeline.py` | | |
| Lab5 prompts added | `prompts/lab5/implementation/` and `prompts/lab5/review/` exist | | |
| DevOps mode in menu | Option 4 shows "DevOps" in agentic loop menu | | |
| **DevOps Review Execution** |
| DevOps collector evidence | Workflow jobs validated, report.json keys verified | | |
| Implementation output | Evidence-based recommendation (≤30 words) | | |
| Review output | Risk assessment or approval (≤30 words) | | |
| **Teardown and Cleanup** |
| Service teardown verified | `docker-compose down -v` in workflow | | |

---

## Improvement Cycle Record

**Review Target:** DevOps

**Prompt Changed:** [filename]

**Background:** [Context for the change]

**Before:** [Original issue/observation]

**After:** [Improvement made]

**Evidence:** [Output comparison or validation result]

**Decision:** [Accept/Partially Accept/Reject]

---

## Reflection

<details>
<summary>Answer Briefly:</summary>

1. Which CI validation step provided the strongest evidence?

2. How did DevOps evidence collector improve pipeline analysis?

3. What workflow improvement should be prioritized next?

4. What makes this CI configuration release-ready?

</details>
