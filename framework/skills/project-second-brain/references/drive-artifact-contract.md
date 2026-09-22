# Drive Artifact Contract

## Purpose

This contract defines how `project-second-brain` stores and registers durable project artifacts in the standard Skillz-for-all runtime.

The standard claimed deployment is **Drive-only for mutable tenant persistence**: Project Memory, durable project knowledge and ordinary human-facing artifacts live in recipient-owned Google Drive under stable observed Drive IDs.

Software/source-control/runtime producer artifacts may remain in their authoritative producer system and are referenced from Project Memory; they are not copied into Drive merely because they are binary or external.

## Storage boundary

### Canonical in recipient-owned Google Drive

Persist ordinary durable project and delivery artifacts in the owning Brain/project Drive location, including:

- Project-Memory Markdown/JSON/YAML;
- PPT/PPTX;
- DOC/DOCX;
- XLS/XLSX;
- PDF;
- PNG/JPEG/TIFF and comparable review/export images;
- EPUB and other publications;
- audio/video;
- ZIP and handoff bundles;
- Google Docs, Sheets and Slides when they are the intended canonical business artifact;
- delivery manifests, QA reports and artifact registers that belong to tenant project state.

### Remain at authoritative producer/source system

Do not move/copy an artifact into Drive as a competing Source of Truth when it is canonically owned by a producer system, for example:

- software source/configuration;
- CI/CD;
- Docker/Compose;
- database schemas/migrations;
- build/test/runtime dependencies;
- deployable services/images/packages;
- controlled records whose authoritative system is external.

Project Memory records stable observed references, revision/freshness and concise status instead.

## Canonical project location

Each Project/Child Brain uses one canonical recipient-owned Drive root, identified by stable folder ID.

Resolution order:

1. reuse the root/folder ID already recorded in project state;
2. reuse an explicitly established project folder from the current verified handoff;
3. resolve an existing exact folder only after identity/suitability verification;
4. otherwise create exactly one private project location below the configured tenant Drive root.

Do not create a second folder simply because a workflow wants a different artifact type.

Never use a source-owner Drive object after Claim/Rebind.

Preserve existing sharing state and keep newly created project folders private unless the tenant/user explicitly chooses otherwise.

## Project-Memory representation

`ASSETS.md` is the human-readable artifact register; `state.json` is the compact machine-readable projection.

For each registered artifact record, where available:

- stable local asset ID;
- role/purpose;
- canonical file name;
- observed Drive file ID and URL;
- parent folder ID;
- MIME/artifact type;
- lifecycle state: `working|review|released|superseded|archived`;
- producer/source;
- related Project-Memory event;
- provider revision/modified timestamp/checksum where useful;
- last verified timestamp.

Never invent provider values.

## Link-first delivery policy

All human-facing generated deliverables follow `docs/DOCUMENT-ARTIFACT-DELIVERY-CONTRACT.md`.

Normal order:

```text
generate
  -> QA/audit
  -> write exact approved revision to canonical recipient-owned Drive
  -> read-back verify
  -> register/update state
  -> return observed Drive link
```

A local/sandbox/chat file is only an intermediate build artifact. It is not a completed Skillz-for-all delivery.

If Drive is unavailable, record `pending|blocked`; a temporary file may be exposed as an explicit fallback but not represented as canonical/final.

## Upload/update protocol

1. Resolve owning Brain/project and canonical Drive root by stable ID.
2. Classify producer-owned exceptions before copying anything.
3. Upload/create the artifact in the canonical project location, or update an intentionally mutable working artifact.
4. Read back the stored object and capture observed ID/URL/parent/type/revision state.
5. Update `ASSETS.md`, `state.json` and the relevant event/manifest consistently.
6. For released/frozen outputs, prefer a versioned new object or auditable Drive revision rather than silent replacement.
7. Return the observed canonical Drive link.

## Handoff

Downstream workflows receive provider-neutral locators whose standard profile resolves to Google Drive, including Brain root, Project-Memory state and relevant asset IDs/URLs.

They must reuse the canonical root and must not create a parallel artifact folder.

## Failure rules

The artifact step is incomplete when:

- Drive write/read-back is not verified;
- recorded ID/URL/revision is guessed;
- the object is outside the canonical recipient-owned project location without explicit authority;
- a producer-owned artifact was duplicated as a competing truth;
- a released/frozen artifact was silently overwritten;
- a parallel Drive project root was created;
- a source-owner/other-tenant Drive object is treated as canonical;
- a local/sandbox/chat attachment is reported as final delivery.

A Drive outage is a pending external state, not evidence of successful persistence.
