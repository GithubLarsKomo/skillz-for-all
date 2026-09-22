# Constant Second-Brain Bootstrap

Status: active

## Purpose

Stable startup contract for substantive work using this tenant's federated Second-Brain system.

This bootstrap is stored and executed from recipient-owned Google Drive. Skillz for All does not support GitHub or another backend as the canonical claimed Second-Brain runtime store.

## Startup sequence

1. Read this bootstrap.
2. Read the tenant instance configuration.
3. Read the Super Brain `state.json` and `registry.json` using their bound Knowledge Store locators.
4. Resolve the canonical Child Brain by scope, domain and registry status.
5. Read the Child Brain's canonical Project-Memory root before relying on prior project/domain knowledge.
6. Respect Source-of-Truth ownership and do not answer from Super-Brain summaries when the Child Brain is reachable.
7. Follow `Ingest -> Query -> Promote -> Lint` semantically.
8. Before closure or handoff, apply the tenant framework's Knowledge Promotion Contract.
9. Apply the tenant framework's Second-Brain Lint Contract when triggered.

## Governing framework

Resolve these logical files below the bound tenant Skillz framework root:

- `docs/KNOWLEDGE-STORE-CONTRACT.md`
- `docs/DRIVE-STORAGE-AND-DELIVERY-CONTRACT.md`
- `docs/DOCUMENT-ARTIFACT-DELIVERY-CONTRACT.md`
- `docs/ARTIFACT-PRODUCTION-CONTRACT.md`
- `skills/second-brain-federation-workflow/SKILL.md`
- `skills/project-second-brain/SKILL.md`
- `docs/SECOND-BRAIN-OPERATING-CYCLE.md`
- `docs/KNOWLEDGE-PROMOTION-CONTRACT.md`
- `docs/SECOND-BRAIN-LINT-CONTRACT.md`

## Failure behavior

If the tenant framework, Super Brain or canonical Child Brain cannot be verified, do not invent prior knowledge.

Use current-task evidence where possible and mark persistence/routing as pending or blocked. Never write substantive knowledge into a convenient non-canonical target. Generated non-code artifacts likewise remain pending until written to and read back from the canonical Drive location.
