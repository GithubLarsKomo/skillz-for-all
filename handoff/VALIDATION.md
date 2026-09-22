# Deployment Validation

## Integrity

- [ ] Deployment manifest is readable.
- [ ] Release version is identified.
- [ ] Required components exist.
- [ ] Deterministic hashes match the release manifest.
- [ ] No unexpected file appears in the frozen framework release.

## Ownership and independence

- [ ] Active deployment root is recipient-owned or organization-owned.
- [ ] Framework root ID is recipient-controlled.
- [ ] Super Second Brain root ID is recipient-controlled.
- [ ] Tenant Deliveries root ID is recipient-controlled.
- [ ] Runtime storage policy is `drive-only`.
- [ ] No source-owner Drive ID is required at runtime.
- [ ] No source-owner credentials are required.

## Privacy

- [ ] Starter Super Brain registry contains zero real Brains.
- [ ] No source-owner Project Memory is present.
- [ ] No source-organization-specific skills, corporate assets, templates, fixtures or embedded references are present.
- [ ] No secrets are present.
- [ ] Sharing policy is private by default unless intentionally changed.

## Functional smoke test

- [ ] Bootstrap can be read.
- [ ] Framework contracts can be resolved.
- [ ] Registry/state can be read.
- [ ] Sandbox Child Brain can be created.
- [ ] Sandbox Child Brain can be registered and routed.
- [ ] Sandbox Project-Memory event can be written and read back.
- [ ] A generated non-code sandbox artifact can be written to Drive and read back.
- [ ] The sandbox artifact is registered with observed Drive ID/URL.
- [ ] The final smoke-test handoff uses the verified Drive link, not a local/sandbox download.

Only after all applicable checks pass is the deployment considered claimed.
