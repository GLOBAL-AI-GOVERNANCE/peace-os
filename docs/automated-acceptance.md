# Automated acceptance validation

The `v0.3.0-rc2` release workflow uses automated acceptance validation to verify the exact public candidate before publication.

The release controller verifies:

- repository identity and exact commit lineage;
- source inventory, tests, scoring invariants, and shared-data parity;
- public/private and personal-data boundaries;
- semantic accessibility source contracts;
- exact GitHub Pages assets, workflow-generated `deployment.json`, and expected product markers;
- complete browser journeys for both scenarios and all three modes;
- confirmation invalidation, retained corrupt-session handling, schema-valid downloaded AARs, print completeness, and narrow-screen behavior;
- absence of unexpected external runtime dependencies;
- exact-commit provenance, SBOM, and release checksums.

The workflow produces human-readable Markdown, machine-readable JSON, and a SHA-256 ledger bound to the deployed URL and exact commit. The workflow fails on a deployment-metadata mismatch, failed journey, failed control, browser console error, or unexpected external request.

Automated acceptance validation does not establish human usability, learning effectiveness, screen-reader compatibility, WCAG conformance, professional assessment validity, operational fitness, or Godot and Windows runtime readiness. Those remain separate evidence streams for stable or desktop releases.

## Local verification

A change is reviewable when it includes:

- the problem and evidence;
- the doctrine or learning objective affected;
- tests for scoring, policy, or data-contract changes;
- declared assumptions and remaining limitations;
- no live incident data, personal data, classified material, or autonomous-action capability.

Changes to scoring, scenario data, policy, release language, AAR records, or finalization gates trigger re-audit under `docs/validation/re-audit-triggers.md`.

Local verification commands:

```bash
python tools/sync_core_data.py
python tests/generate_golden_vectors.py
python tools/validate_repository.py
python tools/generate_manifest.py --check
python tests/browser_smoke.py
```

The browser smoke script may report HOLD when the local container cannot execute Chromium. Required browser evidence must be collected from a supported environment or deployed review URL.
