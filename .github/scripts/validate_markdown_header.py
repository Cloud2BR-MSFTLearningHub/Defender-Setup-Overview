#!/usr/bin/env python3

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

MAIN_TITLE_PATTERN = re.compile(r"^\s{0,3}#\s+\S")


def list_markdown_files(repo_root: Path) -> list[Path]:
    try:
        result = subprocess.run(
            ["git", "-C", str(repo_root), "ls-files", "*.md"],
            check=True,
            capture_output=True,
            text=True,
        )
    except subprocess.CalledProcessError:
        return sorted(
            path for path in repo_root.rglob("*.md") if ".git" not in path.parts
        )

    return sorted(repo_root / Path(line) for line in result.stdout.splitlines() if line)
def validate_markdown_file(file_path: Path) -> list[str]:
    lines = file_path.read_text(encoding="utf-8-sig").splitlines()
    if any(MAIN_TITLE_PATTERN.match(line) for line in lines):
        return []

    return ["missing a main title that starts with '# '."]


def main() -> int:
    repo_root = Path(__file__).resolve().parents[2]
    markdown_files = list_markdown_files(repo_root)

    if not markdown_files:
        print("No Markdown files found.")
        return 0

    failures: dict[Path, list[str]] = {}

    for file_path in markdown_files:
        errors = validate_markdown_file(file_path)
        if errors:
            failures[file_path.relative_to(repo_root)] = errors

    if not failures:
        print(f"Validated a main title in {len(markdown_files)} Markdown files.")
        return 0

    print("Markdown header validation failed.\n")

    for relative_path, errors in failures.items():
        print(f"- {relative_path}")
        for error in errors:
            print(f"  * {error}")

    print("\nEach Markdown file must contain a main title that starts with '# '." )
    return 1


if __name__ == "__main__":
    sys.exit(main())