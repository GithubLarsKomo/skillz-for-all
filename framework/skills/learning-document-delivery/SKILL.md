---
name: learning-document-delivery
description: Überführt ein kanonisches Learning-Content-Modell und seine Visuals DESIGN.md-konform in ein editierbares Lern-DOCX und daraus in ein geprüftes PDF, mit Corporate-Renderer-Routing wenn ein verbindlicher Firmenkontext vorliegt. Verwenden für Lernhandouts, SOP-Drafts und Video-Study-Guides; nicht zum inhaltlichen Re-Authoring beim Rendering.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.2.0
status: candidate
owners:
  - White Label Maintainer
requires:
  - learning-content-design-system
outputs:
  - learning-handout.docx
  - learning-handout.pdf
  - learning-document-qa.json
lastEvaluated: 2026-09-22
---

# Learning Document Delivery

## Grundarchitektur

`learning-content-model.json -> canonical DOCX -> full-page QA -> PDF -> parity QA`

DOCX und PDF werden nicht unabhängig neu geschrieben.

## Renderer-Routing

1. explizit bereitgestelltes Nutzer-/Corporate-DOCX-Template;
2. anwendbarer bestätigter tenant- oder projektspezifischer Corporate Renderer;
3. sonst neutraler professioneller A4-Lernreport auf Basis des aktiven Learning-DESIGN.md.

Kein stilles Corporate-Fallback oder erfundene Unternehmensfreigabe.

## Inhaltliche Struktur

Je nach Content-Modell:

- Titel/Source block;
- Lernziele;
- Key Takeaways;
- Mental Model;
- erklärende Kapitel;
- Visuals mit Caption;
- optional derived SOP;
- Critical details / Common mistakes;
- Self-check / FAQ;
- Source Map / Timestamp references;
- offene Evidenzlücken.

## Fidelity

Beim Rendering müssen erhalten bleiben:

- Claim-Inhalt und Confidence;
- `observed/derived/recommended`;
- Zahlen, Einheiten und Negationen;
- Warnungen;
- Schrittfolge;
- Timestamp-Referenzen;
- Visual-ID/Caption/Provenance;
- Quellen.

## DOCX QA

Komplettes Dokument seitenweise rendern und prüfen:

- Seitenformat/Margins;
- Heading-Hierarchie;
- Tabellen;
- Visual-Clipping;
- Captions;
- Header/Footer;
- Seitenumbrüche;
- Font-/Glyph-Probleme;
- Quellen/Timestamp-Lesbarkeit.

## PDF QA

Nach DOCX-PASS:

- jede PDF-Seite rendern;
- Seitenzahl/Inhaltsreihenfolge vergleichen;
- keine Reflow-/Glyph-/Bildfehler;
- sichtbare Parität zum kanonischen DOCX;
- Corporate Design Gate zusätzlich PASS, wenn anwendbar.

## Drive Storage and Delivery Gate

Alle erzeugten Nicht-Code-Artefakte folgen dem framework-weiten `docs/DRIVE-STORAGE-AND-DELIVERY-CONTRACT.md`.

- lokale/Sandbox-Dateien sind nur Build-Zwischenstände;
- finale Artefakte werden in den owning Child-Brain-Drive-Root geschrieben; ohne passenden Brain in den tenantweiten `Deliveries`-Root;
- nach dem Write werden Drive-ID, URL, Parent und soweit verfügbar Revision/Modified State read-back-verifiziert;
- Projektartefakte werden über `project-second-brain` in `ASSETS.md`/`state.json` registriert;
- ein erfolgreicher Nutzer-Handoff liefert die verifizierten Drive-Links;
- fehlende Drive-Schreibfähigkeit bedeutet `pending|blocked`, nicht erfolgreiche Delivery und keinen GitHub-/Sandbox-Fallback.


## Abschluss

Abgeschlossen, wenn DOCX editierbar, PDF visuell vollständig geprüft und beide inhaltlich identisch zur kanonischen Learning-Basis sind, beide angeforderten Formate in Drive read-back-verifiziert wurden und ihre Drive-Links im Delivery-Handoff stehen.
