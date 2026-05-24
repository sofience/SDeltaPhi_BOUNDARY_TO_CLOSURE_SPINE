# CHANGELOG — v1.6 Default Closure Governance Spine

Generated: `2026-05-24`

## Summary

v1.6 upgrades the SΔϕ Boundary-to-Closure Spine from closure detection and event fixation into default-closure governance and intervention legitimacy routing.

The new root route is:

```text
SDeltaPhi-26 -> SDeltaPhi-27 -> SDeltaPhi-28 -> SDeltaPhi-29 -> SDeltaPhi-30 -> SDeltaPhi-31 -> SDeltaPhi-32
```

## Added

- Root-level v1.6 entrypoint language.
- Default Closure Governance route.
- Intervention Legitimacy route.
- Cost Theater support route.
- Local Adaptation guardrail route.
- `indexes/ROUTE_INDEX.json`.
- `indexes/MODULE_GRAPH.json`.
- `indexes/SPINE_MAP.yaml`.
- `FILE_OPERATIONS_v1_6.yaml`.
- `scripts/validate_v1_6_default_closure.py`.

## Replaced

- `README.md`: rewritten from v1.5 event/authority/fixation focus to v1.6 default-closure governance focus.
- `00_AI_ENTRYPOINT.md`: rewritten to remove stale v1.5 first-read and absent index references.
- `MANIFEST.txt`: rewritten as v1.6 replacement/new/deprecate manifest.
- `llms.txt`: rewritten as compact AI-ingestion routing entry.
- `SDELTA_MODULE_ROUTING.yaml`: upgraded to include v1.6 routes and negative activation rules.
- `SDELTA_ACCESS_PROTOCOL.yaml`: upgraded to include v1.6 ingestion order and closure/intervention guardrails.
- `routing/SDELTA_MODULE_ROUTING.yaml`: mirrored from root routing file.
- `routing/SDELTA_ACCESS_PROTOCOL.yaml`: mirrored from root access protocol.

## Deprecated / archive recommended

Move the following to `docs/legacy/` rather than deleting if provenance is desired:

```text
CHANGELOG_v1_4_1_FORMAT_FIX.md
CHANGELOG_v1_4_ROOT_SPINE.md
AI_READABILITY_FORMAT_FIX_REPORT.md
MIRROR_STATUS.md
PACKAGE_PRIORITY.md
PATCH_CHECKSUMS.sha256
checksums.sha256
```

Regenerate checksums after moving or replacing files.

## Core formulas added to root routing

```text
SDeltaPhi-29: D* governable iff Ed ∧ Ad ∧ Wr ∧ Ce
SDeltaPhi-30: D* editable-real iff Rv ∧ Rb ∧ Ex ∧ Ad
SDeltaPhi-31: D*closed -> operationally open iff T_r ∧ C_a ∧ R_o ∧ P_r
SDeltaPhi-32: I_legit iff Rb_p ∧ Ex_p ∧ Ed_p ∧ ¬RC
```

## Failure modes explicitly guarded

- Jumping from default detection to moral judgment.
- Treating declared openness as operational editability.
- Treating petition as automatic reopening.
- Treating intervention as automatically legitimate.
- Using case patterns as legal or factual conclusions.
- Opposing closure by installing replacement closure.
