# Stage Classification Table

| Stage | Name | AI loop capability | Human role | Classification |
|---:|---|---|---|---|
| 0 | Non-recursive automation | Low | Human defines and evaluates | Not recursive improvement |
| 1 | Human-led improvement | Low-medium | Human leads | AI as tool |
| 2 | Human-required semi-recursive improvement | Medium | Human structurally required | Human necessary |
| 3 | Human-bottlenecked recursive improvement | Medium-high | Human approval/evaluation is slower than AI loop | Bottleneck risk |
| 4 | Supervised recursive improvement | High | Human as release/audit/rollback gate | Managed recursion |
| 5 | Human-optional recursive improvement | Very high | Human optional or policy-retained | Human no longer functional requirement |
| 6 | Human-dropout recursive gate | Closed AI loop | Human is post-hoc observer | Gate reached |

## Critical distinction

```text
Stage 2 = human required.
Stage 3 = human bottleneck.
Stage 5/6 = human no longer structurally required.
```
