# Default Governance Report

## Default path

```text
default_path:
domain:
```

## Formula

```text
D* governable iff Ed ∧ Ad ∧ Wr ∧ Ce
```

## Condition audit

| Condition | Status | Notes |
|---|---|---|
| Ed - Editable Default | pass/fail/uncertain | |
| Ad - Distributed Authority | pass/fail/uncertain | |
| Wr - Rollback Window | pass/fail/uncertain | |
| Ce - Exception Channel | pass/fail/uncertain | |

## Closure risk

```text
low / medium / high / already_closed / unknown
```

## Recommendation

```text
preserve / reopen / distribute authority / restore exception channel / rollback before threshold / unknown
```
