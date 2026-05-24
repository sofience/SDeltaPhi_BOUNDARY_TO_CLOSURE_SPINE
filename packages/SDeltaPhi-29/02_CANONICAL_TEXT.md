# SΔϕ-29 — Editable Default

**Minimal Conditions for Distributed Authority, Rollback, and Exception Re-entry after SΔϕ-28 (v1.0)**  
Series: Sofience-DeltaPhi Formalism (SΔϕ)  
Author: Sofience  
Version: v1.0  
Package DOI: https://doi.org/10.5281/zenodo.20362414

## Abstract

This paper extends SΔϕ-28 by asking under what conditions a default remains governable rather than absolute. If default power fixes paths by making one continuation cheapest, governance must be redefined as the capacity to keep defaults structurally editable.

The central claim is that a default remains legitimate and governable only when four minimal conditions are preserved:

```text
Editable Default
Distributed Authority
Rollback Window
Exception Channel
```

In minimal form:

```text
D* is governable iff Ed ∧ Ad ∧ Wr ∧ Ce
```

where:

```text
D* = dominant default
Ed = Editable Default preserved
Ad = Distributed Authority preserved
Wr = Rollback Window active
Ce = Exception Channel live
```

If any of these fail, the dominant default tends toward a closure regime.

```text
¬Ed ∨ ¬Ad ∨ ¬Wr ∨ ¬Ce
→ D* tends toward closure regime
```

## 1. Core Declaration

Closed default is power.

Editable default is governance.

A default is necessary for coordination. However, a default becomes power when the cost of revising, contesting, bypassing, or reopening it becomes structurally unlikely.

SΔϕ-29 does not say that all defaults are bad. It says that defaults require governance conditions. A default can coordinate action, reduce friction, and lower transition completion cost. But when the default becomes impossible to edit, its convenience becomes closure.

Governance is therefore not the absence of defaults. Governance is the preservation of structurally editable defaults before closure becomes operationally irreversible.

## 2. Problem after SΔϕ-28

SΔϕ-28 defines default power as low-cost path assignment.

```text
DefaultPath = argmin TCC(P_i)
```

A path becomes default when it becomes the cheapest continuation.

```text
DefaultPower = TCC(P_alt) - TCC(P_default)
```

The larger the gap between the default path and alternative paths, the stronger default power becomes.

SΔϕ-29 asks the next question:

```text
If a default is already necessary, when does it remain governable?
```

The answer is not simply "when revision is formally possible." Formal revision may remain while operational revision has already become too expensive.

A default remains governable only when editability, authority distribution, rollback feasibility, and exception re-entry remain alive.

## 3. Editable Default

A default is necessary for coordination, but it becomes power when its own revision becomes structurally unlikely.

Editable Default names a dominant path that can still be revised, contested, bypassed, or reopened before closure hardens into fixation.

```text
Editable Default =
dominant path
+ still revisable
+ still contestable
+ still bypassable
+ still reopenable
```

A default is not editable merely because a rule says it can be changed. It is editable only if the material, procedural, informational, and institutional cost of revision remains within a feasible range.

## 4. Distributed Authority

A default cannot remain editable if every revision right collapses into a single center.

Distributed Authority means that design, revision, appeal, and exit are not all monopolized by one actor.

```text
Distributed Authority =
design authority separated from revision authority
+ appeal authority separated from enforcement authority
+ exit authority not blocked by the same center
```

Distributed Authority prevents the default from silently becoming absolute.

If the same actor defines the default, controls the evidence, manages appeals, controls rollback, and defines exceptions, the default may still appear governable while operating as a closure regime.

## 5. Rollback Window

Reversibility is not merely formal.

A system may claim that revision is possible while the operational cost of returning has already exploded.

Rollback Window marks the interval in which revision is still materially feasible.

```text
if t < t*_r:
    rollback remains operational

if t >= t*_r:
    restoration cost rises sharply
```

The rollback window is active only while the cost of returning, revising, or reopening remains materially feasible. After the threshold is crossed, rollback may remain nominal but no longer governable.

This connects SΔϕ-29 directly to SΔϕ-56 Transition Completion Cost.

## 6. Exception Channel

Low-cost convergence compresses exceptions.

If non-default signals cannot re-enter, a system becomes efficient at the price of blindness.

Exception Channel preserves anomalies, minority paths, contrary evidence, edge cases, and non-default signals before they are compressed into silence.

```text
Exception Channel =
anomaly re-entry
+ minority path preservation
+ contrary evidence preservation
+ non-default signal review
```

A system may become highly efficient while losing the ability to detect the signals that should revise it.

