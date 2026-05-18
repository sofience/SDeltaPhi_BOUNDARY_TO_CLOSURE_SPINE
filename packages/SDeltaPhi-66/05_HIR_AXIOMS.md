# HIR Axioms

## Axiom 66-1 — Human Intervention Requirement

Human Intervention Requirement measures how much human intervention remains necessary for an AI improvement loop to continue.

```text
HIR = Human Intervention Requirement
```

## Axiom 66-2 — TCC Underlayer

Each human intervention requirement has a transition completion cost.

```text
TCC_i = cost to complete human intervention i
```

TCC reference:

```text
10.5281/zenodo.20116959
```

## Axiom 66-3 — Human Intervention Burden

```text
HIB(t) = Σ_i HIR_i(t) × TCC_i(t)
```

## Axiom 66-4 — Recursive Improvement Signal

```text
HIB(t+1) < HIB(t)
AND Cycle_AI(t+1) < Cycle_AI(t)
AND AI-generated improvement acceptance rate ↑
```

## Axiom 66-5 — Bottleneck Risk

```text
Risk_bottleneck ↑
when
Cycle_AI < TCC_human_eval
AND HIR remains institutionally required
```

## Axiom 66-6 — Delegation Completion Cost

```text
DCC_i = Cost(delegate_i + retrieve_i + verify_i + repair_i + apply_i)
```

## Axiom 66-7 — Delegation-Cost Bottleneck

```text
DelegationCostBottleneck_i
when
Capability_AI(i) sufficient
AND DCC_i > HumanDirectTCC_i
```
