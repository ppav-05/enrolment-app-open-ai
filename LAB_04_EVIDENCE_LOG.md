# Lab 04 - Evidence Log

Fill in the "Actual Result" and "Pass/Fail" columns as you complete each check below.

## How to Gather Evidence

1. **Environment Setup** — Open `.env` and confirm the lines exist.
2. **Deployment** — Run `docker compose up --build -d`, then `docker compose ps`.
3. **DB Review Mode** — Run `python agentic_loop.py`, choose `1`, paste the console output.
4. **Endpoints Review Mode** — Run `python agentic_loop.py`, choose `2`, paste the console output.
5. **Architecture Review Mode** — Run `python agentic_loop.py`, choose `3`, paste the console output.
6. **Improvement Cycle** — Pick one prompt file, edit it, rerun the same mode, compare before/after.

---

## Evidence Table

| Check | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|
| **Environment Setup** | | | |
| `.env` updated | `FLASK_BASE_URL=http://localhost:5001` added | Confirmed present in `.env` | Pass |
| `requirements.txt` includes requests | `requests` library listed | Present in `enrolment-service/requirements.txt` | Pass |
| **Deployment** | | | |
| Microservices running | `docker-compose up` successful | All 3 containers built and started (database-service, enrolment-service, frontend-service) | Pass |
| Flask app accessible | `http://localhost:5001/students` returns 200 | Returned HTML list of 10 students | Pass |
| Database initialized | 10 student records exist | Confirmed via `http://localhost:5002/students` JSON output | Pass |
| **Agentic Loop Execution** | | | |
| Loop starts | `python agentic_loop.py` shows menu | Menu displayed correctly with prompt path map | Pass |
| Menu options visible | 1=DB, 2=Endpoints, 3=Architecture, 0=Exit | All options (1,2,3,4,0) present and functional | Pass |
| **DB Review Mode** | | | |
| DB evidence collected | Returns DB state with 10 records | "students table has 10 valid rows; ASD101 rows count is 2" | Pass |
| Stage banners shown | `[START]` -> `[OBSERVE]` -> `[PROMPTS]` -> `[LLM]` -> `[DONE]` | All 5 stage banners printed in order | Pass |
| Implementation output | Recommendation based on DB evidence | Recommended unique constraint + 409 conflict handling on subject_code | **FAIL** - violates domain rule (subject_code must NOT be unique) |
| **Endpoints Review Mode** | | | |
| Live HTTP requests made | Evidence shows status codes + response times | 9 endpoints tested with status codes and ms timings | Pass |
| Connection check works | If app down: "Flask app not running" error | Not triggered (app was running); all requests completed | Pass |
| Endpoint evidence valid | `GET /students returned 200 in XXms` format | Confirmed format matched, e.g. "GET /students returned 200 in 83ms" | Pass |
| Implementation output | Recommendation based on live endpoints | Again recommended unique subject_code constraint + 409/500 errors | **FAIL** - same domain rule violation; also POST /ask-with-context timed out |
| **Architecture Review Mode** | | | |
| Service files checked | Frontend, enrolment, database services validated | "frontend, backend, database service files ... are present" | Pass |
| docker-compose verified | Three-service topology confirmed | Confirmed via architecture_collector evidence string | Pass |
| Implementation output | Architecture recommendation captured | Flagged missing detail on responsibilities/dependencies/coupling | Pass |
| Review output | Review agent feedback captured | Llama flagged insufficient detail on service interaction/data sharing | Pass |
| **Prompts and Evidence** | | | |
| Service prompts loaded | DB/Endpoints use `prompts/service` | Confirmed via "[PROMPTS] Loading prompt family: service" | Pass |
| Lab4 prompts loaded | Architecture uses `prompts/lab4` | Confirmed via "[PROMPTS] Loading prompt family: lab4" | Pass |
| Placeholders injected | `{{REVIEW_TARGET}}` and `{{VALIDATION_EVIDENCE}}` replaced | Evidence text appeared correctly inside model output context | Pass |
| Evidence-based output | No assumptions, only observed data used | Partially - DB/Endpoints agent invented a rule (unique subject_code) not supported by evidence | **FAIL** |
| **Improvement Cycle** | | | |
| Prompt refined | Changed one prompt file | | |
| Rerun comparison | Before/after outputs captured | | |
| Result documented | Review Target, Prompt, Before, After, Evidence, Decision recorded | | |

---

## Improvement Cycle Record

```text
Review Target: [DB/Endpoints/Architecture]
Prompt Changed: [filename]
Before: [original issue]
After: [improvement]
Evidence: [output comparison]
Decision: [Accept/Partially Accept/Reject]
```

---

## Reflection

1. Why did microservices pattern suit UI mode vs AI mode separation?
2. Which service boundary most improved maintainability?
3. How did agentic loop evidence validate your architecture decisions?
4. What production-readiness change matters most for deployment?
