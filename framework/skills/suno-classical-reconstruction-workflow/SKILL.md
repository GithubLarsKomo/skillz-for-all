---
name: suno-classical-reconstruction-workflow
description: Spezialisiert den Suno-Produktionsworkflow für den erkennbaren Nachbau, die motivische Reduktion und die EDM-Transformation gemeinfreier oder anderweitig freigegebener klassischer Musik. Verwendet eine quellentreue symbolische MIDI-Masterspur, erzeugt verpflichtend mobile-taugliche WAV-Referenzen und prüft Motivtreue vor der Suno-Generation. Verwenden bei Wagner-, Verdi-, Opern-, Sinfonie-, Leitmotiv- oder sonstigen Classical-to-EDM-Projekten, insbesondere wenn der Nutzer auf iPhone/iOS arbeitet.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - White Label Maintainer
requires:
  - suno-song-production-workflow
  - project-second-brain
outputs:
  - classical-source-manifest.json
  - classical-symbolic-master.mid
  - classical-source-reference.wav
  - classical-derivative-pairs
  - classical-mobile-handoff.md
lastEvaluated: 2026-09-13
---

# Suno Classical Reconstruction Workflow

## Zweck

Dieser Spezialworkflow ergänzt `suno-song-production-workflow`, wenn eine **konkrete klassische Komposition oder ein klar identifizierbares Motiv** als musikalische Quelle für Suno rekonstruiert oder transformiert werden soll. Ziel ist nicht bloß ein stilistischer Prompt, sondern ein belastbarer Quellen-Handoff, bei dem die relevante Melodie, Harmonik, Rhythmik und Phrasierung nachweisbar erhalten bleiben.

Er löst insbesondere das mobile Problem, dass ein symbolischer MIDI-Master auf iPhone/iOS nicht zuverlässig als Suno-Eingabe verfügbar ist: **MIDI bleibt der editierbare Master, WAV ist das verpflichtende mobile Austauschformat.**

## Routing

Diesen Workflow verwenden, wenn mindestens eines gilt:

- der Nutzer nennt ein konkretes Werk, eine Arie, Ouvertüre, Sinfonie, ein Leitmotiv oder einen bekannten klassischen Abschnitt;
- ein bestehendes Werk soll erkennbar in EDM, Trance, Techno, Mainstage, Cinematic Bass oder eine andere moderne Form überführt werden;
- Noten/Partitur werden in eine MIDI- oder Audio-Referenz rekonstruiert;
- ein vorhandener MIDI-Entwurf soll für Suno auf iPhone/iOS nutzbar gemacht werden.

Für allgemeine „klassisch klingende“ Musik ohne konkrete Quellkomposition reicht `suno-song-production-workflow`.

## Gate C0 — Quelle und Rechte

Vor der Rekonstruktion dokumentieren:

- Werk, Komponist, Abschnitt/Motiv und möglichst Partiturstelle;
- Status der zugrunde gelegten **Komposition und konkreten Notenausgabe**: gemeinfrei, eigene Transkription oder anderweitig freigegeben;
- keine ungeklärte moderne Aufnahme oder moderne fremde Bearbeitung als versteckte Quelle übernehmen;
- wenn eine historische Partitur/Edition verwendet wird, Provenienz im `classical-source-manifest.json` festhalten.

Bei gemeinfreien Kompositionen darf die konkrete Melodie rekonstruiert werden. Die allgemeine Regel des Suno-Basisworkflows gegen das Kopieren fremder moderner Melodien ist hier nicht auf eine gemeinfreie Quellkomposition anzuwenden; Rechte an modernen Aufnahmen, Arrangements und Editionsbestandteilen bleiben separat zu prüfen.

## Phase C1 — Source-faithful musical extraction

Vor jeder EDM-Transformation eine quellentreue musikalische Repräsentation erzeugen. Mindestens prüfen und dokumentieren:

- Tonhöhen und Intervallstruktur;
- Rhythmus und Auftakte;
- Taktart;
- Ausgangstempo bzw. musikalisch sinnvolle Referenzgeschwindigkeit;
- Phrasen- und Motivgrenzen;
- charakteristische Harmonik/Bassbewegung;
- Artikulation, soweit sie für die Wiedererkennbarkeit wesentlich ist;
- Transpositionen oder Vereinfachungen ausdrücklich kennzeichnen.

