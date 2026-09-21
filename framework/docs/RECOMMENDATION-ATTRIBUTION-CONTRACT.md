# Recommendation Authorization & Attribution Contract

**Status:** active capability contract  
**Date:** 2026-09-21

## Purpose

This contract separates evidence, interpretation and recommendations. It prevents a research, analysis, report or rewrite request from silently becoming an advisory mandate.

## 0. Precedence and default authority

This is a repository-wide default contract. It overrides skill-local schemas, templates or habitual output sections that would otherwise add a recommendation, prioritization, roadmap, mitigation, owner/cadence, decision posture, or next action.

A skill name or workflow type such as `assessment`, `due-diligence`, `strategy`, `review`, `report` or `analysis` does **not** itself authorize advice. Recommendation fields that are mandatory in an older schema are treated as optional/null unless the user explicitly authorizes advisory output.

## 1. Recommendation Authorization Gate

Default state: **recommendations are not authorized**.

A workflow may generate an assistant-authored recommendation only when the user has explicitly requested recommendation, advice, prioritization, selection, a proposed course of action, implementation guidance, decision support, or an equivalent advisory output.

Requests to research, analyze, compare, summarize, document, report, assess evidence, map risks, or describe implications do **not** by themselves authorize recommendations.

When recommendations are not authorized:

- do not add a recommended option, priority, action plan, roadmap, owner/cadence, decision posture, `nextSafeAction`, mitigation plan or "what to do next";
- findings may state evidence, implications, constraints, uncertainties, risks, options and open questions;
- do not turn an evidence gap into an imperative.

A skill whose normal schema contains recommendation fields must leave them absent/null or replace them with descriptive evidence/option fields unless the user authorized advice.

## 2. Third-party recommendations

A recommendation made by an external source remains a **source claim**, not an assistant recommendation.

Every third-party recommendation must:

1. identify the recommending source or authoring body;
2. remain visibly attributed in the sentence or label;
3. retain the source's scope, population, conditions and uncertainty;
4. never be rewritten into unattributed imperative voice.

### Substantiated recommendations

Recommendations from peer-reviewed publications, consensus statements, professional guidelines, standards/guidance documents or competent authorities must be visibly presented as quotations when their recommendation wording is material. Peer review, consensus or guideline status strengthens provenance but does not transfer recommendation ownership to the assistant.

Use:

- a short direct quote with quotation marks and source reference; or
- when the original wording is too long, a short decisive quote anchor plus an explicitly attributed paraphrase.

Do not quote more text than necessary. A citation alone is not enough if the wording would otherwise appear to be the assistant's recommendation.

Example:

> **Recommendation of the study authors (quote):** “...should be repeated...” [source]

The surrounding text may explain applicability, but must not silently adopt the recommendation.

## 3. Statement ownership

For evidence-bearing writing, distinguish where material:

- `fact`
- `source-interpretation`
- `third-party-recommendation`
- `assistant-interpretation`
- `assistant-recommendation`

`assistant-recommendation` is permitted only after the Recommendation Authorization Gate passes.

## 4. Rewriting and synthesis

Rewriting must preserve recommendation ownership.

Forbidden transformations include:

- source recommendation -> neutral fact;
- source recommendation -> assistant imperative;
- descriptive implication -> assistant recommendation;
- quoted recommendation -> de-attributed paraphrase;
- evidence gap -> invented mitigation or next step.

## 5. QA gate

PASS only if:

- recommendation authorization is explicit or recommendations are absent;
- all third-party recommendations remain attributed;
- substantiated recommendations are marked as quotations as defined above;
- recommendations are not presented as facts;
- no renderer or summarizer introduces a new recommendation.

This contract applies across research, evidence synthesis, reports, memos, presentations and downstream document production.
