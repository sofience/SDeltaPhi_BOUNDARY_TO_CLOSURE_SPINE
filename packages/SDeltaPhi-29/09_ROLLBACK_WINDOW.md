# Rollback Window

Reversibility is not merely formal.

Rollback Window marks the interval in which revision remains materially feasible.

```text
if t < t*_r:
    rollback remains operational

if t >= t*_r:
    restoration cost rises sharply
```

A rollback window is active only while returning, revising, or reopening remains feasible at acceptable transition completion cost.
