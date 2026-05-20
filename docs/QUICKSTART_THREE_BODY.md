# Quickstart Three-Body

This document gives the fastest path to seeing OMNIA-THREE-BODY as a dynamic divergence stress test.

The public mental model is:

    initial state -> perturbation -> trajectory divergence -> structural instability

---

## Clean install

    git clone https://github.com/Tuttotorna/OMNIA-THREE-BODY.git
    cd OMNIA-THREE-BODY
    python -m pip install -e .
    pytest

---

## What to look for

After installation and tests, look for the smallest available example.

The point is not to prove physics.

The point is to identify:

    What initial state is used?
    What perturbation is applied?
    How does the trajectory diverge?
    What structural instability appears?
    What artifact is produced?
    What does the result not prove?

---

## Expected stress-test behavior

A good OMNIA-THREE-BODY path should produce a dynamic divergence artifact.

It should not silently become:

    physical proof
    semantic judgment
    final decision
    truth certificate
    universal chaos claim

---

## Public compression

    OMNIA-THREE-BODY shows structural divergence under perturbation.
    It is a stress test.
    It is not a physics proof.
    Decision remains external.

