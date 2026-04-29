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

---

## 2. `requirements.txt`

```text
numpy
matplotlib


---

3. examples/run_three_body_demo.py

import os
import json
import numpy as np
import matplotlib.pyplot as plt


G = 1.0
DT = 0.005
STEPS = 4000


os.makedirs("results", exist_ok=True)


def acceleration(pos, masses):
    n = len(masses)
    acc = np.zeros_like(pos)

    for i in range(n):
        for j in range(n):
            if i == j:
                continue

            r = pos[j] - pos[i]
            dist = np.linalg.norm(r) + 1e-9
            acc[i] += G * masses[j] * r / dist**3

    return acc


def simulate(pos, vel, masses):
    traj = []

    pos = pos.copy()
    vel = vel.copy()

    for _ in range(STEPS):
        traj.append(pos.copy())

        acc = acceleration(pos, masses)

        vel += acc * DT
        pos += vel * DT

    return np.array(traj)


def structural_distance(a, b):
    return np.mean(np.linalg.norm(a - b, axis=2))


def omega_score(d):
    return 1.0 / (1.0 + d)


masses = np.array([1.0, 1.0, 1.0])

initial_pos = np.array([
    [-1.0, 0.0],
    [1.0, 0.0],
    [0.0, 0.5],
])

initial_vel = np.array([
    [0.0, -0.4],
    [0.0, 0.4],
    [0.5, 0.0],
])

perturbed_pos = initial_pos.copy()
perturbed_pos[2, 0] += 0.0001

traj_ref = simulate(initial_pos, initial_vel, masses)
traj_pert = simulate(perturbed_pos, initial_vel, masses)

distances = []

for t in range(STEPS):
    d = structural_distance(
        traj_ref[:t + 1],
        traj_pert[:t + 1],
    )
    distances.append(d)

distances = np.array(distances)

threshold = 0.5
div_idx = np.argmax(distances > threshold)

if distances[div_idx] <= threshold:
    div_idx = -1

final_distance = distances[-1]
omega = omega_score(final_distance)

print("\n================ OMNIA THREE BODY ================\n")
print(f"TΔ  = {div_idx}")
print(f"Ω   = {omega:.6f}")
print(f"IRI = {final_distance:.6f}")

metrics = {
    "T_delta": int(div_idx),
    "Omega": float(omega),
    "IRI": float(final_distance),
    "threshold": float(threshold),
    "steps": int(STEPS),
    "dt": float(DT),
}

with open("results/three_body_metrics.json", "w") as f:
    json.dump(metrics, f, indent=2)

print("\nSaved metrics:")
print(json.dumps(metrics, indent=2))

np.save("results/traj_ref.npy", traj_ref)
np.save("results/traj_pert.npy", traj_pert)
np.save("results/distances.npy", distances)

plt.figure(figsize=(10, 5))
plt.plot(distances)
plt.axhline(threshold, linestyle="--")
plt.title("Structural Divergence")
plt.xlabel("Time Step")
plt.ylabel("Structural Distance")
plt.savefig(
    "results/structural_divergence.png",
    dpi=300,
    bbox_inches="tight",
)
plt.show()

plt.figure(figsize=(8, 8))

plt.plot(
    traj_ref[:, 0, 0],
    traj_ref[:, 0, 1],
    label="Body 1 reference",
)

plt.plot(
    traj_pert[:, 0, 0],
    traj_pert[:, 0, 1],
    linestyle="--",
    label="Body 1 perturbed",
)

plt.title("Trajectory Divergence")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()

plt.savefig(
    "results/trajectory_divergence.png",
    dpi=300,
    bbox_inches="tight",
)

plt.show()


---

4. examples/make_dashboard.py

import os
import json
import numpy as np
import matplotlib.pyplot as plt


os.makedirs("results", exist_ok=True)

traj_ref = np.load("results/traj_ref.npy")
traj_pert = np.load("results/traj_pert.npy")
distances = np.load("results/distances.npy")

with open("results/three_body_metrics.json", "r") as f:
    metrics = json.load(f)

div_idx = metrics["T_delta"]
omega = metrics["Omega"]
final_distance = metrics["IRI"]
threshold = metrics["threshold"]

fig = plt.figure(figsize=(14, 6))

ax1 = fig.add_subplot(1, 2, 1)

ax1.plot(distances, linewidth=2)
ax1.axhline(threshold, linestyle="--", label=f"Threshold = {threshold}")
ax1.axvline(div_idx, linestyle="--", label=f"TΔ = {div_idx}")

ax1.set_title("OMNIA Structural Divergence")
ax1.set_xlabel("Time Step")
ax1.set_ylabel("Structural Distance")
ax1.legend()

text = f"TΔ = {div_idx}\nΩ = {omega:.6f}\nIRI = {final_distance:.6f}"

ax1.text(
    0.05,
    0.95,
    text,
    transform=ax1.transAxes,
    verticalalignment="top",
    bbox=dict(boxstyle="round", alpha=0.15),
)

ax2 = fig.add_subplot(1, 2, 2)

for body in range(3):
    ax2.plot(
        traj_ref[:, body, 0],
        traj_ref[:, body, 1],
        linewidth=1.8,
        label=f"Body {body + 1} reference",
    )

    ax2.plot(
        traj_pert[:, body, 0],
        traj_pert[:, body, 1],
        linestyle="--",
        linewidth=1.2,
        label=f"Body {body + 1} perturbed",
    )

ax2.set_title("Three-Body Trajectory Divergence")
ax2.set_xlabel("x")
ax2.set_ylabel("y")
ax2.legend(fontsize=8)

plt.tight_layout()

plt.savefig(
    "results/omnia_three_body_dashboard.png",
    dpi=300,
    bbox_inches="tight",
)

plt.show()

print("Saved: results/omnia_three_body_dashboard.png")


---

5. docs/THREE_BODY_STRUCTURAL_DIVERGENCE.md

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

---

## 6. `.gitignore`

```text
__pycache__/
*.pyc
*.pyo
*.pyd

.ipynb_checkpoints/

.venv/
venv/
env/

.DS_Store

results/*.npy


---

7. data/.gitkeep



File vuoto.


---

8. results/.gitkeep



File vuoto.


---

