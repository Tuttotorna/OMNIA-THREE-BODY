# OMNIA-THREE-BODY Results Index

## Purpose

This file gives a public entrypoint into OMNIA-THREE-BODY result artifacts.

## Main result artifacts

### Base structural divergence

Relevant file:

- `results/three_body_metrics.json`

Purpose:

- record the base controlled perturbation result
- report TΔ, Ω, IRI, threshold, steps, and dt

### Perturbation sweep

Relevant files:

- `results/perturbation_sweep.json`
- `results/perturbation_sweep_dashboard.png`

Purpose:

- test how structural divergence changes as perturbation strength increases

Observed pattern:

```text
epsilon increases
TΔ decreases
Ω decreases
IRI increases
```

### Cross-representation analysis

Relevant files:

- `results/representation_comparison.json`
- `results/representation_comparison.png`

Purpose:

- compare whether the same simulated system remains structurally stable across different representations

Key reading:

```text
local trajectory representations may collapse
global invariant-like representations may remain stable
```

### Visual dashboard

Relevant file:

- `results/omnia_three_body_dashboard.png`

Purpose:

- provide a compact visual summary of structural divergence behavior

## Reading rule

```text
result artifact = structural measurement artifact
result artifact != physics proof
result artifact != decision authority
```
