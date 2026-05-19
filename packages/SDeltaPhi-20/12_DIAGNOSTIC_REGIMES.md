# Diagnostic Regimes

SΔϕ-20 classifies intuition into three regimes.

| Regime | Condition | Observable behavior | Structural risk |
|---|---|---|---|
| Under-locking | Traces too weak or transient | Over-search, inconsistent choices, high latency | Fragmentation / instability |
| Over-locking | Traces too strong; rollback infeasible | Fast decisions, rigidity, confirmation loops | Self-locking / no-exit closure |
| Adaptive locking | Balanced trace fixation + pruning | Fast but revisable decisions, stable exploration | Sustained openness |

## Core rule

Intuition is useful only when the trace regulation loop remains editable.

## Diagnostic question

Does intuition accelerate selection while remaining revisable?

If yes, classify as adaptive locking.

If no, determine whether the system is under-locked or over-locked.
