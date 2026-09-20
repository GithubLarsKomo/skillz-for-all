---
name: structured-regatta-results-extraction
description: Extrahiert große Regatta-Ergebnisbestände aus verteilten Web- und PDF-Quellen in eine validierte Athleten-CSV. Verwenden, wenn Ergebnisportale Platz/Zeit/Status getrennt von offiziellen Startlisten oder Ergebnis-PDFs bereitstellen und Crewlisten, Jahrgänge, Vereine sowie DNS/DNF/DSQ/EXC belastbar zusammengeführt werden müssen.
userFacing: true
implicitInvocation: false
category: research-knowledge
version: 1.0.0
status: candidate
owners:
  - White Label Maintainer
requires: []
outputs:
  - validated athlete-level CSV
  - extraction exceptions list
lastEvaluated: 2026-09-15
---

# Strukturierte Regatta-Ergebnisextraktion

Erzeuge aus großen Regatta-Webbeständen eine zeilenweise, nachvollziehbare Athleten-Tabelle. Behandle unterschiedliche Quellen nach ihrer nachgewiesenen Stärke und vermische ihre Rollen nicht.

## Quellenrollen

Verwende bevorzugt drei Ebenen:

1. **Ergebnisportal / Aggregator** für Eventstruktur, Finals, Startnummer, Platzierung und Finish-Zeit. Wenn RegattaCentral vorhanden ist, eignet sich die Eventseite häufig für einen kompletten Eventabruf.
2. **Offizielle Detail-Startliste** für Crewmitglieder, Geburtsjahre, Länder und vollständige Vereins-/Composite-Angaben. Ziehe möglichst eine Tages- oder Blockliste statt hunderter Einzel-PDFs.
3. **Offizielles Einzel-Ergebnis-PDF** als Konflikt- und Statusquelle bei beschädigten Tabellenzeilen, Seitenumbrüchen, verschmolzenen Crews oder unklaren `-`-Werten.

Firecrawl kann dabei URL-Verzeichnisse, HTML-Ergebnisse und PDF-Text erschließen. Nutze Crawl nur bei kleinen, klar begrenzten Mengen; bei Rate-Limits auf Map/Verzeichnisliste + gezielte Scrapes wechseln.

## Datenmodell

Eine Zeile entspricht einem startberechtigten Athleten, nicht einem Boot. Empfohlene Spalten:

- Kategorie (z. B. MM, MW, MM/MW)
- Bootsklasse
- Altersklasse
- kombinierte Kategorie-Boot-Alter-Kennung
- Eventnummer und Rennbezeichnung
- Rennnummer und Final-/Heat-Bezeichnung
- Start-/Bugnummer
- Platzierung
- Finish-Zeit
- Sportlername
- Geburtsjahr
- Alter im Veranstaltungsjahr
- Land
- Verein bzw. vollständige Composite-Vereinsangabe
- Status

Coxswains nur aufnehmen, wenn der Auftrag dies ausdrücklich verlangt. Bei einer Athletenanalyse der Ruderer standardmäßig ausschließen und die Regel dokumentieren.

## Vorgehen

### 1. Vollständigen Scope feststellen

- Ermittle alle Events, Rennen/Finals und offiziellen Ergebnisdateien.
- Prüfe Nummernlücken separat; eine fehlende PDF-Nummer ist nicht automatisch ein fehlendes Rennen.
- Bestimme Event-ID-Mappings des Ergebnisportals einmal zentral.

### 2. Ergebnisse eventweise abrufen

Rufe pro Event möglichst eine vollständige Ergebnisseite ab und extrahiere für jedes Boot:

- Final/Heat,
- Bugnummer,
- angezeigte Platzierung bzw. Reihenfolge,
- Finish-Zeit,
- Kurzbezeichnung von Verein/Composite,
- expliziten Status.

Ein fehlender Zeitwert oder `-` ist **kein** Beweis für DNS. Status immer aus einer Quelle mit expliziter Kennzeichnung bestätigen.

### 3. Crew-Daten blockweise holen

Nutze offizielle Detail-Startlisten für ganze Renntage oder Rennblöcke. Extrahiere pro Bugnummer:

