# AGENTS.md

Instructions for coding agents working in this repository.

## Setup and checks

```bash
python3 tools/check_history_privacy.py
python3 tools/validate_repository.py
python3 tools/check_schema_ids.py
python3 tools/generate_manifest.py --check
```

After content changes that affect the published web app, regenerate inventory hashes:

```bash
python3 tools/generate_manifest.py
```

Local preview:

```bash
python3 -m http.server 8000 --directory web
```

## Rules

- Scenarios are synthetic. Do not add real operational data, live feeds, or external AI calls.
- Every public result keeps `authority_effect: "NONE"`. Do not add a path that approves, certifies, or authorizes.
- Prefer squash-merge through green CI. Do not force-push `main`.

## Setup guide

End-to-end local setup for the toolkit and MCP: [AGENT_SETUP](https://ai-governance.solutions/AGENT_SETUP.html).
