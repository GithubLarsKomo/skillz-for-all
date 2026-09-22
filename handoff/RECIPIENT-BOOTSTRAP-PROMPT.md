# Recipient Bootstrap Prompt

Use this after the complete deployment package has been copied into a Google Drive location owned by the recipient.

Copy the following instruction into an AI assistant that has access to the recipient's Google Drive:

> I have copied a Skillz + Second-Brain white-label deployment into my own Google Drive. Treat the copied folder I identify as the deployment root. Read `00-START-HERE.md`, `deployment-manifest.json`, `release/manifest.json`, `handoff/CLAIM.md` and `handoff/VALIDATION.md`. Do not use any source-owner Drive IDs as canonical runtime locators. Resolve the recipient-owned Drive IDs for the deployment root, framework root, Super Second Brain root, tenant Deliveries root, BOOTSTRAP.md, registry.json and state.json. Rebind `instance.yaml` and create a completed `claim.json` from `handoff/claim.example.json`. Verify that the Starter registry is empty, required release files are present, sharing is private by default, and all mutable tenant files are writable in my Drive. Then perform the functional smoke test with a clearly marked sandbox Child Brain. Also generate a small non-code test artifact, persist it in recipient-owned Drive, read it back, and verify that the handoff uses the observed Drive link rather than a local/sandbox download. Read back every created or modified file before declaring success. Finally give me the exact minimal system-prompt hook for this claimed instance. Do not import or infer any private knowledge from the source owner.

The recipient should identify/select the copied deployment root in the connected Drive when asked by the assistant.

## Completion result

The bootstrap is complete only when:

- `instance.yaml` contains recipient-owned Drive locators;
- `claim.json` records the recipient-owned IDs and `rebindStatus: complete`;
- the Starter registry contains no source-owner Brain;
- the sandbox routing/write/read-back test succeeds;
- the Drive-only artifact write/read-back/link-handoff smoke test succeeds;
- the final system-prompt hook points to the recipient-owned bootstrap;
- the instance remains operational without source-owner Drive access.
