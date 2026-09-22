---
name: project-second-brain
description: Führt eine Google-Drive-native, versionierbare Projektdokumentation als verlinkten Second Brain ab dem Requirements-Grilling. Nutzt recipient-owned Drive als kanonischen Knowledge Store, registriert erzeugte Nicht-Code-Artefakte im selben Brain und liefert verifizierte Drive-Links, während ausführbare Producer-Artefakte und private Chain-of-Thought getrennt bleiben.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.5.0
status: candidate
owners:
  - White Label Maintainer
requires: []
outputs:
  - project-memory-index.md
  - project-memory-state.json
  - project-memory-event.md
  - project-memory-assets.md
lastEvaluated: 2026-09-22
---

# Project Second Brain

## Zweck

Dieser Skill hält den vollständigen Projektweg **ab dem Grilling** als Google-Drive-native, versionierbare Wissensspur zusammen. In Skillz for All liegt der kanonische Project Memory nach Claim/Rebind zwingend in recipient-owned Google Drive. GitHub ist Framework-/Producer-Quelle, aber kein alternativer Runtime-Store für den Brain.

Er ersetzt keine fachlichen Producer-Artefakte, keine kontrollierten Records und keine externen Sources of Truth. Er verlinkt und projiziert deren verifizierten Zustand als nachvollziehbaren Projektgraphen.

Markdown/JSON/YAML sowie erzeugte normale Projekt- und Delivery-Artefakte liegen im selben recipient-owned Drive-Brain. Software, Build/Test/Runtime-Artefakte und kontrollierte Quellsysteme bleiben außerhalb des Brain, wenn sie dort kanonisch produziert oder verwaltet werden. Für alle Nicht-Code-Outputs gilt zusätzlich `docs/DRIVE-STORAGE-AND-DELIVERY-CONTRACT.md`.

Seine Kernfrage lautet: **Welcher verifizierbare Projektzustand entstand in diesem Schritt, worauf basiert er und wohin führt er als Nächstes?**

## Trigger

Verwenden:

- unmittelbar nach dem ersten abgeschlossenen projektbezogenen `round-based-requirements-grilling`,
- bei jedem wesentlichen Übergang zwischen Grilling, Wayfinding, Research, Spezifikation, Decision Record, Issue-Zerlegung, Implementierung, Review, Delivery und Handoff,
- wenn ein projektbezogener nicht-textueller Input oder Output erzeugt, empfangen, reviewt, freigegeben oder übergeben wird,
- wenn ein Projekt nach einer Unterbrechung aus seinem kanonischen Knowledge Store ohne erneute Vollanalyse fortgesetzt werden soll,
- wenn der Nutzer eine Obsidian-kompatible Projektchronik, einen Projektgraphen oder einen Second-Brain-artigen Wissensstand verlangt.

Nicht für jedes Shell-Kommando, jede Toolabfrage oder jede Zwischenüberlegung einen Event erzeugen. Dokumentiert werden **semantische Zustandsänderungen und abgeschlossene Arbeitsabschnitte**.

## Voraussetzungen

- Ein projektbezogener Kontext oder ein abgeschlossener Grilling-Schritt ist vorhanden.
- Der kanonische Knowledge Store oder ein eindeutiger Bootstrap-Zielstore kann bestimmt werden.
- Der konfigurierte Knowledge Store ist recipient-owned Google Drive; fehlende Drive-Schreibfähigkeit wird als `pending|blocked` behandelt, nicht durch einen anderen Runtime-Provider ersetzt.
- Kanonische Producer-Artefakte bleiben in ihren autoritativen Systemen und werden nicht als zweite Wahrheit in den Project Memory kopiert.
- Bei externen Producer-Systemen wird deren stabile Evidenzidentität verifiziert, zum Beispiel Commit SHA, Dokument-ID, Record-ID oder Release-ID.
- Provider-IDs, Revisionen, URLs und Sharing-Zustände werden beobachtet und nicht erfunden.

## Kanonischer Ablageort

Die logische Project-Memory-Struktur liegt in genau einem kanonischen Brain-Root des Knowledge Stores:

```text
docs/project-memory/
├── INDEX.md
├── TIMELINE.md
├── ASSETS.md
├── state.json
├── events/
├── decisions/
├── knowledge/
└── retrospectives/
```

