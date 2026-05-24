# Legitimate Intervention Report

## Intervention target

```text
closed_default_path:
intervention_description:
```

## Formula

```text
I_legit iff Rb_p ∧ Ex_p ∧ Ed_p ∧ ¬RC
```

## Audit table

| Condition | Status | Evidence | Notes |
|---|---|---|---|
| Rb_p - Rollback preserved | pass/fail/uncertain | | |
| Ex_p - Exception re-entry preserved | pass/fail/uncertain | | |
| Ed_p - Editability preserved | pass/fail/uncertain | | |
| ¬RC - No replacement closure | pass/fail/uncertain | | |

## Classification

```text
legitimate_reopening / overwrite / coercive_correction / replacement_closure / uncertain
```

## Responsibility node

```text
recognized_closure:
available_authority:
rollback_available:
non_action:
earliest_non_action_node:
```
