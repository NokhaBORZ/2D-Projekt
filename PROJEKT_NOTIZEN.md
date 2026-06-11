# Projektnotizen

> Laufende Dokumentation größerer Änderungen gemäß `KI_Projekt_Guideline.md`.
> Neueste Notiz immer oben anfügen.

---

## [2026-06-11] Projektstruktur + Stage 1 (Preprocessing) + Stage 2 (Segmentierung)

### Kurzbeschreibung
Grundstruktur des Projekts angelegt (`src/`, `tests/`, `requirements.txt`) und die
ersten beiden Pipeline-Stufen implementiert: Vorverarbeitung und Hautfarben-Segmentierung.

### Betroffene Bereiche
- `src/preprocessing.py` (neu)
- `src/segmentation.py` (neu)
- `src/main.py` (neu, minimaler Einstiegspunkt zum visuellen Testen)
- `requirements.txt`, `.gitignore` (neu)

### Was wurde umgesetzt?
- **Stage 1:** Gauß-Filter zur Rauschunterdrückung, optionaler Histogrammausgleich
  (nur auf dem Y-Kanal, damit die Hauttöne nicht verschoben werden),
  Konvertierung nach HSV und YCbCr.
- **Stage 2:** Hautfarben-Schwellwert (Standard: YCbCr, alternativ HSV oder beide
  per UND-Verknüpfung), morphologisches Closing (Löcher füllen) gefolgt von
  Opening (Rauschblobs entfernen), danach Regionenmarkierung mit Auswahl der
  größten zusammenhängenden Komponente.
- **main.py:** Bild- und Live-Modus zeigen Eingabe, Binärmaske und maskierte Hand
  nebeneinander, um die Schwellwerte visuell abstimmen zu können.

### Warum wurde es so umgesetzt?
- YCbCr als Standard-Farbraum: Der Hautbereich liegt nur in den Chroma-Kanälen
  (Cr, Cb), der Helligkeitskanal Y bleibt unbeschränkt → robust gegen
  Beleuchtungsänderungen. HSV bleibt als Alternative wählbar.
- Histogrammausgleich ist standardmäßig aus: Er verändert nur Y, die
  Segmentierung arbeitet aber auf den Chroma-Kanälen — er bringt dort nichts
  und verstärkt in dunklen Bildern das Rauschen. Per Flag zuschaltbar.
- Reihenfolge Closing → Opening entspricht der Vorgabe aus `PROJECT_GOAL.md`:
  erst Löcher in der Hand schließen, dann kleine Störflächen entfernen.
- Größte Komponente statt aller Hautflächen: Gesicht oder Hintergrundflecken
  fallen so automatisch weg (Annahme: die Hand ist das größte Hautobjekt im Bild).

### Bezug zu Vorlesung / Skript / Buch
- Lect 04 (Filter): Gauß-Filter als linearer, separierbarer Glättungsfilter
- Lect 02/03 (Punktoperationen): Schwellwertbildung/Binarisierung, Histogrammausgleich
- Lect 10 (Farbräume): HSV- und YCbCr-Umrechnung, Chroma/Luminanz-Trennung
- Lect 07 (Morphologische Operationen): Closing `I•H`, Opening `I◦H`, Strukturelement
- Lect 08 (Regionen): Regionenmarkierung, Auswahl über Flächenmerkmal
- Extern (nur Zahlenwerte, nicht die Methode): Hautfarbbereich Cr∈[133,173],
  Cb∈[77,127] nach Chai & Ngan (1999) — im Code als extern gekennzeichnet.

### Wichtige Erkenntnisse
- Die Wahl des Farbraums ist die zentrale Designentscheidung der Segmentierung:
  Chroma-basierte Schwellwerte (YCbCr) trennen Hautfarbe von Helligkeit.
- Morphologie ersetzt kein gutes Thresholding — sie räumt nur auf.
- Die Maske ist die einzige Schnittstelle zu Stage 3: spätere Stufen brauchen
  nur das Binärbild, nicht das Farbbild.

### Relevanz für die Präsentation
- Folie „Pipeline-Überblick" mit den 5 Stufen und dem Datenfluss Bild → Maske.
- Folie „Warum YCbCr?" mit Beispielbild: gleiche Hand bei unterschiedlicher
  Beleuchtung, Maske bleibt stabil.
- Gutes Codebeispiel: `segment_hand()` — die komplette Stufe in 3 Zeilen,
  jede Zeile entspricht einem Vorlesungskonzept.

### Offene Punkte
- Hautfarb-Schwellwerte mit echten Testbildern verschiedener Hauttöne und
  Beleuchtungen prüfen und ggf. nachjustieren.
- Testbilder in `tests/` sammeln (verschiedene Gesten, Hintergründe).
- Entscheidung, ob Live-Modus die Maske zusätzlich glätten muss (Flackern).
