# Fantasy Draft Tools — Consensus + VBD Engine

> Build calm, reproducible draft day decisions with consensus rankings, tiers, and VBD metrics.

![Cover](../assets/ff-draft-tools-demo.png)

## Problem
Rankings are fragmented and inconsistent across sources; cross‑positional calls are noisy and error‑prone.

## Approach
- Aggregate FantasyPros, ESPN, Yahoo, NFL.com, CBS
- Compute consensus boards, position tiers, VBD (VOLS/VORP/BEER)
- League presets + offline caching; export to Google Sheets/CSV

## Impact
- Faster, clearer decisions; traceable inputs; reproducible boards

## Quickstart
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m ff_tools.build --league ppr --export sheets
```

## Architecture
```mermaid
%%{init: {"theme":"dark","themeVariables":{"primaryColor":"#0F172A","primaryTextColor":"#E2E8F0","lineColor":"#14B8A6"}} }%%
flowchart LR
A[Sources] --> B[Ingestion]
B --> C[Normalization]
C --> D[VBD Engine]
D --> E[Consensus Board]
E --> F[Exports]
```

## Observability
- Artifacts: `artifacts/*.csv` `artifacts/*.json`
- Caching: `cache/`

## Links
- Case Study: ../docs/case-studies/ff-draft-tools.md
- Docs: ../docs/
