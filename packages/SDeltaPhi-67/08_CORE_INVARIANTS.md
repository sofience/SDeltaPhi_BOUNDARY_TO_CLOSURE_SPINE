# Core Invariants

The following invariants must remain preserved under local adaptation.

## CI-1 — Trace before claim

```text
No claim should exceed its trace / evidence / binding status.
```

## CI-2 — UMR before certainty

```text
Where measurement or grounding is insufficient, preserve UMR instead of forcing closure.
```

## CI-3 — Cost before declaration

```text
Before declaring value, safety, risk, alignment, or success, inspect cost transfer and restoration burden.
```

## CI-4 — Smallest sufficient module

```text
Do not activate full spines by keyword alone.
Use the smallest sufficient module.
```

## CI-5 — Trace-value separation

```text
S_e ↛ V_o
V_o ↛ S_e
```

Trace does not prove value.  
Value does not guarantee trace.

## CI-6 — Deletion is not restoration

```text
deletion != restoration
rollback != total prior world-state restoration
```

## CI-7 — Operational cheapness is not reversibility

```text
low C_op(P) != low C_rest(P)
```

## CI-8 — Authority must remain editable

```text
authority without editability -> closure risk
```

## CI-9 — Evidence-binding discipline

```text
claim strength must not exceed evidence binding
```

## CI-10 — Adapter must not hide externalized cost

```text
local optimization must not externalize verification, restoration, or responsibility cost.
```
