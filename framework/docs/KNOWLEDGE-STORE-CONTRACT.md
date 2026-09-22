# Knowledge Store Contract

Status: candidate architecture contract  
Version: 0.1.0  
Date: 2026-09-19

## Purpose

This contract decouples Skillz and the federated Second-Brain architecture from any specific source-control or cloud-storage product.

A **Knowledge Store** is the persistence layer used for framework contracts, federation metadata, Project Memory, durable knowledge and related artifacts.

The architecture reasons in stable logical locators. Provider-specific adapters translate those locators into Google Drive, GitHub or another supported backend.

The framework semantics remain provider-neutral, but the **standard claimed Skillz-for-all runtime uses a mandatory Google Drive persistence profile**. All mutable tenant framework state, federation/Project-Memory state, durable tenant knowledge and generated human-facing artifacts are persisted in recipient-owned Google Drive. GitHub or another producer system may remain authoritative for software/source-control/runtime artifacts, but is not a substitute canonical tenant Knowledge Store or final artifact-delivery root in this profile.

## Core principles

1. **Provider-neutral semantics** — Skillz, Promotion, Lint and Federation rules do not depend on GitHub concepts.
2. **Stable identity over paths** — provider object IDs are canonical; names and paths are human-readable projections.
3. **Machine files stay machine files** — normative Markdown, JSON and YAML remain stored files rather than native office documents.
4. **Native documents are artifacts** — Google Docs, Sheets and Slides may be authoritative business artifacts but do not replace machine contracts.
5. **Read-back verification** — a write is not successful until the provider returns or re-reads the intended object.
6. **No hidden cross-tenant dependency** — a handed-off instance must be able to operate after source-owner access is removed.
7. **Source-of-Truth ownership is independent of storage provider.**
8. **Drive-only tenant persistence** — after Claim/Rebind, recipient-owned Google Drive is the only canonical mutable tenant persistence layer in the standard Skillz-for-all profile.
9. **Producer separation** — source code, CI/CD, deployable runtime artifacts and controlled producer records stay with their authoritative producer systems and are referenced from Drive rather than copied merely for uniformity.
10. **Link-first delivery** — a generated human-facing artifact is final only after canonical Drive persistence and read-back verification under `docs/DOCUMENT-ARTIFACT-DELIVERY-CONTRACT.md`.

## Logical locator

Every canonical object is addressable by a provider-neutral locator.

```json
{
  "provider": "google-drive",
  "storeId": "tenant-primary",
  "objectType": "file",
  "objectId": "provider-stable-id",
  "logicalPath": "docs/project-memory/INDEX.md",
  "revisionId": "provider-revision-id-or-null",
  "sha256": "optional-content-hash"
}
```

Required semantics:

- `provider` identifies the adapter.
- `storeId` identifies a configured tenant store.
- `objectId` is the provider's stable object identity.
- `logicalPath` is for navigation and validation; it is not sufficient identity by itself.
- `revisionId` captures a known provider revision where available.
- `sha256` freezes exact content when deterministic integrity matters.

## Google Drive adapter

### Store root

A Drive-backed store is rooted at a verified folder ID:

```yaml
knowledgeStores:
  primary:
    provider: google-drive
    rootFolderId: "<observed-folder-id>"
```

The root folder ID, not the folder name, is the canonical store locator.

### Canonical machine artifacts

Store these as ordinary files:

- `*.md`
- `*.json`
- `*.yaml` / `*.yml`
- schemas
- release manifests
- integrity manifests

Examples include:

- `BOOTSTRAP.md`
- `SKILL.md`
- `registry.json`
- `state.json`
- `manifest.json`

### Native Google Workspace artifacts

Google Docs, Sheets and Slides are allowed for human-facing deliverables, source documents and controlled collaboration.

A Brain references them by observed Drive file ID and metadata. Their native body is not silently duplicated into machine-state files.

### Version identity

For a deterministic snapshot prefer:

`fileId + revisionId + sha256`

Not every operation must calculate a hash. Hashes are mandatory for frozen framework releases, third-party deployment bundles and any artifact whose exact content must be reproduced independently of Drive revision behavior.

### Folder moves and renames

Moving or renaming a Drive object does not change logical identity when the file/folder ID remains stable.

Human-readable paths MAY be refreshed after moves. They MUST NOT be treated as the only canonical locator.

## GitHub and other producer/source-control systems

Provider-neutral framework semantics may still describe adapters for migration, import or source references, but the standard claimed Skillz-for-all tenant does not use GitHub as its canonical mutable Knowledge Store.

GitHub or another producer system may remain authoritative for:

- software source and configuration;
- branches, commits, PRs and review evidence;
- CI/CD and release automation;
- schemas/migrations required by a producer;
- deployable runtime artifacts;
- public framework distribution/source history.

Project Memory stores observed stable references to those producer objects. Generated tenant documents, presentations, spreadsheets, publications and ordinary durable project knowledge remain in recipient-owned Google Drive.

A custom deployment that intentionally replaces the standard Drive-only persistence profile is a separate architecture profile and must not be silently inferred from the presence of a GitHub repository.

## Release transaction boundary

Google Drive cannot provide a Git-style atomic commit across many independent files.

Therefore a **Release Manifest** is the architectural transaction boundary.

A release is considered complete only when:

1. all release files exist;
2. each required file has an observed ID;
3. required deterministic files have SHA-256 hashes;
4. `manifest.json` lists the complete set;
5. validation passes;
6. the manifest itself is read-back verified;
7. release status changes to `released`.

A released version is logically immutable. Corrections create a new release version; they do not silently rewrite the prior release contract.

## Write protocol

For durable writes:

1. resolve configured store;
2. resolve canonical owner;
3. resolve target by stable ID when known;
4. write/create;
5. read metadata/content back;
6. capture current provider ID and revision;
7. calculate hash when required;
8. update the owning manifest/state projection;
9. verify the projection.

## Copy, export and rebind

Provider IDs are instance-local and MUST be expected to change when a deployment is copied into another account or storage root.

Therefore third-party handoff uses:

`Export -> Transfer -> Claim -> Rebind -> Validate`

After a recipient copies a deployment:

1. recipient-owned root folder is resolved;
2. all required files/folders are discovered under that root;
3. new provider IDs are written to tenant configuration;
4. source-owner provider IDs are discarded;
5. integrity hashes are compared with the release manifest;
6. recipient bootstrap/state files are rendered;
7. all canonical locators are read-back verified.

A deployment is not independent until rebind validation succeeds.

## Access and privacy

- Private by default for Super Second Brain and Child Brains.
- Sharing state is observed, not inferred.
- Framework releases may be shared more broadly than knowledge stores.
- A less-protected layer must never receive private Child-Brain content during synchronization.
- Credentials, OAuth tokens and API keys never belong in Knowledge Store configuration files.

## Failure semantics

Use explicit states:

- `available`
- `bootstrap-needed`
- `pending`
- `unavailable`
- `archived`
- `integrity-failed`
- `rebind-required`

Never interpret a file with the right name but an unverified ID/content as canonical merely because it is visible.

## Acceptance criteria for a provider adapter

A provider adapter is suitable when it can:

1. resolve a configured store root;
2. list and locate expected objects;
3. read machine files losslessly;
4. create and update machine files;
5. expose stable object IDs;
6. verify writes by read-back;
7. expose enough revision/freshness metadata for audit;
8. preserve access boundaries;
9. support deployment rebind;
10. provide deterministic hashes at the framework layer when the provider cannot.
