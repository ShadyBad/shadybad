# Python Essentials for AI Engineering

## Executive Summary

A focused, practice-first guide to the Python features AI engineers use daily: core data structures, comprehensions & functional tools, dataclasses & typing, JSON & pathlib, and the foundational libraries NumPy and Pandas. Mastering these tools eliminates friction in data wrangling, debugging, and productionizing ML pipelines.

## Key Concepts

- Data wrangling dominates AI work: most bugs stem from messy data flows, not model math.
- Python as orchestration layer: typed, structured code that interfaces cleanly with numerics (NumPy) and tabular operations (Pandas).
- Reproducibility & clarity: dataclasses, typing, and pathlib make pipelines readable and maintainable.

## Processes / Algorithms

### Typical Experiment Data Flow

```mermaid
%%{init: {"theme":"dark","themeVariables":{"primaryColor":"#0F172A","primaryTextColor":"#E2E8F0","lineColor":"#14B8A6","secondaryColor":"#0F172A","tertiaryColor":"#0F172A","edgeLabelBackground":"#0F172A"}} }%%
flowchart LR
A[Raw Data (CSV/JSON)] -->|pathlib| B[Pandas DataFrame]
B -->|validation| C[Cleaned DF]
C -->|to_numpy| D[NumPy arrays]
D --> E[Feature Engineering]
E --> F[Model / Training Script]
F --> G[Metrics + Artifacts (JSON/CSV)]

```

## Core Data Structures

### Lists—Ordered, Mutable

```python
feature_vector = [0.2, 0.5, 0.1, 1.0]
feature_vector.append(0.0)
```

### Dictionaries—Mapping Keys → Values

```python
hyperparams = {"lr": 1e-3, "batch_size": 64}
hyperparams["lr"] = 5e-4
```

### Sets—Uniqueness & Fast Membership

```python
sentence = "the quick brown fox jumps over the lazy dog the"
unique = set(sentence.split())
```

### Tuples—Ordered, Immutable

```python
image_size = (256, 256, 3)
w, h, c = image_size
```

## Functional Tools

```python
preds = [0.1, 0.9, 0.85, 0.3, 0.95, 0.6]
hi = [p for p in preds if p >= 0.8]
scaled = [p * 100 for p in preds]
```

## Dataclasses & Typing

```python
from dataclasses import dataclass, field
from typing import List

@dataclass
class ExperimentConfig:
    run_name: str
    model_name: str
    learning_rate: float = 1e-3
    layers: List[int] = field(default_factory=lambda: [128, 64])
```

## JSON Handling

```python
import json, time
settings = {"model": "bert", "lr": 2e-5, "ts": time.time()}
text = json.dumps(settings, indent=2)
parsed = json.loads(text)
```

## File Handling with pathlib

```python
from pathlib import Path
import json

root = Path("output")
root.mkdir(exist_ok=True, parents=True)
```

## NumPy—Vectorized Numerics

```python
import numpy as np
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
a + b
np.mean(a)
```

## Pandas—Tabular Data

```python
import pandas as pd
df = pd.DataFrame({
    "participant_id":[1,2,3,4],
    "treatment_group":["A","B","A","B"],
    "outcome_score":[0.7,0.5,0.8,0.6]
})
df.head()
```

## Examples

### Minimal CSV → DF → NumPy → Save Metrics

```python
from pathlib import Path
import pandas as pd, numpy as np, json

data = Path("data") / "supercars.csv"
df = pd.read_csv(data)
df = df.rename(columns=lambda c: c.strip().lower().replace(" ", "_"))
top_speed = df["top_speed_(mph)"].to_numpy()
stats = {"mean_speed": float(np.mean(top_speed)), "max_speed": int(np.max(top_speed))}
Path("artifacts").mkdir(exist_ok=True)
Path("artifacts/metrics.json").write_text(json.dumps(stats, indent=2))
```

## Pitfalls

| Pitfall | Symptom | Fix |
| --- | --- | --- |
| Iterator exhaustion | Empty lists after prior `list(...)` | Recreate iterator or cache as list |
| Mixed dtypes in NumPy | Upcast to `object` / slow ops | Ensure homogeneous numeric dtype |
| Pandas chained assignment | `SettingWithCopyWarning` | Use `.loc[row_filter, "col"] = value` |
| Path inconsistencies | File not found on Windows/macOS | Use `pathlib.Path` and `/` |
| Mutable defaults | Shared lists across instances | Use `field(default_factory=...)` in dataclasses |
| Un-typed APIs | Runtime bugs | Add function & dataclass type hints |

