# Second-Brain Operating Cycle

Status: active capability contract  
Date: 2026-09-18

## Canonical operating model

The federated Second-Brain system uses this lifecycle as its default operating model:

```text
Ingest -> Query -> Promote -> Lint
   ^                         |
   +-------------------------+
```

The cycle is **semantic, not mechanical**. Not every task executes every phase.

- **Ingest** runs when new authoritative or useful source material enters the system.
- **Query** is the actual research, reasoning, synthesis, project or execution work against current sources and accumulated knowledge.
- **Promote** runs as a gate after every substantive Query or workflow step.
- **Lint** runs when maintenance triggers are present, not after every small query.

The output of Lint may create a new Ingest, Query or Promotion need, which closes the loop.

## 1. Ingest

Purpose: introduce new evidence without confusing source material with durable synthesis.

For new material:

1. preserve the authoritative/raw source in its canonical source system;
2. identify source type, provenance, date/version and authority;
3. extract or synthesize only what is needed for the owning Brain;
4. link the derived knowledge back to the source instead of copying the full corpus;
5. keep historical facts scoped to their source/date;
6. surface contradictions rather than silently overwriting existing knowledge;
7. trigger a scoped Lint after bulk or structurally significant ingestion.

Ingest is not mandatory for a Query that can be answered from already available knowledge and current evidence.

## 2. Query

Purpose: use accumulated knowledge and current evidence to accomplish the user's actual goal.

For substantive work:

1. resolve the canonical Child Brain through Federation when persistent context matters;
2. read the Child Brain rather than relying on Super-Brain summaries;
3. use current authoritative evidence where freshness matters;
4. distinguish source facts, synthesis, assumptions and recommendations;
5. produce the requested answer, decision support, artifact or execution result.

A Query may itself create new knowledge even if no new source was ingested.

## 3. Promote

Purpose: make useful synthesis compound instead of disappearing into chat history.

After every substantive Query or workflow step, apply `KNOWLEDGE-PROMOTION-CONTRACT.md`.

Ask:

> Did this work produce confirmed reusable knowledge that would materially change a future answer or execution?

If yes:

- freeze supporting evidence;
- formulate the smallest reusable abstraction;
- resolve the canonical owner;
- check semantic novelty;
- classify `new|strengthen|refine|contradict|project-only|run-only|insufficient-evidence|blocked-no-target`;
- persist only to the canonical knowledge owner;
- preserve provenance, freshness and counterconditions;
- read back before claiming success.

If no, leave the result run-only.

Promotion is therefore a **mandatory decision gate**, not a mandatory write.

## 4. Lint

Purpose: maintain quality of accumulated knowledge and routing.

Apply `SECOND-BRAIN-LINT-CONTRACT.md` after:

- bulk source ingestion;
- material restructuring, migration or supersession;
- several related promotions;
- suspected contradiction, staleness, orphaning or duplication;
- before high-stakes synthesis over a large accumulated corpus;
- periodic maintenance of active long-running Brains.

Lint checks provenance, freshness, contradiction/supersession, duplication, discoverability, promotion debt, routing ownership and privacy boundaries.

Lint may route a finding back into:

- **Ingest** — evidence is missing or stale;
- **Query** — reconciliation or deeper analysis is needed;
- **Promote** — durable synthesis exists but is not yet in its canonical Brain.

## Source-of-Truth boundary

The operating cycle never changes ownership rules:

- raw/controlled evidence remains in the authoritative source or producer system;
- project-specific knowledge remains in the owning Project/Collection Brain;
- reusable domain knowledge remains in the owning Domain/Collection Brain;
- workflow/gate/schema/evaluation logic remains in Skillz;
- user-specific durable memory remains governed separately by the Memory Path Contract;
- the Super Second Brain remains routing/federation, not a domain-content store.

## Closure rule

A substantive task is operationally complete when:

1. the user-facing goal has been fulfilled or a bounded useful result produced;
2. current evidence and Source-of-Truth boundaries were respected;
3. the Promotion decision was made;
4. any triggered Lint was completed or explicitly left as an evidence-backed open finding;
5. writes that are claimed successful were read-back verified.

## Design origin

This operating model extends Andrej Karpathy's 2026 `LLM Wiki` pattern of Ingest, Query and Lint with an explicit **Promote** gate. The additional stage separates transient query output from durable knowledge and enforces canonical ownership, provenance and freshness in a federated multi-Brain architecture.
