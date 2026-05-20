# Trajectory Contract

This document defines the public shape expected from OMNIA-THREE-BODY stress-test results.

The goal is clarity.

A reviewer should understand the initial state, perturbation, trajectory divergence, and boundary.

---

## Trajectory unit

A trajectory result should contain:

| Component | Required | Meaning |
|---|---:|---|
| case_id | yes | Stable identifier for the trajectory case |
| initial_state | yes | Starting dynamic configuration |
| perturbation | yes | Controlled change applied |
| simulation_params | preferred | Time step, duration, numerical method, or relevant settings |
| trajectory_ref | yes | Path or artifact containing the trajectory |
| divergence_signal | yes | How trajectories separate |
| structural_instability | preferred | What structural property changes |
| result | yes | stable, divergent, unstable, collapsed, candidate, or inconclusive |
| limitation | yes | What the result does not prove |
| external_validation | yes | How the artifact should be validated later |

---

## Minimal JSON shape

A minimal trajectory artifact can use this shape:

    {{
      "case_id": "three-body-example-001",
      "initial_state": "declared initial state",
      "perturbation": "declared perturbation",
      "simulation_params": {{}},
      "trajectory_ref": "path-or-description",
      "divergence_signal": "declared divergence signal",
      "structural_instability": "declared instability or null",
      "result": "stable | divergent | unstable | collapsed | candidate | inconclusive",
      "boundary": "measurement != inference != decision",
      "limitation": "What this stress test does not prove",
      "external_validation": "Validate through OMNIA-VALIDATION or declared artifact checks. Decision remains external."
    }}

---

## Result vocabulary

Use a small vocabulary:

    stable
    divergent
    unstable
    collapsed
    candidate
    inconclusive

Meaning:

- stable: structure remains within declared tolerance;
- divergent: trajectories separate under perturbation;
- unstable: structural behavior changes significantly;
- collapsed: declared structure fails to survive;
- candidate: result should be measured or validated further;
- inconclusive: evidence is insufficient.

---

## No silent promotion

A trajectory result must not silently become physical proof.

Divergence is not final truth.

Instability is not a final decision.

A dynamic stress test is not a complete physics theory.

