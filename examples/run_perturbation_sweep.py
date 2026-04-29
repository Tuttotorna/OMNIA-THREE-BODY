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


perturbations = [
    1e-6,
    1e-5,
    1e-4,
    1e-3,
    1e-2,
]

threshold = 0.5

traj_ref = simulate(initial_pos, initial_vel, masses)

results = []

for eps in perturbations:

    perturbed_pos = initial_pos.copy()
    perturbed_pos[2, 0] += eps

    traj_pert = simulate(
        perturbed_pos,
        initial_vel,
        masses,
    )

    distances = []

    for t in range(STEPS):
        d = structural_distance(
            traj_ref[:t + 1],
            traj_pert[:t + 1],
        )
        distances.append(d)

    distances = np.array(distances)

    div_idx = np.argmax(distances > threshold)

    if distances[div_idx] <= threshold:
        div_idx = -1

    final_distance = distances[-1]
    omega = omega_score(final_distance)

    result = {
        "epsilon": eps,
        "T_delta": int(div_idx),
        "Omega": float(omega),
        "IRI": float(final_distance),
    }

    results.append(result)

    print(result)


with open(
    "results/perturbation_sweep.json",
    "w"
) as f:
    json.dump(results, f, indent=2)


eps_vals = [r["epsilon"] for r in results]
td_vals = [r["T_delta"] for r in results]
omega_vals = [r["Omega"] for r in results]
iri_vals = [r["IRI"] for r in results]


plt.figure(figsize=(10, 6))

plt.plot(
    eps_vals,
    td_vals,
    marker="o",
)

plt.xscale("log")

plt.title("TΔ vs Perturbation")
plt.xlabel("Perturbation ε")
plt.ylabel("TΔ")

plt.savefig(
    "results/tdelta_vs_perturbation.png",
    dpi=300,
    bbox_inches="tight",
)

plt.show()


plt.figure(figsize=(10, 6))

plt.plot(
    eps_vals,
    omega_vals,
    marker="o",
)

plt.xscale("log")

plt.title("Ω vs Perturbation")
plt.xlabel("Perturbation ε")
plt.ylabel("Ω")

plt.savefig(
    "results/omega_vs_perturbation.png",
    dpi=300,
    bbox_inches="tight",
)

plt.show()


plt.figure(figsize=(10, 6))

plt.plot(
    eps_vals,
    iri_vals,
    marker="o",
)

plt.xscale("log")

plt.title("IRI vs Perturbation")
plt.xlabel("Perturbation ε")
plt.ylabel("IRI")

plt.savefig(
    "results/iri_vs_perturbation.png",
    dpi=300,
    bbox_inches="tight",
)

plt.show()


fig = plt.figure(figsize=(16, 5))

td_plot = np.where(
    np.array(td_vals) < 0,
    np.nan,
    np.array(td_vals),
)

ax1 = fig.add_subplot(1, 3, 1)

ax1.plot(
    eps_vals,
    td_plot,
    marker="o",
    linewidth=2,
)

ax1.set_xscale("log")

ax1.set_title("Divergence Time vs Perturbation")
ax1.set_xlabel("Perturbation ε")
ax1.set_ylabel("TΔ")

ax1.grid(True, alpha=0.3)

ax2 = fig.add_subplot(1, 3, 2)

ax2.plot(
    eps_vals,
    omega_vals,
    marker="o",
    linewidth=2,
)

ax2.set_xscale("log")

ax2.set_title("Residual Coherence vs Perturbation")
ax2.set_xlabel("Perturbation ε")
ax2.set_ylabel("Ω")

ax2.grid(True, alpha=0.3)

ax3 = fig.add_subplot(1, 3, 3)

ax3.plot(
    eps_vals,
    iri_vals,
    marker="o",
    linewidth=2,
)

ax3.set_xscale("log")

ax3.set_title("Irreversibility vs Perturbation")
ax3.set_xlabel("Perturbation ε")
ax3.set_ylabel("IRI")

ax3.grid(True, alpha=0.3)

fig.suptitle(
    "OMNIA-THREE-BODY — Perturbation Regime Sweep",
    fontsize=16,
)

plt.tight_layout()

plt.savefig(
    "results/perturbation_sweep_dashboard.png",
    dpi=300,
    bbox_inches="tight",
)

plt.show()


print("\nSaved:")
print("results/perturbation_sweep.json")
print("results/tdelta_vs_perturbation.png")
print("results/omega_vs_perturbation.png")
print("results/iri_vs_perturbation.png")
print("results/perturbation_sweep_dashboard.png")