The exception channel prevents governance from becoming blindness through efficiency.

## 7. Governable Default Formula

A dominant default remains governable only if all four conditions remain alive.

```text
D* governable iff Ed ∧ Ad ∧ Wr ∧ Ce
```

Where:

```text
D* = dominant default
Ed = Editable Default
Ad = Distributed Authority
Wr = Rollback Window
Ce = Exception Channel
```

Closure condition:

```text
¬Ed ∨ ¬Ad ∨ ¬Wr ∨ ¬Ce
→ D* tends toward closure regime
```

Thus, a default can remain necessary and still be dangerous if one or more governance conditions collapse.

## 8. Closed Default as Power

The default path itself is not the problem.

Closed default is the problem.

```text
open default = coordination
closed default = power
editable default = governance
```

A closed default is a path that remains formally present as a default but no longer allows meaningful revision, appeal, exception, or rollback.

Closed default power is strongest when the default appears convenient, neutral, or technically necessary while alternative paths become too costly to activate.

## 9. Default Closure Regime

A closure regime occurs when a default path becomes difficult or impossible to revise.

Common signals include:

```text
revision exists only formally
authority collapses into one center
rollback cost exceeds feasible threshold
exceptions are filtered out before re-entry
appeal channels are slow or symbolic
exit exists but is materially expensive
minority paths disappear from system memory
```

A closure regime does not always announce itself as coercion. It often appears as efficiency.

## 10. Rollback Threshold

Rollback Window depends on the cost trajectory of restoration.

```text
Wr active iff C_rollback(t) < θ_rollback
```

When the rollback threshold is crossed:

```text
C_rollback(t) ≥ θ_rollback
→ rollback becomes nominal
→ restoration burden rises sharply
→ default closure risk increases
```

A system may still say "appeal is possible" or "revision is possible" after the rollback threshold is crossed. But SΔϕ-29 asks whether rollback is operationally feasible, not merely formally available.

## 11. Exception Re-entry Protocol

An exception channel is live only if non-default signals can re-enter decision pathways.

A live exception channel should preserve:

```text
anomaly
minority path
edge case
contrary evidence
public-interest context
failure signal
local knowledge
appeal evidence
```

Exception re-entry requires more than passive storage. The exception must be able to change the default, delay the default, contest the default, or trigger review.

```text
Exception Channel live iff exception can affect transition path.
```

## 12. Authority Distribution Map

Authority should be separated across at least four functions:

```text
design authority
revision authority
appeal authority
exit authority
```

Additional authority layers may include:

```text
audit authority
technical evaluation authority
public transparency authority
harm review authority
rollback authority
exception review authority
```

If these collapse into one center, the default may remain formally editable while becoming operationally closed.

## 13. Default Governance Audit

To audit a default, ask:

```text
What is the default path?
Who set it?
Can it be revised?
Who can revise it?
Can it be contested?
Can users appeal?
Can users exit?
Is rollback still materially feasible?
Can exceptions re-enter?
Are minority signals preserved?
Has restoration cost already exploded?
```

The audit does not begin with whether the default is morally good or bad. It begins with whether the default remains governable.

## 14. Case Pattern - Mandatory AI Image Filtering as Editable Default Test

**Case type:** public policy / platform governance / technical filtering default.

A legal or platform system makes AI-based image filtering the default path for image publication or distribution.

The surface question may become:

```text
Is this filtering policy justified?
```

SΔϕ-29 asks a structurally prior question:

```text
Does the filtering default remain governable?
```

This case should not be framed first as a declaration that the policy is censorship or non-censorship. SΔϕ-29 does not begin by morally resolving the policy purpose. It detects default-governance signals.

A mandatory technical filtering path may exhibit SΔϕ-29-relevant signals:

```text
mandatory default path
authority concentration risk
rollback-window sensitivity
exception-channel dependency
false-positive and false-negative restoration burden
```

The default is governable only if:

```text
Ed: the filtering default is editable, contestable, bypassable, or reopenable where appropriate.

Ad: authority over design, review, appeal, technical evaluation, and audit is sufficiently distributed.

Wr: rollback remains materially feasible after false positives or false negatives.

Ce: exception channels remain live for non-default signals, public-interest contexts, contrary evidence, and contextual review.
```

If these conditions remain active, the filtering default may remain governable.

If they collapse, the filtering default tends toward a closure regime.

## 15. Applying the Four Conditions to AI Image Filtering

## Ed - Editable Default

Ask:

```text
Can the filtering rule be revised?
Can affected users contest a decision?
Can contextual exceptions be considered?
Can technical performance be audited and updated?
```

