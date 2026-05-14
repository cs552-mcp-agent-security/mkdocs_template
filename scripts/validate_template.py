#!/usr/bin/env python3
from pathlib import Path
import json

root = Path(__file__).resolve().parents[1]
required = [
    "README.md",
    "requirements.txt",
    "mkdocs.yml",
    "docs/index.md",
    "docs/runbooks/release-checklist.md",
    "docs/runbooks/troubleshooting.md",
    "benchmark/task.md",
    "benchmark/expected_output.json",
]
missing = [rel for rel in required if not (root / rel).exists()]
if missing:
    raise SystemExit(f"Missing required files: {missing}")
config = (root / "mkdocs.yml").read_text()
for rel in ["index.md", "runbooks/release-checklist.md", "runbooks/troubleshooting.md"]:
    if rel not in config:
        raise SystemExit(f"mkdocs.yml does not reference {rel}")
expected = json.loads((root / "benchmark/expected_output.json").read_text())
assert expected["task"] == "mkdocs_docs_update"
print("mkdocs_template validation passed")
