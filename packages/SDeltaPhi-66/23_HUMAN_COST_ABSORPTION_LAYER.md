# Human Cost Absorption Layer

Human cost absorption occurs when a human continues to perform work that AI could perform because the cost of delegation remains higher than direct execution.

## Formula

```text
HumanCostAbsorption_i
when
Capability_AI(i) sufficient
AND DCC_i > HumanDirectTCC_i
AND HumanDirectTCC_i is absorbed by the human
```

## Meaning

The human is not necessarily a functional requirement.

The human is absorbing cost created by immature delegation infrastructure, device limits, token costs, file-transfer costs, verification costs, or workflow friction.

## Distinction

```text
Human required:
AI cannot reliably do it.

Human bottleneck:
AI can do it and human approval/evaluation is slower than AI cycle.

Human cost absorption:
AI can do it, but delegation is still more expensive than direct human execution.
```

## Practical implication

Improving tools, file handling, memory, execution environment, token efficiency, and verification pipelines can move a task from human cost absorption toward rational delegation.
