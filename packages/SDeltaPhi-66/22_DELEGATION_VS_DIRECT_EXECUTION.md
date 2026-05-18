# Delegation vs Direct Execution

SΔϕ-66 distinguishes direct human execution from AI delegation.

## Direct human execution

```text
HumanDirectTCC_i = cost for the human to perform task i directly
```

## AI delegation

```text
DCC_i = cost to delegate task i to AI, retrieve, verify, repair, and apply the result
```

## Decision rule

```text
DCC_i > HumanDirectTCC_i
→ direct human execution remains the temporary low-cost path

DCC_i < HumanDirectTCC_i
→ AI delegation becomes the lower-cost path
```

## Interpretation

When direct human execution remains lower-cost, this does not prove that the human is structurally necessary.

It indicates a delegation infrastructure bottleneck.

## Transition signal

```text
DCC_i(t+1) < DCC_i(t)
```

If DCC decreases repeatedly, delegation infrastructure is improving and human cost absorption may decline.
