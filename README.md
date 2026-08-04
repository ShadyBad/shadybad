<div align="center">

**AI Engineer building production GenAI systems with evals, types, and human-in-the-loop guardrails.**

Enterprise IT Systems Engineer (GCP, Workato, Workspace) transitioning full-time into AI engineering. I ship typed Python, instrumented pipelines, and agents that earn their autonomy.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-brandonpshay-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/brandonpshay)
[![Location](https://img.shields.io/badge/Orange_County-CA-3b3b3b?style=flat-square)](https://maps.google.com)
![Status](https://img.shields.io/badge/Open_to-AI_Engineer_roles-1f8a5b?style=flat-square)

## Stack

**Core AI/ML**
![Claude API](https://img.shields.io/badge/Claude_API-D97757?style=flat-square)

**Backend**
![Python](https://img.shields.io/badge/Python_3.13-3776AB?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=flat-square&logo=pydantic&logoColor=white)
![Postgres](https://img.shields.io/badge/Postgres-336791?style=flat-square&logo=postgresql&logoColor=white)
![uv](https://img.shields.io/badge/uv_(Astral)-261230?style=flat-square)

**Infra & Ops**
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GH_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white)
![Railway](https://img.shields.io/badge/Railway-0B0D0E?style=flat-square&logo=railway&logoColor=white)
![PostHog](https://img.shields.io/badge/PostHog-1D4AFF?style=flat-square&logo=posthog&logoColor=white)
![mypy + Ruff](https://img.shields.io/badge/mypy_strict_+_Ruff-2c2c2c?style=flat-square)

## Engineering Principles

**Eval-first.** Every GenAI project ships with an eval harness before it ships a feature. If you can't measure it, you can't trust it in production.
**Typed, modular Python.** `mypy --strict`, Ruff, no notebooks in main, no untyped public APIs. Code that's read more than it's run.
**Human-in-the-loop on irreversible actions.** Models propose; engineers commit. Reversible architecture by default. Every action has an undo path.
**Observable by construction.** Structured logs, cost + latency budgets. Debugging a production agent at 2am should not require new instrumentation.
