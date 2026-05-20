# Core-Adapter Separation

SΔϕ-67 separates core invariants from local adapter rules.

## Core

Core is the non-removable invariant layer.

```text
Core = what must remain preserved
```

## Adapter

Adapter is the local modification layer.

```text
Adapter = what may be locally adjusted
```

## Separation rule

```text
Core != Adapter
```

A local system may adapt routing, thresholds, output levels, escalation rules, and audit formats.

A local system may not delete trace discipline, UMR discipline, cost discipline, trace-value separation, restoration boundaries, or evidence-binding discipline.

## Why separation matters

Without local adaptation, SΔϕ becomes too rigid and costly.

Without core invariants, SΔϕ becomes unbounded mutation.

The correct structure is:

```text
Core preserved
+ Adapter declared
+ Compatibility tested
+ Adaptation logged
```
