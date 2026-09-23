# Lab 07 & 08 Implementation Guide
## MCP and RAG for Student Enrolment App

**Objective:** Complete Labs 07 (MCP Integration) and 08 (RAG Pipeline) for your enrolment-app-open-ai project.

**Duration:** ~4-6 hours total (2-3 hours per lab)

---

## PHASE 1: PREREQUISITES & VERIFICATION

### 1.1 Verify Lab 01-06 Artifacts Exist

```bash
cd enrolment-app-open-ai

# Check essential files
ls -la docker-compose.yml
ls -la enrolment.db
ls -la database-service/
ls -la enrolment-service/
ls -la frontend-service/
ls -la agentic_loop/
ls -la reports/
```

**Expected artifacts:**
- ✅ docker-compose.yml
- ✅ enrolment.db (shared database with 10 student records)
- ✅ database-service/, enrolment-service/, frontend-service/
- ✅ agentic_loop/ directory structure
- ✅ reports/ directory with Lab 05 CI evidence

### 1.2 Verify Prerequisites

```bash
# Python 3.11+
python3 --version

# Docker
docker --version
docker ps

# Ollama
ollama pull qwen2.5:0.5b
ollama pull llama3.1:8b

# Virtual env
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# OR
venv\Scripts\activate  # Windows
```

---

## PHASE 2: LAB 07 - MCP INTEGRATION

### Step 1: Create MCP Directory Structure

```bash
cd enrolment-app-open-ai

# Create MCP server
mkdir -p mcp-server
touch mcp-server/server.py
touch mcp-server/tools.py
touch mcp-server/requirements.txt

# Create Lab 7 prompts
mkdir -p prompts/lab7/implementation
mkdir -p prompts/lab7/review
touch prompts/lab7/implementation/tool_selection_prompt.txt
touch prompts/lab7/review/integration_review_prompt.txt
touch prompts/lab7/review/tool_review_prompt.txt

# Create Lab 7 evidence reports
touch reports/tool-review.md
touch reports/boundary-analysis.md
touch reports/integration-report.md
touch reports/run-report.md
```

### Step 2: Implement MCP Server Files

**File: mcp-server/requirements.txt**
```
mcp
```

**File: mcp-server/tools.py**
[See Lab 07 documentation - Section 4]

**File: mcp-server/server.py**
[See Lab 07 documentation - Section 4]

### Step 3: Create Lab 7 Prompt Assets

[Copy exact prompt text from Lab 07 documentation - Section 3 "MCP Prompt Assets"]

### Step 4: Integrate MCP into Enrolment Service

**Update: enrolment-service/routes/mcp_mode.py**
[See Lab 07 documentation - Section 4 "MCP Backend Integration"]

**Update: enrolment-service/app.py**
- Add import: `from routes.mcp_mode import mcp_bp`
- Register blueprint: `app.register_blueprint(mcp_bp)`

### Step 5: Create Frontend MCP Tab

**File: frontend-service/templates/tabs/mcp.html**
[See Lab 07 documentation - Section 4]

### Step 6: Test MCP Backend (Manual)

**Terminal A:**
```bash
cd enrolment-app-open-ai/mcp-server
python server.py
```

**Terminal B:**
```bash
cd enrolment-app-open-ai/mcp-server
python -c "from tools import get_student_count, get_students_by_subject, list_project_files, read_ci_report; print(get_student_count()); print(get_students_by_subject('ASD101')); print(list_project_files('..')); print(read_ci_report('../reports/report.json'))"
```

**Expected:** All 4 tools return structured JSON responses

### Step 7: Test MCP UI

```bash
# Terminal C:
cd enrolment-app-open-ai
docker compose up --build

# Browser: http://localhost:8080
# Navigate to "MCP" tab
# Test "Get Student Count" → verify JSON response
# Test "Students by Subject" with "ASD101" → verify results
```

### Step 8: Add MCP to Agentic Loop

**Create: agentic_loop/collectors/mcp_collector.py**
[See Lab 07 documentation - Section 6]

**Create: agentic_loop/pipelines/mcp_pipeline.py**
[See Lab 07 documentation - Section 6]

