MorphologischeFilter MorphologischeGrundoperationen MorphologischeFilterfürGrauwertbilder
| Morphologische | Filter |     |
| -------------- | ------ | --- |
71
| 2D Computer | Vision, Vorlesung | No. |
| ----------- | ----------------- | --- |
M. O. Franz
1
fallsnichtandersvermerkt,sinddieAbbildungenentnommenausBurger&Burge,2005.

MorphologischeFilter MorphologischeGrundoperationen MorphologischeFilterfürGrauwertbilder
Übersicht
1 Morphologische Filter
2 Morphologische Grundoperationen
3 Morphologische Filter für Grauwertbilder

MorphologischeFilter MorphologischeGrundoperationen MorphologischeFilterfürGrauwertbilder
Übersicht
1 Morphologische Filter
2 Morphologische Grundoperationen
3 Morphologische Filter für Grauwertbilder

MorphologischeFilter MorphologischeGrundoperationen MorphologischeFilterfürGrauwertbilder
Nichtlineare Filter: Beispiel 3 x 3-Medianfilter
AbrundungvonEcken
KleineStrukturenverschwinden
beeinflußtwirddieFormderBildregionen
Ziel:NichtlineareFilterzurgezieltenFormveränderungvon
Bildstrukturen.

MorphologischeFilter MorphologischeGrundoperationen MorphologischeFilterfürGrauwertbilder
| Grundidee:                                           | schrumpfen | und wachsen |
| ---------------------------------------------------- | ---------- | ----------- |
| 1 SchrittweisesSchrumpfendurchEntfernenderRandpixel⇒ |            |             |
kleineBildstrukturenverschwinden.
| 2 ÜbriggebliebeneRegionenwiederwachsenlassen |     |     |
| -------------------------------------------- | --- | --- |

MorphologischeFilter MorphologischeGrundoperationen MorphologischeFilterfürGrauwertbilder
| Schrumpfen | und Wachsen | auf Pixelebene |
| ---------- | ----------- | -------------- |

MorphologischeFilter MorphologischeGrundoperationen MorphologischeFilterfürGrauwertbilder
| Nachbarschaften | bei rechteckigem | Bildraster |
| --------------- | ---------------- | ---------- |
4er-Nachbarschaft:dievierPixel,dieinhorizontalerund
vertikalerRichtungangrenzen.
8er-Nachbarschaft:4er-Nachbarschaft+vierdiagonalePixel

MorphologischeFilter MorphologischeGrundoperationen MorphologischeFilterfürGrauwertbilder
Binäre nichtlineare Filter
ÄhnlichwiebeimlinearenFilterwirddas
VerhalteneinesmorphologischenFilters
durcheinebinäreMatrixbeschrieben,
demsog.StrukturelementH mit
H(i,j)∈{0,1}.
BinärbilderundStrukturelementwerdenoftMengen2-dimensionaler
KoordinatenpaarederVordergrundpixelbeschrieben:
Q ={(u,v)|I(u,v)=1}
I

MorphologischeFilter MorphologischeGrundoperationen MorphologischeFilterfürGrauwertbilder
Operationen auf Binärbildern in Mengennotation
InvertierungI(u,v)→¬I(u,v)istäquivalentzurBildungder
Komplementärmenge:
Q =Q
¬I I
PunktweiseODER-OperationI ∨I ergibtdieVereinigungder
1 2
zugehörigenPunktemengenQ undQ :
1 2
Q =Q ∪Q
I1∨I2 I1 I2
PunktweiseUND-OperationI ∧I ergibtdieSchnittmengeder
1 2
zugehörigenPunktemengenQ undQ :
1 2
Q =Q ∩Q
I1∧I2 I1 I2
VereinfachteDarstellungI ∪I bedeutetQ ∪Q ,I bedeutetQ .
1 2 I1 I2 I

MorphologischeFilter MorphologischeGrundoperationen MorphologischeFilterfürGrauwertbilder
Übersicht
1 Morphologische Filter
2 Morphologische Grundoperationen
3 Morphologische Filter für Grauwertbilder

MorphologischeFilter MorphologischeGrundoperationen MorphologischeFilterfürGrauwertbilder
Dilatation
DilatationführtzumWachstumeinerBildregion:
I⊕H ={(u(cid:48),v(cid:48))=(u+i,v+j)|(u(cid:48),v(cid:48))∈Q ,(i,j)∈Q }.
I H
StrukturelementH wirdanjedemgesetztenBildpixelrepliziert(oder
umgekehrt).

MorphologischeFilter MorphologischeGrundoperationen MorphologischeFilterfürGrauwertbilder
Erosion
ErosionführtzumSchrumpfeneinerBildregion:
I(cid:9)H ={(u(cid:48),v(cid:48))|(u(cid:48)+i,v(cid:48)+j)∈Q ,(i,j),∀(i,j)∈Q }.
I H
EswerdennurdiePixelbeibehalten,umdieherumdas
StrukturelementvollständigindieBildregionhineinpaßt.

