---
name: local-scraping-handoff
description: Erzeugt reproduzierbaren Code, den der Nutzer gegen eine lokal erreichbare oder private Scraping-Instanz (insbesondere self-hosted Firecrawl) ausführt, und definiert eine belastbare Rückgabe per ZIP/JSON/CSV oder Drive für die anschließende Verarbeitung durch den Agenten. Verwenden, wenn der Agent eine Zielquelle nicht direkt erreicht, Cloud-Scraping limitiert ist, lokale/private Netzwerkzugriffe nötig sind oder große Web-/PDF-Batches besser lokal ausgeführt werden sollen.
userFacing: true
implicitInvocation: true
category: research-infrastructure
version: 0.1.0
status: candidate
owners:
  - White Label Maintainer
requires: []
outputs:
  - executable local extraction script
  - structured handoff package
  - manifest with success/failure evidence
---

# Local Scraping Handoff

Dieser Skill verwandelt eine Scraping-Aufgabe, die lokal oder in einem privaten Netz besser ausführbar ist, in ein reproduzierbares Nutzer-Skript plus ein strukturiertes Übergabepaket, das der Agent anschließend ohne erneutes Scraping weiterverarbeiten kann.

## Grenzen

Der Skill führt den lokalen/private-network Scrape nicht selbst aus. Er erzeugt Code und klare Ausführungsanweisungen für den Nutzer. Er übernimmt außerdem nicht die fachliche Endauswertung; diese beginnt nach Rückgabe des Handoff-Pakets.

## Voraussetzungen

- Ziel-URLs oder eine reproduzierbare Methode zu ihrer Ermittlung;
- lokale Scraping-Basis-URL, falls vorhanden, z. B. eine self-hosted Firecrawl-Instanz;
- gewünschter Umfang und Zielformat;
- optional ein Zielordner in Google Drive statt Chat-Upload.

## Workflow

### 1. Engpass erkennen

Nutze diesen Workflow, wenn mindestens eines zutrifft:

- die Zielquelle ist nur aus dem Nutzer-Netz erreichbar;
- Cloud-Firecrawl/Web-Zugriff ist limitiert, blockiert oder teuer;
- ein großer Batch soll lokal laufen;
- der Nutzer verfügt bereits über eine lokale Firecrawl-Instanz;
- der Agent benötigt Rohdaten statt einer bereits lokal interpretierten Endtabelle.

### 2. Übergabeformat zuerst festlegen

Bevor Code erzeugt wird, definiere das spätere Handoff-Artefakt. Standard für große Batches:

```text
<job-name>/
  manifest.json
  results.jsonl
  raw/
    indexes/
    startlists/
    results/
```

`manifest.json` enthält mindestens:

- verwendete lokale API-Basis-URL ohne Secrets;
- API-Version oder verwendeten Endpoint;
- Zielbereich/Filter;
- Anzahl entdeckter Quellen;
- Anzahl erfolgreicher und fehlgeschlagener Abrufe;
- Fehlerliste mit URL und Fehlermeldung;
- Quell-URLs.

Für Chat-Handoff wird der Ordner als ZIP gepackt. Alternativ kann der Nutzer das Paket in einen vereinbarten Drive-Ordner legen.

### 3. Minimal kompatiblen Firecrawl-Request erzeugen

Bei self-hosted Firecrawl niemals ungeprüft Cloud-Schema-Optionen voraussetzen.

Reihenfolge:

1. Readiness prüfen, typischerweise `/v0/health/readiness`.
2. Verfügbaren Scrape-Endpoint testen (`/v2/scrape`, danach `/v1/scrape` oder umgekehrt abhängig vom Stack).
3. Einen minimalen Smoke-Test gegen `https://example.com` ausführen.
4. Erst danach Zielquelle testen.
5. Bei PDFs zunächst minimal starten, z. B. `formats=["markdown"]` und nur dann `parsers=["pdf"]`, wenn die lokale Version dies akzeptiert.
6. Optionale Felder wie `pdfOptions` nur verwenden, wenn ein lokaler Smoke-Test sie bestätigt.

Ein HTTP `400` mit `unrecognized_keys` ist als Schema-Inkompatibilität zu behandeln, nicht als Netzwerkfehler. Ein `503` bedeutet zunächst Service-/Dependency-Probleme und darf nicht als „falscher Endpoint“ zusammengefasst werden. Ein Timeout des Readiness-Endpunkts weist auf API-/Netz-/Containerprobleme hin, bevor Batch-Scraping sinnvoll ist.

### 4. Immer Ein-Datei-Test vor Batch

Vor einem großen Lauf muss das Skript einen Einzeltest erlauben oder explizit mit nur einer Quelle gestartet werden können.

Abschlusskriterium des Smoke-Tests:

- HTTP erfolgreich;
- erwarteter Inhalt vorhanden;
- Rohantwort lokal gespeichert;
- Parser-/Schema-Optionen akzeptiert;
- keine stillen leeren Resultate.

