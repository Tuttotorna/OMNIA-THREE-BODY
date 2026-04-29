# OMNIA-THREE-BODY

Structural divergence measurement for chaotic three-body dynamics under controlled perturbations.

This repository does **not** solve the three-body problem.

It uses the three-body problem as a canonical stress test for OMNIA:

> when does a deterministic system stop preserving recognizable structure under small perturbations?

---

## Core idea

The three-body problem is governed by simple deterministic laws, but its trajectories can become highly sensitive to initial conditions.

OMNIA-THREE-BODY measures this transition structurally.

It does not ask:

```text
Where will the bodies be exactly?

It asks:

How long does the system preserve structural coherence?


---

Visual result

Structural divergence under minimal perturbation:




---

Canonical claim

OMNIA does not solve chaotic dynamics.
OMNIA measures when structural coherence collapses.


---

What is measured

Given a reference three-body simulation and a minimally perturbed variant, the repository measures:

structural divergence time

residual trajectory coherence

accumulated divergence

loss of structural similarity under perturbation



---

First result

Minimal controlled perturbation test:

{
  "T_delta": 1345,
  "Omega": 0.33353144232183113,
  "IRI": 1.9982180781477268,
  "threshold": 0.5,
  "steps": 4000,
  "dt": 0.005
}

Interpretation:

The system preserves structural coherence until step 1345.
After that point, the perturbed trajectory crosses the divergence threshold.
Final residual coherence is Ω ≈ 0.3335.
Accumulated irreversible divergence is IRI ≈ 1.9982.


---

Minimal pipeline

initial state
↓
controlled perturbation
↓
three-body simulation
↓
structural comparison
↓
divergence threshold
↓
persistent metrics + visual output


---

Metrics

TΔ — Structural Divergence Time

The first timestep where structural divergence exceeds the chosen threshold.

lower TΔ
=
faster structural instability


---

Ω — Residual Structural Coherence

A normalized measure of remaining structural coherence.

Ω = 1 / (1 + IRI)

Ω ≈ 1.0  -> high residual coherence
Ω ≈ 0.0  -> structural collapse


---

IRI — Irreversibility Index

The final accumulated structural distance between reference and perturbed trajectories.

higher IRI
=
greater irreversible divergence


---

Generated outputs

Running the demo generates:

results/
├── structural_divergence.png
├── trajectory_divergence.png
├── omnia_three_body_dashboard.png
└── three_body_metrics.json


---

Run

Install dependencies:

pip install -r requirements.txt

Run the demo:

python examples/run_three_body_demo.py

Run the dashboard generator:

python examples/make_dashboard.py


---

Why the three-body problem?

Because it is a clean boundary case:

simple law
+
deterministic evolution
+
minimal perturbation
+
high sensitivity
+
structural instability

This makes it an ideal testbed for measuring divergence, fragility, and loss of structural coherence.


---

Important boundary

This repository does not claim:

prediction of exact future states

violation of known physics

elimination of chaos

solution of the three-body problem

universal forecasting


The purpose is structural measurement only.


---

Ecosystem

Part of the MB-X.01 / OMNIA ecosystem.

Core principle:

measurement != inference != decision


---

Author

Massimiliano Brighindi
Project: MB-X.01