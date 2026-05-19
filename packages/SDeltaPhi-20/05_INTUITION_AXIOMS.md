# Intuition Axioms

## Axiom 20-1 — Boundedness

Any persistent system has bounded resources; therefore it must compress.

```text
Persistent system → bounded resources → compression required
```

## Axiom 20-2 — Irreversible Locking

Compression becomes non-invertible when rollback cost greatly exceeds update budget.

```text
rollback cost ≫ update budget
```

## Axiom 20-3 — Trace Re-entry

Non-invertible compression leaves traces that re-enter as constraints on future transitions.

```text
Non-invertible compression → trace → future transition bias
```

## Axiom 20-4 — Intuition Signal

Intuition is the system's marker of trace-dominant basins.

```text
Intuition := "search is no longer worth it here"
```

## Axiom 20-5 — Cross-System Convergence

Different substrates under similar constraints converge to similar basins, producing similar intuition-like correspondences.

```text
similar constraints → similar basins → intuition-like convergence
```

## Boundary

These axioms do not claim a shared semantic ontology across species or models.

They claim shared constraint-driven convergence.