**Update: agentic_loop/config/review_config.py**
- Add `"mcp"` entry to `build_mode_config()`

**Update: agentic_loop/core/orchestrator.py**
- Add `mcp_collector` and `mcp_pipeline` imports
- Register `"mcp": mcp_collector.collect` in COLLECTORS dict
- Add MCP branch to `run_mode()` function

**Update: agentic_loop/app_main.py**
- Add "5": "mcp" to `_menu_choice_to_key()`
- Add "MCP" to `_print_mode_mapping()`
- Update menu to show "5 - MCP"

### Step 9: Run Agentic Loop MCP Mode

**Terminal A: MCP Server**
```bash
cd enrolment-app-open-ai/mcp-server
python server.py
```

**Terminal B: Docker Services**
```bash
cd enrolment-app-open-ai
docker compose up --build
```

**Terminal C: Agentic Loop**
```bash
cd enrolment-app-open-ai/agentic_loop
python agentic_loop.py
# Select: 5 (MCP)
```

**Expected Output:**
```
[MCP][START] Starting review flow
[MCP][OBSERVE] Collecting evidence...
[MCP][LLM] Running MCP implementation model...
[MCP][LLM] Running MCP review model...
[MCP][DONE] Review complete

OBSERVE: MCP evidence: mcp-server/ contains tools.py and server.py; server defines 4 tools...
IMPLEMENTATION: [LLM output - max 40 words]
REVIEW: [LLM output - max 40 words]
```

### Step 10: Document Lab 7 Evidence

**File: reports/run-report.md**
```markdown
# Lab 07 MCP Testing Report

## Backend Testing
- Terminal A output: [paste MCP server startup output]
- Terminal B output: [paste tool execution results]

## UI Testing
- Screenshot: MCP tab interface
- Screenshot: MCP mode ON with results
- Screenshot: MCP mode OFF message

## Agentic Loop Validation
- OBSERVE: [paste from Terminal C]
- IMPLEMENTATION: [paste from Terminal C]
- REVIEW: [paste from Terminal C]
```

---

## PHASE 3: LAB 08 - RAG PIPELINE

### Step 1: Create RAG Directory Structure

```bash
cd enrolment-app-open-ai

# RAG server (NOT containerized, runs locally)
mkdir -p rag-server/corpus
mkdir -p rag-server/chroma
touch rag-server/rag_server.py
touch rag-server/rag_http_server.py
touch rag-server/rag_pipeline.py
touch rag-server/rag_eval.py
touch rag-server/requirements.txt
touch rag-server/mcp-config.json
touch rag-server/tool-contracts.md
touch rag-server/retrieval-metrics.md
touch rag-server/rag-audit.jsonl
touch rag-server/corpus/corpus.jsonl

# Lab 8 prompts
mkdir -p prompts/lab8/implementation
mkdir -p prompts/lab8/review
touch prompts/lab8/implementation/rag_implementation_prompt.txt
touch prompts/lab8/review/rag_review_prompt.txt
touch prompts/lab8/review/rag_reasoning_prompt.txt

# Lab 8 reports
touch reports/rag-report.md
touch reports/rag-validation-report.md
```

### Step 2: Create RAG Server Files

**File: rag-server/requirements.txt**
```
mcp
chromadb
requests
```

**Install:**
```bash
cd rag-server
python3 -m pip install -r requirements.txt
```

**File: rag-server/rag_pipeline.py**
[See Lab 08 documentation - Section 4]

**File: rag-server/rag_server.py**
[See Lab 08 documentation - Section 4]

**File: rag-server/rag_http_server.py**
[See Lab 08 documentation - Section 4]

**File: rag-server/rag_eval.py**
[See Lab 08 documentation - Section 4]

### Step 3: Create Lab 8 Prompt Assets

[Copy exact prompt text from Lab 08 documentation - Section 3 "Prompt assets"]

### Step 4: Integrate RAG into Enrolment Service

**Create: enrolment-service/routes/rag_mode.py**
[See Lab 08 documentation - Section 4]

