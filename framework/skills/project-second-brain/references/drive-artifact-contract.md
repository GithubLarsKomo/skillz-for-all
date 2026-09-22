# Drive Artifact Contract

## Purpose

This contract defines how `project-second-brain` persists and registers generated non-code artifacts inside the recipient-owned Google Drive runtime required by Skillz for All.

It specializes the framework-wide `docs/DRIVE-STORAGE-AND-DELIVERY-CONTRACT.md`. Project Memory and its generated project/delivery artifacts share the same canonical Child-Brain Drive root; GitHub is not a parallel artifact store.

## Storage boundary

### Keep in the producer system

Do not move an artifact into the Brain merely because it is binary when it is required for source control, build, test, deployment or runtime, or when another controlled system is the authoritative record. Reference the verified producer/source object from Drive instead.

### Store in the owning Brain Drive root

Store generated documentary, referential, review-oriented and delivery material in the owning Child Brain's Drive artifact area. Typical examples include:

- PPT/PPTX, DOC/DOCX, XLS/XLSX and PDF;
- PNG/JPEG/TIFF/SVG and other review/export images;
- EPUB and packaged publications;
- HTML/Markdown/JSON/YAML delivery manifests and reports;
- audio/video;
- ZIP or other handoff bundles;
- native Google Docs, Sheets and Slides when they are the authoritative business artifact.

If no owning Child Brain is appropriate, use the tenant `Deliveries` root from `instance.yaml`. Do not create a second ad-hoc project store.

## Brain Drive identity

Reuse the Brain root and artifact root IDs already recorded in `state.json`. Resolve by stable Drive ID, not by folder name.

Recommended projection:

```text
<CHILD_BRAIN_ROOT>/
├── docs/project-memory/
└── artifacts/
    ├── working/
    └── released/
```

Do not change sharing permissions merely to satisfy this contract. Preserve the tenant's protection boundary.

## Project Memory representation

`docs/project-memory/ASSETS.md` is the human-readable asset register. `state.json` carries the compact machine projection.

Each registered asset records at least: stable asset ID, role, canonical file name, Drive file ID, observed Drive URL, artifact/MIME type, lifecycle state, producer, related event, and verification timestamp. Revision/checksum/modified time are added when materially useful.

Do not invent Drive IDs, URLs, revisions, checksums or verification timestamps.

## `state.json` projection

Use the Brain's existing Drive `knowledgeStore` plus `externalArtifacts`; do not materialize a separate non-Drive artifact provider.

```json
{
  "schemaVersion": 3,
  "knowledgeStore": {
    "provider": "google-drive",
    "storeId": "primary",
    "rootFolderId": "observed-brain-root-folder-id",
    "artifactRootFolderId": "observed-artifact-root-folder-id",
    "deliveryPolicy": "drive-only"
  },
  "externalArtifacts": [
    {
      "id": "ASSET-004",
      "role": "final-presentation",
      "name": "NDD Review.pptx",
      "driveFileId": "observed-file-id",
      "url": "observed-drive-file-url",
      "status": "released",
      "producer": "template-presentation-workflow",
      "event": "docs/project-memory/events/EVT-....md",
      "verifiedAt": "observed timestamp"
    }
  ]
}
```

## Write and delivery protocol

1. Determine producer ownership and Brain ownership.
2. Resolve the canonical Child-Brain artifact root, or the tenant `Deliveries` root when no Brain applies.
3. Generate locally only as a build intermediate.
4. Write the artifact to Drive.
5. Read back metadata/content as appropriate and capture observed ID, URL, parent, MIME/type and revision/modified state.
6. Register/update `ASSETS.md`, `state.json` and the related event.
7. For released/frozen deliverables use an auditable version/supersession transition.
8. Return the verified Drive link as the primary user-facing handoff.

## Event linkage

Use stable asset IDs and observed Drive IDs/URLs. The event is an index/evidence record, not a duplicate of the binary artifact.

## Handoff

Downstream skills reuse the same Brain/artifact root IDs. They do not create their own storage tree. Delivery manifests reference Drive object IDs/URLs rather than local/sandbox paths as final refs.

## Failure rules

The artifact step is incomplete when:

- the Drive write was not read back/verified;
- the file/folder ID or URL is guessed;
- a generated non-code artifact exists only locally/sandboxed;
- a final artifact was placed outside the owning Brain or tenant Deliveries root without documented reason;
- a released artifact was silently overwritten;
- a parallel Drive project folder was created despite an existing canonical Brain root;
- a software build/runtime asset was moved to Drive solely because it is binary.

A Drive outage is `pending|blocked`, not successful delivery. A temporary local/download link is not the normal final handoff.
