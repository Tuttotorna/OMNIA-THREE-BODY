<!-- MB-X.01 LON RELEASE:START -->

## MB-X.01 / L.O.N. release state

Repository: Tuttotorna/OMNIA-THREE-BODY
Release tag: v2026.05.21
Release commit: f84a928
Release DOI: 10.5281/zenodo.20322693

Boundary:

measurement != validation
validation != orchestration
orchestration != decision
decision != measurement

<!-- MB-X.01 LON RELEASE:END -->

# OMNIA-THREE-BODY

<!-- ZENODO DOI:START -->

## DOI

[![DOI](https://zenodo.org/badge/DOI/10.5281%2Fzenodo.20322693.svg)](https://doi.org/10.5281/zenodo.20322693)

Zenodo DOI badge for this repository.

Repository: Tuttotorna/OMNIA-THREE-BODY
GitHub repository id: 1224623666
Release tag: v2026.05.21
Latest release DOI: 10.5281/zenodo.20322693

<!-- ZENODO DOI:END -->


## DOI

[![DOI](https://zenodo.org/badge/1224623666.svg)](https://zenodo.org/badge/latestdoi/1224623666)

Release DOI: [10.5281/zenodo.19895700](https://doi.org/10.5281/zenodo.19895700)

GitHub release: [OMNIA-THREE-BODY v1.0.0 release](https://github.com/Tuttotorna/OMNIA-THREE-BODY/releases/tag/v1.0.0)

## Start here

From a clean environment:

    git clone [OMNIA-THREE-BODY.git](https://github.com/Tuttotorna/OMNIA-THREE-BODY.git)
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

## Ecosystem entry point

For the full ecosystem map, start here:

[lon-mirror](https://github.com/Tuttotorna/lon-mirror)

For public validation artifacts, start here:

[OMNIA-VALIDATION](https://github.com/Tuttotorna/OMNIA-VALIDATION)

For core structural measurement, start here:

[OMNIA](https://github.com/Tuttotorna/OMNIA)

---


## Smoke-test required terms

    not a truth oracle
    not a semantic judge
    not a general physics simulator

## Related repositories

| Repository | Role |
|---|---|
| [lon-mirror](https://github.com/Tuttotorna/lon-mirror) | Canonical public entry point |
| [OMNIA-VALIDATION](https://github.com/Tuttotorna/OMNIA-VALIDATION) | Public validation showroom |
| [OMNIA](https://github.com/Tuttotorna/OMNIA) | Core structural measurement engine |
| [OMNIABASE](https://github.com/Tuttotorna/OMNIABASE) | Representation invariance foundation |
| [omnia-limit](https://github.com/Tuttotorna/omnia-limit) | Stop / continue boundary layer |
| [OMNIA-RADAR](https://github.com/Tuttotorna/OMNIA-RADAR) | Structural signal detection layer |
| [OMNIA-INVARIANCE](https://github.com/Tuttotorna/OMNIA-INVARIANCE) | Structural invariance layer |
| [OMNIA-CONSTANT](https://github.com/Tuttotorna/OMNIA-CONSTANT) | Structural constant candidate layer |
| [OMNIAMIND](https://github.com/Tuttotorna/OMNIAMIND) | Structural cognition orchestration layer |
| [OMNIA-THREE-BODY](https://github.com/Tuttotorna/OMNIA-THREE-BODY) | Dynamic divergence stress test |
| [OMNIA-SECURITY](https://github.com/Tuttotorna/OMNIA-SECURITY) | Bounded structural security diagnostics |
| [OMNIA-CRYPTO](https://github.com/Tuttotorna/OMNIA-CRYPTO) | Bounded structural crypto diagnostics |

---

## Boundary and smoke-test required terms

    measurement != inference != decision
    It is not a physics proof

---

## License

MIT.
