# Repo Migration Checklist v1.6

## Import packages

- [ ] Extract SDeltaPhi-29 package into `/packages/SDeltaPhi-29/`
- [ ] Extract SDeltaPhi-30 package into `/packages/SDeltaPhi-30/`
- [ ] Extract SDeltaPhi-31 package into `/packages/SDeltaPhi-31/`
- [ ] Extract SDeltaPhi-32 package into `/packages/SDeltaPhi-32/`
- [ ] Extract SDeltaPhi-67 package into `/packages/SDeltaPhi-67/`
- [ ] Extract SDeltaPhi-68 package into `/packages/SDeltaPhi-68/`

## Update repo

- [ ] Store original ZIPs in `/archives/`
- [ ] Merge DOI map additions
- [ ] Merge series index additions
- [ ] Add route files
- [ ] Add pipeline files
- [ ] Apply README patch
- [ ] Apply llms.txt patch
- [ ] Run `python scripts/validate_sdelta_v1_6_routes.py`
