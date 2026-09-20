# Third-Party Deployment and Handoff

Status: draft deployment contract  
Version: 0.1.0

## Goal

Transfer a complete white-label Skillz + Second-Brain architecture to another person or organization so that the recipient becomes operationally independent of the source owner.

The handoff transfers **architecture and selected portable framework content**, not the source owner's private accumulated knowledge.

## Handoff model

```text
SOURCE OWNER
  |
  | Build + sanitize + freeze
  v
DEPLOYMENT RELEASE
  |
  | Share folder or transfer archive
  v
RECIPIENT
  |
  | Copy/import into recipient-owned Drive
  v
CLAIM
  |
  | Discover new IDs + rebind
  v
VALIDATE
  |
  v
INDEPENDENT TENANT
```

## Deployment modes

### Starter

Contains architecture, portable Skillz, empty Super Second Brain and Child-Brain templates.

Use for normal third-party inheritance.

### Curated

Starter plus explicitly approved reusable/public knowledge packs or examples.

Every added content pack requires provenance and an explicit redistribution classification.

### Trusted migration

Moves selected existing tenant knowledge to another owner.

This is a separate migration operation and MUST NOT be inferred from a normal white-label handoff.

## Deployment package structure

```text
<instance>-deployment-vX.Y.Z/
├── 00-START-HERE.md
├── instance.yaml
├── deployment-manifest.json
├── release/
│   ├── manifest.json
│   └── SHA256SUMS.json
├── framework/
│   ├── docs/
│   ├── skills/
│   ├── schemas/
│   └── templates/
├── second-brain/
│   └── super-second-brain/
├── templates/
│   └── child-brain/
└── handoff/
    ├── CLAIM.md
    ├── VALIDATION.md
    └── SUPPORT.md
```

The package contains placeholders rather than source-owner Drive IDs.

## Sender phase: Build

1. choose distribution profile;
2. render tenant-neutral package;
3. exclude all `private` skills/content;
4. apply the mandatory private source-organization exclusion policy;
5. sanitize owner names, private endpoints, credentials and real Brain registries;
6. calculate SHA-256 for deterministic release files;
7. create `release/manifest.json`;
8. run integrity/privacy validation;
9. freeze release version;
10. share the deployment package read-only or transfer a frozen archive.

## Recipient phase: Claim

The recipient MUST create a recipient-owned copy/root.

Claim records:

- recipient instance ID;
- recipient display name;
- recipient Drive root folder ID;
- claimed release version;
- claim timestamp;
- framework root folder ID;
- Super Second Brain root folder ID.

After claim, source-owner object IDs are not runtime dependencies.

## Rebind

Rebind resolves all logical components to recipient-owned Drive IDs:

- framework root;
- normative docs;
- skills root;
- Super Second Brain root;
- bootstrap file;
- registry file;
- state file;
- Child-Brain template root.

No real Child Brains are registered automatically.

A first Child Brain is created only when the recipient has a real durable project/domain scope.

## Validation gates

### Integrity

- every manifest file exists;
- deterministic file hashes match;
- no unexpected executable or secret material appears;
- release version matches the claimed manifest.

### Independence

- no source-owner Drive ID is required;
- no source-owner private repository is required;
- no source-owner credentials are required;
- recipient can read and write all mutable tenant state.

### Privacy

- Super Second Brain registry is empty for a Starter release;
- no source-owner Project Memory exists;
- no source-owner personal/company identifiers survive outside explicit attribution/license files;
- no source-organization-specific skills, corporate assets, templates, fixtures or embedded references survive the release;
- sharing state matches tenant policy.

### Functional smoke test

The recipient agent must be able to:

1. read the tenant bootstrap;
2. resolve framework contracts;
3. read empty federation registry/state;
4. instantiate one sandbox Child Brain;
5. register it;
6. route from Super Brain to Child Brain;
7. write and read back a sandbox Project-Memory event;
8. remove/archive the sandbox Brain or keep it clearly marked as test.

## Ownership handoff

A deployment is considered complete only after the recipient-owned copy passes validation.

The source owner may then remove sharing access to the source deployment folder if desired. The recipient instance MUST continue to function.

## Update channel after handoff

Updates are separate from ownership.

Supported models:

- `manual`: recipient imports selected future releases;
- `shared-release-feed`: source owner publishes read-only release packages;
- `managed`: source owner helps apply releases;
- `detached`: no upstream update relationship.

Updates modify framework content only. They MUST NOT overwrite tenant Brain knowledge, tenant registry, tenant state or tenant configuration without an explicit migration contract.

## Deployment manifest

See `templates/deployment-package/deployment-manifest.example.json`.

The deployment manifest identifies:

- package identity;
- release version;
- profile;
- required components;
- placeholder/rebind policy;
- privacy expectations;
- compatibility level.

It does not contain secrets.

## Completion criteria

A third-party deployment is complete when:

- recipient owns the active Drive root;
- all required IDs have been rebound;
- release integrity passes;
- privacy checks pass;
- no source-owner runtime dependency remains;
- bootstrap resolves;
- federation starts with expected state;
- smoke test succeeds;
- recipient receives the final system-prompt hook and operational instructions.


## Reference build command

```bash
python scripts/build_white_label_release.py \
  --output dist/<instance>-deployment \
  --release-version <semver> \
  --instance-id <instance-id> \
  --display-name "<display name>" \
  --maintainer "<recipient or organization>" \
  --zip

python scripts/validate_white_label_release.py dist/<instance>-deployment
```

The build step applies the source-owner sanitization gate before the release is frozen.

The generated package includes the recipient-side validator under `tools/validate_white_label_release.py`. After transfer, the recipient can optionally re-run it before claim:

```bash
python tools/validate_white_label_release.py .
```

After copying the package into recipient-owned Google Drive, use `handoff/RECIPIENT-BOOTSTRAP-PROMPT.md` to perform Claim -> Rebind -> Validate with an AI assistant that has access to that Drive.
