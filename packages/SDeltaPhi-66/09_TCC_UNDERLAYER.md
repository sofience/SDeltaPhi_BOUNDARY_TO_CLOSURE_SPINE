# TCC Underlayer

SΔϕ-66 uses Transition Completion Cost as the underlayer for human intervention requirements.

TCC reference:

```text
https://doi.org/10.5281/zenodo.20116959
```

## Role

HIR asks:

```text
Is human intervention required?
```

TCC asks:

```text
How costly is it to complete that human intervention?
```

## Combined role

```text
Human Intervention Burden = HIR × TCC
```

## Why TCC is needed

Two interventions can have the same HIR score but very different completion costs.

Example:

```text
approval required, low TCC
→ still manageable

approval required, high TCC
→ human bottleneck risk
```
