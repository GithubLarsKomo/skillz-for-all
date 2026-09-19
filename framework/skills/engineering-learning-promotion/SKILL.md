---
name: engineering-learning-promotion
description: Extrahiert nach verifizierten Software-Deliveries, Migrationen, Incidents, Architekturentscheidungen oder Algorithmusversuchen nur wirklich wiederverwendbare Engineering-Learnings aus einem Projekt, prüft Neuheit und Gegenbedingungen und promotet sie mit Provenienz und Reifegrad in das kanonische Coding Brain. Verwenden nach semantisch abgeschlossenem Engineering-Zustand; nicht als Ersatz für Project Memory, Code Review oder Delivery-Verifikation.
userFacing: true
implicitInvocation: true
category: engineering
version: 0.1.0
status: candidate
owners:
  - White Label Maintainer
requires:
  - iterate-software-projects
  - project-second-brain
outputs:
  - engineering-learning-card.md
  - engineering-learning-card.json
  - engineering-learning-promotion-result.json
lastEvaluated: 2026-09-14
---

# Engineering Learning Promotion

## Zweck

Dieser Skill schließt die Lernschleife zwischen einzelnen Softwareprojekten und dem projektübergreifenden `White Label Maintainer/coding-brain`.

Er beantwortet nicht die Frage **„Was ist in diesem Projekt passiert?“** — dafür ist `project-second-brain` zuständig. Er beantwortet:

> **Was davon ist evidenzbasiert, neu und über dieses Repository hinaus wiederverwendbar?**

Das Coding Brain bleibt eine abstrahierte Lernschicht. Quellcode, vollständige Logs, projektspezifische Secrets, aktuelle Betriebsdetails und projektinterne Wahrheit bleiben im owning repository.

## Trigger

Verwenden nach mindestens einem dieser Zustände:

- verifiziertem Merge oder Release eines materiellen Inkrements;
- erfolgreicher Migration, Cutover-Probe oder Restore-/Rollback-Probe;
- Incident/Postmortem mit belastbarer Ursache und Abhilfe;
- implementierter Architekturentscheidung mit Verifikation;
- neuem wiederverwendbarem Test-, Diagnose-, Recovery- oder Deployment-Harness;
- Algorithmus-/Modellversuch mit messbarem Ergebnis;
- MCP-/Agent-/LLM-Integrationsmuster mit realem Einsatznachweis;
- wichtigem gescheitertem Ansatz mit übertragbarem `doNotRepeat`;
- demselben Muster in einem zweiten Projekt, sodass dessen Reifegrad neu bewertet werden sollte.

Nicht ausführen für reine Ideen, ungeprüfte Branch-Experimente, einzelne Shell-Kommandos, unveränderte CI-Polls oder bloße Tool-Nutzung ohne erkennbares Lernsignal.

## Voraussetzungen

Vor Promotion müssen verfügbar sein:

1. Owning repository und relevanter Branch/Commit oder Release.
2. Verifizierter Delivery-/Review-Zustand oder klar als Experiment/Postmortem abgegrenzte Evidenz.
3. Relevanter Project-Memory-Event oder gleichwertige stabile Projektquelle.
4. Nachweis, dass das Learning nicht nur aus Planung oder README-Behauptung abgeleitet wird.

Wenn Delivery noch `pending`, `review-stale`, `unknown` oder nur lokal behauptet ist, darf höchstens ein **candidate-draft** erzeugt werden; keine stabile Promotion ins Coding Brain behaupten.

## Source-of-truth-Grenzen

- **Projekt-Repository:** Implementierungswahrheit.
- **Project Second Brain:** verifizierter Projektzustand, Entscheidungen, Events und Evidenzlinks.
- **Skillz:** reproduzierbarer Arbeitsablauf.
- **Coding Brain:** abstrahiertes projektübergreifendes Engineering-Learning.
- **Super Second Brain:** Routing zwischen Wissensdomänen.

Keine dieser Schichten darf die andere durch Kopieren ersetzen.

