---
name: medical-device-regulatory-strategy
description: Orchestriert evidenzbasierte Multi-Market-Regulatory-Strategie für Medical Devices und IVDs aus bestätigtem Produktkontext, spezialisierten EU/FDA-Assessments und – sofern vorhanden – versionierten historischen Decision Precedents, ohne Fachanalyse, Authority Decision oder Wayfinder zu duplizieren.
userFacing: true
implicitInvocation: true
category: regulated-engineering
version: 0.2.0
status: candidate
owners:
  - White Label Maintainer
requires: 
  - regulated-product-context
  - eu-mdr-ivdr-regulatory-specialist
  - fda-medical-device-ivd-regulatory-specialist
  - medical-device-risk-management-iso14971
  - large-work-wayfinder
outputs: 
  - regulatory-strategy.json
  - regulatory-strategy.md
  - regulatory-wayfinding-handoff.json
lastEvaluated: 2026-08-04
---

# medical-device-regulatory-strategy

## Zweck

Ersetzt eine breite Head-of-RA-Persona durch einen dünnen strategischen Orchestrator für Markets, Sequencing, Evidence Reuse, Dependencies, Decisions und Investigations.

## Trigger

Verwenden für regulatorische Gesamtstrategie über mehrere Märkte, Market Sequencing, Submission-/Evidence Roadmap, cross-functional Regulatory Dependencies oder Executive Regulatory Decision Preparation.

## Gemeinsame Regulated-Engineering-Regeln

- Aussagen mit regulatorischer Wirkung trennen `regulation/law`, `standard`, `guidance`, `organizational-policy`, `precedent` und `interpretation`.
- Zeitabhängige regulatorische Fakten benötigen `asOf` und eine nachvollziehbare Source-Referenz; fehlt sie, bleibt der Punkt `unknown`.
- Volltexte urheberrechtlich geschützter Standards werden nicht reproduziert. Verwende zugängliche autoritative Quellen und organisationslizenzierte Normtexte nur als Evidenz.
- Fehlende Evidenz ist kein positiver Compliance-Nachweis.
- Bei High-Impact-Klassifikation, Zulassung, Zertifizierung, Freigabe oder Legal Interpretation wird die erforderliche menschliche/behördliche Autorität nicht simuliert.

## Fachregeln

- Der Skill konsumiert Specialist Assessments; er klassifiziert MDR/IVDR/FDA nicht noch einmal unabhängig.
- Market Priorities, Sequencing, Evidence Reuse, Dependencies, Resource Needs und Irreversible Decisions werden explizit getrennt.
- Fees, Authority Review Times, Guidance-Versionen, NB Capacity und Übergangsregeln sind volatile Planning Inputs und benötigen aktuelles asOf/Source Evidence.
- Strategieoptionen enthalten Preconditions, Regulatory Risk, Evidence Gaps, Reversibility und Decision Owner/Authority Status.
- Bei kritischer Unsicherheit wird ein begrenztes Investigation Backlog an large-work-wayfinder übergeben statt eine scheinpräzise Roadmap erfunden.
- Approval/Clearance/CE/Submission Accepted werden nur aus externer bestätigter Evidenz als Status übernommen.

## Decision-Precedent-Regel

Wenn eine gepflegte Regulatory Decision & Precedent Library verfügbar ist, nutze sie **nach** Fixierung des Produktkontexts und **vor** endgültiger Strategieentscheidung als historischen Konsistenz- und Reasoning-Layer.

Ein Precedent ist niemals regulatorische Autorität. Bevor er wiederverwendet wird:

1. stabile Precedent-ID und Version erfassen;
2. `status` prüfen (`active`, `qualified`, `superseded`, `retired`);
3. Gemeinsamkeiten und materielle Unterschiede zum neuen Fall dokumentieren;
4. `non-transferable specifics` explizit ausschließen;
5. alle für den neuen Fall relevanten externen Anforderungen/Guidance/Standards aktuell verifizieren;
6. Transfer Conditions und Re-verification Triggers prüfen;
7. Ergebnis als `reused`, `reused-with-qualification`, `not-applicable`, `supersede-candidate` oder `new-precedent-candidate` markieren.

