#!/usr/bin/env python3
"""Regenera quizzes.json recorriendo el repo y validando los JSON de quiz."""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent
OUT = ROOT / "quizzes.json"
SKIP_DIRS = {".git", "fonts", "node_modules", "__pycache__"}


def is_valid_quiz(data):
    if not isinstance(data, dict):
        return False
    if "tema" not in data or "preguntas" not in data:
        return False
    if not isinstance(data["preguntas"], list) or not data["preguntas"]:
        return False
    return True


def main():
    groups = {}
    for path in sorted(ROOT.rglob("*.json")):
        rel = path.relative_to(ROOT)
        if any(part in SKIP_DIRS for part in rel.parts):
            continue
        if rel.name == OUT.name:
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            print(f"  skip {rel}: {exc}", file=sys.stderr)
            continue
        if not is_valid_quiz(data):
            continue
        group_name = rel.parts[0] if len(rel.parts) > 1 else "Otros"
        groups.setdefault(group_name, []).append({
            "name": path.stem,
            "tema": data["tema"],
            "count": len(data["preguntas"]),
            "path": str(rel).replace("\\", "/"),
        })

    manifest = {
        "groups": [
            {"name": name, "files": files}
            for name, files in sorted(groups.items())
        ]
    }
    OUT.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    total = sum(len(g["files"]) for g in manifest["groups"])
    print(f"Manifest: {total} quizzes en {len(manifest['groups'])} grupos -> {OUT.name}")


if __name__ == "__main__":
    main()
