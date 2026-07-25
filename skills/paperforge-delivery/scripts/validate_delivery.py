from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
from pathlib import Path
from typing import Any


REQUIRED_TOP = {
    "schema_version",
    "project",
    "paper",
    "protocol",
    "evidence",
    "figures",
    "delivery",
    "gates",
    "truth_only_metadata",
}

REQUIRED_SECTIONS: dict[str, set[str]] = {
    "project": {
        "name",
        "canonical_root",
        "repository_root",
        "branch",
        "commit",
        "remote",
    },
    "paper": {
        "target_venue",
        "article_type",
        "primary_question",
        "prediction_or_decision_unit",
        "information_boundary",
        "primary_claim",
        "claim_ceiling",
        "primary_comparison",
        "primary_outcomes",
    },
    "protocol": {
        "source",
        "data_version_or_hash",
        "config_fingerprint",
        "split_manifest",
        "locked_test_status",
        "declared_runs",
        "realized_runs",
    },
    "evidence": {
        "canonical_results",
        "statistics_record",
        "claim_map",
        "negative_results_record",
        "literature_benchmark",
        "literature_benchmark_shortfall",
    },
    "figures": {"registry", "source_directory", "final_directory"},
    "delivery": {
        "submission_package",
        "code_package",
        "provenance_record",
        "final_artifacts",
    },
}

HARD_GATES = {
    "protocol_code_alignment",
    "split_and_leakage",
    "formal_matrix",
    "statistics",
    "claim_traceability",
    "matched_20_papers",
    "figure_visual_review",
    "reporting_compliance",
    "render_and_package",
}

PASS_VALUES = {"pass", "passed", "waived", "not_applicable", "n/a"}
BLOCK_VALUES = {"blocked", "fail", "failed", "pending", "unknown", ""}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError("contract root must be a JSON object")
    return value


