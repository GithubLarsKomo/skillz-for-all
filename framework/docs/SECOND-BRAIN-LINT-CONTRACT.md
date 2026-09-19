# Second-Brain Lint Contract

Status: active capability contract  
Date: 2026-09-19

## Operating-cycle role

This contract owns the **Lint** phase of the canonical [Second-Brain Operating Cycle](SECOND-BRAIN-OPERATING-CYCLE.md):

`Ingest -> Query -> Promote -> Lint`

Lint is trigger-based maintenance. Its findings may route work back to Ingest, Query or Promote.

## Purpose

Second-Brain lint is the maintenance loop for accumulated knowledge. It detects structural and semantic decay without turning lint into an independent Source of Truth.

Lint operates at two levels:

1. **Child-Brain lint** — quality of knowledge inside one Project/Collection Brain.
2. **Federation lint** — ownership, routing and consistency across Brains.

The lint pass may create findings and evidence-backed corrections. It must never invent supporting evidence or silently rewrite controlled source records.

## Trigger

Run a lint pass:

- after a bulk ingest or large source import;
- after material restructuring, migration, merge or Brain supersession;
- after a series of promotions that changed several knowledge items;
- when contradictions, duplication or stale facts are suspected;
- before a high-stakes synthesis that depends on a large accumulated corpus;
- periodically for active long-running Brains.

A normal small query does not require a full lint pass.

## Child-Brain lint

Check at least:

### Provenance

- durable claims without a source or evidence reference;
- source references that no longer resolve;
- synthesis whose supporting sources are ambiguous;
- external claims lacking authority class where that distinction matters.

### Freshness

- volatile claims without `asOf`;
- items past `reviewAfter` or `expiresAt`;
- historical measurements presented as current;
- source editions or versions that have changed materially.

### Contradictions and supersession

- mutually incompatible active claims;
- later correction without a supersession/contradiction link;
- deprecated knowledge still indexed as current;
- negative evidence that was recorded but never reconciled.

### Duplication

- semantically equivalent facts or notes with different stable identities;
- the same source-derived claim copied into multiple local files;
- repeated query syntheses that should strengthen/refine an existing item rather than create another one.

### Orphans and discoverability

- knowledge files not reachable from the local index/topic map;
- indexed items whose target no longer exists;
- sources not connected to any durable synthesis when they were ingested for that purpose;
- durable knowledge hidden only inside event prose.

### Promotion debt

- repeated useful query syntheses that were never promoted;
- material learnings still only present in transient event/status text;
- reusable project learnings that should be routed to a Domain Brain or specialist promotion workflow.

## Federation lint

Check at least:

- two active equal-rank canonical owners for the same knowledge class;
- a superseded or archived Brain still receiving new writes;
- a registered Brain whose Knowledge Store root or declared memory root is unavailable;
- scope/tags/workflowFamilies that no longer match the Child Brain;
- Project/Collection Brains that exist but are missing from expected routing;
- cross-Brain duplication where one Brain should link to the canonical owner;
- privacy regressions, including private Child metadata or provider locators copied into a less-protected layer;
- knowledge promoted to the Super Brain instead of the owning Child Brain;\n- copied/transferred Brains marked available before provider-ID rebind;\n- integrity mismatches between frozen release manifests and copied framework files.

## Finding states

Each finding is classified as:

- `fix-now` — deterministic correction with sufficient evidence;
- `promotion-needed` — durable knowledge is missing from its canonical owner;
- `reconcile` — contradiction or duplicate ownership needs explicit resolution;
- `stale-review` — freshness threshold reached;
- `broken-reference` — expected target/evidence cannot be resolved;
- `observe` — anomaly worth tracking but not yet actionable;
- `false-positive` — checked and intentionally left unchanged.

## Safe correction rules

Lint may automatically perform a correction only when all are true:

1. the canonical owner is unambiguous;
2. supporting evidence is already present;
3. the change does not alter a controlled source record;
4. no sensitive/private content crosses a protection boundary;
5. stable identity can be preserved;
6. the result is read-back verified.

Otherwise emit a finding and leave the knowledge state unchanged until reconciliation.

## Interaction with Query Promotion

`KNOWLEDGE-PROMOTION-CONTRACT.md` is the write path; this contract is the maintenance path.

Lint specifically looks for **promotion debt**: useful synthesis repeatedly reconstructed in queries but absent from durable knowledge. It may route such items back through the Knowledge Promotion Gate, but it does not bypass provenance, novelty or ownership checks.

## Karpathy reference

Andrej Karpathy's 2026 `LLM Wiki` idea explicitly treats `lint` as one of the core knowledge-base operations alongside ingest and query. This contract adopts that maintenance principle while adding explicit provenance, freshness, Source-of-Truth ownership, privacy and federation checks required by the Skillz architecture.
