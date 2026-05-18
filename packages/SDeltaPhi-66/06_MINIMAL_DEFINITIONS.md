# Minimal Definitions

## Human Intervention Requirement

```text
HIR_i ∈ [0,5]
```

Scale:

```text
0 = human intervention unnecessary
1 = post-hoc review only
2 = approval / rejection required
3 = partial correction required
4 = major design required
5 = impossible without human leadership
```

## Transition Completion Cost

TCC measures the cost of completing a transition.

In SΔϕ-66, TCC is used as the underlayer for each human intervention requirement.

```text
TCC reference = 10.5281/zenodo.20116959
```

## Human Intervention Burden

```text
HIB(t) = Σ_i HIR_i(t) × TCC_i(t)
```

## Human Required

Human is structurally required when the AI loop cannot reliably define, validate, apply, or recover improvement without human intervention.

## Human Bottleneck

Human is a bottleneck when the AI loop can substantially proceed, but human review / approval / policy / interpretation remains slower than the AI improvement cycle.

```text
Cycle_AI < TCC_human_eval
```

## Human Dropout Gate

Human dropout occurs when humans are no longer necessary as a transition condition.

```text
HIR_total ≈ 0
OR
Cycle_AI < TCC_human_eval
```
