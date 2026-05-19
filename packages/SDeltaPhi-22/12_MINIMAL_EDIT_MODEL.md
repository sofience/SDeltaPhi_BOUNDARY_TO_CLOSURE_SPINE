# Minimal Edit Model

AEP applies the smallest edit to authority A that resolves trigger τ.

```text
A′ = MinimalEdit(A, τ)
```

## Function

Minimal edit prevents over-correction.

## Failure modes

```text
no edit → closure risk
excessive edit → drift risk
minimal edit → open persistence
```

## Rule

Do not maximize change.

Do not preserve authority unchanged.

Edit only enough to restore finite-cost revisability.
