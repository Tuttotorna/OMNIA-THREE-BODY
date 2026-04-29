# OMNIA-THREE-BODY

Structural divergence measurement for chaotic three-body dynamics under controlled perturbations.

This repository does **not** solve the three-body problem.

It uses the three-body problem as a canonical stress test for OMNIA:

> when does a deterministic system stop preserving recognizable structure under small perturbations?

---

## Visual result

Structural divergence under minimal perturbation:

![OMNIA Three Body Dashboard](https://raw.githubusercontent.com/Tuttotorna/OMNIA-THREE-BODY/main/results/omnia_three_body_dashboard.png)

---

## Perturbation sweep

Structural response under increasing perturbation:

![Perturbation Sweep Dashboard](https://raw.githubusercontent.com/Tuttotorna/OMNIA-THREE-BODY/main/results/perturbation_sweep_dashboard.png)

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

Perturbation sweep result

Controlled perturbation sweep:

[
  {
    "epsilon": 1e-06,
    "T_delta": -1,
    "Omega": 0.9728208145236964,
    "IRI": 0.027938532020011158
  },
  {
    "epsilon": 1e-05,
    "T_delta": -1,
    "Omega": 0.7904666344102294,
    "IRI": 0.26507553446086235
  },
  {
    "epsilon": 0.0001,
    "T_delta": 1345,
    "Omega": 0.33353144232183113,
    "IRI": 1.9982180781477268
  },
  {
    "epsilon": 0.001,
    "T_delta": 530,
    "Omega": 0.08966687780479642,
    "IRI": 10.152390096340664
  },
  {
    "epsilon": 0.01,
    "T_delta": 451,
    "Omega": 0.0541844638036885,
    "IRI": 17.455474684090664
  }
]

Observed structure:

ε increases
↓
TΔ decreases
Ω decreases
IRI increases

Interpretation:

larger initial perturbation
=
shorter coherence survival time
+
lower residual coherence
+
higher irreversible divergence


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

TΔ = -1 means that the divergence threshold was not crossed within the simulated horizon.


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

Running the demo and sweep generates:

results/
├── structural_divergence.png
├── trajectory_divergence.png
├── omnia_three_body_dashboard.png
├── perturbation_sweep.json
├── tdelta_vs_perturbation.png
├── omega_vs_perturbation.png
├── iri_vs_perturbation.png
├── perturbation_sweep_dashboard.png
└── three_body_metrics.json


---

Run

Install dependencies:

pip install -r requirements.txt

Run the base demo:

python examples/run_three_body_demo.py

Run the perturbation sweep:

python examples/run_perturbation_sweep.py


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

discovery of a universal instability constant


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