- `INDEX.md` ist Map of Content und Einstieg für Mensch und Agent.
- `TIMELINE.md` enthält die chronologische verlinkte Ereignisfolge.
- `ASSETS.md` registriert nicht-textuelle oder externe Artefakte und ihre stabilen Provider-/Source-IDs.
- `state.json` ist die kompakte maschinenlesbare Projektion.
- `events/` enthält atomare, abgeschlossene Projektereignisse.
- `decisions/` ist der bevorzugte Ort für projektbezogene Decision Records, sofern kein anderer kanonischer Ort etabliert ist.
- `knowledge/` enthält nur wiederverwendbare projektbezogene Erkenntnisnotizen, nicht Rohquellenkopien.
- `retrospectives/` enthält abgeschlossene Iterations- oder Meilensteinrückblicke.

Besteht bereits eine gleichwertige Struktur, wird sie weiterverwendet. Kein paralleler Second Brain wird angelegt.

Im Google-Drive-Adapter ist die stabile Root-Folder-ID die kanonische Brain-Identität; Ordnername und Pfad sind Navigation, nicht Identität.

## Portable Markdown und Knowledge-Store-Kompatibilität

Verwende für Project-Memory-Kernartefakte normales Markdown, JSON und YAML. Diese Dateien bleiben verlustfrei exportierbar und unabhängig von einer nativen Office-Oberfläche.

Beispielhafte logische Relationen:

```text
DEC-004 -> ../decisions/DEC-004.md
SPEC -> ../../SPEC.md
EVT-... -> events/EVT-....md
ASSET-004 -> ASSETS.md + stabiler Provider-/Source-Locator
```

Relative Links sind eine lesbare Projektion. Der kanonische Locator für kritische Dateien und externe Assets wird zusätzlich über Provider-ID/Source-ID in `state.json`, `ASSETS.md` oder Event-Metadaten geführt.

Jede Event-Note besitzt YAML-Frontmatter. Native Google Docs/Sheets/Slides dürfen als fachliche Assets referenziert werden, ersetzen aber nicht die maschinenlesbaren Project-Memory-Kernartefakte.

## Dokumentationsvertrag ab Grilling

### 1. Bootstrap nach Grilling

Nach dem ersten projektbezogenen Grilling:

1. kanonischen Knowledge Store und Brain-Root bestimmen;
2. falls noch kein Brain-Root existiert, einen `project-memory-bootstrap` vorbereiten und im bestätigten Store materialisieren;
3. `docs/project-memory/` initialisieren;
4. stabile Root- und Memory-Root-IDs erfassen;
5. ersten Event mit `stage: grilling` erzeugen;
6. bestätigte Ziele, Nicht-Ziele, Entscheidungen, offene Punkte und relevante Grilling-Artefakte verlinken;
7. `INDEX.md`, `TIMELINE.md` und `state.json` aktualisieren;
8. Writes read-back-verifizieren;
9. den Project-Memory-Locator an den nächsten Skill übergeben.

### 2. Document-on-transition Gate

Vor jedem fachlichen Handoff muss der abgeschlossene wesentliche Schritt im Project Second Brain verankert sein.

Typische Übergänge:

```text
Grilling
  -> Wayfinding / Research
  -> Specification
  -> Backlog
  -> Implementation / Producer work
  -> Review
  -> Delivery
  -> nächste Iteration oder Abschluss
```

Wenn ein Schritt keine semantische Zustandsänderung erzeugt, darf auf einen neuen Event verzichtet werden.

### 3. Artifact Gate

Für jedes neue Artefakt zuerst den kanonischen Eigentümer bestimmen:

1. Project-Memory-Kernartefakt -> Brain Knowledge Store.
2. Erzeugtes normales Projekt-/Referenz-/Delivery-Artefakt -> derselbe Child-Brain-Drive-Root; wenn kein Brain passt, tenantweiter `Deliveries`-Root.
3. Build/Test/Runtime/Source-Code-Artefakt -> zuständiges Producer-System.
4. Controlled Record/Evidence Original -> kontrolliertes Quellsystem.

Für registrierte Assets stabile IDs, Provider, Revision/Freshness und gegebenenfalls Hash erfassen. Freigegebene/frozen Deliverables nicht still überschreiben; neue Version oder Supersession erzeugen.