def structural_errors(contract: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    missing_top = REQUIRED_TOP - contract.keys()
    if missing_top:
        errors.append(f"missing top-level keys: {sorted(missing_top)}")
    for section, required in REQUIRED_SECTIONS.items():
        value = contract.get(section)
        if not isinstance(value, dict):
            errors.append(f"{section} must be an object")
            continue
        missing = required - value.keys()
        if missing:
            errors.append(f"{section} missing keys: {sorted(missing)}")
    gates = contract.get("gates")
    if not isinstance(gates, dict):
        errors.append("gates must be an object")
    else:
        missing_gates = HARD_GATES - gates.keys()
        if missing_gates:
            errors.append(f"gates missing keys: {sorted(missing_gates)}")
    return errors


def resolve_under(root: Path, raw: str, label: str, errors: list[str]) -> Path | None:
    if not raw:
        errors.append(f"{label} is empty")
        return None
    candidate = Path(raw)
    if not candidate.is_absolute():
        candidate = root / candidate
    resolved = candidate.resolve(strict=False)
    try:
        resolved.relative_to(root)
    except ValueError:
        errors.append(f"{label} escapes canonical root: {resolved}")
        return None
    return resolved


def require_file(
    root: Path,
    raw: str,
    label: str,
    errors: list[str],
    warnings: list[str],
) -> Path | None:
    path = resolve_under(root, raw, label, errors)
    if path is None:
        return None
    if not path.exists():
        errors.append(f"{label} does not exist: {path}")
    elif not path.is_file():
        errors.append(f"{label} is not a file: {path}")
    elif path.stat().st_size == 0:
        errors.append(f"{label} is empty: {path}")
    elif path.suffix.lower() in {".tmp", ".bak"}:
        warnings.append(f"{label} uses a temporary-looking suffix: {path.name}")
    return path


def require_directory(root: Path, raw: str, label: str, errors: list[str]) -> Path | None:
    path = resolve_under(root, raw, label, errors)
    if path is None:
        return None
    if not path.exists():
        errors.append(f"{label} does not exist: {path}")
    elif not path.is_dir():
        errors.append(f"{label} is not a directory: {path}")
    return path


def benchmark_count(path: Path) -> int:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = csv.DictReader(handle)
        return sum(
            1
            for row in rows
            if row.get("inclusion_decision", "").strip().lower()
            in {"include", "included", "yes"}
        )


def audit_contract(contract_path: Path, contract: dict[str, Any]) -> dict[str, Any]:
    errors = structural_errors(contract)
    warnings: list[str] = []
    checks: dict[str, Any] = {}

    project = contract.get("project", {})
    root_raw = project.get("canonical_root", "") if isinstance(project, dict) else ""
    root = Path(root_raw).expanduser().resolve(strict=False) if root_raw else None
    if root is None:
        errors.append("project.canonical_root is empty")
        return make_report(contract_path, None, checks, errors, warnings)
    if not root.is_absolute():
        errors.append("project.canonical_root must be absolute")
    if not root.exists() or not root.is_dir():
        errors.append(f"canonical root does not exist: {root}")

    for key in ("name", "branch", "commit", "remote"):
        if not str(project.get(key, "")).strip():
            warnings.append(f"project.{key} is empty")

    repo_raw = str(project.get("repository_root", ""))
    if repo_raw:
        require_directory(root, repo_raw, "project.repository_root", errors)
    else:
        warnings.append("project.repository_root is empty")

    protocol = contract.get("protocol", {})
    evidence = contract.get("evidence", {})
    figures = contract.get("figures", {})
    delivery = contract.get("delivery", {})

    for section, key, label in (
        (protocol, "source", "protocol.source"),
        (protocol, "split_manifest", "protocol.split_manifest"),
        (evidence, "canonical_results", "evidence.canonical_results"),
        (evidence, "statistics_record", "evidence.statistics_record"),
        (evidence, "claim_map", "evidence.claim_map"),
        (evidence, "negative_results_record", "evidence.negative_results_record"),
        (figures, "registry", "figures.registry"),
    ):
        if isinstance(section, dict):
            require_file(root, str(section.get(key, "")), label, errors, warnings)

    benchmark_path = require_file(
        root,
        str(evidence.get("literature_benchmark", "")),
        "evidence.literature_benchmark",
        errors,
        warnings,
    )
    if benchmark_path and benchmark_path.exists() and benchmark_path.is_file():
        try:
            count = benchmark_count(benchmark_path)
            checks["matched_paper_count"] = count
            shortfall = str(evidence.get("literature_benchmark_shortfall", "")).strip()
            if count < 20 and not shortfall:
                errors.append(
                    f"literature benchmark has {count} included papers; "
                    "document a genuine shortfall or complete 20"
                )
        except (OSError, csv.Error) as exc:
            errors.append(f"cannot read literature benchmark: {exc}")

    for key in ("source_directory", "final_directory"):
        if isinstance(figures, dict):
            require_directory(root, str(figures.get(key, "")), f"figures.{key}", errors)

    for key in ("submission_package", "code_package"):
        if isinstance(delivery, dict):
            require_directory(root, str(delivery.get(key, "")), f"delivery.{key}", errors)

    artifacts = delivery.get("final_artifacts", []) if isinstance(delivery, dict) else []
    if not isinstance(artifacts, list) or not artifacts:
        errors.append("delivery.final_artifacts must contain at least one artifact")
    else:
        artifact_reports = []
        for index, item in enumerate(artifacts):
            raw_path = item.get("path", "") if isinstance(item, dict) else str(item)
            expected_hash = item.get("sha256", "") if isinstance(item, dict) else ""
            path = require_file(
                root,
                raw_path,
                f"delivery.final_artifacts[{index}]",
                errors,
                warnings,
            )
            if path and path.exists() and path.is_file() and path.stat().st_size:
                actual_hash = sha256(path)
                if expected_hash and expected_hash.lower() != actual_hash:
                    errors.append(f"SHA256 mismatch for {path}")
                artifact_reports.append(
                    {"path": str(path), "size": path.stat().st_size, "sha256": actual_hash}
                )
        checks["final_artifacts"] = artifact_reports

    gates = contract.get("gates", {})
    if isinstance(gates, dict):
        for gate in sorted(HARD_GATES):
            value = str(gates.get(gate, "")).strip().lower()
            if value in BLOCK_VALUES or value not in PASS_VALUES:
                errors.append(f"gate {gate} is not passed or explicitly waived: {value!r}")

    truth = contract.get("truth_only_metadata", {})
    if isinstance(truth, dict):
        unknown = [
            key
            for key, value in truth.items()
            if str(value).strip().lower() in {"", "unknown", "todo", "tbd"}
        ]
        if unknown:
            warnings.append(f"truth-only metadata still requires author input: {unknown}")

    return make_report(contract_path, root, checks, errors, warnings)


def make_report(
    contract_path: Path,
    root: Path | None,
    checks: dict[str, Any],
    errors: list[str],
    warnings: list[str],
) -> dict[str, Any]:
    status = "BLOCKED" if errors else ("WARN" if warnings else "PASS")
    return {
        "schema_version": "1.0",
        "status": status,
        "contract": str(contract_path.resolve()),
        "canonical_root": str(root) if root else None,
        "checks": checks,
        "errors": errors,
        "warnings": warnings,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a PaperForge delivery contract.")
    parser.add_argument("contract", type=Path)
    parser.add_argument(
        "--template",
        action="store_true",
        help="Check schema structure only; allow empty template values.",
    )
    parser.add_argument("--output", type=Path, help="Optional JSON audit output path.")
    args = parser.parse_args()

    try:
        contract = load_json(args.contract)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"BLOCKED: cannot load contract: {exc}", file=sys.stderr)
        return 2

    if args.template:
        errors = structural_errors(contract)
        report = make_report(args.contract, None, {}, errors, [])
    else:
        report = audit_contract(args.contract, contract)

    rendered = json.dumps(report, ensure_ascii=False, indent=2)
    print(rendered)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + "\n", encoding="utf-8")

    return {"PASS": 0, "WARN": 1, "BLOCKED": 2}[report["status"]]


if __name__ == "__main__":
    raise SystemExit(main())
