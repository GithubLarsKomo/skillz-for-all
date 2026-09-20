# Knowledge Promotion Contract

Status: active capability contract  
Date: 2026-09-19

## Operating-cycle role

This contract owns the **Promote** phase of the canonical [Second-Brain Operating Cycle](SECOND-BRAIN-OPERATING-CYCLE.md):

`Ingest -> Query -> Promote -> Lint`

Promotion is a mandatory decision gate after substantive work, not a mandatory write.

## Purpose

This contract formalizes **Query Promotion** for the federated Second-Brain system.

The rule is simple:

> At the end of every substantive query, research pass, analysis, workflow or project step, determine whether the work produced confirmed reusable knowledge that should change a future answer. If yes, route the smallest durable abstraction to its canonical owner and verify the write. If not, keep the result run-only.

This is a cross-cutting knowledge-governance rule. It does not make every conversation durable, and it does not turn the Super Second Brain into a content store.

## Bootstrap / system-prompt hook

A client bootstrap or system prompt should contain only this stable hook:

```text
At the end of every substantive query or workflow, apply the Knowledge Promotion Gate in docs/KNOWLEDGE-PROMOTION-CONTRACT.md before closure or handoff. Promote only evidence-backed reusable knowledge to its canonical owner; otherwise keep it run-only.
```

The detailed policy remains versioned here rather than being duplicated inside a long system prompt.

## What counts as substantive

Run the gate when the work produced at least one of the following:

- a new evidence-backed fact or synthesis that is likely to matter again;
- a correction or contradiction that changes existing durable knowledge;
- a reusable interpretation, heuristic, failure mode, countercondition or decision pattern;
- a cross-source synthesis that would otherwise have to be reconstructed later;
- a stable domain relationship, entity fact or taxonomy;
- a material project learning that changes future execution;
- a reusable workflow or governance improvement.

Do not promote merely because a response was long.

## Run-only by default

Keep these run-only unless another explicit producer owns them:

- raw chat text, private chain-of-thought or scratchpads;
- current task status, open follow-ups or transient repository/tool state;
- raw connector payloads or bulk source copies;
- speculative hypotheses without adequate evidence;
- secrets, credentials or private endpoints;
- sensitive personal information that is not explicitly governed for persistence;
- volatile external facts without provenance and freshness semantics;
- wording variants, incidental examples and low-value intermediate calculations.

## Canonical ownership routing

Promotion follows Source-of-Truth ownership, not convenience.

| Knowledge class | Canonical route |
|---|---|
| concrete project, company, person or matter state | owning Project/Collection Second Brain |
| reusable domain knowledge across projects | owning Domain/Collection Brain |
| reusable software-engineering learning | `engineering-learning-promotion` -> canonical Coding Brain |
| reusable workflow, gate, schema, evaluation or orchestration logic | Skillz framework |
| user-specific communication preference or durable personal constraint/fact | `communication-memory-governance` via the Memory Path Contract |
| controlled record, submission, CAPA, complaint, contract original or evidence record | controlled producer/source system; Second Brain stores references and derived knowledge only |
| volatile law, regulation, guidance, market/database state or other changing external fact | authoritative external source + Brain note with provenance, `asOf` and review/expiry metadata where needed |

The Super Second Brain resolves routing and ownership. It does not receive copied domain content.

## Promotion decision states

Every candidate is classified as exactly one of:

- `new` — genuinely new durable knowledge;
- `strengthen` — independent evidence strengthens an existing item;
- `refine` — scope, countercondition, provenance or wording is materially improved;
- `contradict` — new evidence conflicts with existing durable knowledge and requires explicit reconciliation;
- `project-only` — useful, but only inside the current Project Brain;
- `run-only` — intentionally transient;
- `insufficient-evidence` — plausible but not yet promotable;
- `blocked-no-target` — promotion appears justified but no verified canonical owner is currently writable.

A `strengthen`, `refine` or `contradict` result updates the existing stable identity whenever possible instead of creating a duplicate.

## Knowledge Promotion Gate

### 1. Freeze evidence

Identify the smallest evidence set that supports the candidate: source file, URL, provider object/revision, repository/commit, controlled record, decision record, experiment, tool result or other stable reference.

Separate:

- observed fact;
- interpretation or synthesis;
- recommendation or workflow rule.

### 2. Formulate the durable abstraction

Ask:

> What would we want a future agent to know without replaying this entire conversation or re-reading all sources?

The promoted item should contain the minimum reusable statement plus scope, provenance, freshness and relevant counterconditions.

### 3. Resolve canonical owner

Use the current Project Brain when the knowledge is project-specific. Use Federation routing when the knowledge is reusable across projects or when more than one Brain is plausible.

Never write the same knowledge as equal authority into two active Brains.

### 4. Novelty check

Search the target Brain for semantic equivalents before creating anything new.

Prefer:

- strengthen existing knowledge;
- refine an existing scope;
- add a contradiction/supersession relation;

over a parallel duplicate.

### 5. Persist only the abstraction

Write a concise durable note, fact, learning card or update. Link back to evidence rather than copying the evidence corpus.

For regulated or otherwise volatile knowledge, preserve authority class, `asOf`, and review/expiry semantics.

### 6. Update project/federation state only when needed

A promotion that materially changes project knowledge creates or updates the appropriate Project-Memory event/index/state.

Federation metadata changes only when ownership, routing, scope, availability or Brain structure changes. Ordinary knowledge promotion does not create a global cross-Brain/federation event.

### 7. Read-back verification

Do not claim promotion succeeded until the target artifact can be read back and the intended stable identity, Knowledge Store locator, source references and routing are visible.

## Query write-back rule

A query can itself create durable knowledge.

If answering a question required a useful synthesis that is not already represented in the canonical Brain, the synthesis is a promotion candidate even when no new external source was added.

This is the key compounding behavior: future queries should reuse accumulated synthesis instead of reconstructing it from raw sources every time.

## Lint interaction

Second-Brain lint should detect at least:

- contradictions without explicit reconciliation;
- stale or expired claims;
- duplicate active Sources of Truth;
- orphan knowledge with no index/routing path;
- durable claims lacking provenance;
- missing freshness metadata for volatile claims;
- useful repeated query syntheses that were never promoted;
- obsolete routing or superseded Brains still receiving writes.

Lint may propose promotion, refinement or deprecation; it must not silently invent evidence.

## Relationship to Memory Path Contract

`MEMORY-PATH-CONTRACT.md` governs user-specific durable memory and communication preferences.

This contract governs **domain/project/workflow knowledge** in the federated Second-Brain system.

A candidate must use the correct path; do not send general domain knowledge to personal memory merely because it was discovered in conversation.

## Relationship to Karpathy's LLM Wiki pattern

This design adopts the compounding-knowledge principle of Andrej Karpathy's 2026 `LLM Wiki` idea: raw sources remain available, an LLM-maintained structured knowledge layer accumulates synthesis, queries may write useful analysis back, and lint maintains quality. The Skillz architecture adds explicit Source-of-Truth ownership, federation, provenance/freshness rules and separate governance for personal memory.

The external idea file is a reference, not an authority over local architecture.
