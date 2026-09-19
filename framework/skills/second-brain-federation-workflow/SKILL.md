---
name: second-brain-federation-workflow
description: Verbindet mehrere Project und Collection Second Brains provider-neutral mit einem privaten Super Second Brain als verifizierten Registry-, Routing- und Discoverability-Layer. Prüft Knowledge-Store-Verfügbarkeit und Freshness, registriert nur stabile Locators und Metadaten statt fachliche Inhalte zu duplizieren und konsolidiert überlappende Brains auf eine eindeutige Source of Truth.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.4.0
status: candidate
owners:
  - White Label Maintainer
requires:
  - project-second-brain
consumes:
  - project-memory-index.md
  - project-memory-state.json
  - project-memory-event.md
outputs:
  - super-second-brain-registry.json
  - second-brain-catalog.md
  - second-brain-registration.json
lastEvaluated: 2026-09-19
---

# Second Brain Federation Workflow

## Zweck

Dieser Workflow verbindet mehrere eigenständige `project-second-brain`-Instanzen mit einem **Super Second Brain**. Das Super Second Brain ist kein weiterer fachlicher Speicher und keine Kopie der Child Brains. Es ist ein privater, versionierter **Index-, Routing- und Discoverability-Layer**.

Seine Kernfrage lautet:

**Welcher Second Brain besitzt den relevanten Kontext, ist er erreichbar und wo befindet sich sein aktueller kanonischer Einstiegspunkt?**

Die fachliche Wahrheit bleibt immer im jeweiligen Child Brain und dessen kanonischen Producer-Artefakten.

## Trigger

Verwenden:

- wenn ein neuer Project Second Brain oder Collection Brain angelegt wurde,
- wenn ein bestehender Second Brain umbenannt, verschoben, archiviert, superseded oder wieder aktiviert wurde,
- wenn zwei oder mehr Brains fachlich überlappen und eine eindeutige Source of Truth hergestellt werden muss,
- wenn Workflow-Familien oder Scope eines Second Brains wesentlich geändert wurden,
- wenn der Nutzer eine Gesamtsicht, einen globalen Einstieg oder ein Routing über mehrere Second Brains verlangt,
- für einen expliziten Refresh der Verfügbarkeit oder Freshness registrierter Brains,
- beim Bootstrap eines Super Second Brains aus bereits vorhandenen Child Brains,\n- wenn das Knowledge-Promotion Gate für projektübergreifendes Wissen einen kanonischen Eigentümer auflösen muss,\n- wenn ein lokaler oder föderierter Second-Brain-Lint Ownership-, Routing- oder SSOT-Probleme findet.

Nicht bei jedem einzelnen Project-Memory-Event einen Cross-Brain-Write erzwingen. Normale fachliche Ereignisse bleiben lokal. Der Federation State wird bei strukturellen Änderungen, Handoffs, expliziten Refreshes oder bewusst gewählten Meilensteinen aktualisiert.

## Architektur

```text
                         Super Second Brain
                    registry / routing / index
                               |
          +--------------------+--------------------+
          |                    |                    |
          v                    v                    v
   Project Second Brain   Collection Brain    Project Second Brain
      project A            domain / matters       project B
          |                    |                    |
          v                    v                    v
 canonical sources        child memories      canonical sources
```

### Child Brain

Ein Child Brain bleibt autonome Source of Truth für seinen Scope:

- Projekt-/Domainzustand,
- Decisions,
- Timeline und Events,
- fachliche Evidence/Synthesis,
- Asset-/Producer-Referenzen,
- lokale nächste Aktionen.

### Super Brain

Das Super Brain besitzt ausschließlich:

- Registry der bekannten Second Brains;
- verifizierte Knowledge-Store- und Memory-Root-Locators;
- Scope und Workflow-Familien;
- Availability/Freshness;
- kurze nicht-sensitive Routing-Zusammenfassungen;
- Federation Events wie Register, Move, Archive, Reactivate, Supersede, Rebind oder Refresh;
- Relationen zum kanonischen Child Brain.

Es besitzt **keine Kopie** der fachlichen Child-Inhalte.

Der Storage-Provider wird durch `docs/KNOWLEDGE-STORE-CONTRACT.md` abstrahiert. Im White-Label-Default ist Google Drive der Provider.

## Private-by-default Gate

Ein Super Second Brain aggregiert Metadaten über mehrere Lebens- und Arbeitsbereiche. Bereits Existenz oder Benennung einzelner Child Brains kann sensibel sein.

Daher gilt:

