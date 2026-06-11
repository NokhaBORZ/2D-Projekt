| Histogrammanpassung |                  | Gammakorrektur    |     | EinführunginFilterung |
| ------------------- | ---------------- | ----------------- | --- | --------------------- |
|                     | Punktoperationen | II und Einführung |     | in                    |
Filterung
31
|     | 2D Computer | Vision, Vorlesung | No. |     |
| --- | ----------- | ----------------- | --- | --- |
M. O. Franz
1
fallsnichtandersvermerkt,sinddieAbbildungenentnommenausBurger&Burge,2005.

Histogrammanpassung Gammakorrektur EinführunginFilterung
Überblick
1 Histogrammanpassung
2 Gammakorrektur
3 Einführung in Filterung

Histogrammanpassung Gammakorrektur EinführunginFilterung
Übersicht
1 Histogrammanpassung
2 Gammakorrektur
3 Einführung in Filterung

| Histogrammanpassung |     |     | Gammakorrektur |     |     |     | EinführunginFilterung |
| ------------------- | --- | --- | -------------- | --- | --- | --- | --------------------- |
Histogrammanpassung
|     | Histogrammausgleich |     | führt | zu einem | gleichverteilten |     |     |
| --- | ------------------- | --- | ----- | -------- | ---------------- | --- | --- |
Histogramm.
|       | Gleichverteilung         | maximiert    |               | die in | einem       | Grauwertintervall |        |
| ----- | ------------------------ | ------------ | ------------- | ------ | ----------- | ----------------- | ------ |
|       | [0,K −1]                 | darstellbare | Information.  |        |             |                   |        |
|       | Aber: Bilder             | sehen        | unnatürlich   | aus,   | da          | die meisten       |        |
|       | natürlichen              | Bilder eher  | gaußverteilte |        | Histogramme |                   | haben. |
| Daher | Histogrammanpassung:     |              | Anpassung     |        |             | des Histogramms   |        |
| an    | eine Referenzverteilung. |              |               |        |             |                   |        |

| Histogrammanpassung             |     | Gammakorrektur    |     | EinführunginFilterung |
| ------------------------------- | --- | ----------------- | --- | --------------------- |
| Prinzip der Histogrammanpassung |     |                   |     |                       |
| Ziel:ModifiziereAusgangsbildI   |     | durcheinehomogene |     |                       |
A
| Punktoperationso,daßseineVerteilungsfunktionP |     |     | möglichstgut |     |
| --------------------------------------------- | --- | --- | ------------ | --- |
A
| mitP R einesReferenzbildesI |     | R übereinstimmt. |     |     |
| --------------------------- | --- | ---------------- | --- | --- |
2Schritte:
1 HistogrammwirddurchlinearenHistogrammausgleichineine
Gleichverteilungüberführt:
a(cid:48)
|     | I A | →I A(cid:48) : =P | A (a) |     |
| --- | --- | ----------------- | ----- | --- |
DasResultatwirdüberdieInverseP (a)−1 der
| 2   |     |     | R   |     |
| --- | --- | --- | --- | --- |
Referenzverteilungtransformiert:
|     | I →I      | : a(cid:48)(cid:48) =P | (a(cid:48))−1 |     |
| --- | --------- | ---------------------- | ------------- | --- |
|     | A(cid:48) | A(cid:48)(cid:48)      | R             |     |
Insgesamtalso:
|     | I →I                | : a(cid:48)(cid:48) =P−1(P | (a)) |     |
| --- | ------------------- | -------------------------- | ---- | --- |
|     | A A(cid:48)(cid:48) | R                          | A    |     |

Histogrammanpassung Gammakorrektur EinführunginFilterung
Stückweise lineare Referenzverteilung
ZwischenN vorgegebene
Stützstellen(i,q)wirdlinear
j j
interpoliert:
HomogenePunkttransformation:
Gesamttransformation:
I →I : a(cid:48)(cid:48) =P−1(P (a))
A A(cid:48)(cid:48) L A

| Histogrammanpassung |                     | Gammakorrektur |         | EinführunginFilterung |
| ------------------- | ------------------- | -------------- | ------- | --------------------- |
| Beispiel:           | Histogrammanpassung |                | an eine | stückweise            |
| lineare             | Verteilung          |                |         |                       |