`qualified` Precedents dürfen eine Untersuchung strukturieren, aber nicht ohne zusätzliche Evidenz als Entscheidungsbasis übernommen werden. `superseded` und `retired` dienen nur historischer Nachvollziehbarkeit.

Wird ein bestätigter neuer Regulatory Decision wesentlich anders als ein bestehender Precedent getroffen, soll die Memory-/Second-Brain-Schicht den alten Record nicht still überschreiben, sondern einen versionierten Supersession-/New-Precedent-Kandidaten erzeugen.

## Workflow

1. Produktkontext und Zielmärkte fixieren.
2. EU/FDA/weitere bestätigte Specialist Assessments konsolidieren.
3. Falls verfügbar, relevante versionierte Decision Precedents anhand Jurisdiktion, Domäne, Intended Use, Technologie und Lifecycle Stage abrufen und Transferability prüfen.
4. Evidence Reuse, kritische Pfade, QMS/Risk/Clinical-Performance/Technical-Documentation Dependencies modellieren.
5. Strategieoptionen und Decision Points mit Freshness, Precedent-Fit und Risiko vergleichen.
6. Wayfinder-Investigations für ungelöste kritische Unsicherheit erzeugen.
7. Executive Strategy und nächste sichere Aktion ausgeben.
8. Nach bestätigter Entscheidung einen `reused/new/supersede` Handoff an die zuständige Memory-/Second-Brain-Schicht ausgeben, sofern der Entscheid dauerhaft und nicht-sensitiv wiederverwendbar ist.

## Precedent-Handoff

Wenn eine Precedent Library verwendet wurde, ergänze intern/als maschinenlesbare Begleitstruktur mindestens:

```json
{
  "precedentUse": [
    {
      "precedentId": "RCP-001",
      "version": "1.0.0",
      "status": "active",
      "fit": "reused-with-qualification",
      "same": ["material similarity"],
      "different": ["material difference"],
      "sourcesReverified": ["authoritative source reference"],
      "remainingUnknowns": ["open issue"]
    }
  ]
}
```

Keine privaten Repository-Namen oder sensitiven Projektinhalte in öffentliche Skill-Artefakte schreiben.

## Wayfinder-kompatible Übergabe

Wenn der nächste sichere Schritt durch Unsicherheit blockiert ist, gib eine begrenzte Übergabe mit diesen Feldern aus: `facts, assumptions, hypotheses, unknowns, blockers, decisions, investigations, risks`. Investigations müssen eine einzelne Frage, benötigte Evidenz, Stop Condition und Nicht-Ziele enthalten.

## Compliance Traceability

Verknüpfe relevante Ergebnisse mit `compliance-traceability-v1` als `obligation -> product-requirement -> risk/rationale -> implementation/control -> verification -> evidence -> status`. Quellenbezogene regulatorische Claims folgen `regulatory-source-evidence-v1`.

Precedent-Referenzen werden zusätzlich als historische Rationale-Verknüpfung geführt, aber niemals anstelle der aktuellen Source Evidence.

## Grenzen

- Keine zweite Specialist-Klassifikation.
- Keine statischen Kosten/Reviewzeiten.
- Keine behauptete Regulatory Approval ohne Authority Evidence.
- Kein "precedent says so" als regulatorische Begründung ohne aktuelle Source-/Applicability-Prüfung.
- Keine automatische Übernahme von Sample Sizes, Product Codes, Device Classes, Predicates, Timelines oder Schwellenwerten aus historischen Precedents.

## Qualitätsgate

Pass nur, wenn Facts/Interpretations/Precedents getrennt, Freshness sichtbar, zentrale Claims rückverfolgbar, Unknowns nicht positiv umgedeutet, Cross-Skill-Grenzen respektiert, verwendete Precedents mit Version/Status/Transferability geprüft und die nächste Aktion ohne versteckte Regulatory-Annahme ausführbar ist.