Erst danach Parallelität erhöhen. Für self-hosted Instanzen konservativ beginnen, z. B. 1–3 Worker, und nur bei stabiler Verarbeitung erhöhen.

### 5. Rohdaten bewahren

Der lokale Code soll möglichst wenig fachliche Interpretation vorwegnehmen. Bevorzuge:

- komplette Firecrawl-Antwort je URL als JSON;
- `source_url`, stabile IDs und Metadaten neben dem Rohinhalt;
- zusätzlich JSONL für sequentielle Verarbeitung;
- keine aggressive Normalisierung von Namen, Status oder Tabellenbeziehungen, wenn der Agent diese später quellenübergreifend abgleichen muss.

Der Nutzer darf lokal eine Komfort-CSV erzeugen, aber die Rohantworten bleiben kanonische Übergabequelle.

### 6. Fehler robust erfassen

Jeder Abruf erzeugt entweder ein Erfolgsobjekt oder ein Fehlerobjekt, z. B.:

```json
{
  "ok": false,
  "source_url": "...",
  "error": "400 ... unrecognized key ..."
}
```

Ein Batch darf wegen einzelner Fehler nicht alle bereits erfolgreichen Resultate verlieren. Ergebnisse sofort persistieren und am Ende ein Manifest schreiben.

### 7. Secrets und lokale Adressen behandeln

- API-Keys nur aus Umgebungsvariablen lesen.
- Keine Keys in ZIP, Manifest oder Logs schreiben.
- Private IP-Adressen dürfen im lokalen Skript stehen, wenn der Nutzer sie ausdrücklich vorgibt; sie sind nicht als öffentlich erreichbare URL zu behandeln.
- Nie behaupten, der Agent habe die lokale Instanz selbst erreicht, wenn der Nutzer den Code ausgeführt hat.

### 8. Rückgabe an den Agenten

Bevorzugte Wege:

1. ZIP direkt in den Chat hochladen.
2. ZIP oder entpackten Ordner in Google Drive ablegen und den genauen Ordner/Link nennen.
3. Bei kleinen Resultaten JSONL/CSV direkt hochladen.

Nach Rückgabe liest der Agent zuerst `manifest.json`, prüft Erfolgsquote und Fehlercluster, verarbeitet dann die Rohdaten und erzeugt die fachliche Endausgabe.

## Code-Regeln

Das erzeugte Skript soll:

- unter der vom Nutzer genannten Runtime laufen;
- die API-Basis-URL als Konstante oder CLI-Parameter führen;
- Endpoints per Smoke-Test erkennen, ohne 4xx/5xx zu verwechseln;
- Timeouts explizit setzen;
- Parallelität konfigurierbar machen;
- jeden Abruf sofort persistieren;
- einen Resume-fähigen Modus bevorzugen, der vorhandene erfolgreiche Dateien überspringt;
- am Ende ZIP plus Manifest erzeugen;
- verständliche Konsolenausgaben zu Fortschritt, Erfolgen und Fehlern liefern.

## Firecrawl-Learning aus Self-Hosted-Praxis

Bewährtes Muster aus einem realen Batch:

- falsche lokale IP zuerst durch Readiness-Test isolieren;
- API-Version nicht raten, sondern `/v1/scrape` und `/v2/scrape` testen;
- `503` als Betriebsproblem behandeln;
- `400`-Body vollständig lesen;
- `Unrecognized key: pdfOptions` durch Entfernen von `pdfOptions` lösen, `parsers=["pdf"]` beibehalten;
- danach Ein-Datei-Test durchführen;
- erst bei Erfolg den vollständigen Batch starten;
- Ergebnis als ZIP mit `manifest.json`, `results.jsonl` und Raw-JSON an den Agenten zurückgeben.

## Fehlerbehandlung

### API nicht erreichbar

Readiness lokal und über die private IP vergleichen. Danach Port-Binding, Firewall und Containerstatus prüfen.

### API erreichbar, Scrape 503

Abhängigkeiten und Logs prüfen; insbesondere Worker/Queue, Redis, RabbitMQ/Postgres und Browser-/Playwright-Service je nach Version.

### Scrape 400

Response-Body als API-Vertrag behandeln. Unbekannte optionale Felder entfernen und auf minimalen Request zurückgehen.

### Einzeltest erfolgreich, Batch fehlerhaft

Parallelität auf 1 reduzieren, Timeout erhöhen und Resume aktivieren. Fehlercluster im Manifest bewahren.

## Abschluss

Die Übergabe ist abgeschlossen, wenn:

- das lokale Skript ausführbar und auf einen Einzelfall getestet ist;
- der Nutzer den Batch erfolgreich gestartet oder abgeschlossen hat;
- ein strukturiertes Paket mit Manifest und Rohdaten existiert;
- Erfolgs- und Fehlerzahlen sichtbar sind;
- keine Secrets im Paket enthalten sind;
- der Agent anhand des Pakets ohne erneutes Nutzer-Scraping mit der fachlichen Verarbeitung fortfahren kann.