MorphologischeFilter MorphologischeGrundoperationen MorphologischeFilterfürGrauwertbilder
Aufgabe 8.1
BerechnenSiedieErgebnissefürdieDilatationunddieErosion
zwischendemfolgendenBinärbildunddenStrukturelementenH
1
undH :
2

MorphologischeFilter MorphologischeGrundoperationen MorphologischeFilterfürGrauwertbilder
| Eigenschaften | von Dilatation | und | Erosion | (1) |
| ------------- | -------------- | --- | ------- | --- |
DilatationundErosionbewirkenzwargegenteiligeEffekte,aber
siesindi.A.nichtzueinanderinvers(z.B.könnenwegerodierte
DetailsnichtdurcheineDilatationwiederhergestelltwerden).
EineDilatationdesVordergrundeskanndurcheineErosiondes
Hintergrundeserreichtwerdenundumgekehrt:
|     | I⊕H =I(cid:9)H | und | I(cid:9)H =I⊕H |     |
| --- | -------------- | --- | -------------- | --- |
Dilatationistkommutativ:
I⊕H =H⊕I
NeutralesElementderDilatation:
|     | I⊕δ =δ⊕I | =I, wobei | Q δ ={(0,0)} |     |
| --- | -------- | --------- | ------------ | --- |

MorphologischeFilter MorphologischeGrundoperationen MorphologischeFilterfürGrauwertbilder
| Eigenschaften | von Dilatation | und | Erosion | (2) |
| ------------- | -------------- | --- | ------- | --- |
Dilatationistassoziativ:
|     | (I ⊕I | )⊕I =I ⊕(I | ⊕I ) |     |
| --- | ----- | ---------- | ---- | --- |
|     | 1 1   | 3 1        | 2 3  |     |
EineDilatationmiteinemgroßenStrukturelement
| H =H | ⊕H ⊕···⊕H kannalsFolgevonmehrerenDilatationen |     |     |     |
| ---- | --------------------------------------------- | --- | --- | --- |
| 1    | 2 n                                           |     |     |     |
mitkleinenStrukturelementenH
i dargestelltwerden:
|     | I⊕H =(...((I⊕H | )⊕H | )⊕...)⊕H |     |
| --- | -------------- | --- | -------- | --- |
|     |                | 1   | 2        | n   |
Erosionistnichtkommutativ:
I(cid:9)H (cid:54)=H(cid:9)I
ZweifacheErosion:
|     | (I 1 (cid:9)I 2 | )(cid:9)I 3 =I 1 (cid:9)(I | 2 ⊕I 3 ) |     |
| --- | --------------- | -------------------------- | -------- | --- |

MorphologischeFilter MorphologischeGrundoperationen MorphologischeFilterfürGrauwertbilder
| Beispiel: | Isotrope | Strukturelemente |
| --------- | -------- | ---------------- |

MorphologischeFilter MorphologischeGrundoperationen MorphologischeFilterfürGrauwertbilder
| Beispiel: | Unterschiedliche | Größe des |
| --------- | ---------------- | --------- |
Strukturelements (1)

MorphologischeFilter MorphologischeGrundoperationen MorphologischeFilterfürGrauwertbilder
| Beispiel: | Unterschiedliche | Größe des |
| --------- | ---------------- | --------- |
Strukturelements (2)

MorphologischeFilter MorphologischeGrundoperationen MorphologischeFilterfürGrauwertbilder
| Beispiel: | Frei gestaltete | Strukturelemente | (1) |
| --------- | --------------- | ---------------- | --- |

MorphologischeFilter MorphologischeGrundoperationen MorphologischeFilterfürGrauwertbilder
| Beispiel: | Frei gestaltete | Strukturelemente | (2) |
| --------- | --------------- | ---------------- | --- |

MorphologischeFilter MorphologischeGrundoperationen MorphologischeFilterfürGrauwertbilder
| Beispiel: | Mehrfache | Anwendung | kleiner |
| --------- | --------- | --------- | ------- |
Strukturelemente

MorphologischeFilter MorphologischeGrundoperationen MorphologischeFilterfürGrauwertbilder
Beispiel: Outline
1.Erosionder
Randpixel:
I(cid:48) =I(cid:9)H
2.InversionI(cid:48) ⇒
Hintergrund+Randpixel
3.Schnittmengemit
Originalbild
B=I∩I(cid:48) =I∩I(cid:9)H
enthältnurdie
Randpixel.

