# OMNIA-THREE-BODY

## DOI

[![DOI](https://zenodo.org/badge/1224623666.svg)](https://zenodo.org/badge/latestdoi/1224623666)

Release DOI:

    10.5281/zenodo.19895700

Zenodo latest DOI link:

    https://doi.org/10.5281/zenodo.19895700

GitHub release:

    https://github.com/Tuttotorna/OMNIA-THREE-BODY/releases/tag/v1.0.0

**Dynamic divergence stress test.**

OMNIA-THREE-BODY is the chaotic dynamics stress-test layer of the MB-X.01 / OMNIA ecosystem.

Its role is narrow:

    initial state -> perturbation -> trajectory divergence -> structural instability

It asks one question:

    how does structural behavior diverge when a dynamic system is perturbed?

OMNIA-THREE-BODY is not the ecosystem landing page.

It is not the validation showroom.

It is not the OMNIA core measurement engine.

It is not a physics proof.

It is not a claim that OMNIA replaces physical simulation validation.

It is a stress test for observing structural divergence under controlled perturbation.

Canonical boundary:

    measurement != inference != decision

    Decision remains external

---

## Start here

From a clean environment:

    git clone https://github.com/Tuttotorna/OMNIA-THREE-BODY.git
    cd OMNIA-THREE-BODY
    python -m pip install -e .
    pytest

If example scripts are available, run the smallest demonstration after tests pass.

The goal is to see the dynamic divergence path:

    initial state
      -> perturbation
      -> trajectory divergence
      -> structural instability
      -> external validation

---

## What OMNIA-THREE-BODY does

OMNIA-THREE-BODY uses a three-body style dynamic setting as a stress test for structural divergence.

It can help expose:

- trajectory divergence;
- perturbation sensitivity;
- regime instability;
- structural drift;
- instability candidates worth measuring;
- artifacts suitable for validation.

Public compression:

    small perturbation
    large trajectory divergence
    measurable structural instability

---

## What OMNIA-THREE-BODY does not do

OMNIA-THREE-BODY does not:

- prove physical truth;
- replace physical simulation validation;
- infer semantic truth;
- decide correctness;
- replace OMNIA measurement;
- replace OMNIA-VALIDATION;
- prove universal chaos claims;
- convert trajectory divergence into final decision.

Decision remains external.

---

## Public mental model

    Chaotic systems amplify small differences.
    OMNIA-THREE-BODY uses that amplification as a stress test.
    The target is structural divergence, not physical proof.

---

## Stress-test contract

Every serious OMNIA-THREE-BODY result should make clear:

| Component | Meaning |
|---|---|
| initial state | Starting dynamic configuration |
| perturbation | Controlled change applied |
| trajectory | Observed path after evolution |
| divergence | How trajectories separate |
| structural instability | What structural behavior changes or collapses |
| artifact | Where the result is stored |
| limitation | What the stress test does not prove |
| external validation | How the result should be tested later |

---

## Result vocabulary

Recommended result vocabulary:

    stable
    divergent
    unstable
    collapsed
    candidate
    inconclusive

Meaning:

- stable: trajectory or structure remains within declared tolerance;
- divergent: trajectories separate under perturbation;
- unstable: structure changes significantly;
- collapsed: declared structure fails to survive;
- candidate: result is worth full measurement or validation;
- inconclusive: evidence is insufficient or ambiguous.

---

## Recommended reading order

1. [docs/QUICKSTART_THREE_BODY.md](docs/QUICKSTART_THREE_BODY.md)
2. [docs/THREE_BODY_OVERVIEW.md](docs/THREE_BODY_OVERVIEW.md)
3. [docs/TRAJECTORY_CONTRACT.md](docs/TRAJECTORY_CONTRACT.md)
4. [docs/DIVERGENCE_AND_INSTABILITY.md](docs/DIVERGENCE_AND_INSTABILITY.md)
5. [docs/BOUNDARY.md](docs/BOUNDARY.md)
6. [docs/THREE_BODY_MANIFEST.json](docs/THREE_BODY_MANIFEST.json)

---

## Related repositories

| Repository | Role |
|---|---|
| [lon-mirror](https://github.com/Tuttotorna/lon-mirror) | Canonical ecosystem entry point |
| [OMNIA-VALIDATION](https://github.com/Tuttotorna/OMNIA-VALIDATION) | Public validation showroom |
| [OMNIA](https://github.com/Tuttotorna/OMNIA) | Core structural measurement engine |
| [OMNIABASE](https://github.com/Tuttotorna/OMNIABASE) | Representation invariance foundation |
| [OMNIA-RADAR](https://github.com/Tuttotorna/OMNIA-RADAR) | Structural signal detection layer |
| [OMNIA-INVARIANCE](https://github.com/Tuttotorna/OMNIA-INVARIANCE) | Transformation and invariance layer |
| [omnia-limit](https://github.com/Tuttotorna/omnia-limit) | Stop / continue boundary layer |
| [OMNIA-CONSTANT](https://github.com/Tuttotorna/OMNIA-CONSTANT) | Stable-region falsification layer |
| [OMNIAMIND](https://github.com/Tuttotorna/OMNIAMIND) | Structural cognition orchestration layer |

---

## Ecosystem entry point

For the full ecosystem map, start here:

    https://github.com/Tuttotorna/lon-mirror

For public validation artifacts, start here:

    https://github.com/Tuttotorna/OMNIA-VALIDATION

For core structural measurement, start here:

    https://github.com/Tuttotorna/OMNIA

---


## Smoke-test required terms

    not a truth oracle
    not a semantic judge
    not a general physics simulator

## License

MIT.