1. Der kanonische Super-Brain-Store ist standardmäßig **privat**.
2. Eine reale Registry mit privaten Folder-/File-/Repository-IDs wird nicht in ein weniger geschütztes Framework oder Release kopiert.
3. Öffentliche/portable Skills enthalten nur Schema, Workflow und neutrale Beispiele.
4. Child-Brain-Sichtbarkeit wird beobachtet und dokumentiert, nicht erraten.
5. Inhalte eines privaten Child Brains werden niemals in eine weniger geschützte Ebene kopiert.
6. Third-Party-Copies beginnen mit leerer Registry, sofern keine separate Trusted Migration autorisiert wurde.

Wenn kein ausreichend geschützter Super-Brain-Store verfügbar ist, bleibt Federation `pending`.

## Super-Brain-Struktur

Empfohlene logische Struktur:

```text
README.md
docs/super-memory/
├── INDEX.md
├── REGISTRY.md
├── registry.json
├── state.json
├── brains/
│   ├── <brain-id>.md
│   └── ...
├── domains/
│   └── <domain>.md
└── events/
    └── FED-YYYYMMDD-HHMMSS-<slug>.md
```

- `INDEX.md` ist der globale Einstieg für Mensch und Agent.
- `REGISTRY.md` ist die lesbare Registry-Projektion.
- `registry.json` ist die maschinenlesbare Source of Truth der Federation.
- `state.json` hält Sync, offene Probleme und nächste Federation-Aktion.
- `brains/` enthält pro Child Brain eine Routing-Note.
- `domains/` gruppiert Brains optional nach Domäne/Workflow-Familie.
- `events/` dokumentiert strukturelle Federation-Änderungen append-orientiert.

Im Google-Drive-Adapter ist die Super-Brain-Root-Folder-ID die kanonische Speicheridentität. Der logische Pfad bleibt provider-portabel.

## Child-Brain-Modi

### `project`

Ein Brain repräsentiert primär ein langlebiges Projekt. Standard-Memory-Root:

```text
docs/project-memory/INDEX.md
```

### `collection`

Ein Brain repräsentiert eine Domäne mit mehreren Matters/Projekten. Der Domain-Level-Root darf weiterhin unter `docs/project-memory/` liegen; einzelne langlebige Cases liegen bevorzugt unter:

```text
projects/<project-or-matter-id>/docs/project-memory/
```

Das Super Brain registriert den Collection Brain als Einheit und darf aktive Child Roots referenzieren. Es kopiert deren Inhalt nicht.

Die physische Ablage kann ein Drive-Ordner, Repository oder anderer gültiger Knowledge Store sein.

## Canonical-Ownership- und SSOT-Regel

Wenn mehrere Brains ähnliche Inhalte besitzen, darf die Federation nicht dauerhaft mehrere gleichrangige Wahrheiten erzeugen. Vor einer Konsolidierung werden Inhalte nach Eigentümertyp klassifiziert:

| Inhalt | Kanonischer Eigentümer |
|---|---|
| generisches, wiederverwendbares Domänenwissen | zuständiger Domain-/Collection-Brain |
| konkreter Projekt-, Firmen-, Personen- oder Matter-Zustand | spezifischer Project/Collection Brain |
| ausführbare Methode, Gate, Schema, Evaluation, Routinglogik | Skill-/Workflow-Framework |
| ausführbares Softwareprojekt: Source Code, Tests, CI/CD, Docker/Compose, Migrationen, Schemas, deploybare Services/Apps | eigenes nicht-Brain Producer-System/Repository |
| kontrollierter Record, Submission, CAPA, Complaint, Vertragsoriginal, Evidence Record | kontrolliertes Quellsystem / Producer |
| volatile externe Fakten | autoritative Quelle; im Brain nur mit Provenance/Freshness |

## Software-Producer-Grenze

Second Brains sind Wissens-, Zustands- und Routing-Speicher, keine Software-Producer.

Für jedes Programmierprojekt gilt:

1. Das Projekt besitzt ein dediziertes Producer-System, typischerweise ein Source-Control-Repository.
2. Source Code, Tests, CI/CD, Docker/Compose, Migrationen, Schemas, deploybare Services/Apps und Release-Artefakte leben dort.
3. Der relevante Brain speichert nur verifizierte Producer-Locators, Architektur-/Decision-Zusammenfassung, Projektzustand, Evidence-Links und Learnings.
4. Fehlt ein geeigneter Producer, darf ausführbare Implementierung nicht ersatzweise im Brain abgelegt werden.
5. Wird ausführbare Implementierung in einem Brain gefunden, ist das ein Ownership-Finding.
6. Producer-Systeme werden nicht allein wegen ihrer Existenz als Child Brains registriert.