| Histogrammanpassung |               |                       | Gammakorrektur |       |          | EinführunginFilterung |
| ------------------- | ------------- | --------------------- | -------------- | ----- | -------- | --------------------- |
| Anpassung           | an Histogramm |                       |                | eines | anderen  | Bildes                |
| Problem:            | Natürliche    | Verteilungsfunktionen |                |       | sind oft | nicht                 |
invertierbar.
Ansatz: Schrittweises ”Ausfüllen” der Referenzverteilung P (a)
R
D.h.: für einen geg. Pixelwert a wird der minimale Wert a(cid:48) in
| (a(cid:48)) |              |               |         |       | (a(cid:48)) |              |
| ----------- | ------------ | ------------- | ------- | ----- | ----------- | ------------ |
| P R         | gesucht, bei | dem           | P A (a) | ≤ P R | ist:        |              |
|             | f (a) =      | min{a(cid:48) | ∈ [0,K  | −1]|P | (a) ≤ P     | (a(cid:48))} |
|             | hs           |               |         |       | A R         |              |

| Histogrammanpassung |                     | Gammakorrektur |         | EinführunginFilterung |
| ------------------- | ------------------- | -------------- | ------- | --------------------- |
| Beispiel:           | Histogrammanpassung |                | an eine |                       |
Gaußverteilung

| Histogrammanpassung |                     | Gammakorrektur |                 | EinführunginFilterung |
| ------------------- | ------------------- | -------------- | --------------- | --------------------- |
| Beispiel:           | Histogrammanpassung |                | an Referenzbild |                       |

Histogrammanpassung Gammakorrektur EinführunginFilterung
Übersicht
1 Histogrammanpassung
2 Gammakorrektur
3 Einführung in Filterung

| Histogrammanpassung |     |     |     | Gammakorrektur |     |     |     |     | EinführunginFilterung |
| ------------------- | --- | --- | --- | -------------- | --- | --- | --- | --- | --------------------- |
Gammakorrektur
|     | Reale        | Aufnahmesysteme |               |                 | (Kameras, |       | Scanner,..)       | setzen    |     |
| --- | ------------ | --------------- | ------------- | --------------- | --------- | ----- | ----------------- | --------- | --- |
|     | Intensitäten | nicht           | 1:1           | in Grauwerte    |           | um.   | Die               | Abbildung | von |
|     | Intensitäten | Φ               | in Grauwerte  |                 | ist       | meist | eine nichtlineare |           |     |
|     | Funktion     | a = F(Φ).       |               |                 |           |       |                   |           |     |
|     | Ebenso       | setzen          | Ausgabegeräte |                 |           | (z.B. | Bildschirme)      |           |     |
|     | Grauwerte    | nicht           | 1:1           | in Helligkeiten |           | um.   | Auch              | hier gibt | es  |
Nichtlinearitäten.
|     | Grundidee       | der            | Gammakorrektur: |             |                  | Bilder        | werden     | durch | eine |
| --- | --------------- | -------------- | --------------- | ----------- | ---------------- | ------------- | ---------- | ----- | ---- |
|     | homogene        | Punktoperation |                 |             | so transfomiert, |               | daß        | die   |      |
|     | geräteabhängige |                | Nichtlinearität |             |                  | kompensiert   |            | wird. |      |
|     | Nach der        | Korrektur      |                 | entsprechen |                  | die Grauwerte |            | nicht | den  |
|     | absoluten       | Intensitäten,  |                 | aber        | ihr              | relatives     | Verhältnis |       | ist  |
|     | (idealerweise)  |                | gleich          | wie         | in der           | Wirklichkeit. |            |       |      |

| Histogrammanpassung | Gammakorrektur     | EinführunginFilterung |
| ------------------- | ------------------ | --------------------- |
| Belichtungskurve    | von fotografischem | Film                  |
BeleuchtungBistinlogarithmischenEinheiten,d.h.dieSchwärzung
desFilmsfolgtannäherndeinerlogarithmischenKurve.
DieSteigunginlogarithmischenKoordinatenwirddas”Gamma”des
Filmsgenannt.

