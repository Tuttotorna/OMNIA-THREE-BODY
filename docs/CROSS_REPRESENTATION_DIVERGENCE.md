# Cross-Representation Divergence

## Core idea

The same physical system can appear stable or unstable depending on the chosen representation.

OMNIA measures structural divergence across multiple representations of the same three-body dynamics.

The goal is to test:

```text
which structures survive representation change?


---

Motivation

Chaotic systems are usually observed directly in coordinate space.

But coordinate space is only one representation.

The same system can also be represented through:

pairwise distances

total energy

angular momentum

center of mass

invariant quantities


OMNIA investigates whether structural collapse is representation-dependent.


---

Experiment

Two nearly identical three-body systems are simulated.

The second system receives a minimal perturbation:

Δx = 0.0001

The resulting trajectories are then analyzed through different representations.


---

Representations tested

1. Cartesian coordinates

Direct spatial coordinates:

(x, y)


---

2. Pairwise distances

Distances between all body pairs:

d01
d02
d12


---

3. Total energy

Combined kinetic + potential energy.


---

4. Angular momentum

Global rotational invariant of the system.


---

5. Center of mass

Global averaged system position.


---

Results

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


---

Observed structure

The results show strong representation dependence.

Coordinate space

cartesian_coordinates
TΔ = 1345
Ω ≈ 0.33

The trajectories eventually lose strong structural coherence.


---

Pairwise-distance space

pairwise_distances
TΔ = 827
Ω ≈ 0.15

Relative geometry collapses even earlier than direct coordinate space.


---

Energy space

total_energy
TΔ = -1
Ω ≈ 0.74

Energy remains comparatively stable despite visible trajectory divergence.


---

Angular momentum

angular_momentum
Ω ≈ 1.0
IRI ≈ 0

Angular momentum remains almost perfectly invariant.


---

Center of mass

center_of_mass
Ω ≈ 1.0
IRI ≈ 0

The center of mass remains structurally stable.


---

Interpretation

The same dynamical system can:

collapse in one representation
while remaining coherent in another

This suggests that:

structural instability
is partially representation-dependent


---

OMNIA interpretation

OMNIA does not measure only:

whether a system diverges

It measures:

where divergence appears
and where structure survives

This connects directly to the OMNIABASE principle:

structure stronger than representation


---

Canonical observation

The experiment suggests a hierarchy:

global invariants
↓
more stable

local coordinates
↓
more fragile


---

Important boundary

This experiment does not claim:

new gravitational physics

solution of chaotic dynamics

universal invariance laws


It only measures structural divergence persistence across representations.

