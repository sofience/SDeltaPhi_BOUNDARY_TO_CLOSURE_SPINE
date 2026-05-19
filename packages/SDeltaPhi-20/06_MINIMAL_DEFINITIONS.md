# Minimal Definitions

## Δϕ

A change-rate / phase-difference measure over internal state or prediction distributions.

## Compression

A many-to-one mapping from inputs or histories into a bounded internal representation.

```text
many → one
```

## No-Exit Constraint

A non-invertibility condition where rollback cost exceeds update budget.

```text
No-exit constraint := rollback cost ≫ update budget
```

## Trace

The residual constraint left by non-invertible compression.

```text
Trace := residual constraint left by non-invertible compression
```

## Intuition

The internal marker or functional signal that a basin or route is locked enough to bypass further search.

```text
Intuition := marker(trace-dominant basin)
Intuition := "search is no longer worth it here"
```

## Editable Intuition

Intuition that accelerates selection while remaining revisable.

```text
Editable intuition := fast but revisable trace-guided selection
```