Der Super Brain darf Producer-Systeme als Relations-/Routing-Metadaten referenzieren, ohne sie zu Child Brains zu erklären.

### Konsolidierungsablauf

### Konsolidierungsablauf

1. Überlappung identifizieren und die Ownership-Kategorien explizit trennen.
2. Einen aktiven kanonischen Brain für jede Wissensklasse bestimmen.
3. Generische wiederverwendbare Learnings nur in den kanonischen Domain-Brain übernehmen; konkrete Projekt-/Firmenfakten bleiben im spezifischen Brain.
4. Dubletten in anderen Brains nach Möglichkeit durch Links/Relations ersetzen statt sie parallel weiterzupflegen.
5. Einen abgelösten Brain nicht still löschen: historische Events/Provenance erhalten, Status als `superseded`/`archived` markieren und auf den Nachfolger verweisen.
6. Die aktive Registry darf nur das aktuelle Routingziel enthalten; historische Alias-/Redirect-Notizen dürfen außerhalb der aktiven Registry bestehen bleiben.
7. Domain Maps, Human Registry, machine registry, state und Federation Event konsistent aktualisieren.
8. Read-back prüfen, dass es für dieselbe Wissensklasse kein zweites aktives gleichrangiges Routingziel mehr gibt.

### Regulated-Knowledge-Freshness

Bei regulatorischen, rechtlichen, normativen oder sonst volatilen Wissensdomänen gilt zusätzlich:

- aktuelle externe Anforderungen werden nicht aus Chat-/Memory-Zusammenfassungen als Autorität übernommen,
- Provenance, `asOf` und bei Bedarf `reviewAfter`/`expiresAt` dokumentieren,
- explizite Anforderung, Interpretation, internes Requirement und Evidence voneinander trennen,
- kontrollierte Records nicht in den Second Brain kopieren; nur verifizierte Referenzen, Decisions und generalisierte Learnings persistieren.

## Registry Contract

Neue provider-neutrale Registry-Einträge verwenden bevorzugt Schema-Version 2:

```json
{
  "brainId": "stable-brain-id",
  "label": "Human-readable label",
  "mode": "project",
  "scope": "short routing scope",
  "knowledgeStore": {
    "provider": "google-drive",
    "storeId": "primary",
    "rootObjectId": "observed-brain-root-folder-id"
  },
  "projectMemoryRoot": {
    "logicalPath": "docs/project-memory/INDEX.md",
    "objectId": "observed-memory-root-file-id"
  },
  "status": "available",
  "workflowFamilies": ["example-workflow"],
  "tags": ["example-domain"],
  "lastVerifiedAt": "observed timestamp",
  "latestEventRef": null
}
```

Zulässige `status`-Werte:

- `available` – Brain-Root und deklarierter Memory-Root wurden verifiziert;
- `bootstrap-needed` – Brain-Root existiert, Memory-Struktur fehlt;
- `pending` – konfiguriert, aber nicht vollständig prüfbar;
- `unavailable` – zuvor bekanntes Ziel ist aktuell nicht erreichbar;
- `archived` – bewusst historisiert;
- `rebind-required` – kopierte Instanz besitzt noch keine gültigen recipient-owned Locators;
- `integrity-failed` – Rebind/Release-Integrität konnte nicht bestätigt werden.

Ein superseded Brain wird aus dem aktiven Routing entfernt und historisch referenziert.

Knowledge-Store-Verfügbarkeit und Memory-Root-Verfügbarkeit werden getrennt behandelt.

Legacy Registry-Einträge mit Repository-Feldern bleiben lesbar, sollen bei bewusster Migration aber in Knowledge-Store-Locators überführt werden.

## Initial Bootstrap

Wenn ein Super Second Brain erstmals angelegt wird:

1. Super-Brain-Knowledge-Store und Root verifizieren.
2. Kandidatenliste bereits bekannter Second Brains bestimmen.
3. Jeden Brain auf Root-Zugriff, Schutzstatus und Project-Memory-Root prüfen.
4. `mode`, `scope`, `workflowFamilies` und Tags aus bestätigtem Kontext bestimmen.
5. stabile Provider-/Source-Locators erfassen; Namen/Pfade nicht als alleinige Identität verwenden.
6. Routing-Notes erzeugen.
7. Ownership-Überlappungen vor Registrierung auflösen.
8. `registry.json`, `REGISTRY.md`, `INDEX.md` und `state.json` konsistent erzeugen.
9. Federation-Bootstrap-Event schreiben.
10. alle Writes read-back-verifizieren.

