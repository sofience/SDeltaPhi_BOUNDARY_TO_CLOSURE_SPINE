#!/usr/bin/env python3
"""Validate SΔϕ v1.6 Default Closure Governance repository overlay.

Run from repository root after applying the patch:
    python scripts/validate_v1_6_default_closure.py

This script checks presence of the v1.6 root entrypoints, route indexes,
and default-closure modules. It does not validate Zenodo DOI availability.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path.cwd()

REQUIRED_FILES = [
    "README.md",
    "00_AI_ENTRYPOINT.md",
    "llms.txt",
    "MANIFEST.txt",
    "SDELTA_ACCESS_PROTOCOL.yaml",
    "SDELTA_MODULE_ROUTING.yaml",
    "routing/SDELTA_ACCESS_PROTOCOL.yaml",
    "routing/SDELTA_MODULE_ROUTING.yaml",
    "indexes/SPINE_MAP.yaml",
    "indexes/ROUTE_INDEX.json",
    "indexes/MODULE_GRAPH.json",
    "indexes/DEFAULT_CLOSURE_STACK_INDEX.json",
    "indexes/INTERVENTION_LEGITIMACY_MAP.json",
    "indexes/PACKAGE_IMPORT_MANIFEST_v1_6.json",
    "pipeline/BOUNDARY_TO_CLOSURE_PIPELINE_v1_6.yaml",
    "CHANGELOG_v1_6_DEFAULT_CLOSURE.md",
]

REQUIRED_MODULES = [
    "SDeltaPhi-26",
    "SDeltaPhi-27",
    "SDeltaPhi-28",
    "SDeltaPhi-29",
    "SDeltaPhi-30",
    "SDeltaPhi-31",
    "SDeltaPhi-32",
]

REQUIRED_STRINGS = {
    "README.md": [
        "v1.6-default-closure-governance",
        "SDeltaPhi-26 -> SDeltaPhi-27 -> SDeltaPhi-28 -> SDeltaPhi-29 -> SDeltaPhi-30 -> SDeltaPhi-31 -> SDeltaPhi-32",
        "I_legit iff Rb_p ∧ Ex_p ∧ Ed_p ∧ ¬RC",
    ],
    "00_AI_ENTRYPOINT.md": [
        "v1.6-default-closure-governance",
        "DEFAULT_CLOSURE_STACK_INDEX",
        "INTERVENTION_LEGITIMACY_MAP",
    ],
    "llms.txt": [
        "v1.6 Default Closure Governance route",
        "Smallest sufficient module rule",
    ],
    "SDELTA_MODULE_ROUTING.yaml": [
        "default_closure_governance_spine",
        "intervention_legitimacy_route",
        "cost_theater_route",
    ],
}


def fail(message: str) -> None:
    print(f"[FAIL] {message}")
    sys.exit(1)


def warn(message: str) -> None:
    print(f"[WARN] {message}")


def ok(message: str) -> None:
    print(f"[ OK ] {message}")


def read_text(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def main() -> None:
    missing = [p for p in REQUIRED_FILES if not (ROOT / p).exists()]
    if missing:
        fail("Missing required files: " + ", ".join(missing))
    ok("All required v1.6 files are present.")

    for file_path, required in REQUIRED_STRINGS.items():
        text = read_text(file_path)
        for needle in required:
            if needle not in text:
                fail(f"{file_path} does not contain required string: {needle}")
    ok("Root entrypoint strings validated.")

    route_index_path = ROOT / "indexes/ROUTE_INDEX.json"
    module_graph_path = ROOT / "indexes/MODULE_GRAPH.json"
    stack_index_path = ROOT / "indexes/DEFAULT_CLOSURE_STACK_INDEX.json"

    for json_path in [route_index_path, module_graph_path, stack_index_path]:
        try:
            json.loads(json_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            fail(f"Invalid JSON in {json_path}: {exc}")
    ok("JSON indexes parse successfully.")

    route_index = json.loads(route_index_path.read_text(encoding="utf-8"))
    spine = route_index["routes"]["default_closure_governance_spine"]["modules"]
    if spine != REQUIRED_MODULES:
        fail(f"Default closure spine mismatch: {spine}")
    ok("Default closure governance spine is correctly ordered.")

    for module in REQUIRED_MODULES:
        package_dir = ROOT / "packages" / module
        archive_candidates = list((ROOT / "archives").glob(f"{module}*")) if (ROOT / "archives").exists() else []
        if not package_dir.exists() and not archive_candidates:
            warn(f"No package directory or archive found for {module}; import package if not already present.")

    ok("v1.6 validation completed.")


if __name__ == "__main__":
    main()