Histogrammanpassung Gammakorrektur EinführunginFilterung
Die Gammafunktion
Gammafunktion:
b=f (a)=aγ γ >0
γ
γ heißtGammawert.
wirdnurimBereich[0,1]
eingesetzt,
Funktionswertaγ bleibtdamit
ebenfallsin[0,1].
Fürγ >1verläuftKurve
unterhalbderidentität,für
γ <1oberhalb.
InverseGammafunktion:
a=f−1(b)=b1/γ =f (b),
γ 1/γ
d.h.dieInversederGammafunktionistwiedereineGammafunktion.

| Histogrammanpassung |             | Gammakorrektur    | EinführunginFilterung |
| ------------------- | ----------- | ----------------- | --------------------- |
| Beispiel:           | Stufenkeile | bei verschiedenen | Gammawerten           |
|                     | γ = 0.5     | γ = 1.0           | γ = 2.0               |

| Histogrammanpassung |            |               | Gammakorrektur |         |             | EinführunginFilterung |
| ------------------- | ---------- | ------------- | -------------- | ------- | ----------- | --------------------- |
| Reale               | Gammawerte |               |                |         |             |                       |
|                     | Konkrete   | Gammawerte    | werden         | von den | Herstellern |                       |
|                     | aufgrund   | von Messungen | spezifiziert:  |         |             |                       |
Röhrenmonitore:1.8...2.8,typischist2.4.
LCD:ähnlichwieRöhrenmonitoredurchVoreinstellung
Video-undDigitalkameras:0.4...0.6,Emulationdes
BelichtungsverhaltensvonanalogenKameras
|     | Genormte | Geräte: |     |     |     |     |
| --- | -------- | ------- | --- | --- | --- | --- |
Fernsehen:2.2(NTSC),2.8(PAL)
Fernsehkameras:1/2.2=0.45beibeiden
InternationaleNormITU-RBT.709:2.5für
Wiedergabegeräte,1/1.956=0.51fürKameras
|     | Bei Computermonitoren |               | ist der               | Gammawert     | in    | bestimmten |
| --- | --------------------- | ------------- | --------------------- | ------------- | ----- | ---------- |
|     | Grenzen               | einstellbar.  |                       |               |       |            |
|     | Achtung:              | Modellierung  | über                  | Gammafunktion | ist   | nur eine   |
|     | grobe Näherung        | für           | das Transferverhalten |               | eines | Geräts.    |
|     | Für größere           | Genauigkeiten |                       | muß das Gerät | mit   | exakt      |
|     | vermessenen           | Profilen      | kalibriert            | werden.       |       |            |

Histogrammanpassung Gammakorrektur EinführunginFilterung
Anwendung der Gammakorrektur
Das(idealisierte)GerätsetztIntensitätenBinGrauwerteanach
a=Bγ um.DieGammakorrekturläuftübereinehomogene
PunktoperationmitdeminversenGammawert
b=f (a)=a1/γ.
1/γ
KorrigiertesSignal:b=a1/γ =(Bγ)1/γ =B.
MitSkalierungvon[0,a ]auf[0,1]undzurück:
max
(cid:18)
a
(cid:19)1/γ
b=f (a)=a .
1/γ max a
max

| Histogrammanpassung              | Gammakorrektur | EinführunginFilterung |
| -------------------------------- | -------------- | --------------------- |
| Geräteunabhängige Grauwertbilder |                |                       |

| Histogrammanpassung | Gammakorrektur | EinführunginFilterung |
| ------------------- | -------------- | --------------------- |
Beispiel: Gammakorrektur

| Histogrammanpassung |                | Gammakorrektur |     | EinführunginFilterung |
| ------------------- | -------------- | -------------- | --- | --------------------- |
| Modifizierte        | Gammakorrektur |                |     |                       |
Problem:
| 1 Fürγ | >1istf γ (a)beinahekonstant,alsonumerischschwer |     |     |     |
| ------ | ----------------------------------------------- | --- | --- | --- |
invertierbar.
| 2 Fürγ | <1gehtdieSteigungnahean0gegen∞,d.h.hohe |     |     |     |
| ------ | --------------------------------------- | --- | --- | --- |
VerstärkungdesRauschensderniedrigenIntensitätswerte
Daher:LinearerAbschnittnahe0,FortsetzungmitGammafunktion:
| mits= | γ undd | = 1 | −1. |     |
| ----- | ------ | --- | --- | --- |
aγ
| a0(γ−1)+a1 | −γ  | 0 (γ−1)+1 |     |     |
| ---------- | --- | --------- | --- | --- |
0

