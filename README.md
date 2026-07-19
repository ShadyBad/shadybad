<p align="center">
  <img src="assets/readme/hero.gif" width="100%" alt="Brandon Shay — AI Engineer building production GenAI systems that earn their autonomy. Beside the title, an agent loop: typed input, the agent proposes, an eval gate scores it, a human approves, the engineer commits, and every action stays reversible.">
</p>

<p align="center">
  <a href="https://linkedin.com/in/brandonpshay"><img alt="LinkedIn — brandonpshay" src="https://img.shields.io/badge/LinkedIn-brandonpshay-0A66C2?style=flat-square&logo=linkedin&logoColor=white"></a>
  <a href="https://maps.google.com"><img alt="Orange County, CA" src="https://img.shields.io/badge/Orange_County-CA-3b3b3b?style=flat-square"></a>
  <a href="#hiring"><img alt="Open to AI Engineer roles" src="https://img.shields.io/badge/Open_to-AI_Engineer_roles-1f8a5b?style=flat-square"></a>
</p>

<p align="center">
  <sub>Enterprise IT Systems Engineer (GCP, Workato, Workspace) transitioning full-time into AI engineering.<br>I ship typed Python, instrumented pipelines, and agents that earn their autonomy.</sub>
</p>

<br>

<img src="assets/readme/section-stack.svg" width="100%" alt="Stack — production tools, AI/ML through to infrastructure">

**Core AI/ML**
![LangGraph](https://img.shields.io/badge/LangGraph-1c1c1c?style=flat-square)
![Claude API](https://img.shields.io/badge/Claude_API-D97757?style=flat-square)
![Langfuse](https://img.shields.io/badge/Langfuse-0f172a?style=flat-square)
![pgvector](https://img.shields.io/badge/pgvector-336791?style=flat-square&logo=postgresql&logoColor=white)
![RAG](https://img.shields.io/badge/RAG-1c1c1c?style=flat-square)
![LLM_as_Judge](https://img.shields.io/badge/LLM--as--Judge-1c1c1c?style=flat-square)

**Backend**
![Python](https://img.shields.io/badge/Python_3.12-3776AB?style=flat-square&logo=python&logoColor=white)
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

<br>

<img src="assets/readme/section-principles.svg" width="100%" alt="Engineering Principles — how I ship production GenAI">

**Eval-first.** Every GenAI project ships with an eval harness before it ships a feature. If you can't measure it, you can't trust it in production.

**Typed, modular Python.** `mypy --strict`, Ruff, no notebooks in main, no untyped public APIs. Code that's read more than it's run.

**Human-in-the-loop on irreversible actions.** Models propose; engineers commit. Reversible architecture by default. Every action has an undo path.

**Observable by construction.** Langfuse traces, structured logs, cost + latency budgets. Debugging a production agent at 2am should not require new instrumentation.
