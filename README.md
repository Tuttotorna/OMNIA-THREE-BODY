# OMNIA-THREE-BODY

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19895700.svg)](https://doi.org/10.5281/zenodo.19895700)

**OMNIA-THREE-BODY** is an experimental structural dynamics repository for measuring divergence, perturbation sensitivity, and representation-dependent stability in three-body trajectories.

It does **not** solve the three-body problem.

It is not a general physics simulator.

It is not a truth oracle.

It is not a semantic judge.

It is a structural measurement testbed.

Core boundary:

```text
measurement != inference != decision
```

Decision remains external.

---

## Current role

The three-body problem is used here as a canonical stress case:

```text
simple deterministic law
+ small perturbation
+ sensitive trajectory evolution
+ representation-dependent stability
= useful structural divergence testbed
```

The repository asks:

```text
How long does the system preserve structural coherence?
When does the perturbed trajectory diverge structurally?
Which representations collapse first?
Which representations remain stable?
```

It does not ask for exact future-state prediction.

---

## What is measured

Given a reference three-body simulation and a minimally perturbed variant, the repository measures:

- structural divergence time
- residual trajectory coherence
- accumulated divergence
- loss of structural similarity under perturbation
- representation-dependent stability

This is structural measurement, not physical proof.

---

## What this repository is not

OMNIA-THREE-BODY does not claim:

- solution of the three-body problem
- new physics
- violation of known physics
- universal forecasting
- exact long-horizon prediction
- discovery of a universal instability constant
- semantic interpretation
- decision authority

It is not physics in the sense of proposing a new physical law.

It uses a physical-style dynamical system as a stress test for structural measurement.

---

## Main observation

The core observation is representation-dependent structural collapse:

```text
local trajectory representations can collapse
while global invariant representations remain stable
```

Observed example:

```text
cartesian coordinates -> strong divergence
pairwise distances    -> faster collapse
total energy          -> relatively stable
angular momentum      -> almost invariant
center of mass        -> almost invariant
```

This connects directly to the OMNIABASE principle:

```text
structure is not exhausted by one representation
```

---

## Metrics

### TΔ — Structural Divergence Time

The first timestep where structural divergence exceeds the chosen threshold.

```text
lower TΔ = faster structural instability
TΔ = -1 means threshold not crossed within the simulated horizon
```

### Ω — Residual Structural Coherence

A normalized measure of remaining structural coherence.

```text
Ω = 1 / (1 + IRI)
```

Reading:

```text
Ω ≈ 1.0 -> high residual coherence
Ω ≈ 0.0 -> structural collapse
```

### IRI — Irreversibility Index

The accumulated structural distance between reference and perturbed trajectories.

```text
higher IRI = greater irreversible divergence
```

---

## Minimal pipeline

```text
initial state
  -> controlled perturbation
  -> three-body simulation
  -> structural comparison
  -> divergence threshold
  -> persistent metrics + visual output
```

---

## Visual results

Structural divergence dashboard:

![OMNIA Three Body Dashboard](https://raw.githubusercontent.com/Tuttotorna/OMNIA-THREE-BODY/main/results/omnia_three_body_dashboard.png)

Perturbation sweep dashboard:

![Perturbation Sweep Dashboard](https://raw.githubusercontent.com/Tuttotorna/OMNIA-THREE-BODY/main/results/perturbation_sweep_dashboard.png)

---

## Generated outputs

Current tracked outputs include:

```text
results/three_body_metrics.json
results/perturbation_sweep.json
results/representation_comparison.json
results/omnia_three_body_dashboard.png
results/perturbation_sweep_dashboard.png
results/representation_comparison.png
```

---

## Run

Install dependencies:

```bash
python -m pip install -r requirements.txt
python -m pip install -e .
```

Run checks:

```bash
python -m pytest
```

Run examples:

```bash
python examples/run_three_body_demo.py
python examples/run_perturbation_sweep.py
python examples/run_representation_analysis.py
```

---

## Documentation

Public entrypoints:

- [`docs/THREE_BODY_SCOPE.md`](docs/THREE_BODY_SCOPE.md)
- [`docs/RESULTS_INDEX.md`](docs/RESULTS_INDEX.md)
- [`docs/REPOSITORY_STATUS.md`](docs/REPOSITORY_STATUS.md)

Legacy / detailed notes:

- [`docs/THREE_BODY_STRUCTURAL_DIVERGENCE.md`](docs/THREE_BODY_STRUCTURAL_DIVERGENCE.md)
- [`docs/PERTURBATION_REGIMES.md`](docs/PERTURBATION_REGIMES.md)
- [`docs/CROSS_REPRESENTATION_DIVERGENCE.md`](docs/CROSS_REPRESENTATION_DIVERGENCE.md)

---

## Ecosystem position

Part of the MB-X.01 / OMNIA ecosystem:

```text
OMNIABASE         = representation / multi-base observation layer
OMNIA             = structural measurement core
OMNIA-INVARIANCE  = invariance / trajectory-space analysis
OMNIA-THREE-BODY  = experimental structural dynamics layer
OMNIA-VALIDATION  = evidence / reproducibility layer
Decision           = external layer
```

The boundary remains strict:

```text
measurement != inference != decision
```

---

## Related repositories

- lon-mirror: https://github.com/Tuttotorna/lon-mirror
- OMNIABASE: https://github.com/Tuttotorna/OMNIABASE
- OMNIA: https://github.com/Tuttotorna/OMNIA
- OMNIA-INVARIANCE: https://github.com/Tuttotorna/OMNIA-INVARIANCE
- OMNIA-VALIDATION: https://github.com/Tuttotorna/OMNIA-VALIDATION
- OMNIA-RADAR: https://github.com/Tuttotorna/OMNIA-RADAR

---

## Citation

If you reference this repository, use the archived Zenodo record:

```text
DOI: 10.5281/zenodo.19895700
https://doi.org/10.5281/zenodo.19895700
```

Citation metadata is available in:

- [`CITATION.cff`](CITATION.cff)

---

## Summary

OMNIA-THREE-BODY is an experimental structural dynamics layer.

It uses three-body trajectories as a stress test for structural divergence measurement.

It is not a physics solver.

It is not a truth oracle.

Its central boundary is:

```text
measurement != inference != decision
```
