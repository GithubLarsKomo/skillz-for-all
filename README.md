# Skillz for All

A public, provider-neutral distribution of the Skillz framework and Second-Brain architecture.

This repository contains the validated **full-portable** distribution: the generic skill library, shared contracts and schemas, a Google-Drive-first Second-Brain starter, Child-Brain templates, and third-party handoff material.

## Included

- 342 portable skills
- provider-neutral Knowledge Store, promotion and lint contracts
- Super Second Brain starter with an empty registry
- Child Brain project-memory template
- Google Drive-first Claim → Rebind handoff
- release manifests and SHA-256 integrity data
- self-validation tooling

Company-internal, source-owner-specific and branded private wrappers are excluded. Generic skills that previously contained mixed private routing are retained through neutral distribution overlays.

## Start here

Read [00-START-HERE.md](00-START-HERE.md) and then [handoff/THIRD-PARTY-DEPLOYMENT.md](handoff/THIRD-PARTY-DEPLOYMENT.md).

Validate a checkout with:

```bash
python tools/validate_white_label_release.py .
```

The Starter Super Brain is intentionally empty. Recipients claim the package into their own Knowledge Store and bind their own Drive object IDs before use.

## License

Skillz for All is licensed under the **Apache License 2.0**. See [LICENSE](LICENSE). The license applies to the public distribution in this repository; recipient-created private Brains and content are not automatically contributed back to this repository merely by using the framework.
