# Human Required vs Human Bottleneck vs Delegation-Cost Bottleneck

SΔϕ-66 distinguishes human-required improvement, human-bottlenecked recursive improvement, and delegation-cost bottleneck.

## Human Required

Human intervention is structurally necessary.

The AI cannot reliably close the improvement loop without human involvement.

```text
AI can propose.
AI cannot reliably validate / apply / recover.
Human is structurally required.
```

## Human Bottleneck

The AI can substantially close the improvement loop, but human evaluation, approval, policy, or interpretation remains mandatory and slower than the AI cycle.

```text
AI_loop_capability ↑
AND TCC_human_eval / Cycle_AI > 1
```

## Delegation-Cost Bottleneck

The AI can perform the task, but delegating it remains more expensive than direct human execution.

```text
Capability_AI(i) sufficient
AND DCC_i > HumanDirectTCC_i
```

## Minimal distinction

```text
Human required = AI loop is not closed without humans.

Human bottleneck = AI loop can close, but human intervention remains a high-cost mandatory gate.

Delegation-cost bottleneck = AI can perform the task, but delegation remains more expensive than direct human execution.
```

## Risk claim

Recursive improvement is not the risk by itself.

Risk emerges when human intervention becomes a non-functional bottleneck that incentivizes bypass.

Delegation-cost bottleneck is different: it marks immature delegation infrastructure rather than AI incapability or immediate bypass risk.
