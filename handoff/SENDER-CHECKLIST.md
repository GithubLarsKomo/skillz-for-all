# Sender Handoff Checklist

Before giving a deployment to a third party:

- [ ] Build from an explicit white-label profile.
- [ ] Assign a release version.
- [ ] Run the release validator.
- [ ] Confirm the Starter Super Brain registry is empty.
- [ ] Confirm the package contains no source-owner Project Memory.
- [ ] Confirm forbidden source-owner identifiers/secrets are absent.
- [ ] Confirm the mandatory source-organization exclusion policy was applied and no organization-specific content remains.
- [ ] Confirm `runtimeDependencyOnSourceOwner=false`.
- [ ] Freeze the release manifest and hashes.
- [ ] Transfer/share only the deployment release, not the private development source.
- [ ] Give the recipient `00-START-HERE.md` and `handoff/RECIPIENT-BOOTSTRAP-PROMPT.md`.
- [ ] Tell the recipient to create a recipient-owned copy before claim.
- [ ] Retain the release version and manifest for support/provenance.

After the recipient confirms successful claim and independent operation, source-folder sharing may be revoked if desired.
