# Patch Apply Guide — SΔϕ Boundary-to-Closure Spine v1.5

## Apply method

1. Unzip this patch at the repository root.
2. Allow replacement for files with the same names.
3. Replace root files:
   - README.md
   - 00_AI_ENTRYPOINT.md
   - llms.txt
   - SDELTA_MODULE_ROUTING.yaml
   - SDELTA_ACCESS_PROTOCOL.yaml
   - SERIES_INDEX.json
   - SERIES_DOI_MAP.json
   - MANIFEST.txt
4. Add or replace mirrored routing files:
   - routing/SDELTA_MODULE_ROUTING.yaml
   - routing/SDELTA_ACCESS_PROTOCOL.yaml
5. Add or replace index files:
   - indexes/MODULE_GRAPH.json
   - indexes/SPINE_MAP.yaml
   - indexes/ROUTE_INDEX.json
   - indexes/PACKAGE_STATUS.json

## Commit message

```text
Add v1.5 event-authority-fixation routing layer
```

## Validation checklist

- README.md contains the 19 -> 27 event / authority / fixation route.
- SDELTA_MODULE_ROUTING.yaml contains event_authority_fixation_route.
- indexes/MODULE_GRAPH.json contains edges for 19 -> 27.
- SERIES_DOI_MAP.json contains package DOIs for 19 through 27.
- llms.txt gives a compact LLM entry route.

## Guardrail

Do not activate the full 19-27 spine by keyword alone.
Use the smallest sufficient module.
Use SDeltaPhi-62 for factual/evidential/world-binding claims.
Use SDeltaPhi-56 for transition-completion-cost estimates.
