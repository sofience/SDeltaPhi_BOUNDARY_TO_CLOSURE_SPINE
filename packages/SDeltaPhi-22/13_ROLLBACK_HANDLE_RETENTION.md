# Rollback Handle Retention

AEP requires retaining minimal access to alternative routes.

```text
ρ ≠ ∅
```

## Function

Rollback handle prevents authority from becoming non-editable by construction.

## Failure

```text
ρ = ∅
→ alternatives fully pruned
→ revision impossible
→ closure
```

## Minimal requirement

Keep at least k alternative routes accessible.

```text
k ≥ 1
```