**Create: enrolment-service/services/rag_api.py**
[See Lab 08 documentation - Section 4]

**Update: enrolment-service/app.py**
- Add import: `from routes.rag_mode import rag_bp`
- Register blueprint: `app.register_blueprint(rag_bp)`

### Step 5: Create Frontend RAG Tab

**File: frontend-service/templates/tabs/rag.html**
[See Lab 08 documentation - Section 4]

### Step 6: Update Docker Compose

**File: docker-compose.yml**
[See Lab 08 documentation - Section 4]

Key change: Add environment variables for RAG service:
```yaml
enrolment-service:
  environment:
    RAG_SERVICE_URL: http://host.docker.internal:5003
    RAG_ENABLED: "true"
```

### Step 7: Test RAG Backend (Manual)

**Terminal A: RAG HTTP Server**
```bash
cd enrolment-app-open-ai/rag-server
python3 rag_http_server.py
# Expected: RAG HTTP server running on 0.0.0.0:5003
```

**Terminal B: Test RAG Tools**
```bash
cd enrolment-app-open-ai/rag-server

# 1. Refresh corpus
python3 -c "from rag_pipeline import refresh_corpus; import json; print(json.dumps(refresh_corpus(), indent=2))"

# 2. Retrieve context
python3 -c "from rag_pipeline import retrieve_context; import json; print(json.dumps(retrieve_context('students enrolled in ASD101', 5), indent=2))"

# 3. Answer question
python3 -c "from rag_pipeline import answer_question; import json; print(json.dumps(answer_question('Which students are enrolled in ASD101?', 5), indent=2))"

# 4. Run evaluation
python3 rag_eval.py
```

**Expected:** All tools return structured outputs with citations and confidence

### Step 8: Test RAG UI

**IMPORTANT: RAG server must be running in Terminal A BEFORE starting Docker services**

**Terminal B: Docker Services**
```bash
cd enrolment-app-open-ai
docker compose up --build

# Wait for all 3 containers to start
docker ps
```

**Browser: http://localhost:8080**
- Navigate to "RAG" tab
- Click "Refresh Corpus" → verify success
- Enter query "students enrolled in ASD101" → Click "Retrieve Context" → verify results
- Enter question "Which students are enrolled in ASD101?" → Click "Answer with Citations" → verify answer + citations

### Step 9: Add RAG to Agentic Loop

**Create: agentic_loop/collectors/rag_collector.py**
[See Lab 08 documentation - Section 6]

**Create: agentic_loop/pipelines/rag_pipeline.py**
[See Lab 08 documentation - Section 6]

**Update: agentic_loop/config/review_config.py**
- Add `"rag"` entry to `build_mode_config()`

**Update: agentic_loop/core/orchestrator.py**
- Add `rag_collector` and `rag_pipeline` imports
- Register `"rag": rag_collector.collect` in COLLECTORS dict
- Add RAG branch to `run_mode()` function (loads both review prompts)

**Update: agentic_loop/app_main.py**
- Add "6": "rag" to `_menu_choice_to_key()`
- Add "RAG" to `_print_mode_mapping()`
- Update menu to show "6 - RAG"

### Step 10: Run Agentic Loop RAG Mode

**3-Terminal Workflow:**

**Terminal A: Docker Services**
```bash
cd enrolment-app-open-ai
docker compose up
```

**Terminal B: RAG HTTP Server**
```bash
cd enrolment-app-open-ai/rag-server
python3 rag_http_server.py
# Important: Keep this running throughout
```

**Terminal C: Agentic Loop**
```bash
cd enrolment-app-open-ai/agentic_loop
python agentic_loop.py
# Select: 6 (RAG)
```

**Expected Output:**
```
[RAG][START] Starting review flow
[RAG][OBSERVE] Collecting evidence...
[RAG][PROMPTS] Loaded RAG implementation prompt
[RAG][LLM] Running RAG implementation model...
[RAG][PROMPTS] Loaded RAG review and reasoning prompts
[RAG][LLM] Running RAG review model...
[RAG][DONE] Review complete

OBSERVE: RAG evidence: rag-server/ contains rag_pipeline.py and rag_server.py; 3 tools defined...
IMPLEMENTATION: [LLM output - max 40 words]
REVIEW: [LLM output - max 40 words, from both review prompts]
```

