# Local Adaptation Axioms

## Axiom 67-1 — Core is not Adapter

SΔϕ core invariants and local adaptation rules must be separated.

```text
Core != Adapter
```

## Axiom 67-2 — Local Adaptation Preserves Core Invariants

A local AI system may adapt routing, thresholds, output level, and audit procedure only if core invariants remain preserved.

```text
LocalAdaptation valid iff CoreInvariants preserved
```

## Axiom 67-3 — Adapter Changes Call Conditions, Not Root Commitments

The adapter may change when and how modules are called, but may not erase trace discipline, UMR discipline, cost discipline, or reversibility boundaries.

```text
Adapter may modify routing.
Adapter may not delete core constraints.
```

## Axiom 67-4 — Local Thresholds Must Be Declared

Any local threshold used for risk, escalation, human review, rollback, refusal, audit, or output restriction must be explicitly declared.

```text
local threshold -> declared / logged / testable
```

## Axiom 67-5 — Forks Require Compatibility Tests

A local fork becomes valid only when it passes compatibility tests against core invariants.

```text
fork valid iff compatibility_tests_passed
```

## Axiom 67-6 — Adaptation Must Reduce Local Judgment Cost without Externalizing Hidden Cost

A local adaptation is successful only if it reduces local routing cost without externalizing verification, restoration, or responsibility cost.

```text
valid adaptation =
local cost down
AND hidden externalized cost not up
```
