# Three-Body Structural Divergence

## Core question

The goal is not to solve the three-body problem.

The goal is to measure:

```text
when does deterministic structure stop remaining structurally recognizable?


---

Why the three-body problem?

The three-body problem is one of the cleanest examples of:

simple rules
+
deterministic evolution
+
high sensitivity to perturbation

Small initial changes can eventually produce large trajectory divergence.

This makes the system an ideal structural stress test.


---

OMNIA interpretation

OMNIA treats the system as a structural object observed through time.

Instead of asking:

Where exactly will the bodies be?

OMNIA asks:

How long does the system preserve structural coherence?


---

Structural divergence

Two simulations are initialized with nearly identical states.

Example:

Simulation A:
x = 0.500000

Simulation B:
x = 0.500100

Both systems evolve under identical physical laws.

OMNIA measures how rapidly their structural similarity collapses.


---

Core metrics

TΔ — Structural Divergence Time

The first timestep where divergence exceeds a chosen threshold.

Interpretation:

lower TΔ
=
faster structural instability


---

Ω — Residual Structural Coherence

A normalized measure of remaining similarity between trajectories.

Definition used in the minimal demo:

Ω = 1 / (1 + IRI)

Example interpretation:

Ω ≈ 1.0
high coherence

Ω ≈ 0.0
structural collapse


---

IRI — Irreversibility Index

Measures accumulated non-recoverable divergence.

In the minimal demo, IRI is the final structural distance between the reference trajectory and the perturbed trajectory.

Interpretation:

higher IRI
=
greater irreversible separation


---

Minimal experiment

The initial system uses three equal masses.

A perturbation of 0.0001 is applied to the x-coordinate of the third body.

reference:
body 3 x = 0.0000

perturbed:
body 3 x = 0.0001

The same deterministic update rule is then applied to both systems.


---

First measured result

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

Multi-representation principle

The same system can be analyzed through different representations:

Cartesian coordinates

Relative distances

Energy evolution

Angular momentum

Center-of-mass dynamics

Orbit geometry


A structural property is stronger if it survives across multiple representations.


---

Canonical claim

OMNIA does not solve chaotic systems.

OMNIA measures the persistence and collapse
of structural coherence under transformation.


---

Long-term direction

Potential future experiments:

N-body systems

orbital resonance collapse

chaotic regime transitions

structural phase detection

cross-representation invariance

silent instability detection

comparison between coordinate-space and invariant-space divergence



---

Important boundary

This repository does not claim:

prediction of exact future states

violation of known physics

elimination of chaos

solution of the three-body problem

universal forecasting


The purpose is structural measurement only.