Der Bootstrap ist erst abgeschlossen, wenn kein Kandidat still verloren ging und keine erkannte Wissensklasse zwei gleichrangige aktive Sources of Truth besitzt.

Bei einem Third-Party-Starter ist die Kandidatenliste initial leer. Erst nach erfolgreichem Claim/Rebind werden recipient-owned Child Brains registriert.

## Federation Sync

### 1. Child identifizieren

Nutze stabile `brainId` plus zuletzt verifizierte Knowledge-Store-Locators. Namen allein reichen bei Rename, Move, Copy oder Migration nicht.

### 2. Availability prüfen

Verifiziere mindestens:

- Brain-Root erreichbar;
- beobachteter Schutz-/Sharing-Status;
- deklarierter Project-Memory-Root;
- Provider-/Source-IDs;
- soweit verfügbar letzter Child-Event/State;
- bei kopierten Instanzen Rebind-Status.

### 3. Delta bestimmen

Klassifiziere:

- neu;
- unverändert;
- metadata-changed;
- moved/renamed;
- copied/rebind-required;
- superseded;
- bootstrap-needed;
- unavailable;
- archived/reactivated;
- integrity-failed.

### 4. Registry aktualisieren

Nur Federation-Metadaten ändern. Keine fachlichen Child-Artefakte spiegeln.

### 5. Federation Event schreiben

Event erforderlich bei Register, Move/Rename, Rebind, Scope-Änderung, Supersede, Archive/Reactivate, Availability-/Integrity-Transition oder strukturellem Bootstrap.

### 6. Read-back

Nach Writes Registry, State und betroffene Routing-Notes erneut lesen. Keine erfolgreiche Synchronisierung behaupten, wenn der Zielzustand nicht beobachtet wurde.

## Routing

Wenn ein Auftrag Kontext aus einem Second Brain benötigt:

1. Super Registry lesen.
2. Kandidaten anhand `scope`, `workflowFamilies`, Tags und Status auswählen.
3. Nur `available` oder bewusst akzeptierte `bootstrap-needed` Kandidaten routen.
4. Bei mehreren plausiblen Brains deren Scope und Ownership-Grenzen vergleichen; keine Inhalte raten.
5. kanonischen Child Root lesen.
6. ab dort normalen `project-second-brain`- und Fachworkflow verwenden.

Das Super Brain beantwortet keine fachliche Frage aus seinem eigenen Kurzabstract, wenn der Child Brain erreichbar ist.

## Promotion Routing

Für Query Promotion gilt der framework-weite `docs/KNOWLEDGE-PROMOTION-CONTRACT.md`.

Federation entscheidet bei projektübergreifenden Kandidaten ausschließlich **wohin** promotet werden darf:

1. Wissensklasse bestimmen.
2. Registry/Domain Maps nach dem aktiven kanonischen Eigentümer durchsuchen.
3. Bei genau einem passenden verfügbaren Owner dorthin routen.
4. Bei mehreren gleichrangigen Kandidaten zuerst Ownership reconciliieren; nicht parallel schreiben.
5. Bei fehlendem/verifiziert nicht schreibbarem Ziel `blocked-no-target` zurückgeben.
6. Fachinhalt im Child Brain persistieren und read-back-verifizieren; der Super Brain erhält nur dann ein Update, wenn sich Routing/Scope/Availability dadurch strukturell ändert.

Der Super Brain selbst ist **kein Promotion-Ziel für fachliche Inhalte**.

## Second-Brain Lint

Der normative Prüfvertrag liegt in `docs/SECOND-BRAIN-LINT-CONTRACT.md`.

Federation-Lint prüft insbesondere:

- doppelte aktive kanonische Owner,
- Writes in superseded/archivierte Brains,
- nicht erreichbare registrierte Roots,
- Scope-/Tag-/Workflow-Family-Drift,
- fehlende erwartete Routingziele,
- Cross-Brain-Dubletten statt Links auf den Owner,
- Privacy-Regressions,
- fachliche Inhalte, die fälschlich im Super Brain gelandet sind,
- ausführbarer Projektcode oder Deployment-/Runtime-Artefakte, die fälschlich in irgendeinem Second Brain statt im eigenen Producer-Repository liegen.

Ein Finding darf nur dann automatisch korrigiert werden, wenn Ownership und Evidenz eindeutig sind und der Zielzustand read-back-verifiziert werden kann. Andernfalls bleibt es ein expliziter Reconciliation-Bedarf.

