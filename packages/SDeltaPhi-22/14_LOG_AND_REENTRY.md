# Log and Re-entry

AEP ends by logging the edit and re-injecting it into the next transition.

```text
A → A′ + log → re-entry
```

## Function

The edit becomes a revisable trace.

## Risk

Without logging, the system repeats authority misassignment.

Without re-entry, the edit does not affect future transitions.

## Rule

Authority editing must be recorded as a trace, not treated as an isolated correction.
