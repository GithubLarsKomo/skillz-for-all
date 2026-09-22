---
name: person-profile-document-delivery
description: Überführt einen fachlich und sprachlich finalisierten Personenreport in konsistente DOCX- und PDF-Ausgaben, wählt bei vorhandenem Corporate-Kontext passende Renderer oder Templates und erzwingt visuelle QA ohne inhaltliches Re-Authoring. Verwenden, wenn ein Personenprofil als professionelles editierbares DOCX und/oder finales PDF ausgeliefert werden soll.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.2.0
status: candidate
owners:
  - White Label Maintainer
requires:
  - precision-writing-revision
  - artifact-production-contract
  - artifact-contract-audit
consumes:
  - final-revised-text
  - precision-writing-report.json
outputs:
  - person-profile-report.docx
  - person-profile-report.pdf
  - person-profile-delivery.json
lastEvaluated: 2026-09-22
---

# Person Profile Document Delivery

## Rolle

Dieser Skill ist ein **Delivery- und Rendering-Orchestrator**. Er verändert keine Recherche, Claims oder Schlussfolgerungen. Eingabe ist ein bereits fachlich finalisierter und über `precision-writing-revision` fidelity-geprüfter Personenreport.

## Trigger

Verwenden, wenn der Nutzer einen fertigen Personenreport als:

- DOCX,
- PDF,
- oder DOCX und PDF

benötigt.

Nicht verwenden, solange der Inhalt fachlich offen ist oder der sprachliche Fidelity-Check nicht bestanden wurde.

## Eingabe

Mindestens erforderlich:

- finaler Reporttext,
- Titel und Standdatum,
- Quellen-/Referenzblöcke,
- gewünschte Formate,
- optional Corporate-/Brand-Kontext,
- optional bereitgestelltes DOCX-Template.

Wenn ein Evidence Dossier verfügbar ist, bleibt es Referenzbasis für die Prüfung, dass beim Rendering keine Quellen, Unsicherheiten oder Evidenzhinweise verloren gehen.

## Rendering-Architektur

Grundregel:

`finaler fidelity-geprüfter Report -> kanonisches DOCX -> PDF`

PDF und DOCX dürfen nicht unabhängig voneinander neu geschrieben werden. Das DOCX ist die kanonische editierbare Layoutquelle; das PDF wird daraus oder aus derselben eindeutig kontrollierten Layoutquelle abgeleitet.

### Renderer-Auswahl

1. **Explizites Nutzer-Template:** immer priorisieren, sofern technisch verwendbar.
2. **Bestätigter Corporate-Kontext:** passenden tenant- oder projektspezifisch bereitgestellten Renderer/Template-Skill verwenden.
3. **Kein Corporate-Kontext:** neutralen professionellen A4-Report erzeugen; keine fremde Marke oder Corporate-Freigabe behaupten.

Corporate-Renderer sind optionale Routen und keine inhaltlichen Abhängigkeiten dieses Skills.

## Struktur

Der Dokumentreport soll je nach vorhandenen Inhalten unterstützen:

- Titelblatt oder kompakter Reportkopf,
- Executive Summary,
- Biographie und Ausbildung,
- Karriere-Timeline,
- wissenschaftliche Phasen,
- Publikationscluster,
- IP-/Patentübersicht,
- Arbeitgeber und Rollen,
- optionale öffentliche Aktivitäten/Hobbies/Sport,
- Evidenzlücken und Widersprüche,
- Quellen/Referenzen.

Keine leeren Kapitel erzwingen.

## Fidelity-Regeln

Beim Übergang Markdown/Text -> DOCX -> PDF müssen erhalten bleiben:

- alle Fakten und Zeitangaben,
- Zahlen und Rollentitel,
- Evidenzklassen und Unsicherheitsformulierungen,
- Quellenreferenzen und Links,
- Tabelleninhalt und Reihenfolge,
- Negationen und Einschränkungen.

Layoutänderungen dürfen Bedeutung nicht verändern. Keine Kürzung nur wegen Seitenumbruch. Wenn Platzprobleme entstehen, Layout oder Tabellenstruktur anpassen.

## DOCX-QA

Vor Freigabe:

