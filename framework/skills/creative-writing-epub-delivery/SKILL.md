---
name: creative-writing-epub-delivery
description: Liefert final freigegebene Science-Storytelling- oder Fiction-Manuskripte als ElevenReader-orientiertes EPUB3 aus, nachdem ein narrativer Hörbuchnutzer-Review bestanden wurde, und erzeugt genrespezifische Voice Guidance. Verwendet den generischen EPUB3-Renderer content-neutral; tatsächliche ElevenReader-Import- und Voice-Performance werden ohne realen Plattformtest nicht behauptet.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.2.0
status: candidate
owners:
  - White Label Maintainer
requires:
  - narrative-audiobook-listener-review
  - epub3-publication-renderer
  - artifact-production-contract
  - artifact-contract-audit
consumes:
  - artifact-production-contract.json
  - artifact-figure-contracts.json
  - artifact-contract-audit.json
  - artifact-contract-audit.md
  - narrative-listener-review.json
  - epub3-validation.json
outputs:
  - creative-writing.epub
  - creative-epub-delivery.json
  - creative-voice-guidance.md
lastEvaluated: 2026-09-06
---

# Creative Writing EPUB Delivery

## Zweck

Publikations-/Audiobook-Delivery für kreative Langformtexte. Der Skill verändert keine wissenschaftlichen Claims, keinen Fiction-Canon und keine literarische Stimme.

## Eingänge

Ein final freigegebener Manuskript-Ref, typischerweise:

- `science-story.md`; oder
- `fiction-manuscript.md`.

Der alternative Manuskript-Ref wird im Run Manifest festgehalten und deshalb nicht als statisches `consumes` modelliert.

## Ablauf

### 1. Manuskriptstatus prüfen

Science: Fidelity Gate muss bestanden sein.  
Fiction: Workshop/Revision und Continuity Gate müssen bestanden sein.

### 2. Narratives Hörbuch-Gate

`narrative-audiobook-listener-review` ausführen.

Nur `gateStatus=pass` erlaubt finale Auslieferung.

Science-Texte dürfen weiterhin fachlich dicht sein; Fiction darf nicht in Tutorial-Sprache geglättet werden.

### 3. Voice Guidance

`creative-voice-guidance.md` erzeugen:

- Sprache/Variante;
- gewünschte Erzählerrolle;
- Alter/Stimmcharakter nur als Voice-Design-Merkmal;
- Tempo;
- Artikulation;
- emotionale Bandbreite;
- Umgang mit Dialog;
- Aussprachehinweise für zentrale Eigennamen/Fachbegriffe;
- unerwünschte Eigenschaften.

Eine aktuell verfügbare ElevenReader-Stimme nur empfehlen, wenn ihre Verfügbarkeit im konkreten Lauf belastbar verifiziert ist. Andernfalls Voice-Design-Prompt liefern.

### 3.5 Author identity\n\nVor dem Rendering die Autorenidentität explizit festlegen. Falls eine owner-spezifische Pseudonym-Konvention existiert, muss das gewählte Pseudonym diese erfüllen und projektweit stabil bleiben. Für den Repository-Owner gilt [`docs/CREATIVE-AUTHOR-IDENTITY-CONVENTION.md`](../../docs/CREATIVE-AUTHOR-IDENTITY-CONVENTION.md).\n\nDas ausgewählte Pseudonym wird mindestens als EPUB-`dc:creator` gesetzt und in nachgelagerten Audiobook-/Publishing-Metadaten unverändert wiederverwendet. Eine Änderung des Pseudonyms erfolgt nur nach expliziter Nutzerentscheidung.\n\n### 4. EPUB3 rendern

`epub3-publication-renderer` ausführen.

Nach `structuralStatus=pass` darf das validierte Paket content-neutral als `creative-writing.epub` ausgeliefert werden.

### 5. ElevenReader Compatibility Status

`creative-epub-delivery.json` unterscheidet:

- `structural-pass`: EPUB3-Struktur intern validiert;
- `import-pass`: tatsächlicher ElevenReader-Import in diesem Lauf praktisch bestätigt;
- `voice-smoke-pass`: zusätzlich ein realer Hörtest der gewählten Stimme bestätigt;
- `not-tested`.

**Nie structural-pass als import-pass ausgeben.**

## Qualitätsgate

- **Listener Gate vor EPUB Release.**
- Keine Prosaänderung im Renderer.
- Science Fidelity/ Fiction Continuity müssen upstream bestanden sein.
- EPUB structural status muss `pass` sein.
- Eigennamen-/Fachwort-Aussprache-Risiken werden in Voice Guidance sichtbar gemacht.\n- Autorenidentität/Pseudonym ist vor Release explizit gesetzt; aktive owner-spezifische Namenskonventionen sind erfüllt.
- Aktuelle Voice-Verfügbarkeit nicht raten.
- Reale Plattformtests nur behaupten, wenn sie tatsächlich durchgeführt wurden.

## Run Manifest

```json
{
  "schemaVersion": 1,
  "manuscriptRef": "...",
  "manuscriptType": "science|fiction",\n  "authorName": "...",
  "listenerGateStatus": "pass",
  "epubValidationRef": "epub3-validation.json",
  "epubStructuralStatus": "pass",
  "elevenReaderCompatibility": "structural-pass|import-pass|voice-smoke-pass|not-tested",
  "voiceGuidanceRef": "creative-voice-guidance.md",
  "status": "pass|review|fail"
}
```

## Publication Contract und Drive-Release

Die Manuskript-/Projektentscheidungen werden nicht neu erfunden. Für publikationsspezifische materielle Entscheidungen (z. B. Cover/Visuals, Metadaten, Format-/Editierbarkeits- oder Delivery-Anforderungen) gilt `docs/ARTIFACT-PRODUCTION-CONTRACT.md`; ein bereits bestätigter Projekt-/Publikationsvertrag wird wiederverwendet und nur bei Delta-Bedarf nachgegrillt.

Vor Release wird die exakt zu publizierende EPUB-Revision mit `artifact-contract-audit` gegen den aktiven Vertrag geprüft.

Danach gilt `docs/DOCUMENT-ARTIFACT-DELIVERY-CONTRACT.md`: `creative-writing.epub` ist erst final ausgeliefert, wenn die exakt geprüfte Datei im kanonischen recipient-owned Google Drive gespeichert, read-back-verifiziert und als beobachteter Drive-Link zurückgegeben wurde. Eine lokale/Sandbox-Datei ist nur Zwischenstand.

## Abschluss

Abgeschlossen, wenn Listener Gate und EPUB-Struktur bestanden sind, `creative-writing.epub` und Voice Guidance vorliegen und der ElevenReader-Status exakt die tatsächlich geprüfte Ebene beschreibt.
