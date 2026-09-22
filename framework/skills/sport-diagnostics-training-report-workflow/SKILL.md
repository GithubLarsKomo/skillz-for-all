---
name: sport-diagnostics-training-report-workflow
description: Orchestriert einen vollständigen Sportdiagnostik-Workflow von Test-/Athletendaten über nachvollziehbare Leistungsinterpretation und den kanonischen One-shot-Trainingsplan bis zum kanonischen DOCX und dem daraus abgeleiteten, visuell abgeglichenen PDF. Fachlogik bleibt in den spezialisierten Skills.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.4.0
status: candidate
owners:
  - White Label Maintainer
requires:
  - sport-performance-diagnostics
  - sport-training-plan-workflow
  - template-document-workflow
consumes:
  - sport-diagnostics.json
  - sport-training-plan.json
  - document.docx
  - document.pdf
  - document-delivery-manifest.json
outputs:
  - sport-report-package
lastEvaluated: 2026-09-22
---

# Sport Diagnostics to Training Report Workflow

Koordiniere die spezialisierten Sport-Skills, ohne deren Fachlogik zu duplizieren. Ziel ist ein reproduzierbarer Ablauf von Eingangsdaten über fachliche Arbeitsartefakte bis zum **editierbaren kanonischen DOCX und dem daraus abgeleiteten PDF**.

## Trigger

Nutze diesen Orchestrator bei Aufträgen wie:

- „Werte diesen Laktattest aus, leite einen Trainingsplan ab und erstelle daraus einen professionellen DOCX-/PDF-Report.“
- „Überführe meinen aktuellen Kraftblock in einen Taperplan und generiere den professionellen Report.“
- „Erstelle aus Befund/Leistungsdaten und Trainingsziel einen vollständigen Sportdiagnostik- und Trainingsreport.“

Bei reiner Testauswertung, reiner Trainingsplanung oder reinem Dokumentsatz direkt den jeweiligen Fach- oder Renderer-Skill verwenden. Für reine einmalige Trainingsplanung ist `sport-training-plan-workflow` der kanonische Entrypoint.

## Voraussetzungen

- Eingabedaten und Ziel sind ausreichend klar oder Unsicherheiten werden explizit dokumentiert.
- Für medizinische Befunde liegt der Originaltext oder eine verlässliche Quelle vor; keine Diagnose aus bloßer Erinnerung rekonstruieren.
- Für Trainingsplanung stehen Termin, Sportart, Verfügbarkeit und relevante Last-/Zoneninformationen soweit möglich bereit.
- Vor dem Rendering ist der fachliche Inhalt eingefroren.

## Ablauf

1. **Auftrag zerlegen.** Feststellen, welche Eingangsdaten vorhanden sind und ob Diagnostik, Trainingsplanung und Rendering tatsächlich alle benötigt werden.
2. **Diagnostik ausführen.** Falls erforderlich Testdaten an `sport-performance-diagnostics` übergeben. Ergebnis als `sport-diagnostics.json` sichern.
3. **Trainingsplan ableiten.** Falls erforderlich Diagnostik/Arbeitswerte, Zieltermin, Verfügbarkeit und Belastungsgrenzen an `sport-training-plan-workflow` übergeben. Ergebnis als kanonisches `sport-training-plan.json` sichern. Die darunterliegenden Ziel-/Saison-/Meso-/Mikro-/Strength-/Endurance-Skills bleiben fachliche Eigentümer ihrer Artefakte.
4. **Konsistenz-Gate.** Trainingszonen, 1RM/e1RM, Termine, Übungsnamen, RIR/RPE, Dauer/Kadenz und Sicherheitsgrenzen zwischen Diagnose und Plan widerspruchsfrei halten.
5. **Report-Spec bauen.** Nur freigegebene Inhalte in Metadaten, Abschnitte, Tabellen, Callouts, Charts und Seitenumbrüche des DOCX-Renderer-Schemas transformieren.
6. **Kanonisches DOCX rendern.** `template-document-workflow` mit dem finalen Sport-Report-Inhalt und einem optional bereitgestellten Template aufrufen. Mehrseitige Tabellen müssen ungeteilte Datenzeilen und wiederholte Kopfzeilen behalten.
7. **PDF ableiten und visuell prüfen.** Die PDF-Ausgabe aus demselben `template-document-workflow` ableiten; keine zweite Layoutlogik verwenden.
8. **Paritäts-Gate.** DOCX- und PDF-Seitenbilder auf Reflow, Tabellen, Charts, Header/Footer, Glyphen und sichtbare Inhalte vergleichen. Bei Abweichung zurück zum DOCX-Pfad.
9. **Paket abschließen.** DOCX, PDF und benötigte strukturierte Zwischenartefakte/Quellenreferenzen in den owning Brain Drive schreiben, read-back-verifizieren und gemeinsam über Drive-Locators ausgeben.

