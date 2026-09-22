# Document Artifact Delivery Contract

Status: active capability contract  
Version: 1.0.0  
Date: 2026-09-22

## Purpose

This contract defines the default persistence and delivery policy for human-facing artifacts produced by a claimed Skillz-for-all instance.

The governing rule is:

> **A generated human-facing artifact is delivered only after it has been stored in the recipient-owned canonical Google Drive location, read-back verified, registered where applicable, and surfaced by its observed Drive link.**

The standard Skillz-for-all runtime profile is therefore **Drive-only for durable tenant artifacts**. Local files, chat attachments and sandbox files are build intermediates, not canonical delivery objects.

This applies to, among others:

- PPT/PPTX and presentation PDFs;
- DOC/DOCX and document PDFs;
- XLS/XLSX and comparable spreadsheet outputs;
- EPUB and other publication packages;
- PNG/JPEG/TIFF and review/export images;
- audio/video deliverables;
- ZIP and other handoff bundles;
- Google Docs, Sheets and Slides when they are the intended canonical human-facing artifact.

Software source, CI/CD artifacts, Docker/Compose, schemas, migrations and deployable runtime assets remain with their dedicated producer/source-control system when that system is their Source of Truth.

## Canonical destination

For a generated tenant artifact:

1. Resolve the owning Project/Collection Brain or project context.
2. Reuse the canonical recipient-owned Drive root/folder already recorded by stable Drive ID.
3. If the project has no artifact folder yet, materialize exactly one canonical project artifact location under the configured recipient-owned Drive store and record its observed ID.
4. Never create a parallel folder merely to make delivery easier.
5. Never use a source-owner Drive location as the canonical destination after Claim/Rebind.
6. Do not substitute GitHub, local disk, sandbox storage or chat attachment storage as the final destination in the standard Skillz-for-all profile.

## Delivery sequence

The normal sequence is:

```text
generate
  -> format/semantic QA
  -> contract audit where applicable
  -> store in canonical recipient-owned Drive
  -> read-back verify
  -> register/update artifact state
  -> return observed Drive link
```

A successful delivery records, where available:

- Drive file ID;
- observed Drive URL;
- parent folder ID;
- MIME/artifact type;
- lifecycle state;
- revision/modified timestamp;
- checksum when exact reproducibility matters;
- producer/workflow;
- related Project-Memory event or delivery manifest;
- verification timestamp.

Never invent IDs, URLs, revisions or verification timestamps.

## Local and sandbox files

Local/sandbox files are allowed only as working material required for generation, conversion, rendering or QA.

They do not satisfy delivery.

A temporary chat/download link may be exposed only when:

- Google Drive is temporarily unavailable or unwritable; or
- the active connector cannot persist the required file type; or
- the user explicitly requests an additional local copy.

In that case:

- mark canonical Drive persistence as `pending` or `blocked`;
- do not call the temporary copy canonical or final;
- preserve the pending action in Project Memory or the delivery manifest;
- complete the Drive write on the next execution where the canonical store is writable.

## Versioning and immutability

For released/frozen artifacts:

- prefer explicit versioned files or an auditable Drive revision transition;
- do not silently overwrite a released object;
- preserve supersession history in the owning artifact register/state.

Working drafts may update in place only when the active project/production contract explicitly permits mutability.

## Link-first completion gate

A human-facing artifact workflow is complete only when:

- required content/format QA has passed;
- any applicable Artifact Production Contract audit has passed;
- the artifact exists in the canonical recipient-owned Drive destination;
- the Drive write has been read-back verified;
- the owning manifest/state is consistent with the observed object;
- the user receives the observed Drive link.

If Drive persistence cannot be completed, the workflow may return `pending|blocked` plus an explicit temporary fallback, but not `complete`.

## Relationship to other contracts

This contract complements:

- `docs/KNOWLEDGE-STORE-CONTRACT.md` — tenant storage and stable identity;
- `docs/ARTIFACT-PRODUCTION-CONTRACT.md` — Grilling, frozen intent/layout/figure requirements and audit;
- `skills/project-second-brain/SKILL.md` — project ownership, provenance and asset registration;
- `skills/project-second-brain/references/drive-artifact-contract.md` — Drive-specific artifact registration details.

Production and delivery are separate gates:

- **Production contract:** did we build the intended artifact correctly?
- **Delivery contract:** did we persist and hand off the exact approved artifact correctly?

## Failure conditions

Do not claim successful final delivery when:

- the artifact exists only locally, in a sandbox or as a chat attachment;
- Drive write/read-back failed;
- the observed object is outside the canonical recipient-owned project location without an explicit authority reason;
- the returned link/ID was guessed;
- a released artifact was silently overwritten;
- a parallel project folder was created although a canonical Drive root was already known;
- a source-owner or other tenant's Drive object is being used as canonical state.

## Completion

The contract is satisfied when the exact approved human-facing artifact is persisted in recipient-owned canonical Google Drive, read-back verified, registered with stable observed identity and returned to the user by Drive link.
