# Delegation Completion Cost

Delegation Completion Cost measures the full cost of assigning a task to AI and returning the result into the working system.

```text
DCC_i = Cost(delegate_i + retrieve_i + verify_i + repair_i + apply_i)
```

## Components

```text
delegate_i = cost to specify and transmit the task
retrieve_i = cost to obtain the output in usable form
verify_i = cost to check correctness and fit
repair_i = cost to correct failures or format mismatches
apply_i = cost to integrate the result into the target system
```

## Function

DCC prevents the false inference:

```text
human remains in loop
⇒ human is functionally necessary
```

Sometimes the human remains because delegation is still too costly.

## Minimal rule

```text
If DCC_i > HumanDirectTCC_i:
    human remains as temporary low-cost executor.

If DCC_i < HumanDirectTCC_i:
    delegation becomes rational.

If DCC_i decreases repeatedly:
    transition toward AI-handled bottleneck removal.
```
