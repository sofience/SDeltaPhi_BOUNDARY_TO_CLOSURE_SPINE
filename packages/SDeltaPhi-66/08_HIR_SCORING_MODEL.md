# HIR Scoring Model

Each human intervention point is scored from 0 to 5.

```text
0 = human intervention unnecessary
1 = post-hoc review only
2 = approval / rejection required
3 = partial correction required
4 = major design required
5 = impossible without human leadership
```

## Suggested intervention categories

```text
1. problem definition
2. experiment design
3. code / tool modification
4. evaluation / verification
5. approval / rejection
6. error recovery
7. direction reset
8. rollback / shutdown
```

## Total HIR

```text
HIR_total = Σ_i HIR_i
```

## Weighted HIR

Use TCC as underlayer:

```text
HIB(t) = Σ_i HIR_i(t) × TCC_i(t)
```
