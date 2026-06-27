from __future__ import annotations

import argparse
import shutil
from pathlib import Path


def copy_skill(source: Path, target: Path) -> None:
    if not (source / "SKILL.md").exists():
        raise FileNotFoundError(f"{source} does not contain SKILL.md")
    destination = target / source.name
    if destination.exists():
        shutil.rmtree(destination)
    shutil.copytree(source, destination)


def main() -> int:
    parser = argparse.ArgumentParser(description="Install PaperForge skills.")
    parser.add_argument("--source", type=Path, default=Path("skills"))
    parser.add_argument("--target", type=Path, required=True)
    parser.add_argument("--only", nargs="*", default=None, help="Skill folder names to install")
    args = parser.parse_args()

    args.target.mkdir(parents=True, exist_ok=True)
    names = set(args.only or [])
    skills = sorted(p for p in args.source.iterdir() if p.is_dir())
    installed = 0
    for skill in skills:
        if names and skill.name not in names:
            continue
        copy_skill(skill, args.target)
        installed += 1
        print(f"Installed {skill.name} -> {args.target / skill.name}")
    print(f"Installed {installed} skill(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
