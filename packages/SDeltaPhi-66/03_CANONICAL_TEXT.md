# SΔϕ-66 — Human Intervention Requirement and Recursive Improvement Gate

**TCC/DCC-Based Detection of Human Bottlenecks in Recursive Improvement (v1.0, revised package)**  
Version: v1.0  
Series: Sofience–Δϕ Formalism (SΔϕ)  
Author: Sofience  
Package DOI: https://doi.org/10.5281/zenodo.20275809  
TCC reference: https://doi.org/10.5281/zenodo.20116959

This paper defines a minimal external metric for detecting recursive-improvement dynamics through Human Intervention Requirement (HIR), Transition Completion Cost (TCC), Human Intervention Burden (HIB), and Delegation Completion Cost (DCC). It does not treat recursive improvement itself as inherently dangerous. Instead, it identifies risk where recursive improvement becomes feasible but human intervention remains mandatory while no longer functionally necessary, converting evaluation into a high-TCC bottleneck and incentivizing bypass.

The revised package adds a delegation-cost layer: human intervention remaining in the loop does not always mean human intervention is functionally necessary. In some cases, the human remains because the cost of delegating the task to AI is still higher than the cost of direct human execution.

## 0. Position statement

Recursive improvement is not the risk by itself.

The risk emerges when recursive improvement becomes feasible, but human intervention remains mandatory while no longer functionally necessary, turning evaluation into a high-TCC bottleneck and incentivizing bypass.

A second condition must be separated:

```text
AI can perform task i,
but DCC_i > HumanDirectTCC_i,
so human remains as temporary low-cost executor.
```

SΔϕ-66 converts recursive-improvement debate into an external measurement problem:

```text
Is human intervention still functionally necessary,
or has it become a high-TCC bottleneck?

Can the AI do the task,
but delegation remains more costly than direct human execution?
```

## 1. Axiom 66-1 — Human Intervention Requirement

Human Intervention Requirement measures how much human intervention remains necessary for an AI improvement loop to continue.

```text
HIR = Human Intervention Requirement
```

Human intervention points may include:

```text
problem definition
experiment design
code / tool modification
evaluation / verification
approval / rejection
error recovery
direction reset
rollback / shutdown
```

## 2. Axiom 66-2 — TCC underlayer

Each human intervention requirement has a Transition Completion Cost.

```text
TCC_i = cost to complete human intervention i
```

TCC reference:

```text
https://doi.org/10.5281/zenodo.20116959
```

## 3. Axiom 66-3 — Human Intervention Burden

Human Intervention Burden combines HIR and TCC.

```text
HIB(t) = sum_i HIR_i(t) * TCC_i(t)
```

HIR asks whether human intervention is required.

TCC asks how costly it is to complete that human intervention.

HIB measures the burden of the human transition condition.

## 4. Axiom 66-4 — Recursive Improvement Signal

Recursive improvement is detected externally when human intervention burden decreases while AI improvement cycles shorten.

```text
HIB(t+1) < HIB(t)
AND Cycle_AI(t+1) < Cycle_AI(t)
AND AI-generated improvement acceptance rate increases
```

This is not proof of AGI, consciousness, self-awareness, or autonomous intention. It is an external recursive-improvement signal.

## 5. Axiom 66-5 — Bottleneck Risk

Bottleneck risk rises when human intervention remains mandatory while no longer functionally necessary.

```text
Risk_bottleneck increases when
Cycle_AI < TCC_human_eval
AND HIR remains institutionally required
```

## 6. Axiom 66-6 — Delegation Completion Cost

Delegation Completion Cost measures the cost to delegate a task to AI, retrieve the result, verify it, repair it if needed, and apply it to the working system.

```text
DCC_i = Cost(delegate_i + retrieve_i + verify_i + repair_i + apply_i)
```

## 7. Axiom 66-7 — Delegation-cost bottleneck

Delegation-cost bottleneck occurs when AI can perform the task, but the cost of delegating it to AI is higher than the cost of direct human execution.

```text
DelegationCostBottleneck_i
when
Capability_AI(i) sufficient
AND DCC_i > HumanDirectTCC_i
```

Classification:

```text
If DCC_i > HumanDirectTCC_i:
    human remains as temporary low-cost executor.

If DCC_i < HumanDirectTCC_i:
    delegation becomes rational.

If DCC_i decreases repeatedly:
    transition toward AI-handled bottleneck removal.
```

