# Local Context Profile

A local context profile declares the environment in which SΔϕ is adapted.

## Required fields

```text
adapter_id
adapter_version
system_type
domain
operator
deployment_context
memory_access
tool_access
action_authority
external_world_write_access
domain_risk
user_harm_potential
rollback_capacity
evidence_requirement
default_sdelta_routes
required_modules
```

## Function

The local context profile prevents silent environmental assumptions.

If the system can act in the external world, use stricter routing and audit rules.

If rollback capacity is low, require stronger restoration-cost checks.

If evidence requirement is strict, prioritize SDeltaPhi-62 and SDeltaPhi-39.
