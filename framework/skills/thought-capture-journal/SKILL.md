---
name: thought-capture-journal
description: Normalisiert fortlaufend aufgezeichnete, unstrukturierte Gedanken aus einer einzelnen datierten Markdown- oder Textdatei zu einem nachvollziehbaren Thought Journal. Verwenden, wenn Ideen per Smartphone, Diktat oder Quick-Note gesammelt und anschließend für Graphanalyse vorbereitet werden sollen; der Skill interpretiert noch keine Beziehungen zwischen Gedanken.
userFacing: true
implicitInvocation: true
category: productivity
version: 0.3.0
status: candidate
owners:
  - White Label Maintainer
requires: []
outputs:
  - thought-journal.md
  - thought-journal.json
lastEvaluated: 2026-09-20
---

# Thought Capture Journal

## Zweck

Überführe eine pragmatische, fortlaufende Gedankensammlung in ein stabiles Importformat. Die Erfassung soll auf dem Smartphone möglichst reibungsarm sein und darf zunächst bewusst unstrukturiert bleiben.

## Empfohlener Capture-Workflow

### iPhone / iOS: Apple Kurzbefehle als Standard

Für iPhone ist **Apple Kurzbefehle + iOS-Diktat + eine einzelne Markdown-Datei in iCloud Drive** der Standardvorschlag. Die Lösung benötigt keine zusätzliche kostenpflichtige App, kann per Siri, Home-Screen, Widget, Kontrollzentrum oder Aktionstaste gestartet werden und schreibt jeden gesprochenen Gedanken direkt mit Zeitstempel an dieselbe Datei an.

### Capture-Modi

**Staging (Standard bei read-only Obsidian):** Wenn Obsidian nur als Viewer/Projektion verwendet wird, schreibt der Kurzbefehl nicht in den Vault, sondern in eine neutrale Capture-Zone, bevorzugt:

`iCloud Drive/Shortcuts/SecondBrain Capture/Thought Journal.md`

Diese Datei ist die rohe Capture-Quelle. Sie ist noch kein Second Brain und kein kanonisches Wissensartefakt.

**Writable Vault (Opt-in):** Nur wenn der Obsidian-Vault ausdrücklich als schreibbare Arbeitsfläche vorgesehen ist, darf direkt nach

`iCloud Drive/Obsidian/<Vault>/00 Inbox/Thought Journal.md`

geschrieben werden. Ein read-only Vault oder eine aus kanonischen Brains erzeugte Obsidian-Projektion darf niemals als Capture-Ziel verwendet werden.

Alternativ kann die Datei außerhalb eines Vaults als normale `Thought Journal.md` oder `thoughts.md` in iCloud Drive liegen und später importiert werden.

Empfohlener Kurzbefehl **Gedanke festhalten**:

1. Aktion `Text diktieren` bzw. Spracheingabe für den neuen Gedanken verwenden.
2. Spezialvariable `Aktuelles Datum` abrufen.
3. Mit `Datum formatieren` das benutzerdefinierte Format `yyyy-MM-dd HH:mm` erzeugen.
4. Einen Textblock bilden:

```markdown

## <formatiertes Datum>
<diktierten Text>
```

5. Diesen Text mit einer Datei-Aktion an `Thought Journal.md` **anhängen**, nicht die Datei ersetzen.
6. Optional eine explizite Capture-ID mitschreiben. Fehlt sie, erzeugt der Normalisierungsschritt eine stabile Entry-ID und bewahrt die Source-Referenz.
7. Optional eine kurze Bestätigung anzeigen; keine semantische Struktur, Tags, Projekte oder Brain-Ziele während des Diktats erzwingen.

Der Capture-Pfad muss offline funktionieren und darf weder LLM, Repository-Zugriff, Workflow-Automation noch einen erreichbaren Second-Brain-Dienst voraussetzen. Direkter Schreibzugriff in einen Obsidian-Vault ist nur im Modus `writable-vault` zulässig; bei `staging` bleibt Obsidian nachgelagerte Projektion.

### Android: Markor QuickNote

