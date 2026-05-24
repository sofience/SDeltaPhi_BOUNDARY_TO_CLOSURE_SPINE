#!/usr/bin/env python3
from pathlib import Path
import json, sys
ROOT = Path(__file__).resolve().parents[1]
required = [
    'indexes/DEFAULT_CLOSURE_STACK_INDEX.json',
    'indexes/INTERVENTION_LEGITIMACY_MAP.json',
    'indexes/CASE_PATTERN_INDEX.json',
    'routing/SDELTA_DEFAULT_CLOSURE_GOVERNANCE_ROUTE.yaml',
    'routing/SDELTA_INTERVENTION_LEGITIMACY_ROUTE.yaml',
    'pipeline/BOUNDARY_TO_CLOSURE_PIPELINE_v1_6.yaml',
    'docs/CASE_PATTERN_USAGE_POLICY.md',
]
errors=[]
for rel in required:
    if not (ROOT/rel).exists(): errors.append(f'Missing required file: {rel}')
for path in ROOT.rglob('*.json'):
    try: json.loads(path.read_text(encoding='utf-8'))
    except Exception as exc: errors.append(f'Invalid JSON: {path.relative_to(ROOT)} :: {exc}')
doi=ROOT/'indexes'/'SERIES_DOI_MAP.v1_6.additions.json'
if doi.exists():
    additions=json.loads(doi.read_text(encoding='utf-8')).get('additions',{})
    for m in ['SDeltaPhi-29','SDeltaPhi-30','SDeltaPhi-31','SDeltaPhi-32','SDeltaPhi-67','SDeltaPhi-68']:
        if m not in additions: errors.append(f'DOI additions missing {m}')
stack=ROOT/'indexes'/'DEFAULT_CLOSURE_STACK_INDEX.json'
if stack.exists():
    s=json.loads(stack.read_text(encoding='utf-8')).get('spine',[])
    if s[-5:] != ['SDeltaPhi-28','SDeltaPhi-29','SDeltaPhi-30','SDeltaPhi-31','SDeltaPhi-32']:
        errors.append(f'Default closure stack tail mismatch: {s[-5:]}')
if errors:
    print('SΔϕ v1.6 validation failed:')
    for e in errors: print(' -', e)
    sys.exit(1)
print('SΔϕ v1.6 validation passed.')
