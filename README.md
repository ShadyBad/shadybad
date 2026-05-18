<div align="center">

# Brandon Shay

**AI Engineer building production GenAI systems with evals, types, and human-in-the-loop guardrails.**

Enterprise systems engineer (GCP, Workato, Workspace at Alation) transitioning full-time into AI engineering. I ship typed Python, instrumented pipelines, and agents that earn their autonomy.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-brandonpshay-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/brandonpshay)
[![Location](https://img.shields.io/badge/Orange_County-CA-3b3b3b?style=flat-square)](https://maps.google.com)
[![Status](https://img.shields.io/badge/Open_to-AI_Engineer_roles-1f8a5b?style=flat-square)](#hiring)

## Currently Building

### `auto-co` Agent OS with Engineer-in-the-Loop
Flagship project. Autonomous task graph for long-running engineering work, with a hard human-approval gate on every irreversible action. The agent never commits code on its own.

**Why it's interesting:** LLM-judge eval harness gates every release. Regressions on plan quality, tool-call faithfulness, and cost-per-task block merge.
**Stack:** Python 3.12 · LangGraph · FastAPI · Supabase · Claude API · PostHog · Langfuse
**Architecture:** Reversible-by-default state machine; full session replay via Langfuse traces.

### `NotionIQ` LLM workspace auditor
Scans a Notion workspace, classifies content with Claude, and emits health metrics + actionable cleanup playbooks.

Multi-provider LLM orchestration with safe fallbacks; cached runs cut API spend significantly.
Typed Python, JSON-reportable outputs, zero-config quickstart.

### `margin-invest` Deterministic equity scoring
Portfolio piece. Beneish M-Score · Altman Z-Score · five-factor analysis · 13F overlays · Kelly sizing.

FastAPI + Supabase, fully typed, reproducible outputs from the same input vector every time.

## Stack

**Core AI/ML**
![LangGraph](https://img.shields.io/badge/LangGraph-1c1c1c?style=flat-square)
![Claude API](https://img.shields.io/badge/Claude_API-D97757?style=flat-square)
![Langfuse](https://img.shields.io/badge/Langfuse-0f172a?style=flat-square)
![pgvector](https://img.shields.io/badge/pgvector-336791?style=flat-square&logo=postgresql&logoColor=white)
![RAG](https://img.shields.io/badge/RAG-1c1c1c?style=flat-square)
![LLM_as_Judge](https://img.shields.io/badge/LLM--as--Judge-1c1c1c?style=flat-square)

**Backend**
![Python 3.12](https://img.shields.io/badge/Python_3.12-3776AB?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Supabase](https://img.shields.io/badge/Supabase-3FCF8E?style=flat-square&logo=supabase&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=flat-square&logo=pydantic&logoColor=white)
![Postgres](https://img.shields.io/badge/Postgres-336791?style=flat-square&logo=postgresql&logoColor=white)
![uv](https://img.shields.io/badge/uv_(Astral)-261230?style=flat-square)

**Infra & Ops**
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GH_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white)
![Railway](https://img.shields.io/badge/Railway-0B0D0E?style=flat-square&logo=railway&logoColor=white)
![Fly.io](https://img.shields.io/badge/Fly.io-7c3aed?style=flat-square&logo=fly.io&logoColor=white)
![PostHog](https://img.shields.io/badge/PostHog-1D4AFF?style=flat-square&logo=posthog&logoColor=white)
![mypy + Ruff](https://img.shields.io/badge/mypy_strict_+_Ruff-2c2c2c?style=flat-square)

## Engineering Principles

**Eval-first.** Every GenAI project ships with an eval harness before it ships a feature. If you can't measure it, you can't trust it in production.
**Typed, modular Python.** `mypy --strict`, Ruff, no notebooks in main, no untyped public APIs. Code that's read more than it's run.
**Human-in-the-loop on irreversible actions.** Models propose; engineers commit. Reversible architecture by default. Every action has an undo path.
**Observable by construction.** Langfuse traces, structured logs, cost + latency budgets. Debugging a production agent at 2am should not require new instrumentation.

<a id="hiring"></a>

## Hiring

**Open to full-time AI Engineer roles** at AI labs, infra companies, and Series B–D startups shipping LLM products.

**LinkedIn:** [linkedin.com/in/brandonpshay](https://linkedin.com/in/brandonpshay)
**GitHub:** [@ShadyBad](https://github.com/ShadyBad)
**Based in:** Orange County, CA — open to remote, hybrid, or relocation for the right team.
