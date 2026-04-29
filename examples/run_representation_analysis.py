import os
import json
import numpy as np
import matplotlib.pyplot as plt


G = 1.0
DT = 0.005
STEPS = 4000
THRESHOLD = 0.5

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
    traj_pos = []
    traj_vel = []

    pos = pos.copy()
    vel = vel.copy()

    for _ in range(STEPS):
        traj_pos.append(pos.copy())
        traj_vel.append(vel.copy())

        acc = acceleration(pos, masses)

        vel += acc * DT
        pos += vel * DT

    return np.array(traj_pos), np.array(traj_vel)


def omega_score(d):
    return 1.0 / (1.0 + d)


def divergence_metrics(distances, threshold):
    distances = np.array(distances)

    div_idx = np.argmax(distances > threshold)

    if distances[div_idx] <= threshold:
        div_idx = -1

    iri = float(distances[-1])
    omega = float(omega_score(iri))

    return {
        "T_delta": int(div_idx),
        "Omega": omega,
        "IRI": iri,
    }


def pairwise_distances(traj_pos):
    d01 = np.linalg.norm(traj_pos[:, 0] - traj_pos[:, 1], axis=1)
    d02 = np.linalg.norm(traj_pos[:, 0] - traj_pos[:, 2], axis=1)
    d12 = np.linalg.norm(traj_pos[:, 1] - traj_pos[:, 2], axis=1)

    return np.stack([d01, d02, d12], axis=1)


def total_energy(traj_pos, traj_vel, masses):
    kinetic = 0.5 * np.sum(
        masses[None, :] * np.sum(traj_vel**2, axis=2),
        axis=1,
    )

    potential = np.zeros(len(traj_pos))

    for i in range(3):
        for j in range(i + 1, 3):
            r = np.linalg.norm(traj_pos[:, i] - traj_pos[:, j], axis=1) + 1e-9
            potential -= G * masses[i] * masses[j] / r

    return kinetic + potential


def angular_momentum(traj_pos, traj_vel, masses):
    momenta = masses[None, :, None] * traj_vel

    cross_z = (
        traj_pos[:, :, 0] * momenta[:, :, 1]
        - traj_pos[:, :, 1] * momenta[:, :, 0]
    )

    return np.sum(cross_z, axis=1)


def center_of_mass(traj_pos, masses):
    total_mass = np.sum(masses)

    return np.sum(
        traj_pos * masses[None, :, None],
        axis=1,
    ) / total_mass


def mean_distance_series(a, b):
    return np.array([
        np.mean(np.linalg.norm(a[:t + 1] - b[:t + 1], axis=-1))
        for t in range(len(a))
    ])


def scalar_distance_series(a, b):
    return np.array([
        np.mean(np.abs(a[:t + 1] - b[:t + 1]))
        for t in range(len(a))
    ])


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

traj_ref_pos, traj_ref_vel = simulate(initial_pos, initial_vel, masses)
traj_pert_pos, traj_pert_vel = simulate(perturbed_pos, initial_vel, masses)

representations = {}

representations["cartesian_coordinates"] = mean_distance_series(
    traj_ref_pos,
    traj_pert_pos,
)

representations["pairwise_distances"] = mean_distance_series(
    pairwise_distances(traj_ref_pos),
    pairwise_distances(traj_pert_pos),
)

representations["total_energy"] = scalar_distance_series(
    total_energy(traj_ref_pos, traj_ref_vel, masses),
    total_energy(traj_pert_pos, traj_pert_vel, masses),
)

representations["angular_momentum"] = scalar_distance_series(
    angular_momentum(traj_ref_pos, traj_ref_vel, masses),
    angular_momentum(traj_pert_pos, traj_pert_vel, masses),
)

representations["center_of_mass"] = mean_distance_series(
    center_of_mass(traj_ref_pos, masses),
    center_of_mass(traj_pert_pos, masses),
)

results = {}

for name, distances in representations.items():
    metrics = divergence_metrics(distances, THRESHOLD)
    results[name] = metrics

    print(name, metrics)


with open("results/representation_comparison.json", "w") as f:
    json.dump(results, f, indent=2)


names = list(results.keys())
t_delta = [results[name]["T_delta"] for name in names]
omega = [results[name]["Omega"] for name in names]
iri = [results[name]["IRI"] for name in names]

t_delta_plot = [
    np.nan if value < 0 else value
    for value in t_delta
]

x = np.arange(len(names))

fig = plt.figure(figsize=(15, 5))

ax1 = fig.add_subplot(1, 3, 1)
ax1.bar(x, t_delta_plot)
ax1.set_title("TΔ by Representation")
ax1.set_xticks(x)
ax1.set_xticklabels(names, rotation=45, ha="right")
ax1.set_ylabel("TΔ")

ax2 = fig.add_subplot(1, 3, 2)
ax2.bar(x, omega)
ax2.set_title("Ω by Representation")
ax2.set_xticks(x)
ax2.set_xticklabels(names, rotation=45, ha="right")
ax2.set_ylabel("Ω")

ax3 = fig.add_subplot(1, 3, 3)
ax3.bar(x, iri)
ax3.set_title("IRI by Representation")
ax3.set_xticks(x)
ax3.set_xticklabels(names, rotation=45, ha="right")
ax3.set_ylabel("IRI")

fig.suptitle(
    "OMNIA-THREE-BODY — Cross-Representation Divergence",
    fontsize=16,
)

plt.tight_layout()

plt.savefig(
    "results/representation_comparison.png",
    dpi=300,
    bbox_inches="tight",
)

plt.show()

print("\nSaved:")
print("results/representation_comparison.json")
print("results/representation_comparison.png")