# Fantasy Draft Tools — Case Study

## Problem
Rankings are fragmented across sources and often inconsistent, making cross‑positional decisions noisy and error‑prone on draft day.

## Approach
- Aggregate rankings from FantasyPros, ESPN, Yahoo, NFL.com, and CBS
- Compute consensus boards, position tiers, and advanced VBD metrics (VOLS/VORP/BEER)
- League presets and offline‑ready caching for stable performance
- Exports to Google Sheets and CSV to fit any draft workflow

## Impact
- Calm, reproducible draft day decisions with traceable inputs
- Faster comparisons across positions and formats
- Simple handoff to sheets/dashboards without manual wrangling

## Quickstart
See repository: https://github.com/ShadyBad/ff_draft_tools

## Tech Highlights
- Python, Pandas/Polars, caching, CLI tooling
- Deterministic exports with artifacts committed for reproducibility

