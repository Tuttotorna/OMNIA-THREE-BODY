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

plt.axhline(
    threshold,
    linestyle="--",
)

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