## Cross-Brain-Verknüpfungen

Verbindungen zwischen Projekten werden im Super Brain als **Relationen**, nicht als zusammenkopierte Inhalte, dokumentiert. Beispiele:

- `supports`,
- `depends-on`,
- `shares-evidence-with`,
- `supersedes`,
- `related-domain`,
- `derived-from`.

Jede Relation nennt beide `brainId`-Werte und einen kurzen, nicht-sensitiven Grund. Bei fachlich sensitiver Relation genügt ein neutraler Relationstyp ohne Detailtext.

## Failure Handling

- **Super Brain fehlt:** Bootstrap-Manifest vorbereiten, Federation `pending`; Child Brains funktionieren unabhängig weiter.
- **Brain-Root existiert, Memory fehlt:** `bootstrap-needed`.
- **Child vorübergehend nicht erreichbar:** letzten Registry-Eintrag behalten, `unavailable` und Freshness markieren.
- **Rename/Move:** stabile `brainId` und Provider-ID beibehalten, lesbare Pfade aktualisieren.
- **Copy/Transfer:** `rebind-required`; alte Provider-IDs nicht als recipient-owned behandeln.
- **Integrity mismatch:** `integrity-failed`; keine automatische Aktivierung.
- **Ownership-Überlappung:** keine parallelen aktiven Sources of Truth fortschreiben.
- **Supersession:** Provenance erhalten, Routing auf Nachfolger umstellen.
- **Privacy-Konflikt:** keinen Inhalt in weniger geschützte Ebene kopieren.
- **Widersprüchliche Registry-Daten:** Reconciliation statt stilles Überschreiben.
- **Software ohne Producer-System:** Implementierung nicht im Brain ablegen; geeigneten Producer auflösen/anlegen.

## Handoff

Nach erfolgreicher Federation kann ein provider-neutraler Handoff enthalten:

```json
{
  "superSecondBrain": {
    "provider": "google-drive",
    "storeId": "primary",
    "rootObjectId": "observed-super-root-folder-id",
    "indexObjectId": "observed-index-file-id",
    "registryObjectId": "observed-registry-file-id",
    "stateObjectId": "observed-state-file-id",
    "lastVerifiedAt": "observed timestamp"
  },
  "projectMemory": {
    "brainId": "stable-brain-id",
    "rootObjectId": "observed-child-root-folder-id",
    "memoryRootObjectId": "observed-memory-root-file-id"
  }
}
```

Alle Werte müssen beobachtet oder aus der kanonischen Registry gelesen sein.

Bei Third-Party-Deployment ist ein Handoff erst gültig, wenn Claim/Rebind abgeschlossen ist und keine source-owner Provider-ID als Runtime-Abhängigkeit verbleibt.

## Memory Path

Federation persistiert keine fachlichen Inhalte und nutzt den persönlichen Memory Path nicht als Ersatz für Child-Brain-Wissen. User-spezifische stabile Präferenzen/Fakten/Constraints können separat an `communication-memory-governance` gehen. Domain-/Projektwissen folgt dem Knowledge Promotion Contract in den kanonischen Child Brain. Registry-, Availability- und Routingzustände bleiben Federation-State und werden nicht als persönliche Memory-Fakten behandelt.

## Abschlusskriterien

Der Workflow ist abgeschlossen, wenn:

- der Super-Brain-Knowledge-Store geschützt und erreichbar ist oder explizit `pending` bleibt;
- alle bekannten Child-Brain-Kandidaten klassifiziert wurden;
- jeder registrierte Brain stabile `brainId`, Scope, Modus und verifizierte Knowledge-Store-Locators besitzt;
- keine fachliche Wahrheit aus Child Brains dupliziert wurde;
- für erkannte Überlappungen eindeutige kanonische Ownership festgelegt ist;
- superseded Brains nicht mehr aktive Routingziele sind, ihre Historie aber erhalten bleibt;
- private Provider-IDs und Registry-Daten nicht in weniger geschützte Framework-/Release-Artefakte gelangen;
- Registry, Human Index, Domain Maps und Routing-Notes konsistent und read-back-verifiziert sind;
- ein Agent deterministisch vom Super Brain zum kanonischen Child Brain routen kann;
- eine kopierte Third-Party-Instanz vollständig rebound ist, bevor sie als `available` gilt;
- kein Second Brain ausführbaren Projektcode, CI/CD, Docker/Compose, Migrationen, Schemas oder deploybare Software als eigenen Producer-Inhalt führt.
