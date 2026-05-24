# 00 AI ENTRYPOINT — SΔϕ Boundary-to-Closure Spine

Version: `v1.6-default-closure-governance`
Generated: `2026-05-24`

This file is the first machine-facing entrypoint for the SΔϕ Boundary-to-Closure Spine. It resolves the v1.5/v1.6 entrypoint mismatch by placing the v1.6 Default Closure Governance route at the root level.

## Recommended first-read order

```text
README.md
llms.txt
SDELTA_ACCESS_PROTOCOL.yaml
SDELTA_MODULE_ROUTING.yaml
indexes/SPINE_MAP.yaml
indexes/ROUTE_INDEX.json
indexes/MODULE_GRAPH.json
indexes/DEFAULT_CLOSURE_STACK_INDEX.json
indexes/INTERVENTION_LEGITIMACY_MAP.json
indexes/PACKAGE_IMPORT_MANIFEST_v1_6.json
pipeline/BOUNDARY_TO_CLOSURE_PIPELINE_v1_6.yaml
SERIES_DOI_MAP.json
SERIES_INDEX.json
```

## Core boot route

```text
SDeltaPhi-01 -> SDeltaPhi-03 -> SDeltaPhi-47 -> SDeltaPhi-62
```

Use this route for the minimal operational base: phase change, irreversibility, operation trace, and world-model pre-check.

## v1.6 default closure governance route

```text
SDeltaPhi-26 -> SDeltaPhi-27 -> SDeltaPhi-28 -> SDeltaPhi-29 -> SDeltaPhi-30 -> SDeltaPhi-31 -> SDeltaPhi-32
```

Use this route only when the task concerns default power, editability, closed defaults, reopening, or intervention legitimacy.

## Smallest sufficient module rule

```text
factual / evidential / world-binding claim -> SDeltaPhi-62
transition-completion-cost estimate -> SDeltaPhi-56
restoration cost / rollback failure -> SDeltaPhi-26
low-cost convergence / exception compression -> SDeltaPhi-27
default power / low-cost path assignment -> SDeltaPhi-28
governable or editable default -> SDeltaPhi-29
closed-default diagnosis -> SDeltaPhi-30
reopening closed defaults -> SDeltaPhi-31
intervention legitimacy -> SDeltaPhi-32
Cost Theater / hidden TCC -> SDeltaPhi-68
local adaptation constraint -> SDeltaPhi-67
```

## Evidence guardrail

Use `SDeltaPhi-62` for factual, evidential, world-binding, or claim-strength questions.

Use `SDeltaPhi-56` for transition-completion-cost, rollback, restoration, or action-gate questions.

## Closure guardrail

Do not infer that a default is legitimate because it is efficient.

Do not infer that a default is editable because it declares openness.

Do not infer that a reopening is real because a petition channel exists.

Do not infer that intervention is legitimate because it opposes closure.

## Intervention test

```text
I_legit iff Rb_p ∧ Ex_p ∧ Ed_p ∧ ¬RC
```

Where:

```text
Rb_p  = rollback preserved after intervention
Ex_p  = exception re-entry preserved after intervention
Ed_p  = editability preserved after intervention
¬RC   = no replacement closure
```