Google-Drive-spezifische Asset-Regeln stehen in `references/drive-artifact-contract.md`; die tenantweite Pflicht zur Drive-Ablage und Link-Übergabe kommt aus `docs/DRIVE-STORAGE-AND-DELIVERY-CONTRACT.md`.

### 4. Query-Promotion Gate

Vor Abschluss oder Handoff eines substanziellen Queries, Research-Passes, Analyse- oder Workflow-Schritts wird `docs/KNOWLEDGE-PROMOTION-CONTRACT.md` angewendet.

- bestätigtes wiederverwendbares Wissen prüfen;
- Rohchat, transienten Status, ungeprüfte Hypothesen und Secrets nicht promoten;
- kanonischen Owner bestimmen;
- vor Neuanlage auf semantische Dubletten prüfen;
- nur die kleinste dauerhafte Abstraktion mit Provenance/Freshness persistieren;
- Erfolg erst nach Read-back behaupten.

## Ablauf

1. Knowledge Store, Brain-Root, `state.json` und letzten relevanten Event verifizieren.
2. Kanonische Inputs und externe Producer-/Source-Evidenz bestimmen.
3. Artefakte gemäß Artifact Gate routen; erzeugte Nicht-Code-Artefakte in Drive schreiben, read-back-verifizieren und registrieren.
4. Nur bei semantischer Zustandsänderung einen neuen Event erzeugen.
5. Wesentliche Entscheidungen über `decision-record` referenzieren.
6. `INDEX.md`, `TIMELINE.md`, `ASSETS.md` soweit vorhanden und `state.json` konsistent aktualisieren.
7. Knowledge-Promotion Gate ausführen.
8. Writes und Kern-Locators read-back-verifizieren.
9. Genau eine nächste Aktion und das Routingziel festhalten.
10. Drive-basierten `projectMemory`-Locator und verifizierte Stored-Artifact-Links an den nächsten Skill übergeben.

## Event-Modell

Event-IDs sind stabil und kollisionsarm, bevorzugt:

`EVT-YYYYMMDD-HHMMSS-<kurzer-slug>`

Beispiel:

```yaml
---
id: EVT-20260919-133000-spec-created
type: project-event
project: example-project
stage: specification
status: completed
date: 2026-09-19T13:30:00+02:00
source_skill: conversation-to-spec
brain_root_id: observed-provider-folder-id
memory_root_file_id: observed-provider-file-id
provider: google-drive
provider_revision: observed-revision-or-null
previous_event: EVT-...
inputs:
  - ../../requirements-handoff.json
outputs:
  - ../../SPEC.md
producer_evidence:
  - type: git-commit
    ref: observed-commit-sha
external_outputs:
  - asset_id: ASSET-004
    provider: google-drive
    object_id: observed-file-id
decisions:
  - ../decisions/DEC-004.md
tags:
  - project-memory
  - stage/specification
---
```

Der Event-Text enthält mindestens Kontext, Inputs, beobachtbares Ergebnis, bestätigte Entscheidungen/Annahmen, Evidenz, offene Schleifen, genau eine nächste Aktion und Links/Locators auf kanonische Quellen.

## Keine Chain-of-Thought-Persistenz

Nachvollziehbarkeit bedeutet **Entscheidungsrationale, Evidenz, Alternativen, Annahmen und Ergebnisse**, nicht das Speichern privater interner Gedankengänge.

Nicht persistieren:

- private Chain-of-Thought oder versteckte Scratchpads,
- Zugangsdaten, Tokens oder Secrets,
- unnötige personenbezogene Inhalte,
- vollständige Logs, wenn ein kleiner Evidenzausschnitt oder ein stabiler Link genügt,
- große Quellenkopien, die bereits kanonisch verfügbar sind.

## Umgang mit kanonischen Artefakten

Project Second Brain besitzt **keine zweite fachliche Wahrheit**.

- normative Spezifikationen bleiben beim vorgesehenen Producer/Workflow;
- Decision Records bleiben bei `decision-record`;
- Implementierungs- und Review-Evidenz bleibt bei Engineering-/Producer-Systemen;
- kontrollierte Records bleiben im kontrollierten Quellsystem;
- normale Dokumente, Präsentationen, Tabellen, Bilder, EPUBs, HTML und andere erzeugte Nicht-Code-Projektartefakte **müssen** im Drive Knowledge Store liegen;
- Software-Source, CI/CD, Docker/Compose, Migrationen, Schemas und deploybare Runtime-Artefakte bleiben in dedizierten Producer-Systemen.

