# SΔϕ Repo Integration Patch v1.6 — Default Closure Governance Spine

Target repository:

```text
https://github.com/sofience/SDeltaPhi_BOUNDARY_TO_CLOSURE_SPINE
```

This package provides new index, routing, pipeline, documentation, README patch, llms.txt patch, and validation files for integrating the new SΔϕ packages into the existing repository.

## Core update

Extend the default-power bridge:

```text
SDeltaPhi-26 -> SDeltaPhi-27 -> SDeltaPhi-28 -> SDeltaPhi-29 -> SDeltaPhi-30 -> SDeltaPhi-31 -> SDeltaPhi-32
```

Meaning:

```text
event fixation
-> low-cost convergence
-> default power
-> editable default conditions
-> closed default diagnosis
-> reopening intervention
-> legitimate intervention audit
```

## New packages to import

```text
SDeltaPhi-29
SDeltaPhi-30
SDeltaPhi-31
SDeltaPhi-32
SDeltaPhi-67
SDeltaPhi-68
```

## Installation

1. Copy `indexes/*` to repo `/indexes/`.
2. Copy `routing/*` to repo `/routing/`.
3. Copy `pipeline/*` to repo `/pipeline/`.
4. Copy `docs/*` to repo `/docs/`.
5. Copy `scripts/*` to repo `/scripts/`.
6. Apply `patches/README_v1_6_INSERT.md` to `README.md`.
7. Apply `patches/llms_v1_6_INSERT.txt` to `llms.txt`.
8. Extract package ZIPs into `/packages/SDeltaPhi-XX/`.
9. Store original ZIPs in `/archives/`.
10. Run `python scripts/validate_sdelta_v1_6_routes.py`.

## Deletion rule

Do not hard-delete provenance files. Move malformed duplicates or obsolete route drafts to `/deprecated/` or `/archives/legacy/`.
