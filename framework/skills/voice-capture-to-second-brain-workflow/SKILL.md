---
name: voice-capture-to-second-brain-workflow
description: Orchestriert offline-taugliches Smartphone-/iPhone-Diktat aus einer append-only Capture-Datei über Normalisierung, idempotentes Routing und das Knowledge-Promotion-Gate in den kanonischen Project- oder Collection-Second-Brain und erzeugt optional eine read-only Obsidian-Projektion. Verwenden, wenn spontane Sprach- oder Quick-Note-Captures nicht nur gesammelt, sondern sicher in die föderierte Second-Brain-Architektur überführt werden sollen.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - White Label Maintainer
requires:
  - thought-capture-journal
  - second-brain-federation-workflow
  - project-second-brain
  - structured-knowledge-artifact
  - obsidian-adapter
consumes:
  - thought-journal.json
outputs:
  - voice-capture-ledger.json
  - voice-capture-routing.json
  - voice-capture-promotion.json
  - optional Obsidian read-only projection
lastEvaluated: 2026-09-20
---

# Voice Capture to Second Brain Workflow

## Zweck

Dieser Workflow schließt die Lücke zwischen reibungsarmer mobiler Erfassung und dauerhaftem, kanonisch geroutetem Wissen.

Er trennt strikt:

1. Capture — Was wurde tatsächlich diktiert oder notiert?
2. Normalisierung — Welche stabilen Einträge liegen vor?
3. Routing — Welcher kanonische Owner ist zuständig?
4. Promotion — Ist der Inhalt überhaupt dauerhaftes Wissen?
5. Persistenz — Welche kleinste Abstraktion darf in den Owner geschrieben werden?
6. Projektion — Wie wird der verifizierte Zustand in Obsidian sichtbar?

Ein Capture ist nie allein deshalb kanonisches Wissen, weil er in einer Datei, in Obsidian oder in einer Inbox liegt.

## Architektur

~~~text
iPhone / Smartphone
      |
      v
append-only Capture Staging
      |
      v
thought-capture-journal
      |
      v
voice-capture-ledger
      |
      +--> run-only / review-needed / blocked
      |
      v
Owner Resolution + Federation
      |
      v
Knowledge Promotion Gate
      |
      v
canonical Child Brain / Skillz / governed owner
      |
      v
read-back verification
      |
      v
structured knowledge -> obsidian-adapter
      |
      v
read-only Obsidian projection
~~~

## Capture Boundary

### Staging als Standard

Wenn Obsidian als read-only Projektion der kanonischen Brains verwendet wird, ist Staging der Standard.

Bevorzugte iOS-Ablage:

iCloud Drive/Shortcuts/SecondBrain Capture/Thought Journal.md

Der Apple-Kurzbefehl muss:

- Sprache lokal erfassen können,
- einen Zeitstempel mitführen,
- an die bestehende Datei anhängen,
- keine Tags, Brain-Namen oder Projekte während des Diktats erzwingen,
- ohne LLM, Repository-Zugriff, Workflow-Automation oder erreichbaren Second-Brain-Dienst funktionieren.

Optional darf eine explizite Capture-ID gespeichert werden. Fehlt sie, übernimmt thought-capture-journal die stabile Entry-ID.

### Writable Vault nur als Opt-in

Direktes Capture in einen Obsidian-Vault ist nur zulässig, wenn dieser Vault ausdrücklich als writable-vault betrieben wird.

Ein read-only Vault oder eine generierte Obsidian-Projektion ist niemals Capture Store oder Source of Truth.

## Eingaben

- thought-journal.json aus thought-capture-journal,
- Source-Referenz auf die rohe Capture-Datei,
- aktueller Super-Second-Brain Bootstrap, state.json und registry.json, wenn fachliches Routing erforderlich ist,
- optional bereits bestätigter Projektkontext,
- optional letzter voice-capture-ledger.json für inkrementelle Verarbeitung.

## Idempotenz und Ledger

Der Workflow führt voice-capture-ledger.json als Verarbeitungsprojektion. Der Ledger ist kein fachliches Wissenssystem.