Bei Leitmotiven oder Orchesterpassagen darf eine reduzierte Repräsentation verwendet werden, sie muss aber als `reduction` bezeichnet sein und darf nicht als vollständige Partiturtranskription ausgegeben werden.

## Gate C1 — Motif Fidelity

PASS nur wenn ein Hörer das Quellmotiv anhand der Reduktion grundsätzlich identifizieren kann und keine wesentliche falsche Tonfolge, Taktstruktur oder Phrase eingeführt wurde.

## Phase C2 — Symbolic MIDI master

Die extrahierte Quelle wird als MIDI-Master gespeichert. MIDI ist der **kanonische editierbare und reproduzierbare Master** für spätere Änderungen.

Für EDM-Projekte bevorzugt folgende Paarstruktur, soweit musikalisch sinnvoll:

- `MAIN` — möglichst quellentreues Hauptmotiv;
- `DROP` — EDM-kompatible Ableitung mit erhaltenem melodischem Fingerabdruck;
- `BASS` — aus Harmonik, Grundtönen oder charakteristischen Intervallen abgeleitete Bass-DNA;
- `BUILD` — Motivfragment/Ostinato für den Spannungsaufbau;
- `SUNO_multitrack` — kombinierte Testfassung erst nach erfolgreicher Einzelprüfung.

Jede Transformation dokumentiert, **welche Eigenschaften erhalten** und welche bewusst verändert wurden.

## Phase C3 — Mandatory WAV bridge

### Harte Regel

> Für klassische Rekonstruktions-/Nachbauprojekte ist ein MIDI-only-Handoff unvollständig.

Zu **jedem MIDI-Artefakt, das als Suno-Referenz vorgesehen ist, wird eine hörbare WAV-Datei erzeugt**. Die WAV-Datei ist auf mobilen/iPhone-Workflows die primäre operative Eingabe; die MIDI-Datei bleibt als symbolischer Master erhalten.

### Render-Standard

Default, sofern kein Zielsystem etwas anderes verlangt:

- WAV PCM;
- 48 kHz;
- 24 Bit;
- Stereo;
- Peak mit Headroom, Ziel etwa -1 dBFS, kein Clipping;
- keine aggressive Loudness-Bearbeitung;
- neutrale, gut unterscheidbare Klangfarben;
- kein starkes Hall-/FX-Design, das Tonhöhen, Rhythmus oder Motivgrenzen verschleiert.

Der WAV-Render ist **keine Vorproduktion des finalen EDM-Tracks**. Er dient dazu, Suno und dem Nutzer die musikalische Information möglichst eindeutig zu übergeben.

### Audio-QC vor Handoff

Mindestens prüfen:

- Datei ist nicht leer/stumm und technisch lesbar;
- Sample Rate, Bit-Tiefe und Kanäle entsprechen dem Render-Standard oder sind begründet abweichend;
- kein digitales Clipping;
- Start/Ende schneiden keine musikalisch relevanten Noten ab;
- Motiv, Rhythmus, Taktgefühl und Transposition entsprechen dem zugehörigen MIDI-Master;
- bei mehrspurigen Dateien verschleiert keine Spur das Hauptmotiv.

## Gate C2 — Mobile Source Ready

PASS nur wenn:

- für jedes Suno-relevante MIDI ein gleichnamiger oder eindeutig zuordenbarer WAV-Companion existiert;
- MAIN-WAV hörbar und motivtreu ist;
- der Nutzer auf iPhone/iOS **nicht** selbst MIDI konvertieren muss;
- der mobile Handoff direkte WAV-Dateien priorisiert.

## Phase C4 — Mobile/iPhone handoff order

Bei iPhone/iOS den Nutzer nicht mit dem symbolischen Master beginnen lassen. Standardreihenfolge:

1. `MAIN.wav` — Test: erkennt/erhält Suno das Originalmotiv?
2. `DROP.wav` — Test: bleibt das Motiv unter EDM-kompatibler Transformation erkennbar?
3. optional `BASS.wav` und `BUILD.wav` zur Diagnose einzelner Funktionen;
4. `SUNO_multitrack.wav` erst, wenn MAIN und DROP einzeln funktionieren.

Im Nutzer-Handoff **WAV-Link zuerst**, MIDI-Link danach als Archiv-/Desktop-/DAW-Option.

Nie plattformübergreifend behaupten, ein MIDI-Import sei verfügbar, nur weil er auf einer anderen Suno-Oberfläche oder in einer anderen Studio-Version existiert. Der `suno-capability-snapshot` soll relevante Unterschiede zwischen iOS/iPhone, Web/Desktop und Studio-Funktionen getrennt erfassen, wenn sie für die konkrete Ausführung entscheidend sind.

## Phase C5 — EDM transformation

Erst nach Gate C2 die moderne Produktion weiter treiben. Das Quellmotiv soll die Produktionsarchitektur steuern, nicht nur über einen fertigen EDM-Unterbau gelegt werden.

Bevorzugte Ableitung:

`Quellmotiv -> MAIN -> DROP-Transformation -> harmonisch abgeleitete BASS-DNA -> BUILD-Fragment -> Suno-WAV-Handoff -> Generation -> Hörprüfung`

Für maximale Wiedererkennbarkeit:

- Drop möglichst auf einem charakteristischen Motivbeginn oder Motivhöhepunkt starten;
- rhythmische Quantisierung nicht stärker verändern als für Groove nötig;
- charakteristische Intervalle priorisieren;
- zuerst eine eindeutige monophone/klare MAIN-Referenz testen, bevor dichte Orchestrierung hinzugefügt wird;
- bei schlechter Motiverhaltung zuerst die Quelle vereinfachen/verdeutlichen, nicht den Style-Prompt immer weiter aufblasen.

## Phase C6 — Review und Lernen

Zusätzlich zum normalen `suno-generation-review.json` bewerten:

- source motif recognizability;
- melodic fidelity;
- rhythmic fidelity;
- harmonic identity;
- degree of transformation;
- whether the drop is *derived from* the motif rather than merely accompanied by it;
- whether WAV vs. MIDI/source arrangement changed Suno behavior;
- iPhone/mobile usability.

Erfolgreiche und fehlgeschlagene Varianten werden im Project Second Brain dokumentiert. Modellabhängige Beobachtungen bleiben modell-/versionsbezogen.

## Stop-Regeln

Blockierend:

- ungeklärte Rechte an einer nicht gemeinfreien Quellkomposition oder konkreten Aufnahme/Bearbeitung;
- Rekonstruktion wird als originalgetreu bezeichnet, obwohl sie nur eine freie Annäherung ist;
- Suno-relevantes MIDI ohne WAV-Companion;
- WAV mit Clipping, Stille, abgeschnittenem Motiv oder hörbar falscher Ton-/Rhythmusfolge;
- iPhone-Handoff verlangt vom Nutzer eine zusätzliche MIDI-Konvertierung;
- Multitrack wird als erster Test verwendet, obwohl unklar ist, ob MAIN allein erhalten bleibt.

Nicht blockierend:

- einfache/kunstlose Instrumentklänge im Referenz-WAV, solange Motiv und Timing klar sind;
- MIDI bleibt für den Nutzer auf iPhone ungenutzt, solange es als reproduzierbarer Master archiviert ist;
- ein `reduction`-Master bildet nicht die vollständige Orchestrierung ab, wenn dies transparent dokumentiert ist.

## Abschluss

Der Spezialworkflow endet, wenn:

1. Quelle und Rechte dokumentiert sind;
2. ein quellentreuer symbolischer Master vorliegt;
3. relevante MAIN/DROP/BASS/BUILD-Ableitungen nachvollziehbar dokumentiert sind;
4. jedes Suno-relevante MIDI einen geprüften WAV-Companion besitzt;
5. der mobile Handoff WAV-first ist;
6. Suno-Generationen auf Motiverhaltung hörgeprüft wurden;
7. Learnings in den Project Second Brain zurückgeschrieben sind;
8. die nächste musikalische Iteration eindeutig benannt ist.