| Histogrammanpassung | Gammakorrektur | EinführunginFilterung |
| ------------------- | -------------- | --------------------- |
Modifizierte Gammafunktion
InverseKorrektur:

| Histogrammanpassung |              | Gammakorrektur | EinführunginFilterung |
| ------------------- | ------------ | -------------- | --------------------- |
| Beispiel:           | Modifizierte | Gammakorrektur | in Standards          |

Histogrammanpassung Gammakorrektur EinführunginFilterung
Übersicht
1 Histogrammanpassung
2 Gammakorrektur
3 Einführung in Filterung

| Histogrammanpassung |     |     | Gammakorrektur |     | EinführunginFilterung |
| ------------------- | --- | --- | -------------- | --- | --------------------- |
Filterung
| Beispiel: | Glättung             |              |                       |                |               |
| --------- | -------------------- | ------------ | --------------------- | -------------- | ------------- |
|           | Mit Punktoperationen |              | allein läßt           | sich keine     | Glättung oder |
|           | Schärfung            | eines Bildes | erzielen              | ⇒ Filterung    | notwendig,    |
|           | Auch Filterung       | ändert       | nicht die             | Bildgeometrie, | d.h. die      |
|           | Position             | der Pixel    | bleibt nach Filterung | unverändert.   |               |

| Histogrammanpassung |                 | Gammakorrektur | EinführunginFilterung |
| ------------------- | --------------- | -------------- | --------------------- |
| Beispiel:           | Glättungsfilter | (1)            |                       |
Idee:ErsetzejedenPixeldurchdenDurchschnittseiner
| Nachbarschaftp | 1 ,p 2 ...p 9 | :   |     |
| -------------- | ------------- | --- | --- |
1(cid:88) 9
I(cid:48)(u,v)←
p
9 i
i=1

Histogrammanpassung Gammakorrektur EinführunginFilterung
Beispiel: Glättungsfilter (2)
InrelativenBildkoordinaten:
Filtermerkmale:
ErgebniswirdnichtauseinemeinzigenPixelberechnet,
sondernauseinerMengevonPixeln.
DieKoordinatenderQuellpixelhabeeinefesterelativePosition
zumZielpixelundbildeni.A.einezusammenhängendeRegion.
Parameter:
GrößederFilterregion
FormderFilterregion
GewichtungderQuellpixel(konstantoderortsabhängig)

Histogrammanpassung Gammakorrektur EinführunginFilterung
Lineare Filter
LineareFilter:WertdesZielpixelswirdalsgewichteteSummeder
Quellpixelberechnet.
GrößeundFormderFilterregionundGewichtedesFilterwerden
durcheineMatrixvonFilterkoeffizientenspezifiziert,derFiltermatrix
H oderFiltermaske,z.B.
ij
DieFiltermatrixist-wieeinBild-eine
diskretezweidimensionaleFunktion.
Koordinatenwerdenmeistrelativzum
Zentrumangegeben(”hotspot”).

| Histogrammanpassung     | Gammakorrektur | EinführunginFilterung |
| ----------------------- | -------------- | --------------------- |
| Anwendung eines Filters |                |                       |

| Histogrammanpassung |                 |                  | Gammakorrektur |                       |               | EinführunginFilterung |
| ------------------- | --------------- | ---------------- | -------------- | --------------------- | ------------- | --------------------- |
| Praktische          | Implementierung |                  |                | von Filteroperationen |               |                       |
| Im Gegensatz        | zu              | Punktoperationen |                | ist bei               | Filtern keine | ”in                   |
| place”-Verarbeitung |                 | möglich,         | da             | die Quellpixel        | mehrere       | Male                  |
| benötigt            | werden.         |                  |                |                       |               |                       |

| Histogrammanpassung |             | Gammakorrektur        | EinführunginFilterung |
| ------------------- | ----------- | --------------------- | --------------------- |
| Beispiel:           | einfacher   | 3 × 3-Glättungsfilter |                       |
| ”Box”-Filter:       | 4 Schleifen |                       |                       |

| Histogrammanpassung |                          | Gammakorrektur        | EinführunginFilterung |
| ------------------- | ------------------------ | --------------------- | --------------------- |
| Beispiel            | 2: 3 × 3-Glättungsfilter | mit unterschiedlichen |                       |
Koeffizienten
Glockenförmiger
Glättungsfilter: