# Authority Editing Protocol — AEP

AEP is the minimal re-entry governance loop that keeps authority revisable at finite cost.

## Step 1 — Detect τ

Detect conflict, error, external perturbation, or closure precursor.

```text
detect τ
```

## Step 2 — Freeze Execution Softly

Maintain execution but introduce damping.

```text
continue execution
but reduce update velocity
and keep A revisable
```

## Step 3 — Isolate A from I

Separate intuition marker from assigned authority.

```text
I ≠ A
```

## Step 4 — Estimate Revision Cost

Compare revision cost against continuation cost under current authority.

```text
RevisionCost(A) vs ContinuationCost(A)
```

## Step 5 — Apply Minimal Edit

Perform the smallest edit to A that resolves τ.

```text
A′ = MinimalEdit(A, τ)
```

## Step 6 — Retain Rollback Handle

Keep at least k alternative routes accessible.

```text
ρ ≠ ∅
```

## Step 7 — Log + Re-entry

Record the edit and re-inject it into the next transition.

```text
A → A′ + log → re-entry
```