- Land,
- vollständige Vereine,
- Crewmitglieder mit Geburtsjahr,
- gegebenenfalls Cox zur späteren Entfernung.

Tageslisten sind schnell, können aber bei PDF-Seitenumbrüchen Crewzeilen verschmelzen. Sie sind daher keine alleinige Autorität für auffällige Datensätze.

### 4. Konflikte gezielt auflösen

Öffne das **einzelne offizielle Ergebnis-PDF**, wenn:

- die erwartete Crewgröße nicht erreicht wird,
- mehr Personen als für die Bootsklasse möglich erscheinen,
- Namen zweier Bugnummern ineinanderlaufen,
- ein Geburtsjahr fehlt,
- ein Ergebnisportal nur `-` zeigt,
- DNS/DNF/DSQ/EXC/OOC/BUW unklar ist.

Übernimm keine plausibel klingenden Werte aus benachbarten Zeilen. Wenn das offizielle Einzel-PDF den Wert ebenfalls nicht enthält, markiere ihn als fehlend statt zu raten.

### 5. Quellen priorisieren

Bei Widersprüchen gilt standardmäßig:

1. offizielles Einzel-Ergebnis-PDF für Status und die tatsächlich gestartete Crew,
2. offizielles Startlisten-PDF für Meldedaten und Jahrgänge,
3. Ergebnisportal für Eventnavigation und kompakte Platz-/Zeitübersicht.

Die tatsächlich beobachtete Qualität kann eine Anpassung verlangen; die gewählte Rollenverteilung im Run dokumentieren.

### 6. Qualitätskontrollen

Vor dem Merge mindestens prüfen:

- erwartete Crewgröße je Bootsklasse,
- eindeutige Kombination aus Event/Rennnummer/Bugnummer,
- keine Cox-Zeilen bei entsprechendem Auftrag,
- Geburtsjahr numerisch und Alter = Veranstaltungsjahr - Geburtsjahr,
- Platzierung nur numerisch, wenn tatsächlich als Platz belegt,
- Statuswerte kontrolliertes Vokabular (`FIN`, `DNS`, `DNF`, `DSQ`, `EXC`, `OOC`, `BUW`),
- DNS/DNF ohne erfundene Finish-Zeit,
- keine stillen Duplikate beim Merge,
- UTF-8-BOM für Excel-kompatible CSV, wenn dies dem Zielworkflow entspricht.

## Firecrawl-Learnings

- Große Site-Crawls können trotz funktionierendem Einzel-Scrape in 429/Concurrency-Limits laufen. Dann nicht wiederholt denselben Crawl forcieren.
- Verzeichnis-/Linklisten zuerst extrahieren; anschließend nur relevante Seiten oder PDFs scrapen.
- Bei einem Eventportal ist ein Event-Abruf meist effizienter als ein Abruf pro Rennen.
- PDF-`query`-Antworten sind kompakt, können aber Tabellenzuordnungen halluzinationsartig verschieben. Für konfliktträchtige Stellen Roh-Markdown des einzelnen PDFs bevorzugen.
- Ein strukturierter Query-Output darf nie gegen erkennbare Tabelleninkonsistenzen 'glattgezogen' werden.
- Blockweise Startlisten + eventweise Resultate + Einzel-PDF-Ausnahmen sind effizienter und zuverlässiger als ein Vollcrawl aller PDFs.

## Zwischenstände

Nach abgeschlossenen Events einen versionierten Arbeitsstand erzeugen. Neue Events an den validierten Bestand anhängen, sortieren und erneut auf Schlüsselduplikate prüfen. Zwischenstände klar als Arbeitsstand kennzeichnen; erst nach vollständiger Scope-Prüfung eine Datei als final bezeichnen.

## Abschlusskriterium

Der Lauf ist abgeschlossen, wenn alle Events des definierten Scopes verarbeitet sind, jede Bugnummer eine plausible Crewzahl besitzt, alle nicht-finishenden Boote einen belegten Status haben, Konflikte auf Einzel-PDF-Ebene geklärt oder explizit als fehlend markiert sind und die Gesamtdatei die Eindeutigkeits- und Duplikatprüfungen besteht.