Project Memory speichert Locators, Status, Provenance, Freshness und einen knappen verifizierten Abstract statt divergierender Kopien.

## Knowledge Store und Artifact Contract

Die allgemeine Drive-Storage-, Identitäts-, Read-back-, Release- und Rebind-Semantik liegt in `docs/KNOWLEDGE-STORE-CONTRACT.md`; die verpflichtende Artefaktablage und Link-first-Auslieferung in `docs/DRIVE-STORAGE-AND-DELIVERY-CONTRACT.md`.

Für Google Drive gelten zusätzlich die Detailregeln in `references/drive-artifact-contract.md`.

Kernregeln:

- genau ein kanonischer Brain-Root pro Project Memory;
- stabile Provider-IDs statt Namen als Identität;
- vorhandene Root-ID wiederverwenden statt über Namen neu zu erraten;
- bestehende Sharing-Rechte erhalten; keine implizite Freigabe;
- jeden relevanten Write read-back-verifizieren;
- `ASSETS.md` als menschenlesbares Asset-Register und `state.json` als maschinenlesbare Projektion führen;
- freigegebene/frozen Artefakte nicht still überschreiben;
- Provider-Ausfälle als `pending`/`unavailable` dokumentieren;
- bei Copy/Handoff Rebind durchführen, weil Provider-IDs sich ändern können.

## Decision Records

Wesentliche fachliche, technische, regulatorische, rechtliche, Sicherheits-, Architektur- oder Governance-Entscheidungen werden nicht als Fließtext im Event versteckt.

1. `decision-record` verwenden, wenn dessen Trigger erfüllt ist.
2. Decision Record im Project Memory verlinken.
3. Event nennt Decision-ID, Status und Konsequenz.
4. Supersession wird als neuer Decision Record plus neuer Event dokumentiert; alte akzeptierte Records werden nicht überschrieben.

## Producer- und Revisionsbezug

Wenn der Arbeitsschritt ein externes Producer-System betrifft, speichert der Event dessen bestmögliche stabile Evidenzidentität.

Beispiele:

- Git: Repository + fixierter Commit SHA + PR/Issue, soweit relevant;
- Google Drive: File/Folder ID + Revision/Freshness;
- controlled system: Record-/Submission-/CAPA-/Document-ID;
- Deployment: Release-/Image-/Deployment-ID.

Bewegliche Branches, Dateinamen oder Pfade allein sind keine unveränderliche Evidenz, wenn ein stabilerer Identifier verfügbar ist.

Die Historie des Project Memory wird append-/supersession-orientiert geführt; frühere Events werden nicht nachträglich glattgeschrieben.

## `INDEX.md`

Die Map of Content enthält mindestens:

- Projektziel und aktueller Status,
- Link auf `state.json`,
- Link auf `ASSETS.md`, wenn ein externer Artifact Store existiert,
- letzte 5 bis 10 Events,
- aktuelle normative Artefakte,
- akzeptierte Decisions,
- offene Schleifen,
- aktuellen nächsten Schritt,
- Links auf stage-bezogene Einstiegspunkte oder wichtige Wissensnotizen.

Sie ist eine **aktuelle Projektion**, keine unveränderliche Historie.

## `TIMELINE.md`

Chronologisch, append-orientiert. Beispielhafte Darstellung ohne auflösbare Repo-Links:

```text
- 2026-09-02 09:45 — EVT-...-grilling-closed -> events/EVT-...md — Requirements bestätigt; Routing zu Wayfinding.
- 2026-09-02 10:15 — EVT-...-spec-created -> events/EVT-...md — SPEC v1 erstellt; DEC-004 akzeptiert.
- 2026-09-10 12:00 — EVT-...-presentation-released -> events/EVT-...md — ASSET-004 in kanonischem Drive-Projektordner verifiziert und released.
```

In der tatsächlichen `TIMELINE.md` werden die vorhandenen Event-Dateien als relative Markdown-Links gesetzt.

Keine alten Ereignisse löschen, nur weil sie überholt sind. Stattdessen Folgeevent beziehungsweise Supersession verlinken.

