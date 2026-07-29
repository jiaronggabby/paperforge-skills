#!/usr/bin/env python3
"""Validate one-to-one multipart-figure panel/caption mappings."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


def panel_marker_position(caption: str, label: str) -> int | None:
    """Return the first explicit caption marker position for one panel."""
    escaped = re.escape(label)
    patterns = (
        rf"(?<![A-Za-z0-9])panel\s*\(?{escaped}\)?(?=\s*[,.;:)])",
        rf"(?<![A-Za-z0-9])\({escaped}\)(?=\s*[,.;:)])",
        rf"(?<![A-Za-z0-9]){escaped}(?=\s*[,.;:)])",
    )
    positions = [match.start() for pattern in patterns for match in re.finditer(pattern, caption, re.I)]
    return min(positions) if positions else None


def validate_registry(registry: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    contract = registry.get("caption_contract", {})
    if contract.get("standalone_generated_caption_markdown", True):
        errors.append("caption_contract forbids standalone generated caption Markdown")
    figures = registry.get("figures")
    if not isinstance(figures, list) or not figures:
        errors.append("figures must contain at least one figure entry")
        return errors

    for index, figure in enumerate(figures, start=1):
        prefix = f"figures[{index - 1}]"
        if not isinstance(figure, dict):
            errors.append(f"{prefix} must be an object")
            continue
        labels = figure.get("panel_labels")
        descriptions = figure.get("panel_descriptions")
        caption = str(figure.get("caption", "")).strip()
        if not isinstance(labels, list) or not labels:
            errors.append(f"{prefix}.panel_labels must be a non-empty list")
            continue
        if len(set(labels)) != len(labels):
            errors.append(f"{prefix}.panel_labels contains duplicates")
        if not all(isinstance(label, str) and re.fullmatch(r"[A-Za-z]", label) for label in labels):
            errors.append(f"{prefix}.panel_labels must contain single letters")
        if not isinstance(descriptions, dict) or set(descriptions) != set(labels):
            errors.append(f"{prefix}.panel_descriptions must exactly match panel_labels")
        elif any(not str(descriptions[label]).strip() for label in labels):
            errors.append(f"{prefix}.panel_descriptions cannot contain empty text")
        if not caption:
            errors.append(f"{prefix}.caption is empty")
            continue

        positions: list[int] = []
        for label in labels:
            position = panel_marker_position(caption, label)
            if position is None:
                errors.append(f"{prefix}.caption does not explain panel {label}")
            else:
                positions.append(position)
        if len(positions) == len(labels) and positions != sorted(positions):
            errors.append(f"{prefix}.caption panel markers are not in registry order")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("registry", type=Path)
    parser.add_argument("--report", type=Path, help="write a JSON report; never writes Markdown")
    args = parser.parse_args()
    try:
        registry = json.loads(args.registry.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: cannot read registry: {exc}", file=sys.stderr)
        return 2
    errors = validate_registry(registry)
    report = {"status": "PASS" if not errors else "FAIL", "errors": errors}
    if args.report:
        args.report.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    else:
        print(json.dumps(report, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
