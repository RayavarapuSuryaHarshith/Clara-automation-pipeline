# Clara AI Automation Pipeline

This project demonstrates a zero-cost automation workflow that converts customer demo and onboarding conversations into structured operational configurations for a Retell AI voice agent.

Pipeline A:
Demo call transcript → Extract account memo → Generate preliminary Retell agent spec (v1)

Pipeline B:
Onboarding update → Update memo → Generate agent spec (v2) → Produce changelog.

Outputs are stored per account with versioning.

Structure:
outputs/accounts/<account_id>/v1
outputs/accounts/<account_id>/v2

v1 contains demo-derived assumptions.
v2 reflects onboarding-confirmed updates.