- Dokument öffnet fehlerfrei,
- A4/gewünschtes Seitenformat korrekt,
- Überschriftenhierarchie konsistent,
- Tabellen nicht abgeschnitten,
- Links und Quellen lesbar,
- keine verwaisten Überschriften oder problematischen Seitenumbrüche,
- Header/Footer und Branding entsprechen der gewählten Route,
- keine defekten Glyphen oder ungewollten Font-Substitutionen,
- alle Seiten visuell geprüft.

## PDF-QA

PDF erst nach erfolgreicher DOCX-QA erzeugen. Danach prüfen:

- gleiche Inhaltsreihenfolge und inhaltliche Vollständigkeit,
- keine zusätzlichen oder verlorenen Seiten,
- keine Reflow-, Tabellen-, Bild- oder Glyphenfehler,
- Quellen und Links bleiben lesbar,
- visuelle Parität zum kanonischen DOCX.

Bei PDF-Problemen die Ursache im DOCX/Template korrigieren und erneut konvertieren; nicht unabhängig im PDF nachbearbeiten.

## Output-Metadaten

`person-profile-delivery.json` dokumentiert mindestens:

```json
{
  "schemaVersion": 1,
  "source": "person-profile-report.md",
  "fidelityStatus": "pass",
  "requestedFormats": ["docx", "pdf"],
  "rendererRoute": "neutral|corporate|supplied-template|other",
  "templateStatus": "neutral|public-reference|supplied|approved",
  "docxQa": "pass|not-requested|blocked",
  "pdfQa": "pass|not-requested|blocked",
  "driveArtifacts": [],
  "storageStatus": "verified|pending|blocked",
  "warnings": []
}
```

## Artifact Production Contract Gate

Bei substantieller Neuerstellung oder materieller Überarbeitung zuerst den gemeinsamen `artifact-production-contract` aus angemessenem Grilling erzeugen bzw. einen gültigen gefrorenen Vertrag wiederverwenden. Dieser Workflow führt den gefrorenen Vertrag aus und darf INVARIANT-Festlegungen nicht neu interpretieren. Vor Release prüft `artifact-contract-audit` die exakt auszuliefernde Revision. Ein Audit-PASS ist Voraussetzung für den anschließenden Drive-Delivery-Gate; reine deterministische Konvertierungen dürfen den bestehenden Vertrag erben.

## Drive Storage and Delivery Gate

Alle erzeugten Nicht-Code-Artefakte folgen dem framework-weiten `docs/DOCUMENT-ARTIFACT-DELIVERY-CONTRACT.md`.

- lokale/Sandbox-Dateien sind nur Build-Zwischenstände;
- finale Artefakte werden in den owning Child-Brain-Drive-Root geschrieben; ohne passenden Brain in den tenantweiten `Deliveries`-Root;
- nach dem Write werden Drive-ID, URL, Parent und soweit verfügbar Revision/Modified State read-back-verifiziert;
- Projektartefakte werden über `project-second-brain` in `ASSETS.md`/`state.json` registriert;
- ein erfolgreicher Nutzer-Handoff liefert die verifizierten Drive-Links;
- fehlende Drive-Schreibfähigkeit bedeutet `pending|blocked`, nicht erfolgreiche Delivery und keinen GitHub-/Sandbox-Fallback.


## Fehlerbehandlung

- Fidelity-Status nicht `pass`: keine finale DOCX/PDF-Ausgabe.
- DOCX-Erzeugung technisch nicht möglich: keine Fake-Datei erzeugen; klar blockieren.
- PDF-Konvertierung fehlgeschlagen: geprüfte DOCX kann in Drive gespeichert und verlinkt werden, PDF bleibt `blocked`.
- Visuelle QA nicht möglich: betroffenes Format nicht als final geprüft kennzeichnen.
- Corporate-Template fehlt: nur dann neutralen Stil verwenden, wenn kein Corporate-Template ausdrücklich verlangt wurde.
- Nutzer hat ein bestimmtes Template verlangt und es ist nicht verfügbar/kompatibel: nicht still auf einen anderen Stil wechseln.

## Abschlusskriterien

Abgeschlossen ist der Skill, wenn alle angeforderten Formate aus derselben finalen fidelity-geprüften Inhaltsbasis erzeugt, in Drive gespeichert und read-back-verifiziert wurden, die gewählte Template-/Renderer-Route dokumentiert ist, DOCX und PDF ihre jeweilige visuelle QA bestanden haben und keine inhaltliche Abweichung zwischen den Formaten erkennbar ist.
