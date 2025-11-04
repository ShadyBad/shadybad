# Intrinsic Value Calculator — Live DCF at Scale

> Consistent, auditable valuations driven by live market data and parallel DCF.

![Cover](../assets/intrinsic-value-demo.png)

## Problem
Ad‑hoc valuation workflows are inconsistent, hard to audit, and slow to update as markets move.

## Approach
- Live data ingestion (Yahoo Finance) + FRED risk‑free rates
- Parallel DCF with growth/risk adjustments; validation and error handling
- Investor‑ready CSV/JSON reports for dashboards and research

## Impact
- Timely, auditable valuations with drop‑in artifacts for BI/quant tooling

## Quickstart
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m iv.calc --ticker AAPL --out artifacts/AAPL.json
```

## Architecture
```mermaid
%%{init: {"theme":"dark","themeVariables":{"primaryColor":"#0F172A","primaryTextColor":"#E2E8F0","lineColor":"#14B8A6"}} }%%
flowchart LR
A[Yahoo/FRED] --> B[Ingestion]
B --> C[Validation]
C --> D[DCF Engine]
D --> E[Reports]
```

## Observability
- Artifacts: `artifacts/*.json` `artifacts/*.csv`
- Logs: `logs/`

## Links
- Case Study: ../docs/case-studies/intrinsic-value.md
- Docs: ../docs/
