# Three-Body Overview

OMNIA-THREE-BODY is a dynamic divergence stress test inside the MB-X.01 / OMNIA ecosystem.

It uses a chaotic dynamic setting to make perturbation sensitivity visible.

Canonical boundary:

    measurement != inference != decision

    Decision remains external

---

## Dynamic divergence pipeline

The core pipeline is:

    initial state
      -> perturbation
      -> trajectory divergence
      -> structural instability
      -> external validation

Meaning:

| Stage | Role |
|---|---|
| initial state | Starting configuration |
| perturbation | Controlled small change |
| trajectory divergence | Separation between evolved paths |
| structural instability | Measured or observed change in structural behavior |
| external validation | Artifact testing outside this repository |

---

## What makes this repository different

OMNIA-THREE-BODY is not trying to answer:

    Is OMNIA physically complete?
    Is this a proof of physics?

It asks:

    Can a dynamic stress test expose structural divergence under perturbation?

This is a narrower claim.

That narrowness is intentional.

---

## Correct use

Correct use:

    define initial state
    apply perturbation
    observe trajectory divergence
    produce artifact
    route result to OMNIA or validation

Incorrect use:

    treat divergence as universal proof
    treat simulation as physical truth
    treat instability as final decision
    treat stress test as complete theory

---

## Relation to OMNIA

OMNIA-THREE-BODY creates or organizes a dynamic stress-test case.

OMNIA can measure structural behavior.

OMNIA-INVARIANCE can check what survives transformation.

OMNIA-VALIDATION validates artifacts and claims.

