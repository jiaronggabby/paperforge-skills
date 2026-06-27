from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


NAME_RE = re.compile(r"^[a-z0-9-]+$")


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise ValueError("missing opening frontmatter marker")
    end = text.find("\n---", 4)
    if end == -1:
        raise ValueError("missing closing frontmatter marker")
    raw = text[4:end].strip().splitlines()
    data: dict[str, str] = {}
    for line in raw:
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"')
    return data


def validate_skill(path: Path) -> list[str]:
    errors: list[str] = []
    skill_md = path / "SKILL.md"
    if not skill_md.exists():
        return [f"{path}: missing SKILL.md"]
    text = skill_md.read_text(encoding="utf-8")
    try:
        meta = parse_frontmatter(text)
    except ValueError as exc:
        return [f"{skill_md}: {exc}"]
    name = meta.get("name", "")
    description = meta.get("description", "")
    if not name:
        errors.append(f"{skill_md}: missing name")
    elif not NAME_RE.match(name):
        errors.append(f"{skill_md}: invalid name {name!r}")
    elif name != path.name:
        errors.append(f"{skill_md}: name {name!r} does not match folder {path.name!r}")
    if not description:
        errors.append(f"{skill_md}: missing description")
    elif len(description) < 80:
        errors.append(f"{skill_md}: description is too short for reliable triggering")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate PaperForge skill folders.")
    parser.add_argument("skills_dir", type=Path)
    args = parser.parse_args()

    roots = sorted(p for p in args.skills_dir.iterdir() if p.is_dir())
    errors: list[str] = []
    for root in roots:
        errors.extend(validate_skill(root))

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print(f"Validated {len(roots)} skills.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