## Ablauf

### 1. Evidence Pack fixieren

Bestimme den kleinsten belastbaren Evidenzsatz:

- Repository;
- Branch/Commit/Tag/PR/Release soweit relevant;
- Project-Memory-Event oder Decision Record;
- Tests, Runtime-, Migration-, Recovery- oder Incident-Evidence;
- zeitlicher Stand.

Trenne ausdrücklich:

- beobachtetes Verhalten;
- dokumentierte Entscheidung;
- abgeleitete wiederverwendbare Aussage.

### 2. Lernkandidat formulieren

Ein Kandidat muss alle folgenden Fragen beantworten:

1. **Problem** — welches wiederkehrende Engineering-Problem lag vor?
2. **Context** — unter welchen Randbedingungen trat es auf?
3. **Pattern** — was wurde tatsächlich umgesetzt oder bewusst verworfen?
4. **Why it worked / failed** — welche beobachtbare Evidenz trägt die Aussage?
5. **Applicability** — in welchen anderen Projekttypen ist es plausibel nützlich?
6. **Counterconditions** — wann sollte es ausdrücklich nicht wiederverwendet werden?
7. **Provenance** — welche Quellen beweisen die Herleitung?
8. **Maturity** — wie stark ist die Wiederverwendung bereits belegt?

Fehlt insbesondere Evidence oder Countercondition, nicht promoten.

### 3. Abstraktionsprüfung

Verwerfe oder reduziere Kandidaten, die nur Folgendes enthalten:

- projektspezifische Dateinamen ohne generalisierbaren Mechanismus;
- private Hosts, Tokens, Secrets oder unnötige interne Infrastrukturdetails;
- eine Bibliothek lediglich als Tool-Liste;
- Stilpräferenzen ohne Engineering-Wirkung;
- Behauptungen aus Roadmaps ohne Implementierungsnachweis;
- ein einmaliges Workaround, dessen Randbedingungen nicht verstanden sind.

Ein gutes Learning beschreibt Mechanismus + Kontext + Beleg + Grenzen.

### 4. Novelty Check im Coding Brain

Suche vor Neuanlage im kanonischen `White Label Maintainer/coding-brain` mindestens in:

- `docs/project-memory/TOPICS.md`;
- `docs/project-memory/projects/`;
- vorhandenen Learning Cards/Knowledge Notes;
- relevanten Events.

Entscheide genau einen Zustand:

- `new` — semantisch neues Learning;
- `strengthen` — bestehendes Learning erhält neue unabhängige Evidenz;
- `refine` — neue Countercondition, Scope-Grenze oder bessere Formulierung;
- `contradict` — neue Evidenz widerspricht einem bestehenden Learning;
- `project-only` — nützlich, aber nicht ausreichend übertragbar;
- `insufficient-evidence` — Promotion noch nicht gerechtfertigt.

Bei `strengthen` oder `refine` keine Dublette anlegen.

### 5. Reifegrad bestimmen

Verwende diese Stufen:

- **experimental** — kontrollierter Versuch oder einzelne belastbare Implementierung; Übertragbarkeit noch unbewiesen.
- **candidate** — produktiv oder realitätsnah verifiziert und plausibel übertragbar.
- **repeated** — in mindestens zwei unabhängigen Projekten/Contexts erfolgreich belegt.
- **stable** — mehrfach wiederverwendet, Gegenbedingungen verstanden, keine wesentlichen offenen Widersprüche.
- **deprecated** — frühere Regel wird durch bessere Evidenz ersetzt; Nachfolger und Grund nennen.

Reifegrad nie aus Alter oder subjektiver Wichtigkeit ableiten.

### 6. Learning Card erzeugen

`engineering-learning-card.json` enthält mindestens:

```json
{
  "schemaVersion": 1,
  "id": "EL-<stable-slug>",
  "name": "...",
  "category": "architecture|algorithm|migration|verification|recovery|security|agent-llm-mcp|tooling|deployment|workflow|anti-pattern",
  "maturity": "experimental|candidate|repeated|stable|deprecated",
  "problem": "...",
  "context": ["..."],
  "pattern": "...",
  "whyItWorkedOrFailed": "...",
  "applicability": ["..."],
  "counterconditions": ["..."],
  "evidence": [
    {"repository": "owner/repo", "ref": "branch-or-sha", "artifact": "stable reference"}
  ],
  "sourceProjects": ["owner/repo"],
  "relatedPatterns": [],
  "doNotRepeat": [],
  "lastVerified": "YYYY-MM-DD"
}
```

Die Markdown-Fassung ist menschenlesbar und darf zusätzliche Begründung enthalten, aber keine private Chain-of-Thought.

### 7. Promotion ins Coding Brain

Wenn Schreibzugriff vorhanden ist:

1. vorhandenes äquivalentes Learning aktualisieren oder neue Learning Card unter der etablierten Knowledge-Struktur ablegen;
2. relevante `TOPICS.md`-Sektion knapp ergänzen;
3. Projektdossier nur dann aktualisieren, wenn dessen aktueller Evidence Snapshot dadurch wirklich erweitert wird;
4. einen Coding-Brain-Event für die Promotion schreiben;
5. keine Quellartefakte duplizieren — Provenienz verlinken.

Wenn Schreibzugriff fehlt, `engineering-learning-promotion-result.json` mit `status: pending-external-write` erzeugen und exakte Zieländerungen beschreiben. Keine erfolgte Promotion behaupten.

### 8. Widerspruchsbehandlung

Wenn neue Evidenz ein bestehendes Learning schwächt:

- bestehende Regel nicht still überschreiben;
- `contradict` markieren;
- betroffene Evidence und Contexts gegenüberstellen;
- Scope einschränken, Reifegrad herabsetzen oder Learning deprecaten;
- bei echter Unvereinbarkeit beide Bedingungen dokumentieren, bis weitere Evidenz entscheidet.

## Ausgabe

`engineering-learning-promotion-result.json` enthält mindestens:

```json
{
  "schemaVersion": 1,
  "sourceRepository": "owner/repo",
  "sourceRef": "...",
  "promotionDecision": "new|strengthen|refine|contradict|project-only|insufficient-evidence",
  "targetBrain": "White Label Maintainer/coding-brain",
  "learningId": "EL-...",
  "maturityBefore": null,
  "maturityAfter": "candidate",
  "writesVerified": false,
  "updatedArtifacts": [],
  "openEvidenceGaps": []
}
```

## Komposition

Empfohlener Pfad:

```text
iterate-software-projects
→ two-axis-code-review / relevante Specialist Gates
→ engineering-delivery-followup
→ project-second-brain
→ engineering-learning-promotion
→ nächste Iteration
```

Der Skill darf `iterate-software-projects` nicht ersetzen und keine Delivery-States erfinden.

## Qualitätsregeln

- Evidence first; README/Planung ist schwächer als Code/Test/Runtime/Delivery-Evidence.
- Branch-/Commit-Kontext festhalten, wenn er die Aussage beeinflusst.
- Negative Evidenz ist zulässig und wertvoll: gescheiterte Ansätze können starke Anti-Patterns erzeugen.
- Toolnamen allein sind kein Learning; die Entscheidung und ihr Kontext sind es.
- Ein zweites Projekt sollte ein bestehendes Learning bevorzugt stärken statt duplizieren.
- Secrets, private Endpoints und personenbezogene Daten gehören nicht in das Coding Brain.
- Counterconditions sind Pflicht, damit Learnings nicht zu universellen Dogmen werden.

## Abschlusskriterien

Eine Ausführung ist abgeschlossen, wenn ein Kandidat evidenzbasiert klassifiziert wurde, Novelty und Reifegrad bestimmt sind, eine Learning Card oder eine begründete Nicht-Promotion vorliegt und alle tatsächlich vorgenommenen Coding-Brain-Writes read-back-verifizierbar sind.