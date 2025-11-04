# NotionIQ — LLM Workspace Auditor

> Audit Notion workspaces with multi‑provider LLMs and deliver actionable, cost‑controlled cleanup plans.

![Cover](../assets/notioniq-demo.png)

## Problem
Fragmented pages, inbox bloat, and duplicative databases slow teams and hide critical knowledge.

## Approach
- Multi‑provider orchestration (Claude/GPT/Gemini) with safe fallbacks and structured outputs
- Workspace/page/inbox/database scanning → health metrics and confidence‑scored playbooks
- JSON‑first reporting for dashboards and automation; aggressive caching to cut API spend

## Impact
- Clear, prioritized cleanup plans; repeatable audits with predictable cost profiles
- Ready‑to‑consume JSON artifacts for ops tooling and BI

## Quickstart
```bash
# 1) Create env
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
# 2) Install deps
pip install -r requirements.txt  # or: uv pip install -r requirements.txt
# 3) Configure providers
export OPENAI_API_KEY=...  # optional
export ANTHROPIC_API_KEY=...
export GOOGLE_API_KEY=...
# 4) Run a sample audit
python -m notioniq.audit --mode workspace --out artifacts/report.json
```

## Architecture
```mermaid
%%{init: {"theme":"dark","themeVariables":{"primaryColor":"#0F172A","primaryTextColor":"#E2E8F0","lineColor":"#14B8A6","secondaryColor":"#0F172A","tertiaryColor":"#0F172A","edgeLabelBackground":"#0F172A"}} }%%
flowchart LR
A[Sources] --> B[Scanner]
B --> C[Provider Router]
C --> D[LLM Evaluation]
D --> E[Health Metrics]
E --> F[Playbooks]
F --> G[JSON Artifacts]
```

## Observability
- Logs: `logs/` (rotating by date)
- Artifacts: `artifacts/*.json` (reports + metrics)

## Links
- Case Study: ../docs/case-studies/notioniq.md
- Docs: ../docs/
- License: MIT (suggested)
