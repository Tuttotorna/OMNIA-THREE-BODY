from omnia_three_body import (
    adapt_three_body_measurement_to_boundary_certificate,
    observe_three_body_envelope,
    run_three_body_backbone_flow,
)
from omnia_limit import validate_certificate


def test_adapt_three_body_measurement_to_boundary_certificate_continue_flow():
    measurement = {
        "trajectory_stability_score": 0.82,
        "perturbation_step": 2,
        "gate_status": "CONTINUE",
        "system_family": "restricted_three_body",
        "integration_window": "local",
    }

    raw_certificate = adapt_three_body_measurement_to_boundary_certificate(
        measurement,
        target_repository="OMNIA-THREE-BODY",
        certificate_id="three-body-boundary-cert",
        timestamp="2026-05-20T20:00:00Z",
    )

    cert = validate_certificate(raw_certificate)

    assert cert.certificate_id == "three-body-boundary-cert"
    assert cert.target_repository == "OMNIA-THREE-BODY"
    assert round(cert.ast_deformation_index, 2) == 0.18
    assert cert.perturbation_step == 2
    assert cert.should_continue is True
    assert cert.saturation_detected is False
    assert raw_certificate["metrics"]["domain"] == "three_body_trajectory"
    assert raw_certificate["metrics"]["system_family"] == "restricted_three_body"
    assert raw_certificate["metrics"]["integration_window"] == "local"
    assert raw_certificate["metrics"]["trajectory_stability_score"] == 0.82


def test_run_three_body_backbone_flow_stop_flow():
    measurement = {
        "orbital_stability_score": 0.97,
        "perturbation_step": 5,
        "gate_status": "STOP",
        "system_family": "three_body_chaotic",
        "integration_window": "trajectory",
    }

    observation = run_three_body_backbone_flow(
        measurement,
        target_repository="OMNIA-THREE-BODY",
        certificate_id="three-body-stop-cert",
        timestamp="2026-05-20T20:00:00Z",
    )

    assert observation["observer"] == "OMNIA-THREE-BODY"
    assert observation["role"] == "domain_experiment_producer_adapter"
    assert observation["observed_status"] == "GATE_CLOSED_SATURATION_REACHED"
    assert observation["certificate_id"] == "three-body-stop-cert"
    assert observation["target_repository"] == "OMNIA-THREE-BODY"
    assert observation["saturation_detected"] is True
    assert round(observation["ast_deformation_index"], 2) == 0.03
    assert observation["perturbation_step"] == 5
    assert observation["physical_truth_claim"] is None
    assert observation["backbone_contract_preserved"] is True


def test_run_three_body_backbone_flow_continue_flow():
    measurement = {
        "trajectory_divergence": 0.21,
        "perturbation_step": 1,
        "gate_status": "CONTINUE",
        "system_family": "three_body_numeric",
        "integration_window": "single_step",
    }

    observation = run_three_body_backbone_flow(
        measurement,
        target_repository="OMNIA-THREE-BODY",
        certificate_id="three-body-continue-cert",
        timestamp="2026-05-20T20:00:00Z",
    )

    assert observation["observer"] == "OMNIA-THREE-BODY"
    assert observation["role"] == "domain_experiment_producer_adapter"
    assert observation["observed_status"] == "GATE_OPEN_MEASUREMENT_REQUIRED"
    assert observation["certificate_id"] == "three-body-continue-cert"
    assert observation["target_repository"] == "OMNIA-THREE-BODY"
    assert observation["saturation_detected"] is False
    assert observation["ast_deformation_index"] == 0.21
    assert observation["perturbation_step"] == 1
    assert observation["physical_truth_claim"] is None
    assert observation["backbone_contract_preserved"] is True


def test_observe_existing_envelope_without_physical_truth_claim():
    envelope = {
        "envelope_id": "three-body-env",
        "timestamp": "2026-05-20T20:00:00Z",
        "validation_status": "GATE_CLOSED_SATURATION_REACHED",
        "details": {
            "target_repository": "OMNIA",
            "certificate_id": "existing-three-body-cert",
            "saturation_detected": True,
            "ast_deformation_index": 0.04,
            "perturbation_step": 9,
        },
    }

    observation = observe_three_body_envelope(envelope)

    assert observation["observer"] == "OMNIA-THREE-BODY"
    assert observation["role"] == "domain_experiment_producer_adapter"
    assert observation["observed_status"] == "GATE_CLOSED_SATURATION_REACHED"
    assert observation["certificate_id"] == "existing-three-body-cert"
    assert observation["target_repository"] == "OMNIA"
    assert observation["physical_truth_claim"] is None
    assert observation["backbone_contract_preserved"] is True