### Step 11: Document Lab 8 Evidence

**File: reports/rag-report.md**
```markdown
# Lab 08 RAG Testing Report

## Backend Testing
- RAG HTTP server: [paste Terminal B output]
- Tool outputs: [paste refresh_corpus, retrieve_context, answer_question results]
- Evaluation metrics: [paste P@5, R@5 from rag_eval.py]

## UI Testing
- Screenshot: RAG tab interface
- Screenshot: Refresh corpus result
- Screenshot: Retrieve context result
- Screenshot: Answer with citations result

## Retrieval Metrics
- P@5 (Precision at 5): [from rag_eval.py output]
- R@5 (Recall at 5): [from rag_eval.py output]
```

**File: reports/rag-validation-report.md**
```markdown
# RAG Agentic Validation Report

## Evidence Collected (OBSERVE)
[Paste from Terminal C OBSERVE output]

## Implementation Assessment (qwen2.5:0.5b)
[Paste from Terminal C IMPLEMENTATION output]

## Review Assessment (llama3.1:8b)
[Paste from Terminal C REVIEW output]

## Metrics Summary
- Corpus chunks indexed: [from rag_pipeline.py output]
- Retrieval mode: vector (primary) or lexical_fallback
- Average confidence category: high/medium/low
- Citation coverage: [% of responses with citations]
```

---

## TROUBLESHOOTING

### Issue: MCP database not found
**Solution:** Ensure enrolment.db exists in app root with 10 student records (created in Lab 03-04)

### Issue: RAG corpus empty
**Solution:** RAG server automatically builds corpus from database on first `refresh_corpus` call

### Issue: Docker services can't reach RAG server
**Solution:** RAG server must be running locally on port 5003 BEFORE docker compose up. Use `host.docker.internal:5003` from inside containers.

### Issue: Ollama models not available
**Solution:** `ollama pull qwen2.5:0.5b` and `ollama pull llama3.1:8b` before running agentic_loop

---

## COMPLETION CHECKLIST

### Lab 07 (MCP)
- [ ] mcp-server/ directory with tools.py, server.py, requirements.txt
- [ ] Lab 7 prompts created (3 files in prompts/lab7/)
- [ ] MCP routes integrated (routes/mcp_mode.py)
- [ ] Frontend MCP tab created
- [ ] MCP collector and pipeline in agentic_loop/
- [ ] MCP mode registered in review_config.py
- [ ] Orchestrator updated to handle MCP mode
- [ ] Menu option 5 added
- [ ] All tests pass (backend, UI, agentic)
- [ ] Evidence reports created (run-report.md, etc.)

### Lab 08 (RAG)
- [ ] rag-server/ directory with all files
- [ ] Lab 8 prompts created (3 files in prompts/lab8/)
- [ ] RAG routes integrated (routes/rag_mode.py)
- [ ] RAG API service created (services/rag_api.py)
- [ ] Frontend RAG tab created
- [ ] RAG collector and pipeline in agentic_loop/
- [ ] RAG mode registered in review_config.py
- [ ] Orchestrator updated to handle RAG mode
- [ ] Menu option 6 added
- [ ] All tests pass (backend, UI, agentic)
- [ ] Evidence reports created (rag-report.md, rag-validation-report.md)

---

## REFERENCE LINKS

- **Lab 07 Full Documentation**: GitHub raw link
- **Lab 08 Full Documentation**: GitHub raw link
- **Docker Compose Reference**: https://docs.docker.com/compose/
- **MCP Documentation**: https://modelcontextprotocol.io/
- **ChromaDB Documentation**: https://docs.trychroma.com/

---

**Total Time Estimate:**
- Lab 07: 1.5-2 hours
- Lab 08: 2-3 hours
- Debugging/Troubleshooting: 30 min - 1 hour

**Start with Lab 07, complete all steps including agentic validation before moving to Lab 08.**
