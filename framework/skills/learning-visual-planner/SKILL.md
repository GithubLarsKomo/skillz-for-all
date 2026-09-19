---
name: learning-visual-planner
description: Plant für evidenzgebundene Lerninhalte die jeweils informationsstärkste Visualisierung und entscheidet zwischen Quellframe, Diagramm/SVG, Chart, annotiertem Screenshot oder generierter Illustration. Verwenden vor Grafik- oder Bilderzeugung; nicht zum Erzeugen dekorativer Assets oder zum Verändern fachlicher Claims.
userFacing: false
implicitInvocation: true
version: 0.1.1
status: candidate
owners:
  - White Label Maintainer
requires:
  - multimodal-learning-analysis
outputs:
  - learning-visual-plan.json
lastEvaluated: 2026-08-28
---

# Learning Visual Planner

## Grundsatz

**Message first, visual second.** Ein Visual ist nur gerechtfertigt, wenn es Verständnis, Orientierung, Erinnerung oder sichere Ausführung verbessert.

## Repräsentationswahl

Bevorzugte Zuordnung:

| Lernproblem | Darstellung |
|---|---|
| Prozess / Reihenfolge | Flow, Step Diagram, Timeline |
| Ursache/Wirkung | Causal Diagram |
| Systemaufbau | Architecture / annotated schematic |
| Entscheidung | Decision Tree |
| Vergleich | Matrix / comparison table |
| Messdaten | Chart, nur bei echten Daten |
| UI-Handlung | gezielter Screenshot + Annotation |
| räumliche/physische Handlung | Illustration oder selektierter Quellframe |
| abstraktes Konzept | explanatory illustration |
| Wissensbeziehungen | Concept Map |

SVG/Diagramm wird bevorzugt, wenn Geometrie, Labels und Logik wichtiger sind als Fotorealismus.

## `learning-visual-plan.json`

Jedes Asset enthält mindestens:

```json
{
  "id": "V-01",
  "message": "...",
  "sourceClaims": ["C-01"],
  "timestamps": ["00:12:14"],
  "visualType": "process-diagram",
  "assetMode": "generated-svg",
  "labels": [],
  "altTextIntent": "...",
  "targetSurfaces": ["html", "pptx", "docx", "pdf"],
  "designRequirements": [],
  "evidenceRole": "explanatory"
}
```

## Source-Frame-Regel

Originalframes sind **Evidenzanker**, nicht Default-Illustrationen. Nutze sie nur, wenn der reale Zustand selbst relevant ist. Für übertragbare Lernlogik bevorzuge neu gezeichnete, sachlich abgeleitete Visuals.

## Visual-Claim-Fidelity

Ein Visual kann einen fachlich stärkeren Claim transportieren als seine Caption. Deshalb wird die Grafik selbst wie ein Claim-Träger geprüft.

Vor Rendering oder Freigabe müssen mindestens folgende visuelle Aussagen gegen dieselbe Evidenzbasis wie die Prosa geprüft werden:

- Labels und definierte Begriffe;
- Formeln, Quotienten, Nenner und Einheiten;
- Pfeile, Richtung, Kausalität und Reihenfolge;
- Mengen-/Größenverhältnisse, wenn sie semantische Bedeutung tragen;
- Kategorien, Entscheidungsgrenzen und Ergebniszustände;
- regulatorische oder klinische Geltungsbereiche;
- Trennung von aktuellem Standard, Forschung, Zukunftsszenario und strategischer Hypothese.

Eine vorsichtige Bildunterschrift kompensiert **keine** Grafik, deren visuelle Logik einen falschen, breiteren oder zeitlich weiter fortgeschrittenen Claim suggeriert. Wenn Current-State und Future/Research im selben Visual vorkommen, müssen sie visuell und sprachlich eindeutig getrennt werden.

Bei wissenschaftlich/regulatorisch kritischen Diagrammen soll das Planungsartefakt die prüfpflichtigen visuellen Claims explizit benennen, z. B. in `designRequirements` oder einem nachgelagerten Review-Record.

## Anti-Slop

Nicht planen:

- dekorative Stock-/AI-Bilder ohne Lernfunktion;
- beliebige Hero-Illustrationen, die keinen Claim transportieren;
- 3D-/Glassmorphism-Effekte ohne Informationswert;
- Text, der eigentlich HTML/SVG sein sollte, als Rasterbild;
- komplexe Diagramme nur um Fläche zu füllen;
- Farbvielfalt ohne semantische Rolle.

## Qualitätsgate

- jedes Visual besitzt eine klare Lernbotschaft;
- jeder fachliche Bestandteil ist auf Claims/Evidenz zurückführbar;
- Formeln, Nenner, Labels, Pfeile und Pfadgrenzen bestehen einen Visual-Claim-Fidelity-Check;
- aktuelle klinische/regulatorische Verwendung ist klar von Forschung, Zukunftsszenario und strategischer Hypothese getrennt;
- geeigneter Asset-Typ ist begründet;
- `evidenceRole` trennt `source`, `explanatory` und `illustrative-only`;
- target surfaces und DESIGN.md-Anforderungen sind vor Rendering bekannt.

## Abschluss

Abgeschlossen, wenn SVG- und Bildgeneratoren ein eindeutiges, evidenzgebundenes Briefing erhalten, ohne eigene fachliche Entscheidungen treffen zu müssen, und die geplante visuelle Logik keine stärkeren Claims als die zugrunde liegende Evidenz transportiert.