## Renderer-Routing

Für neue Reports gilt zwingend:

`Report-Spec -> template-document-workflow -> DOCX -> PDF + Render-QA`


## Drive Storage and Delivery Gate

Erzeugte Nicht-Code-Artefakte folgen `docs/DRIVE-STORAGE-AND-DELIVERY-CONTRACT.md`: in Drive persistieren, read-back-verifizieren und über beobachtete Drive-Links referenzieren. Lokale/Sandbox-Dateien bleiben Build-Zwischenstände; ohne Drive-Write ist der Handoff `pending|blocked`.

Fachartefakte, Report-Spec, DOCX, PDF und Paketmanifest liegen nach erfolgreichem Lauf im passenden Drive-Kontext; Software-/Messsystem-Producer bleiben außerhalb des Brain.
## Prüfungen

- Wurde jeder fachliche Wert nur an einer Stelle interpretiert und danach referenziert?
- Wird `sport-training-plan.json` ausschließlich über `sport-training-plan-workflow` erzeugt?
- Stimmen Testmodalität und Trainingsmodalität zusammen oder ist die Übertragung ausdrücklich begründet?
- Sind Plan, Report-Spec, DOCX und PDF numerisch identisch?
- Sind medizinische Quellenbefunde von sportwissenschaftlichen Ableitungen getrennt?
- Sind Warn-/Abbruchregeln vollständig erhalten?
- Wurde jede DOCX-Seite visuell geprüft?
- Wurde das PDF ausschließlich aus dem finalen DOCX erzeugt?
- Wurde die visuelle DOCX/PDF-Parität geprüft?

## Fehlerbehandlung

- **Diagnostik nicht auflösbar:** keine Trainingszone erzwingen; konservative Ersatzsteuerung oder Klärungsbedarf erhalten.
- **Trainingskonflikt:** an `sport-training-plan-workflow` beziehungsweise den dort verantwortlichen Spezialskill zurückgeben; vor dem Rendering korrigieren. Renderer sind kein Ort für fachliche Änderungen.
- **Quellbefund widersprüchlich:** Widerspruch sichtbar erhalten und gezielte Bestätigung/medizinische Klärung verlangen.
- **DOCX-Layoutfehler:** nur Layout an den DOCX-Renderer zurückgeben; Fachartefakte unverändert lassen.
- **PDF-Reflow:** nicht im PDF reparieren; DOCX-Quelle korrigieren und neu konvertieren.
- **Tool-/Dateifehler:** zuletzt verifiziertes Zwischenartefakt erhalten und genau dort wiederaufnehmen.

## Übergabe

`sport-report-package` enthält mindestens:

```json
{
  "diagnostics": "sport-diagnostics.json|not_required",
  "training_plan": "sport-training-plan.json|not_required",
  "report_spec": "report-spec.json",
  "docx": "sport-report.docx",
  "pdf": "sport-report.pdf",
  "drive_links": [],
  "storage_status": "verified|pending|blocked",
  "verification": {
    "content_consistency": true,
    "visual_docx_check": true,
    "visual_pdf_check": true,
    "docx_pdf_parity": true
  }
}
```

Die strukturierten Fachartefakte sind die fachliche Wahrheit; das DOCX ist die kanonische Layoutquelle; das PDF ist deren abgeleitete Präsentationsform.

## Abschlusskriterien

Der Workflow ist abgeschlossen, wenn alle benötigten Fach-Skills beendet wurden, Diagnose und kanonischer Trainingsplan konsistent sind, der Report-Spec keine stillen Inhaltsänderungen enthält, das DOCX visuell geprüft wurde, das PDF ausschließlich daraus konvertiert wurde, die visuelle DOCX/PDF-Übereinstimmung bestätigt ist und die finalen Reportartefakte als verifizierte Drive-Objekte verlinkt sind.