MorphologischeFilter MorphologischeGrundoperationen MorphologischeFilterfürGrauwertbilder
| Zusammengesetzte |     | Operationen: |     | Opening | und |
| ---------------- | --- | ------------ | --- | ------- | --- |
Closing
Opening:ErosiongefolgtvonDilatationmitdemselbenH:
I◦H =(I(cid:9)H)⊕H
entferntkleineBildstrukturen.
Closing:DilatationgefolgtvonErosion:
I•H =(I⊕H)(cid:9)H
fülltLöcherundZwischenräumeinVordergrundstrukturen.
OpeningundClosingsindidempotent,d.h.jedeweitere
AnendungläßtdasBildunverändert:
|     | (I◦H)◦H | =I◦H | und (I•H)•H | =I•H |     |
| --- | ------- | ---- | ----------- | ---- | --- |
OpeningdesVordergrundesistäquivalentzuClosingdes
Hintergrundes(undumgekehrt):
|     |     | I◦H =I•H | und I•H | =I◦H |     |
| --- | --- | -------- | ------- | ---- | --- |

MorphologischeFilter MorphologischeGrundoperationen MorphologischeFilterfürGrauwertbilder
| Beispiel: | Opening | und Closing | (1) |
| --------- | ------- | ----------- | --- |

MorphologischeFilter MorphologischeGrundoperationen MorphologischeFilterfürGrauwertbilder
| Beispiel: | Opening | und Closing | (2) |
| --------- | ------- | ----------- | --- |

MorphologischeFilter MorphologischeGrundoperationen MorphologischeFilterfürGrauwertbilder
Übersicht
1 Morphologische Filter
2 Morphologische Grundoperationen
3 Morphologische Filter für Grauwertbilder

MorphologischeFilter MorphologischeGrundoperationen MorphologischeFilterfürGrauwertbilder
Strukturelemente für morphologische Operatoren auf
Grauwertbildern
StrukturelementewerdennichtalsPunktemengen,sondernals
diskrete2D-FunktionenmitbeliebigenreellenWertendefiniert:
H(i,j)∈R
ImUnterschiedzurlinearenFaltungbeeinflussenauchNullwertedas
Ergebnisunddürfendahernichtweggelassenwerden.LeereZellen
werdendurch×markiert:
MorphologischeOperatorenfürGrauwertbilderwerdenalsVarianten
desMaximum-bzw.Minimumfiltersrealisiert.

MorphologischeFilter MorphologischeGrundoperationen MorphologischeFilterfürGrauwertbilder
Grauwert-Dilatation
Grauwert-Dilatation:ErsetzePixeldurchMaximumderSummenaus
demStrukturelementH undderentsprechendenBildregionI:
(I⊕H)(u,v)= max{I(u+i,v+j)+H(i,j)}
(i,j)∈H

MorphologischeFilter MorphologischeGrundoperationen MorphologischeFilterfürGrauwertbilder
Grauwert-Erosion
Grauwert-Erosion:ErsetzePixeldurchMinimumderDifferenzenaus
demStrukturelementH undderentsprechendenBildregionI:
(I(cid:9)H)(u,v)= min {I(u+i,v+j)−H(i,j)}
(i,j)∈H

MorphologischeFilter MorphologischeGrundoperationen MorphologischeFilterfürGrauwertbilder
| Beispiel: | Grauwert-Dilatation | und -Erosion | (1) |
| --------- | ------------------- | ------------ | --- |

MorphologischeFilter MorphologischeGrundoperationen MorphologischeFilterfürGrauwertbilder
| Beispiel: | Grauwert-Dilatation | und -Erosion | (2) |
| --------- | ------------------- | ------------ | --- |

MorphologischeFilter MorphologischeGrundoperationen MorphologischeFilterfürGrauwertbilder
| Beispiel: | Grauwert-Opening | und -Closing | (1) |
| --------- | ---------------- | ------------ | --- |

MorphologischeFilter MorphologischeGrundoperationen MorphologischeFilterfürGrauwertbilder
| Beispiel: | Grauwert-Opening | und -Closing | (2) |
| --------- | ---------------- | ------------ | --- |

MorphologischeFilter MorphologischeGrundoperationen MorphologischeFilterfürGrauwertbilder
| Beispiel:   | Grauwert-Dilatation | und -Erosion | mit frei |
| ----------- | ------------------- | ------------ | -------- |
| gestalteten | Strukturelementen   | (1)          |          |

MorphologischeFilter MorphologischeGrundoperationen MorphologischeFilterfürGrauwertbilder
| Beispiel:   | Grauwert-Dilatation | und -Erosion | mit frei |
| ----------- | ------------------- | ------------ | -------- |
| gestalteten | Strukturelementen   | (2)          |          |

MorphologischeFilter MorphologischeGrundoperationen MorphologischeFilterfürGrauwertbilder
| Beispiel:   | Grauwert-Opening  | und -Closing | mit frei |
| ----------- | ----------------- | ------------ | -------- |
| gestalteten | Strukturelementen | (1)          |          |

MorphologischeFilter MorphologischeGrundoperationen MorphologischeFilterfürGrauwertbilder
| Beispiel:   | Grauwert-Opening  | und -Closing | mit frei |
| ----------- | ----------------- | ------------ | -------- |
| gestalteten | Strukturelementen | (2)          |          |