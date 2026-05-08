
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]

def test_public_entrypoints_exist():
    required = [
        "README.md",
        "LICENSE",
        "CITATION.cff",
        "pyproject.toml",
        "pytest.ini",
        "docs/THREE_BODY_SCOPE.md",
        "docs/RESULTS_INDEX.md",
        "docs/REPOSITORY_STATUS.md",
    ]
    for rel in required:
        assert (ROOT / rel).exists(), rel

def test_core_directories_exist():
    for rel in ["docs", "examples", "results"]:
        assert (ROOT / rel).exists(), rel

def test_key_examples_exist():
    required = [
        "examples/run_three_body_demo.py",
        "examples/run_perturbation_sweep.py",
        "examples/run_representation_analysis.py",
    ]
    for rel in required:
        assert (ROOT / rel).exists(), rel

def test_key_result_files_exist():
    required = [
        "results/three_body_metrics.json",
        "results/perturbation_sweep.json",
        "results/representation_comparison.json",
        "results/omnia_three_body_dashboard.png",
        "results/perturbation_sweep_dashboard.png",
        "results/representation_comparison.png",
    ]
    for rel in required:
        assert (ROOT / rel).exists(), rel

def test_json_results_parse():
    for rel in [
        "results/three_body_metrics.json",
        "results/perturbation_sweep.json",
        "results/representation_comparison.json",
    ]:
        data = json.loads((ROOT / rel).read_text(encoding="utf-8"))
        assert data is not None

def test_readme_boundary_terms():
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "measurement != inference != decision" in text
    assert "not a truth oracle" in text
    assert "not a semantic judge" in text
    assert "Decision remains external" in text
    assert "not a general physics simulator" in text
