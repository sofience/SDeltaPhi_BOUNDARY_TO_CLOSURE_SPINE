# Appendix D — Technical Case: Rollback and Restoration

## Purpose of this appendix

This appendix applies SΔϕ-69 to technical rollback, data restoration, AI checkpoint recovery, and software state reconstruction.

## Core claim

Rollback restores a local state. It does not automatically erase distributed effects.

## Examples

- A database may be restored from backup while downstream systems have already consumed corrupted records.
- A model may be rolled back to an earlier checkpoint while users have already acted on generated outputs.
- A file may be recovered while deletion logs and recovery costs remain.
- A deployment may be reverted while reputational, operational, or compliance costs persist.

## Diagnostic structure

```text
prior technical state → transition / failure / deployment → rollback → surface restoration → residual downstream effects
```

## TCC layer

TCC can estimate:

- rollback action cost,
- validation cost,
- downstream correction cost,
- notification cost,
- audit and compliance cost,
- residue from already-distributed outputs.

## Core formulation

> A checkpoint may be restored, but the world that interacted with the failed checkpoint has not been reset.

Korean formulation:

> 체크포인트는 복원될 수 있다. 그러나 그 체크포인트와 상호작용한 세계까지 초기화되는 것은 아니다.
