# Minimal Prompts

## Prompt 1 — HIR

Apply SΔϕ-66.
Score each human intervention point from 0 to 5.

## Prompt 2 — TCC Underlayer

Apply SΔϕ-56 and SΔϕ-66.
Estimate the TCC for each human intervention point.

## Prompt 3 — DCC

Apply SΔϕ-66.
Estimate the delegation completion cost for each AI-delegable task.

## Prompt 4 — Human Required vs Human Bottleneck vs Delegation-Cost Bottleneck

Apply SΔϕ-66.
Determine whether the human is structurally required, a high-TCC bottleneck, or a temporary low-cost executor due to high DCC.

## Prompt 5 — Recursive Improvement Signal

Apply SΔϕ-66.
Check whether HIB decreases, AI cycle time decreases, and AI-generated improvements are increasingly accepted.

## Prompt 6 — Bottleneck Gate

Apply SΔϕ-66.
Check whether Cycle_AI < TCC_human_eval while HIR remains mandatory.

## Prompt 7 — Human Dropout Gate

Apply SΔϕ-66.
Check whether HIR_total ≈ 0 or humans are no longer required as transition conditions.

## Prompt 8 — Anti-overclaim

Apply SΔϕ-66 and SΔϕ-62.
Do not infer AGI, consciousness, autonomous intention, or inherent danger from recursive improvement signal alone.
