# Artifact Production Contract

Status: active capability contract  
Version: 1.0.0  
Date: 2026-09-22

## Purpose

This contract governs substantive authored presentation, document and publication artifacts such as PPTX, DOCX, PDF and related outputs.

Its purpose is to capture user intent precisely before material authoring/layout starts, freeze material decisions, prevent downstream renderers from reinterpreting the brief, and audit the exact candidate release against those decisions.

Canonical lifecycle:

```text
proportional Grilling
  -> Artifact Production Contract
  -> Contract Freeze
  -> format-specific production
  -> structural/render QA
  -> Contract Audit
  -> Drive persistence/read-back
  -> final Drive-link delivery
```

The last persistence/delivery phase is governed by `docs/DOCUMENT-ARTIFACT-DELIVERY-CONTRACT.md`.

## Applicability

Apply to substantive first-time generation or material revision of:

- presentations and derived PDFs;
- DOCX reports/memos/handouts and derived PDFs;
- cross-format document packages;
- publication artifacts where visual/content/delivery decisions matter;
- comparable authored office artifacts.

A deterministic conversion of an already frozen canonical artifact may inherit the active contract instead of starting a new Grilling round.

## Proportional Grilling

Before material production, use `round-based-requirements-grilling` at a depth proportional to the task.

Resolve only what is materially needed, using existing confirmed context first:

- purpose and desired outcome;
- audience/use/decision context;
- primary message/effect;
- required content, exclusions and detail level;
- evidence/source expectations;
- structure/storyline;
- language, tone and style;
- template/design authority;
- visual language and material figures;
- output formats and editability;
- canonical Drive destination/distribution context;
- constraints, non-goals and acceptance criteria.

Do not repeat questions already answered by a current instruction, active project contract, approved template/reference or prior confirmed Grilling.

## Canonical contract

The machine-readable contract is `artifact-production-contract.json`; an optional readable projection is `artifact-production-contract.md`.

Minimum semantic sections:

```json
{
  "schemaVersion": 1,
  "artifactId": "...",
  "contractRevision": "1.0",
  "status": "draft|frozen|superseded",
  "intent": {
    "purpose": "...",
    "audience": [],
    "decisionOrEffect": "...",
    "successCriteria": []
  },
  "content": {
    "sourceOfTruth": [],
    "required": [],
    "excluded": [],
    "structure": [],
    "claimsPolicy": {},
    "language": {},
    "evidence": {}
  },
  "visual": {
    "templateAuthority": {},
    "layoutPrinciples": [],
    "typography": {},
    "palette": {},
    "imageLanguage": {},
    "chartTableRules": [],
    "protectedRegions": []
  },
  "delivery": {
    "formats": [],
    "editable": true,
    "canonicalSourceFormat": "...",
    "canonicalStore": "google-drive",
    "canonicalDestinationRef": "...",
    "distributionContext": "...",
    "versioning": {}
  },
  "locks": [],
  "figureContractsRef": "artifact-figure-contracts.json",
  "changeControl": {},
  "acceptanceCriteria": []
}
```

## Lock classes

### INVARIANT

Cannot change during production without explicit contract revision.

Typical examples:

- approved template identity;
- logo/footer/protected-region behavior;
- fixed brand tokens;
- required message/decision ask;
- mandatory/forbidden sections;
- supplied/approved figure composition;
- controlled source data/claim wording;
- canonical source format for a derived PDF;
- canonical Drive destination when explicitly fixed.

An unapproved INVARIANT deviation is a critical audit failure.

### CONTROLLED

May change only when needed to better fulfill the frozen intent and must be documented with reason/impact.

Examples: section order, slide/page count, table-vs-chart choice, wording compression, figure placement, whitespace.

### ADAPTIVE

May be optimized without contract revision while intent, meaning and protected constraints remain unchanged.

Examples: small spacing, non-material line breaks, minor crops and caption wrapping.

## Figure contracts

Material figures use `artifact-figure-contracts.json`.

Each material visual should record at least purpose, message, source refs, visual type, composition, required/forbidden elements, labels, palette roles, editability, placement, caption, provenance, lock class and status.

A supplied or approved figure must not be silently replaced by a generated interpretation.

Generated imagery may support communication but must not fabricate evidence, data, logos, source identity or controlled branding.

## Freeze gate

Production begins only when:

- remaining uncertainty is non-material or explicit;
- INVARIANT items are known;
- material figures are contracted or deliberately delegated;
- source/template authority is resolved;
- requested formats/editability are known;
- canonical Drive persistence/distribution expectations are known;
- acceptance criteria are testable.

Material new requirements during production require a contract revision and re-freeze.

## Production rule

Format-specific workflows execute the frozen contract; they do not reinterpret the brief from scratch.

They may optimize ADAPTIVE scope and document justified CONTROLLED changes.

They must not silently change invariants, claims/data, intended effect, approved figures, template/brand authority or canonical-source relations.

## Contract audit

Before release, `artifact-contract-audit` compares the exact candidate revision against the frozen production contract and figure contracts.

Audit checks at least:

- intent fidelity;
- required/excluded content;
- source/claim fidelity;
- template/design authority;
- protected regions and visual rules;
- figure-by-figure conformance;
- canonical source relation for derived formats;
- requested editability/formats;
- documented CONTROLLED deviations;
- structural/render/parity QA evidence;
- intended canonical Drive destination/delivery semantics.

Severity:

- `critical`: unapproved INVARIANT deviation, missing required content, fabricated evidence, wrong controlled template, wrong source revision, or absent required final render verification;
- `major`: material undocumented CONTROLLED deviation or communication/readability defect;
- `warning`: non-material ADAPTIVE difference or documented limitation.

PASS requires zero open critical and major findings.

## Cross-format rule

Prefer one shared frozen contract for a multi-format package.

Where PDF is derivative:

```text
canonical PPTX or DOCX
  -> derived PDF
```

The PDF inherits the source artifact's content/visual/figure locks and adds only parity requirements.

## Final delivery gate

A production PASS is not a delivery PASS.

After contract audit, the exact approved revision must follow `docs/DOCUMENT-ARTIFACT-DELIVERY-CONTRACT.md`: persist to recipient-owned canonical Google Drive, read back, register and return the observed Drive link.

## Completion

Complete when one frozen production contract and figure-contract set governed the exact released artifact, format/render QA and contract audit passed, and the exact approved output was subsequently delivered through the Drive-only delivery contract.
