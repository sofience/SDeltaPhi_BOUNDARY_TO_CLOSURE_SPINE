# Minimal Definitions

## Core

The set of SΔϕ invariants that cannot be removed without breaking compatibility.

```text
Core = non-removable invariant layer
```

## Adapter

A local layer that changes routing priority, thresholds, output level, escalation rules, or audit formats for a specific AI system or domain.

```text
Adapter = local routing / threshold / output / audit layer
```

## Local Context Profile

A structured description of the AI system's operating environment.

Includes:

```text
domain
risk level
tool access
memory access
action authority
human review availability
rollback capacity
evidence requirements
```

## Local Routing Adapter

A local override that determines which SΔϕ modules are prioritized under local conditions.

## Local Threshold Map

A declared set of thresholds for escalation, refusal, audit, human review, rollback, or output restriction.

## Local Risk Profile

A domain-specific account of harm potential, action authority, rollback capacity, verification burden, and restoration cost exposure.

## Compatibility Test

A test that checks whether local adaptation preserves SΔϕ core invariants.

## Forbidden Mutation

A local change that breaks core compatibility.

## Fork Declaration

A statement that the local adaptation has diverged enough to require explicit naming, versioning, and compatibility reporting.