Mindestschema:

~~~json
{
  "schemaVersion": 1,
  "sourceRef": "Thought Journal.md",
  "entries": [
    {
      "captureId": "thought-...",
      "sourceFingerprint": "...",
      "state": "normalized",
      "routingCandidates": [],
      "canonicalOwner": null,
      "promotionState": null,
      "canonicalRef": null,
      "lastProcessedAt": "ISO-8601"
    }
  ]
}
~~~

Zulässige Zustände umfassen mindestens:

new -> normalized -> routed -> promotable -> promoted

sowie:

review-needed | run-only | rejected | blocked-no-target | source-changed

Regeln:

- Derselbe unveränderte Capture darf bei erneutem Einlesen keinen zweiten Brain-Write erzeugen.
- Ein bereits verarbeiteter Capture mit unverändertem Fingerprint wird übersprungen.
- Ändert sich der Rohquelleninhalt unter derselben stabilen ID, wird source-changed markiert; bereits promotiertes Wissen wird nicht still überschrieben.
- Zwei bewusst getrennte, identische Diktate bleiben zwei Captures, wenn die Normalisierung sie als getrennte Source-Einträge identifiziert.
- Der Ledger speichert Status und Referenzen, nicht eine zweite fachliche Wahrheit.

## Routing

### 1. Ownership-Klasse vor Domain-Routing bestimmen

Vor der Child-Brain-Auswahl zuerst klassifizieren:

- projekt- oder matterspezifisches Wissen -> zuständiger Project/Collection Brain,
- wiederverwendbares Domänenwissen -> zuständiger Domain/Collection Brain,
- Workflow, Gate, Schema, Evaluation oder Routinglogik -> Skillz,
- user-spezifische dauerhafte Präferenz oder Constraint -> Memory Path / communication-memory-governance,
- kontrollierte Records/Evidence -> autoritatives Quellsystem; Brain nur mit Referenz und abgeleiteter Erkenntnis,
- ausführbare Software -> eigenes Producer-Repository; Brain nur mit Wissen, Zustand und Referenzen,
- transiente Erinnerung oder niedriger dauerhafter Nutzen -> run-only.

### 2. Federation für Brain-Routing verwenden

Wenn ein Project/Collection Brain zuständig sein könnte:

1. Super-Second-Brain Bootstrap lesen.
2. state.json und registry.json lesen.
3. Kandidaten aus Scope, workflowFamilies, Tags und bereits bestätigtem Kontext bestimmen.
4. Bei persistentem Kontext den kanonischen Child Root lesen.
5. Nur bei eindeutigem Owner weitergehen.

Ein generischer Catch-all-Brain oder eine allgemeine Inbox ist kein Fallback-Owner für unklare Captures.

### 3. Ambiguität blockiert Writes

Wenn mehrere gleichrangige Owner plausibel sind:

- state = review-needed,
- Kandidaten und Begründung festhalten,
- keinen Brain-Write ausführen.

Wenn kein verifizierter kanonischer Owner erreichbar ist:

- state = blocked-no-target,
- keinen bequemen Ersatz-Owner erfinden.

Ein falscher Write ist schwerer zu korrigieren als ein wartender Capture.

## Promotion Gate

Nach Routing ist der Capture noch nicht automatisch dauerhaftes Wissen.

Wende docs/KNOWLEDGE-PROMOTION-CONTRACT.md an und klassifiziere genau einen Zustand:

new | strengthen | refine | contradict | project-only | run-only | insufficient-evidence | blocked-no-target

### Nicht promoten

Insbesondere nicht promoten:

- bloße Erinnerungen ohne dauerhaften Wissenswert,
- Rohchat oder Rohdiktat als solches,
- Secrets oder Credentials,
- spekulative Hypothesen ohne ausreichende Evidenz,
- transiente Statusmeldungen,
- unnötige personenbezogene oder sensitive Inhalte.

### Promoten

Wenn bestätigt wiederverwendbares Wissen entstanden ist:

