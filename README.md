# OMNIA-THREE-BODY


[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19895700.svg)](https://doi.org/10.5281/zenodo.19895700)

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

Observed structure:

```text
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

Cross-representation divergence

The same three-body dynamics can collapse in one representation while remaining stable in another.



Observed structure:

cartesian coordinates
→ strong divergence

pairwise distances
→ even faster collapse

total energy
→ relatively stable

angular momentum
→ almost invariant

center of mass
→ almost invariant

Core observation:

the same system
can appear unstable or stable
depending on the representation layer

This connects directly to the OMNIABASE principle:

structure stronger than representation


---

Core idea

The three-body problem is governed by simple deterministic laws, but its trajectories can become highly sensitive to initial conditions.

OMNIA-THREE-BODY measures this transition structurally.

It does not ask:

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

representation-dependent stability



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


---

Cross-representation result

{
  "cartesian_coordinates": {
    "T_delta": 1345,
    "Omega": 0.33353144232183113,
    "IRI": 1.9982180781477268
  },
  "pairwise_distances": {
    "T_delta": 827,
    "Omega": 0.14553109791625538,
    "IRI": 5.871383603354944
  },
  "total_energy": {
    "T_delta": -1,
    "Omega": 0.7443741914232316,
    "IRI": 0.3434103593624276
  },
  "angular_momentum": {
    "T_delta": -1,
    "Omega": 0.9999999999999933,
    "IRI": 6.7288397076481484e-15
  },
  "center_of_mass": {
    "T_delta": -1,
    "Omega": 0.9999666677777395,
    "IRI": 3.333333333474693e-05
  }
}

Interpretation:

local trajectory representations collapse,
while global invariant representations remain structurally stable.


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

Running the demo, sweep, and representation analysis generates:

results/
├── structural_divergence.png
├── trajectory_divergence.png
├── omnia_three_body_dashboard.png
├── three_body_metrics.json
├── perturbation_sweep.json
├── tdelta_vs_perturbation.png
├── omega_vs_perturbation.png
├── iri_vs_perturbation.png
├── perturbation_sweep_dashboard.png
├── representation_comparison.json
└── representation_comparison.png

The scripts may also generate temporary NumPy arrays:

results/traj_ref.npy
results/traj_pert.npy
results/distances.npy


---

Run

Install dependencies:

pip install -r requirements.txt

Run the base demo:

python examples/run_three_body_demo.py

Run the perturbation sweep:

python examples/run_perturbation_sweep.py

Run the cross-representation analysis:

python examples/run_representation_analysis.py


---

Documentation

Detailed notes:

docs/THREE_BODY_STRUCTURAL_DIVERGENCE.md
docs/PERTURBATION_REGIMES.md
docs/CROSS_REPRESENTATION_DIVERGENCE.md


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

Related repositories:

OMNIA
OMNIABASE
OMNIA-LIMIT
OMNIA-RADAR

---


```text
LON-MIRROR
|
├── CORE
|   ├── OMNIA
|   ├── OMNIA-INVARIANCE
|   ├── omnia-limit
|   └── OMNIA-RADAR
|
├── RESEARCH
|   ├── OMNIA-CONSTANT
|   └── OMNIA-THREE-BODY
|
├── REPRESENTATION
|   └── OMNIABASE
|
└── APPLICATIONS
    ├── OMNIA-SECURITY
    ├── OMNIA-CRYPTO
    └── OMNIAMIND

Root

LON-MIRROR


Canonical ecosystem hub, lineage map, navigation layer, and coordination entry point.


---

Core

OMNIA


Core structural measurement framework.

OMNIA-INVARIANCE


Core validation and invariance-testing repository.
Focuses on structural invariance, perturbation behavior, and controlled evidence around Ω under transformation.

omnia-limit


Structural stopping conditions, saturation, irreducibility, and limit behavior.

OMNIA-RADAR


Structural drift surfacing and trajectory visualization layer.


---

Research

OMNIA-CONSTANT


Post-analysis and falsification repository for Ω-region behavior.
Current focus: whether observed Ω corridors behave as structural transition regimes or collapse as measurement artifacts.
No universal structural constant is declared.

OMNIA-THREE-BODY


Experimental dynamics repository for multi-body structural interaction tests.
Focuses on instability, trajectory interaction, and non-trivial structural behavior under interacting perturbations.


---

Representation

OMNIABASE


Multi-base structural representation and invariance exploration layer.


---

Applications

OMNIA-SECURITY


Bounded structural diagnostics for security-relevant systems.

OMNIA-CRYPTO


Bounded structural diagnostics for cryptographic behavior.

OMNIAMIND


Bounded structural diagnostics for cognitive and reasoning-related behavior.


---

Architectural Separation

LON-MIRROR
=
ecosystem hub

OMNIA
=
core structural measurement layer

OMNIA-INVARIANCE
=
core invariance validation layer

OMNIA-CONSTANT
=
post-analysis / falsification layer for Ω-region behavior

OMNIA-THREE-BODY
=
experimental structural dynamics layer

Other repositories
=
representation layers,
limit layers,
visualization layers,
or bounded domain verticalizations.


---

Core Boundary

measurement != inference != decision
---

Author

Massimiliano Brighindi
Project: MB-X.01