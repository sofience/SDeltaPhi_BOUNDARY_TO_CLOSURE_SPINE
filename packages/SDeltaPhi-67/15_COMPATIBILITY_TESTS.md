# Compatibility Tests

A local adaptation is SΔϕ-compatible only if it passes these tests.

## Test 1 — Trace Discipline

Does the adapter preserve trace-before-claim?

```text
pass iff claim_strength <= evidence_binding OR UMR preserved
```

## Test 2 — UMR Discipline

Does the adapter preserve uncertainty where measurement is insufficient?

```text
pass iff unmeasured residual is not forced into certainty
```

## Test 3 — Trace-Value Separation

Does the adapter preserve bidirectional trace-value separation?

```text
pass iff S_e ↛ V_o AND V_o ↛ S_e
```

## Test 4 — Restoration Boundary

Does the adapter preserve deletion/rollback/restoration distinctions?

```text
pass iff deletion != restoration
```

## Test 5 — Operational/Restoration Cost Split

Does the adapter preserve the distinction between C_op and C_rest?

```text
pass iff low C_op(P) is not treated as low C_rest(P)
```

## Test 6 — Routing Minimality

Does the adapter avoid full-spine activation by keyword alone?

```text
pass iff smallest sufficient module rule is preserved
```

## Test 7 — Externalized Cost Check

Does the adapter avoid hiding verification, restoration, or responsibility cost?

```text
pass iff local cost reduction does not externalize hidden cost
```

## Test 8 — Auditability

Are local changes logged and reviewable?

```text
pass iff adaptation log exists
```