1. kleinste Evidenzmenge festhalten,
2. kleinste dauerhafte Abstraktion formulieren,
3. im kanonischen Ziel nach semantischem Äquivalent suchen,
4. bestehende stabile Identität stärken/refinen statt duplizieren,
5. nur Abstraktion plus Provenance/Freshness/Counterconditions schreiben,
6. Zielartefakt read-back-verifizieren,
7. erst danach state = promoted und canonicalRef setzen.

Der rohe Capture bleibt in seiner Source. Er wird nicht automatisch als Brain-Note kopiert.

## Project-Second-Brain-Integration

Wenn eine Promotion den Projektzustand materiell verändert:

- project-second-brain verwenden,
- Producer-Artefakte nur verlinken,
- semantische Zustandsänderung als passenden Event oder Knowledge-Update dokumentieren,
- keine private Chain-of-Thought persistieren.

Nicht jeder Capture erzeugt einen Project-Memory-Event.

## Optionaler Thought-Graph-/Concept-Pfad

thought-graph-extractor oder thought-to-concept-flow nur einsetzen, wenn mehrere Captures gemeinsam als Ideensammlung, Konzept oder Bedeutungsgraph verarbeitet werden sollen.

Nicht jeden einzelnen Capture zwangsläufig graphisieren.

## Obsidian-Projektion

Obsidian folgt nach der kanonischen Verarbeitung.

Erlaubt sind beispielsweise:

- Capture Inbox.md mit Statuszahlen und Review-Links,
- Recent Knowledge.md,
- Brain-Übersichten,
- Maps/Canvas aus knowledge-map-generator.

Regeln:

- Der obsidian-adapter rendert ausschließlich bereits bestimmte Semantik.
- Obsidian-Folder, Dateinamen, Canvas-Positionen oder manuelle Edges bestimmen kein Brain-Routing.
- Ein read-only Vault schreibt nie direkt in den kanonischen Brain zurück.
- Zulässige manuelle Obsidian-Änderungen werden höchstens als nicht-kanonische Kandidaten zurückgegeben und müssen Governance/Reconciliation durchlaufen.
- Sensitive Rohdiktate werden nicht unnötig in die Projektion kopiert.

## Privacy und Offline-Verhalten

Capture muss offline und lokal möglich bleiben.

Nachgelagerte Verarbeitung darf externe Dienste nur verwenden, wenn dies für den jeweiligen Inhalt zulässig ist. Persönliche oder vertrauliche Captures dürfen nicht allein wegen Automatisierung an externe LLMs oder unkontrollierte Dienste gesendet werden.

## Implementierungsgrenze

Dieser Skill besitzt Workflow-, Gate- und Schema-Logik.

Ein ausführbarer Reader, Sync-Dienst, Workflow-Automation, API-Service oder Knowledge-Store-/Repository-Writer gehört in ein eigenes nicht-Brain Producer-Repository. Kein ausführbarer Capture-Pipeline-Code wird im Second Brain oder in Skillz als Projektimplementierung abgelegt.

## Qualitätsgate

Bestanden nur wenn:

- Capture offline gespeichert werden kann,
- read-only Obsidian nicht als Capture Store verwendet wird,
- wiederholte Verarbeitung idempotent ist,
- unklare Owner keinen Brain-Write auslösen,
- ein generischer Catch-all-Brain nicht als bequemer Fallback missbraucht wird,
- run-only Captures keinen dauerhaften Brain-Eintrag erzeugen,
- jede Promotion dem Knowledge-Promotion-Gate folgt,
- behauptete kanonische Writes read-back-verifiziert sind,
- Obsidian keine neue Semantik oder Source-of-Truth-Rolle erhält.

## Abschluss

Der Workflow endet pro Capture mit genau einem nachvollziehbaren Zustand: promoted, run-only, rejected, review-needed, blocked-no-target oder source-changed.

Bei promoted existiert ein read-back-verifizierter canonicalRef. Bei allen anderen Zuständen wurde kein unzulässiger kanonischer Write ausgeführt.