## `ASSETS.md`

`ASSETS.md` wird materialisiert, sobald der erste externe Artifact Store oder externe nicht-textuelle Projektartefakt registriert wird. Die Datei enthält mindestens:

- Provider (`Google Drive`),
- beobachteten Link und die Folder-ID des kanonischen Projektordners,
- Zeitpunkt der letzten Verifikation,
- Asset-ID, Rolle, Dateiname, Drive-Link/-ID, Status, Producer, Event-Referenz und Verifikationsstand je Artefakt.

Das Register ist eine Projektion. Historische Beziehungen und Supersessions bleiben nachvollziehbar; veraltete Einträge werden nicht gelöscht, nur weil eine neue Version vorliegt.

## `state.json`

Für neue provider-neutrale Brains gilt bevorzugt Schema-Version 3:

```json
{
  "schemaVersion": 3,
  "projectId": "string",
  "knowledgeStore": {
    "provider": "google-drive",
    "storeId": "primary",
    "rootObjectId": "observed-brain-root-folder-id"
  },
  "memoryRoot": {
    "logicalPath": "docs/project-memory/INDEX.md",
    "objectId": "observed-memory-root-file-id"
  },
  "latestEvent": {
    "logicalPath": "docs/project-memory/events/EVT-....md",
    "objectId": "observed-event-file-id"
  },
  "currentStage": "grilling|wayfinding|research|specification|backlog|implementation|review|delivery|handoff|complete",
  "canonicalArtifacts": [
    {
      "type": "spec",
      "locator": {
        "provider": "google-drive",
        "objectId": "observed-file-id"
      },
      "status": "approved"
    }
  ],
  "externalArtifacts": [],
  "decisions": [],
  "openLoops": [],
  "lastVerified": {
    "providerRevision": "observed-revision-or-null",
    "at": "timestamp"
  },
  "nextAction": {
    "description": "...",
    "skill": "..."
  }
}
```

Bestehende v1/v2 Project Memories bleiben historische/kompatible Zustände und müssen nicht rückwirkend umgeschrieben werden. Bei einer bewussten Migration auf v3 werden Locators read-back-verifiziert.

`state.json` ist eine Projektion und darf aktualisiert werden. Event-Notes sind die historisch stabilen Einheiten.

## Event-Frequenz

Erzeuge einen Event insbesondere bei:

- Abschluss oder Wiederöffnung eines Grillings,
- abgeschlossenem Wayfinding/Research-Schritt mit neuer Evidenz,
- neuer oder erneut freigegebener SPEC,
- neuer, akzeptierter oder supersedierter wesentlicher Entscheidung,
- erzeugtem oder wesentlich neu geschnittenem Issue-Backlog,
- Beginn/Abschluss eines Engineering-Inkrements,
- Review-Entscheidung für einen fixierten SHA,
- Materialisierung oder Wechsel des kanonischen Drive-Artifact-Stores,
- Freigabe, Supersession oder wesentlicher Übergabe eines externen nicht-textuellen Artefakts,
- Merge-/Deployment-/Requirement-Closure,
- Handoff an neue Sitzung/Agenten,
- Meilenstein oder Projektabschluss.

Keine Event-Flut für reine Lesezugriffe, jeden einzelnen Working-File-Save oder wiederholte unveränderte Statuschecks.

## Handoff-Vertrag

Nachgelagerte Workflows erhalten einen provider-neutralen Locator:

```json
{
  "projectMemory": {
    "provider": "google-drive",
    "storeId": "primary",
    "brainRootObjectId": "observed-folder-id",
    "root": {
      "logicalPath": "docs/project-memory/INDEX.md",
      "objectId": "observed-file-id"
    },
    "state": {
      "logicalPath": "docs/project-memory/state.json",
      "objectId": "observed-file-id"
    },
    "latestEvent": {
      "logicalPath": "docs/project-memory/events/EVT-....md",
      "objectId": "observed-file-id"
    }
  }
}
```

Bei externen Assets wird zusätzlich der relevante Asset-Locator aus `ASSETS.md` übergeben.

Nachgelagerte Skills lösen zuerst die stabilen IDs auf, lesen `state.json` und den letzten relevanten Event und erzeugen keinen parallelen Brain-Root.

