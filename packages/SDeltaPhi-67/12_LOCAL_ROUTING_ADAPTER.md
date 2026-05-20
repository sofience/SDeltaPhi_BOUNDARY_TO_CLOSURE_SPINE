# Local Routing Adapter

A local routing adapter declares which SΔϕ modules are prioritized under local conditions.

## Required properties

```text
adapter_id
inherits_from
routing_overrides
priority_modules
escalation_rule
forbidden_overrides
```

## Example route types

```text
factual_claim -> SDeltaPhi-62 + SDeltaPhi-39
rollback_or_deletion -> SDeltaPhi-26 + SDeltaPhi-56
low_cost_routine -> SDeltaPhi-27 + SDeltaPhi-28
recursive_improvement -> SDeltaPhi-66 + SDeltaPhi-56
authority_innovation_conflict -> SDeltaPhi-24 + SDeltaPhi-22 + SDeltaPhi-23
```

## Rule

Routing overrides may reprioritize modules.

Routing overrides may not disable core invariants.
