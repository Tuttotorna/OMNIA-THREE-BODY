# OMNIA-THREE-BODY Backbone Compliance

## Role

OMNIA-THREE-BODY is a Domain Experiment Producer / Adapter.

It adapts three-body / trajectory measurements into the canonical OMNIA backbone.

It observes validated backbone output.

It is not the measurement core.

It is not the boundary validator.

It is not the validation control plane.

It is not a decision engine.

It does not claim final physical truth.

## Canonical flow

OMNIA-THREE-BODY must use the existing backbone:

three-body / trajectory measurement
  -> OMNIA-THREE-BODY adapter
  -> BoundaryCertificate-compatible artifact
  -> omnia-limit validate_certificate()
  -> OMNIA-VALIDATION process_boundary_step()
  -> ValidationEnvelope
  -> OMNIA-THREE-BODY observation

## Public API

OMNIA-THREE-BODY exposes:

adapt_three_body_measurement_to_boundary_certificate(...)
run_three_body_backbone_flow(...)
observe_three_body_envelope(...)

## Contract rule

OMNIA-THREE-BODY does not redefine BoundaryCertificate.

OMNIA-THREE-BODY does not redefine ValidationEnvelope.

OMNIA-THREE-BODY does not bypass omnia-limit.

OMNIA-THREE-BODY does not bypass OMNIA-VALIDATION.

OMNIA-THREE-BODY does not declare final physical truth.

## Three-body / trajectory mapping

trajectory_divergence
  -> ast_deformation_index

orbit_drift
  -> ast_deformation_index

phase_space_drift
  -> ast_deformation_index

energy_residual
  -> ast_deformation_index

angular_momentum_residual
  -> ast_deformation_index

lyapunov_proxy
  -> ast_deformation_index

trajectory_stability_score
  -> ast_deformation_index = 1.0 - trajectory_stability_score

orbital_stability_score
  -> ast_deformation_index = 1.0 - orbital_stability_score

structural_stability_score
  -> ast_deformation_index = 1.0 - structural_stability_score

## Forbidden interpretation

OMNIA-THREE-BODY must not emit final claims such as:

physical truth
final law
proved chaos
proved determinism
complete physics
universal orbit truth

Those are not backbone measurement outputs.

OMNIA-THREE-BODY may report validated trajectory-domain structural evidence.

## Boundary

trajectory evidence != physical truth
domain experiment != proof
adapter != validator
validator != control plane
control plane != decision
decision != measurement

OMNIA-THREE-BODY stays in the Domain Experiment Producer / Adapter layer.
