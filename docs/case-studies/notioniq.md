# NotionIQ — Case Study

## Problem
Teams accumulate fragmented pages, inbox bloat, and duplicative databases in Notion. This creates drag, hides critical knowledge, and makes clean-up costly.

## Approach
- Multi-provider LLM orchestration (Claude, GPT, Gemini) with smart provider selection and fallbacks
- Full workspace/page/inbox/database scanning with deep health metrics
- Actionable playbooks and confidence-scored recommendations
- JSON-first reporting for dashboards and follow-up automation
- Aggressive caching to minimize API spend

## Impact
- Clear, prioritized cleanup plans that reduce knowledge friction
- Reliable, repeatable audits with predictable cost profiles
- Ready-to-consume artifacts (JSON) for ops tooling and BI

## Quickstart
See repository: https://github.com/ShadyBad/notionIQ

## Tech Highlights
- Python, provider SDKs (OpenAI/Anthropic/Google)
- Structured outputs, caching layer, metrics/logging
- Exportable JSON artifacts; asset cards in `assets/`