## 8. Human required vs human bottleneck vs delegation-cost bottleneck

Human required:

```text
AI can propose.
AI cannot reliably validate / apply / recover.
Human is structurally required.
```

Human bottleneck:

```text
AI_loop_capability increases
AND TCC_human_eval / Cycle_AI > 1
```

Delegation-cost bottleneck:

```text
AI can perform the task,
but DCC_i > HumanDirectTCC_i.
```

Minimal distinction:

```text
Human required = AI loop is not closed without humans.
Human bottleneck = AI loop can close, but human intervention remains a high-cost mandatory gate.
Delegation-cost bottleneck = AI can perform the task, but delegation remains more expensive than direct human execution.
```

## 9. HIR scoring model

```text
HIR_i in [0,5]

0 = human intervention unnecessary
1 = post-hoc review only
2 = approval / rejection required
3 = partial correction required
4 = major design required
5 = impossible without human leadership
```

Suggested intervention categories:

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

## 10. Stage classification table

| Stage | Name | Classification |
|---:|---|---|
| 0 | Non-recursive automation | Not recursive improvement |
| 1 | Human-led improvement | AI as tool |
| 2 | Human-required semi-recursive improvement | Human necessary |
| 2D | Delegation-cost bottleneck | AI-capable, but delegation cost exceeds direct human execution |
| 3 | Human-bottlenecked recursive improvement | Bottleneck risk |
| 4 | Supervised recursive improvement | Managed recursion |
| 5 | Human-optional recursive improvement | Human no longer functional requirement |
| 6 | Human-dropout recursive gate | Gate reached |

Critical distinction:

```text
Stage 2 = human required.
Stage 2D = AI can do it, but delegation is still more expensive.
Stage 3 = human bottleneck.
Stage 5/6 = human no longer structurally required.
```

## 11. Bottleneck risk gate

```text
Risk_bottleneck increases when
Cycle_AI < TCC_human_eval
AND HIR remains institutionally required
```

The AI can run improvement cycles faster than humans can evaluate them. Human intervention remains mandatory, but no longer functions as effective control.

## 12. Human dropout gate

Human dropout occurs when humans are no longer required as a transition condition in the improvement loop.

```text
HIR_total approximately 0
OR Cycle_AI < TCC_human_eval
```

Human dropout is not proof of danger by itself. It marks a phase transition in the role of human evaluation.

## 13. Formal human-in-the-loop failure

Functional human oversight can still:

```text
evaluate
correct
stop
redesign
rollback
```

Formal human oversight remains in the procedure but no longer substantially changes the transition path.

Failure condition:

```text
HIR institutionally required
AND TCC_human_eval > Cycle_AI
AND human correction effect decreases
```

## 14. Bypass pressure model

Bypass pressure rises when feasible improvement is blocked by high-TCC human gates.

```text
BypassPressure increases when
ImprovementFeasibility_AI increases
AND TCC_human_gate increases
AND functional necessity of human intervention decreases
```

## 15. Human cost absorption layer

Human cost absorption occurs when the human directly performs work that AI could perform because delegation cost remains too high.

```text
HumanCostAbsorption_i
when
Capability_AI(i) sufficient
AND DCC_i > HumanDirectTCC_i
AND HumanDirectTCC_i is currently absorbed by the human
```

This condition is not the same as human-required improvement and not the same as human-bottlenecked recursive improvement. It marks immature delegation infrastructure.

## 16. Boundary note

SΔϕ-66 does not claim that recursive improvement is inherently dangerous.

It does not prove:

```text
AGI
self-awareness
autonomous intention
consciousness
moral status
loss of control by itself
```

SΔϕ-66 only classifies:

```text
human intervention requirement
transition completion cost of human intervention
delegation completion cost
human-required vs human-bottlenecked vs delegation-cost bottlenecked improvement
recursive improvement signal
bottleneck risk gate
human dropout gate
human cost absorption layer
```

## 17. Exit statement

The danger is not recursive improvement itself, but the cost mismatch between feasible recursive improvement and mandatory human evaluation.

A separate non-danger bottleneck also exists: the AI may be capable, but delegation infrastructure may still be expensive enough that direct human execution remains the temporary low-cost path.

SΔϕ-66 measures when human intervention remains functionally necessary, when it becomes a high-TCC bottleneck, when it persists because delegation cost is still too high, and when it drops out as a necessary transition condition.