## Übergabe

Die Übergabe besteht mindestens aus dem `projectMemory`-Verweis, dem aktuellen Routingziel, den offenen Schleifen und genau einer nächsten Aktion. Der nachgelagerte Skill liest zuerst `state.json` und den letzten relevanten Event und folgt anschließend den verlinkten kanonischen Artefakten. Existiert ein Artifact Store, wird auch der `assetIndex`- und `artifactStore`-Verweis übergeben.

## Memory Path

Dieser Skill persistiert **Projekt- und Domänenwissen nicht über den persönlichen Memory Path**. Wiederverwendbares fachliches Wissen folgt `docs/KNOWLEDGE-PROMOTION-CONTRACT.md` und bleibt beim kanonischen Project/Domain Brain. Nur user-spezifische stabile Präferenzen, Fakten oder Constraints dürfen als `memory-candidate-handoff-v1` an `communication-memory-governance` gehen. Transienter Projektstatus, Connector-Payloads, Secrets und sensible Inhalte bleiben run-only. Jede fachliche Promotion benötigt Provenance; volatile Claims zusätzlich Freshness-Metadaten. Persistenz darf nur nach verifiziertem Ziel-Write behauptet werden.

## Prüfungen

Vor jedem Handoff prüfen:

- Brain-Root, Memory-Root und `latestEvent` sind eindeutig und erreichbar;
- Provider-/Source-IDs wurden beobachtet und nicht erfunden;
- der neue Event beschreibt eine echte semantische Zustandsänderung;
- referenzierte kanonische Artefakte existieren oder sind ausdrücklich `pending`;
- externe Producer-Evidenz nutzt stabile Identitäten, soweit verfügbar;
- `INDEX.md`, `TIMELINE.md`, `ASSETS.md` und `state.json` widersprechen dem Event nicht;
- historische Events wurden nicht still umgeschrieben;
- genau eine nächste Aktion ist benannt;
- keine private Chain-of-Thought, Secrets oder unnötige sensible Inhalte wurden persistiert;
- ein Software-/Runtime-Artefakt wurde nicht fälschlich zum Brain-eigenen Producer-Artefakt gemacht.

## Fehlerbehandlung

Stoppe beziehungsweise korrigiere, wenn:

- kanonische Artefakte in divergierenden Kopien dupliziert werden;
- historische Events still umgeschrieben werden;
- `pending` externe Zustände als abgeschlossen dokumentiert werden;
- Namen/Pfade statt verfügbarer stabiler IDs als einzige Identität verwendet werden;
- Provider-IDs, Revisionen oder URLs ohne Verifikation erfunden werden;
- ein paralleler Brain-Root neben einem kanonischen Root angelegt wird;
- Software-/Build-/Runtime-Artefakte in den Brain verschoben werden, obwohl ein Producer-System ihr kanonischer Owner ist;
- freigegebene/frozen Artefakte still überschrieben werden;
- Secrets oder private Chain-of-Thought gespeichert werden;
- bei einer kopierten Third-Party-Instanz kein Rebind der Provider-IDs erfolgt;
- ein Handoff erfolgt, obwohl der vorherige wesentliche Schritt noch nicht im Projektgraph verankert ist.

## Abschlusskriterien

Der Skill ist erfüllt, wenn:

- das Projekt ab dem Grilling genau einen kanonischen, verifizierten Project-Memory-Root in einem gültigen Knowledge Store besitzt;
- die maschinenlesbaren Kernartefakte provider-portabel bleiben;
- jeder wesentliche Workflow-Übergang durch einen verlinkten Event nachvollziehbar ist;
- Entscheidungen und Evidenz auf kanonische Sources of Truth zeigen;
- normale Projektassets im kanonischen Knowledge Store oder einer anderen verifizierten autoritativen Quelle liegen;
- Software-/Build-/Runtime-Artefakte bei ihren Producer-Systemen verbleiben;
- `INDEX.md`, `TIMELINE.md`, `ASSETS.md` soweit vorhanden und `state.json` konsistent sind;
- keine private Chain-of-Thought oder unnötige sensible Information persistiert wurde;
- ein neuer Agent oder Nutzer den aktuellen Projektstand, die kanonischen Locators und genau den nächsten Schritt ohne erneute Vollanalyse rekonstruieren kann.
