# Drive Storage and Delivery Contract

Status: active architecture contract  
Version: 1.0.0  
Date: 2026-09-22

## Purpose

Skillz for All uses **recipient-owned Google Drive as the mandatory runtime persistence layer** for the deployed framework, Super Second Brain, Child Brains and all generated non-code artifacts.

The public GitHub repository is the distribution and update source. It is not the canonical runtime Knowledge Store of a claimed tenant.

The governing rule is:

> **Persist to the owning Drive location first, verify the stored object, then deliver the verified Drive link.**

## Scope

This contract applies to:

- framework runtime files copied into the claimed tenant (`SKILL.md`, contracts, schemas, templates and configuration);
- Super Second Brain and Child Brain Markdown/JSON/YAML state;
- generated PPTX, DOCX, PDF, XLSX, EPUB and ZIP handoffs;
- generated HTML, Markdown, JSON/YAML manifests and reports that belong to a Brain or delivery run;
- generated PNG/JPEG/TIFF/SVG and other non-code visual assets;
- generated audio/video and other human-facing media;
- native Google Docs, Sheets and Slides when chosen as the authoritative business artifact.

## Explicit boundary

Drive-only runtime storage does **not** move executable producer content into a Brain.

Keep these in their authoritative producer/source systems and reference them from Drive:

- source code, tests, CI/CD, Docker/Compose, migrations, schemas and deployable software;
- repository-native build/runtime assets required by software;
- controlled records whose authoritative source is a QMS, submission system, ticketing system, ERP, LIMS or another controlled application;
- external source material that already has an authoritative URL/object and should not be duplicated.

The owning Brain stores verified locators, decisions, synthesis and delivery artifacts, not a second uncontrolled copy of producer truth.

## Tenant layout

A claimed tenant resolves stable Drive folder IDs for at least:

```text
<TENANT_ROOT>/
├── Skillz/
├── Second-Brain/
│   ├── Super-Second-Brain/
│   └── Brains/
└── Deliveries/
```

A Child Brain keeps its Project Memory and project artifacts below the same recipient-owned Brain root. A recommended projection is:

```text
<CHILD_BRAIN_ROOT>/
├── docs/project-memory/
└── artifacts/
    ├── working/
    └── released/
```

Existing equivalent Drive layouts may be reused. Stable Drive IDs, not names or paths, are canonical.

## Artifact routing

For every generated non-code artifact:

1. resolve the owning Child Brain;
2. if an owning Brain exists, store the artifact below that Brain's Drive root and register it in `ASSETS.md` / `state.json`;
3. if no Brain is appropriate, store it below the tenant `Deliveries` root and record the run manifest there;
4. never create a parallel ad-hoc storage hierarchy when a canonical Brain or tenant delivery root already exists;
5. do not use GitHub, local disk, chat attachments or sandbox storage as the normal final location for a non-code delivery artifact.

## Delivery gate

The normal lifecycle is:

`generate -> Drive write -> read-back verify -> register -> return Drive link`

A local or sandbox file may exist as a build intermediate only.

A document or media workflow is **not complete** while the only copy is local/sandboxed. If Drive is unavailable or unwritable:

- mark storage/delivery `pending|blocked`;
- preserve the local intermediate only as recovery state when possible;
- do not claim final delivery;
- do not substitute a temporary download link as the normal successful handoff.

A temporary local/downloadable copy may be provided only when the user explicitly asks for it in addition to the canonical Drive object.

## Required stored-object metadata

After every Drive write capture observed values when available:

- Drive file/folder ID;
- Drive URL;
- parent folder ID;
- MIME/artifact type;
- revision or modified time;
- verification timestamp;
- checksum when deterministic integrity matters;
- lifecycle state: `working|review|released|superseded|archived`;
- producer skill/run and related Brain event.

Never invent IDs, URLs, revisions or verification timestamps.

## Versioning

Released/frozen artifacts are auditable:

- prefer explicit versioned filenames or Drive revisions with an unambiguous release transition;
- never silently replace a released artifact;
- keep superseded asset relations in the Brain manifest;
- immutable framework releases use release manifests and SHA-256 integrity data.

## Link-first user handoff

For successful document/media generation, return the verified Drive link(s) as the primary user-facing handoff.

Do not present sandbox/download links as the final result when the Drive write succeeded.

## Relationship to other contracts

This contract is normative for Skillz-for-All runtime storage and delivery and is referenced by:

- `KNOWLEDGE-STORE-CONTRACT.md`;
- `project-second-brain`;
- `second-brain-federation-workflow`;
- document, presentation, EPUB, learning and report delivery workflows.

Producer ownership and storage ownership remain distinct: a renderer may own the artifact semantics while Drive owns the canonical persisted instance.

## Failure conditions

A workflow fails the storage/delivery gate when:

- a generated non-code artifact exists only locally/sandboxed;
- a claimed tenant uses GitHub or another backend as canonical runtime Brain storage;
- a final link was guessed rather than read back;
- an artifact was written outside the owning Brain/tenant delivery root without documented reason;
- a released artifact was silently overwritten;
- a second Drive hierarchy was created instead of reusing the canonical root;
- a Drive write failed but delivery was reported as complete.

## Completion

The contract is satisfied when the claimed tenant's framework runtime, Second-Brain state and generated non-code artifacts are in recipient-owned Drive, successful writes are read-back verified, and user-facing delivery uses the stored Drive links.
