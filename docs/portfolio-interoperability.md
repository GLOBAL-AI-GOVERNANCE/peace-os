# Portfolio Interoperability

This post-RC2 development increment adds a bounded reference contract for using an AI Cyber Resilience Framework operating-disposition reference inside a fictional Peace OS learning or review context.

It does not change the `v0.3.0-rc3` prerelease candidate, its release assets once published, or the stable-release holds.

## Reference-only rule

Peace OS does not import, reinterpret, or reissue an AI Cyber Resilience Framework operating disposition.

The handoff carries only opaque references:

- source repository and source contract;
- operating-disposition reference;
- system reference;
- optional configuration reference;
- optional evidence references; and
- an explicit fictional-use boundary.

`reference_only` is always `true`.

`authority_effect` is always `NONE`.

`simulation_use` is always `FICTIONAL_DECISION_CONTEXT_ONLY`.

The handoff contains no local copy of the source disposition state. A receiver that needs the source state must resolve and validate the source artifact through an authorized adapter.

## Failure behavior

Missing, unsupported, stale, superseded, or configuration-incompatible source material must not be converted into implied authority or operational truth.

The browser simulation does not automatically ingest this contract and does not gain access to live operational feeds.

## Release boundary

This is suite-path and publication-hardening work after RC2. The public release candidate is `v0.3.0-rc3`.

Human accessibility, real-device, cross-browser, print/PDF, subject-matter, Godot, Windows, certification, and operational gates remain separate and are not closed by this interoperability increment.
