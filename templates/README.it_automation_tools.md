# IT Automation Tools — Windows/macOS

> Enterprise‑ready remediation and audit scripts with safe prompts and rollbacks.

## Problem
Endpoint drift and brittle manual fixes waste time and create risk.

## Approach
- PowerShell and Bash utilities for trust store, Edge removal, restart governance
- Audit‑grade logging, dry‑run modes, and user‑safe prompts
- Built for MDM pipelines (Intune/SCCM/Kandji) with minimal dependencies

## Impact
- Faster, safer remediations with predictable logs and rollback guidance

## Quickstart
```powershell
# PowerShell (as admin)
Set-ExecutionPolicy Bypass -Scope Process -Force
./scripts/Fix-EdgeFramework.ps1 -WhatIf
```

```bash
# macOS (zsh)
bash scripts/fix-trust-store.sh --dry-run
```

## Observability
- Logs: `logs/` with timestamped files
- Exit codes and clear operator messages

## Links
- Docs: ../docs/