Für Android ist **Markor QuickNote** der Standardvorschlag: QuickNote ist eine frei wählbare einzelne Markdown-Datei, Markor ist freie Open-Source-Software, arbeitet offline und bietet eine Date/Time-Aktion. Diktat erfolgt pragmatisch über die Spracheingabe der installierten Android-Tastatur, z. B. Gboard.

### Plattformneutrale Fallback-Regel

Wenn die Standardlösung nicht verfügbar oder nicht gewünscht ist, ist jede App zulässig, die eine einzelne exportierbare UTF-8-Text-/Markdown-Datei ohne proprietären Lock-in erzeugt. Proprietäre Notizdatenbanken, aus denen jeder Gedanke erst separat exportiert werden muss, sind zweite Wahl.

Empfohlenes Minimalformat:

```markdown
## 2026-08-23 22:17
Gedanke frei diktiert oder geschrieben.

## 2026-08-24 07:42
Nächster Gedanke. Darf fragmentarisch sein.
```

Akzeptiere auch Zeilenpräfixe wie `2026-08-23T22:17`, lokale Datumsformate oder undatierte Blöcke. Undatierte Einträge werden markiert, nicht erfunden.

## Eingaben

- eine einzelne `.md`- oder `.txt`-Datei oder deren vollständiger Inhalt,
- optional Zeitzone und Sprache,
- optional bekannte Projekt-/Themenbezeichnung,
- optional `captureMode: staging|writable-vault`; bei read-only Obsidian ist `staging` der Standard.

## Workflow

1. Datei unverändert als Quelle inventarisieren.
2. Einträge anhand vorhandener Zeitstempel, Überschriften, Leerzeilen oder eindeutiger Trenner segmentieren.
3. Eine vorhandene explizite Capture-ID erhalten; andernfalls jedem Eintrag eine stabile ID geben, z. B. `thought-20260823-2217-001`. Wiederholtes Einlesen derselben unveränderten Quelle darf keine neue Identität erzeugen.
4. Originaltext unverändert erhalten und zusätzlich eine vorsichtig bereinigte Fassung erzeugen.
5. Offensichtliche ASR-/Diktatfehler nur korrigieren, wenn die beabsichtigte Form eindeutig ist; sonst als Unsicherheit markieren.
6. Sprache, Timestamp, Quelle und optionale Tags als Metadaten speichern.
7. Keine Themencluster, Kausalitäten oder Prioritäten erfinden; diese gehören in `thought-graph-extractor`.

## JSON-Vertrag

```json
{
  "schemaVersion": 1,
  "source": {"type": "single-file-journal", "path": "Thought Journal.md", "captureMode": "staging"},
  "entries": [
    {
      "id": "thought-20260823-2217-001",
      "timestamp": "2026-08-23T22:17:00+02:00",
      "timestampStatus": "explicit",
      "raw": "...",
      "normalized": "...",
      "language": "de",
      "uncertainties": []
    }
  ]
}
```

## Qualitätsregeln

- Rohtext nie überschreiben.
- Capture-Automationen müssen neue Einträge anhängen und dürfen bestehende Journal-Inhalte nicht ersetzen.
- `staging` und `writable-vault` sind Storage-Modi, keine fachliche Semantik; Obsidian-Ordner oder Dateinamen bestimmen niemals das spätere Brain-Routing.
- Bei read-only Obsidian darf die Capture-Automation nicht in die Projektion schreiben.
- Zeitstempel nie aus Dateireihenfolge erfinden.
- Diktatfehler nicht kreativ umdeuten.
- Ein Gedanke darf mehrere Sätze enthalten; nicht mechanisch pro Satz splitten.
- Persönliche oder vertrauliche Inhalte nicht an externe Dienste senden, sofern der Nutzer dies nicht ausdrücklich erlaubt.

## Abschluss

Der Skill endet, wenn alle erfassbaren Einträge stabil segmentiert, datiert oder als undatiert markiert und menschen- wie maschinenlesbar übergeben werden können. Für reine Ideengraphen ist `thought-graph-extractor` der nächste Schritt; für die Überführung in föderierte Second Brains ist `voice-capture-to-second-brain-workflow` der bevorzugte Orchestrator.
