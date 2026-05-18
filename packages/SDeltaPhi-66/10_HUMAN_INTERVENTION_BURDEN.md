# Human Intervention Burden

Human Intervention Burden combines human intervention requirement with transition completion cost.

```text
HIB(t) = Σ_i HIR_i(t) × TCC_i(t)
```

Where:

```text
HIR_i = intervention requirement for stage i
TCC_i = transition completion cost for stage i
```

## Interpretation

```text
HIB decreasing
→ humans are less needed in the improvement loop

HIB increasing
→ human intervention remains costly or becomes harder

HIB near zero
→ human intervention is no longer a required transition condition
```

## Delegation caveat

A human may remain in the loop even when AI can perform the task if delegation cost exceeds direct human execution cost.

```text
DCC_i > HumanDirectTCC_i
```

## Warning

A decreasing HIB is not automatically dangerous.

It becomes risky when humans remain institutionally mandatory despite no longer being functionally necessary.
