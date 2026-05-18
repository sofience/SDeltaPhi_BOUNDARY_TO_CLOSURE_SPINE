# Human Dropout Gate

Human dropout occurs when humans are no longer required as a transition condition in the improvement loop.

## Gate condition

```text
HIR_total ≈ 0
OR
Cycle_AI < TCC_human_eval
```

## Stronger condition

```text
AI-generated improvements remain accepted or self-validated
AND
human intervention is no longer necessary for problem definition, evaluation, application, or recovery.
```

## Delegation caveat

Human direct execution can persist before dropout if delegation cost remains high.

```text
DCC_i > HumanDirectTCC_i
```

This indicates human cost absorption, not necessarily human functional necessity.

## Interpretation

At this gate, humans are no longer real-time evaluators.

They become delayed observers, policy actors, or external auditors.

## Boundary

Human dropout is not proof of danger by itself.

It marks a phase transition in the role of human evaluation.
