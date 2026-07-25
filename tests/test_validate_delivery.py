from __future__ import annotations

import csv
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (
    REPO_ROOT
    / "skills"
    / "paperforge-delivery"
    / "scripts"
    / "validate_delivery.py"
)
TEMPLATE = (
    REPO_ROOT
    / "skills"
    / "paperforge-delivery"
    / "assets"
    / "paper-contract.template.json"
)


class ValidateDeliveryTest(unittest.TestCase):
    def build_contract(self, root: Path) -> Path:
        contract = json.loads(TEMPLATE.read_text(encoding="utf-8"))
        contract["project"].update(
            {
                "name": "fixture",
                "canonical_root": str(root),
                "repository_root": ".",
                "branch": "main",
                "commit": "abc123",
                "remote": "git@example.test:fixture.git",
            }
        )

        files = {
            "protocol/source.json": "{}\n",
            "protocol/split.csv": "id,split\n1,train\n",
            "results/canonical.csv": "metric,value\nauc,0.8\n",
            "results/statistics.csv": "estimate,lower,upper\n0.1,0.01,0.2\n",
            "results/claims.csv": "claim_id,evidence\nC1,canonical.csv\n",
            "results/negative.csv": "route,status\nB1,null\n",
            "paper/figure_registry.json": "{}\n",
            "delivery/submission/manuscript.docx": "fixture\n",
            "delivery/code/run.py": "print('ok')\n",
        }
        for relative, content in files.items():
            path = root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")

        benchmark = root / "paper" / "matched_papers.csv"
        with benchmark.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(
                handle,
                fieldnames=["paper_id", "inclusion_decision"],
            )
            writer.writeheader()
            for index in range(20):
                writer.writerow(
                    {"paper_id": f"P{index + 1:02d}", "inclusion_decision": "include"}
                )

        (root / "paper" / "figures" / "source").mkdir(parents=True)
        (root / "paper" / "figures" / "final").mkdir(parents=True)

        contract["protocol"].update(
            {
                "source": "protocol/source.json",
                "data_version_or_hash": "sha256:data",
                "config_fingerprint": "sha256:config",
                "split_manifest": "protocol/split.csv",
                "locked_test_status": "evaluated_once",
            }
        )
        contract["evidence"].update(
            {
                "canonical_results": "results/canonical.csv",
                "statistics_record": "results/statistics.csv",
                "claim_map": "results/claims.csv",
                "negative_results_record": "results/negative.csv",
                "literature_benchmark": "paper/matched_papers.csv",
            }
        )
        contract["figures"].update(
            {
                "registry": "paper/figure_registry.json",
                "source_directory": "paper/figures/source",
                "final_directory": "paper/figures/final",
            }
        )
        contract["delivery"].update(
            {
                "submission_package": "delivery/submission",
                "code_package": "delivery/code",
                "provenance_record": "delivery/package_audit.json",
                "final_artifacts": [
                    {"path": "delivery/submission/manuscript.docx"},
                    {"path": "delivery/code/run.py"},
                ],
            }
        )
        contract["gates"] = {key: "pass" for key in contract["gates"]}
        contract["truth_only_metadata"] = {
            key: "confirmed" for key in contract["truth_only_metadata"]
        }

        path = root / "paper_contract.json"
        path.write_text(json.dumps(contract, indent=2), encoding="utf-8")
        return path

    def run_validator(self, contract: Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(SCRIPT), str(contract)],
            check=False,
            capture_output=True,
            text=True,
        )

    def test_complete_fixture_passes(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            contract = self.build_contract(Path(raw))
            result = self.run_validator(contract)
            self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
            self.assertIn('"status": "PASS"', result.stdout)
            self.assertIn('"matched_paper_count": 20', result.stdout)

    def test_path_escape_blocks_delivery(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            contract_path = self.build_contract(root)
            contract = json.loads(contract_path.read_text(encoding="utf-8"))
            contract["evidence"]["canonical_results"] = "../outside.csv"
            contract_path.write_text(json.dumps(contract, indent=2), encoding="utf-8")
            result = self.run_validator(contract_path)
            self.assertEqual(result.returncode, 2)
            self.assertIn("escapes canonical root", result.stdout)


if __name__ == "__main__":
    unittest.main()
