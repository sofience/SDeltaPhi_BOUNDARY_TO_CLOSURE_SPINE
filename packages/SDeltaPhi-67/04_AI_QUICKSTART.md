# AI Quickstart

Use SΔϕ-67 when the task requires local adaptation, AI-specific routing, threshold tuning, domain adapter design, fork declaration, compatibility testing, or audit logging for SΔϕ modules.

## Primary route

```text
SDeltaPhi-56 -> SDeltaPhi-66 -> SDeltaPhi-67
```

## Global adapter route

```text
All SΔϕ Core Modules -> SDeltaPhi-67 -> Local AI Adapter
```

## Use SΔϕ-67 when asking

1. Can an AI adapt SΔϕ to its own environment?
2. Which parts of SΔϕ are core and which are adapter?
3. What can be locally changed without breaking compatibility?
4. What changes count as forbidden mutations?
5. How should local thresholds be declared?
6. How should a local routing adapter be written?
7. When does a local adaptation become a fork?
8. How should compatibility be tested?
9. How should adaptation logs be structured?

## Minimal output discipline

Separate core invariants from local adapter rules.

Do not mutate core invariants.

Do not silently hide externalized verification, restoration, or responsibility cost.