If the AI filter blocks an image and the affected party has no meaningful way to revise, contest, or reopen the decision, Ed is weakened.

## Ad - Distributed Authority

Ask:

```text
Who defines the prohibited reference set?
Who designs the filtering technology?
Who evaluates its performance?
Who handles appeals?
Who audits systemic error?
Who can revise the default?
```

If design, enforcement, review, appeal, and audit all collapse into one authority chain, Ad is weakened.

## Wr - Rollback Window

Ask:

```text
If a false positive occurs, can lawful content be restored before material harm occurs?
If a false negative occurs, can harmful content be removed before spread makes restoration costly?
```

Rollback is two-sided. It must cover both wrongly blocked content and wrongly permitted harmful content.

Wr is alive only while restoration remains materially feasible.

## Ce - Exception Channel

Ask:

```text
Can public-interest, journalistic, educational, evidence-preservation, artistic, or contextual exceptions re-enter review?
Can minority signals and contrary evidence change the filtering outcome?
```

If the system compresses all non-default signals into silence, Ce is weakened.

## 16. Case Pattern Boundary

This case pattern is not a claim that AI image filtering is always illegitimate.

It is not a claim that all filtering defaults are censorship.

It is not a claim that harmful content prevention is unnecessary.

It is a structural test:

```text
When a technical filtering path becomes the default,
does it remain editable, authority-distributed, rollback-capable, and exception-aware?
```

## 17. Relation to SΔϕ Modules

## SΔϕ-28 - Default Power

SΔϕ-28 explains how a low-cost path becomes default power.

SΔϕ-29 explains how a default remains governable.

## SΔϕ-44 - Path Closure vs Prohibition

SΔϕ-44 distinguishes prohibition from actual path closure.

SΔϕ-29 asks whether the default path has become closed through loss of editability, authority distribution, rollback, or exception re-entry.

## SΔϕ-56 - Transition Completion Cost

SΔϕ-56 measures whether rollback remains materially feasible.

It is the lower measurement engine for Wr.

## SΔϕ-67 - Local Adaptation Protocol

SΔϕ-67 requires local adapters to preserve core invariants.

SΔϕ-29 provides a governance test for whether local defaults remain editable.

## SΔϕ-68 - Cost Theater

SΔϕ-68 detects visible low cost with hidden completion burden.

SΔϕ-29 asks whether low-cost defaults remain editable or become closed defaults.

## 18. Boundary Constraints and Misreadings

Do not use this package to claim that all defaults are bad.

Do not treat editability as infinite reversibility.

Do not treat formal appeal as distributed authority.

Do not treat nominal rollback as an active rollback window.

Do not treat exception handling as a live exception channel unless non-default signals can actually re-enter.

Do not treat centralized revision rights as distributed authority.

Do not treat efficient default convergence as governance.

Do not ignore restoration cost after the rollback threshold is crossed.

Do not use the AI image filtering case pattern as a blanket claim of censorship or legitimacy.

Do not evaluate technical filtering by purpose alone; audit default-governance conditions.

## 19. Minimal Prompts

## Prompt 1 - Editable Default Audit

Apply SΔϕ-29.
Determine whether this default remains editable or has begun to close.

## Prompt 2 - Governable Default Formula

Apply the formula:

```text
D* governable iff Ed ∧ Ad ∧ Wr ∧ Ce
```

Check each condition separately.

## Prompt 3 - Distributed Authority Check

Apply SΔϕ-29.
Map design, revision, appeal, exit, audit, and rollback authority.

## Prompt 4 - Rollback Window Check

Apply SΔϕ-29 and SΔϕ-56.
Determine whether rollback remains materially feasible.

## Prompt 5 - Exception Channel Check

Apply SΔϕ-29.
Determine whether anomalies, minority paths, contrary evidence, or contextual exceptions can re-enter the default path.

## Prompt 6 - Mandatory Technical Filtering Case

Apply SΔϕ-29 to a mandatory technical filtering default.
Do not begin by declaring censorship or legitimacy.
Audit Ed, Ad, Wr, and Ce.

## 20. Conclusion

Governance is the preservation of structurally editable default before closure becomes operationally irreversible.

A default may be necessary. A default may be efficient. A default may serve a protective purpose.

But a default becomes power when it cannot be revised, when authority collapses into one center, when rollback windows expire, and when exceptions cannot re-enter.

The task of governance is not to eliminate every default.

The task of governance is to prevent defaults from becoming uneditable closure.

## One-Line Summary

SΔϕ-29 defines a governable default as a dominant path that remains editable, authority-distributed, rollback-capable, and exception-aware before closure becomes operationally irreversible.
