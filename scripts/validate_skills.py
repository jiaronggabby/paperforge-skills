from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


NAME_RE = re.compile(r"^[a-z0-9-]+$")
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
FORBIDDEN_AUXILIARY = {
    "README.md",
    "CHANGELOG.md",
    "INSTALLATION_GUIDE.md",
    "QUICK_REFERENCE.md",
}


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
    extra_keys = set(meta) - {"name", "description"}
    if extra_keys:
        errors.append(f"{skill_md}: unsupported frontmatter keys {sorted(extra_keys)}")
    if len(text.splitlines()) > 500:
        errors.append(f"{skill_md}: exceeds the 500-line core-skill limit")

    for candidate in path.rglob("*"):
        if candidate.is_file() and candidate.name in FORBIDDEN_AUXILIARY:
            errors.append(f"{candidate}: auxiliary documentation is not allowed inside a skill")
        if candidate.is_dir() and not any(candidate.iterdir()):
            errors.append(f"{candidate}: empty resource directory")

    for markdown in path.rglob("*.md"):
        markdown_text = markdown.read_text(encoding="utf-8")
        headings: set[str] = set()
        for line in markdown_text.splitlines():
            if line.startswith("#"):
                heading = line.lstrip("#").strip().lower()
                if heading in headings:
                    errors.append(f"{markdown}: duplicate heading {heading!r}")
                headings.add(heading)
        for target in LINK_RE.findall(markdown_text):
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            relative = target.split("#", 1)[0]
            resolved = (markdown.parent / relative).resolve()
            try:
                resolved.relative_to(path.resolve())
            except ValueError:
                errors.append(f"{markdown}: link escapes skill folder: {target}")
                continue
            if not resolved.exists():
                errors.append(f"{markdown}: missing linked resource: {target}")

    if path.name == "paperforge-delivery":
        agent_yaml = path / "agents" / "openai.yaml"
        if not agent_yaml.exists():
            errors.append(f"{agent_yaml}: missing controller UI metadata")
        else:
            agent_text = agent_yaml.read_text(encoding="utf-8")
            for field in ("display_name:", "short_description:", "default_prompt:"):
                if field not in agent_text:
                    errors.append(f"{agent_yaml}: missing {field[:-1]}")
            if "$paperforge-delivery" not in agent_text:
                errors.append(f"{agent_yaml}: default_prompt must mention $paperforge-delivery")
        figure_contract = path / "references" / "figure-color-chart-contract.md"
        if not figure_contract.exists():
            errors.append(f"{figure_contract}: missing figure contract")
        else:
            contract_text = figure_contract.read_text(encoding="utf-8")
            required_geometry_rules = {
                'xytext=(-8.0, 4.0)': "fixed panel-label point offset",
                "center_error > 0.02": "heatmap centering threshold",
                "width_error > 0.01": "heatmap equal-width threshold",
                'bbox_inches=None': "fixed Word canvas export",
            }
            for token, rule in required_geometry_rules.items():
                if token not in contract_text:
                    errors.append(f"{figure_contract}: missing {rule}")
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
