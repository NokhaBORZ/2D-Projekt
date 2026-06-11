LineareFilter FormaleEigenschaftenlinearerFilter NichtlineareFilter
Filter
2D Computer Vision, Vorlesung No. 41
M. O. Franz
1
fallsnichtandersvermerkt,sinddieAbbildungenentnommenausBurger&Burge,2005.

LineareFilter FormaleEigenschaftenlinearerFilter NichtlineareFilter
Übersicht
| 1 Lineare      | Filter        |                 |
| -------------- | ------------- | --------------- |
| 2 Formale      | Eigenschaften | linearer Filter |
| 3 Nichtlineare | Filter        |                 |

LineareFilter FormaleEigenschaftenlinearerFilter NichtlineareFilter
Übersicht
| 1 Lineare      | Filter        |                 |
| -------------- | ------------- | --------------- |
| 2 Formale      | Eigenschaften | linearer Filter |
| 3 Nichtlineare | Filter        |                 |

LineareFilter FormaleEigenschaftenlinearerFilter NichtlineareFilter
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

LineareFilter FormaleEigenschaftenlinearerFilter NichtlineareFilter
Anwendung eines Filters
I(cid:48)(u,v)= (cid:80) (cid:80) ·I(u+i,v+j)H(i,j)
i j

LineareFilter FormaleEigenschaftenlinearerFilter NichtlineareFilter
| Praktische          | Implementierung     | von Filteroperationen |                   |
| ------------------- | ------------------- | --------------------- | ----------------- |
| Im Gegensatz        | zu Punktoperationen | ist bei               | Filtern keine ”in |
| place”-Verarbeitung | möglich,            | da die Quellpixel     | mehrere Male      |
| benötigt            | werden.             |                       |                   |

LineareFilter FormaleEigenschaftenlinearerFilter NichtlineareFilter
| Beispiel: | 3 × 3-Glättungsfilter | mit unterschiedlichen |
| --------- | --------------------- | --------------------- |
Koeffizienten
Glockenförmiger
Glättungsfilter:

LineareFilter FormaleEigenschaftenlinearerFilter NichtlineareFilter
Ganzzahlige Filterkoeffizienten
Oftistesvorteilhafter,mitganzzahligenFilterkoeffizientenzu
arbeiten:
keineUmwandlungundSpeicherungdesBildesin
Gleitkommaformatnotwendig
aufmanchenRechnerarchitekturensindGanzzahloperationen
schneller.
aufFPGAssindGleitkommaoperationenextremaufwendig.
RealisierungübereinenSkalierungsfaktor,z.B.

LineareFilter FormaleEigenschaftenlinearerFilter NichtlineareFilter
Beispiel: ganzzahliger (2K + 1) × (2L + 1)-Filter
Typisch:
ungeradzahlige
Größe
zentriert

LineareFilter FormaleEigenschaftenlinearerFilter NichtlineareFilter
Behandlung von Randproblemen bei Filtern
nurZentralbereichauswerten,beidemdieFiltermaskeganzins
Bildpasst⇒Outputbildwirdkleiner.
Zeropadding:Inputbildwirdum0erweitert⇒In-undOutputbild
gleichgroß.
GespiegelteRandbedingungen
KonstanteRandbedingungen

LineareFilter FormaleEigenschaftenlinearerFilter NichtlineareFilter
Beispiel: Randbedingungen

LineareFilter FormaleEigenschaftenlinearerFilter NichtlineareFilter
| Beispiele | für lineare | Filter |
| --------- | ----------- | ------ |

LineareFilter FormaleEigenschaftenlinearerFilter NichtlineareFilter
Übersicht
| 1 Lineare      | Filter        |                 |
| -------------- | ------------- | --------------- |
| 2 Formale      | Eigenschaften | linearer Filter |
| 3 Nichtlineare | Filter        |                 |

LineareFilter FormaleEigenschaftenlinearerFilter NichtlineareFilter
Lineare Faltung
Fürdiskrete2-dimensionaleFunktionenI undH
∞ ∞
(cid:88) (cid:88)
I(cid:48)(u,v)= I(u−i,v−j)·H(i,j)
i=−∞j=−∞
kurz: I(cid:48) =I∗H

LineareFilter FormaleEigenschaftenlinearerFilter NichtlineareFilter
| Faltung und Korrelation |     |     |
| ----------------------- | --- | --- |
BisherigeNotationfürInputbildI undFilterkernH:lineareKorrelation
(cid:98)K/2(cid:99) (cid:98)L/2(cid:99)
I(cid:48)(u,v)= (cid:88) (cid:88)
I(u+i,v+j)·H(i,j)
i=−(cid:98)K/2(cid:99)j=−(cid:98)L/2(cid:99)
| DefinitionFaltung(mitR:BereichvonH |     | mitH(i,j)(cid:54)=0): |
| ---------------------------------- | --- | --------------------- |
∞ ∞
| (cid:88)        | (cid:88)          | (cid:88)            |
| --------------- | ----------------- | ------------------- |
| I(cid:48)(u,v)= | I(u−i,v−j)·H(i,j) | = I(u−i,v−j)·H(i,j) |
i=−∞j=−∞ i,j∈R
(cid:88)
= I(u+i,v+j)·H(−i,−j)
i,j∈R
d.h.FaltungentsprichtKorrelationmitgespiegelterFiltermatrix.

LineareFilter FormaleEigenschaftenlinearerFilter NichtlineareFilter
Eigenschaften der Faltung
Kommutativität:
I∗H = H∗I
Linearität:
| (a·I)∗H | = I∗(a·H)    | = a·(I∗H) |
| ------- | ------------ | --------- |
| (I +I   | )∗H = I ∗H+I | ∗H        |
| 1       | 2 1          | 2         |
aber:
| (b+I)∗H | (cid:54)= b+I∗H |     |
| ------- | --------------- | --- |
Assoziativität:
| A∗(B∗C) | = (A∗B)∗C |     |
| ------- | --------- | --- |

LineareFilter FormaleEigenschaftenlinearerFilter NichtlineareFilter
Separable Filter
AusderAssoziativitätergibtsich,daßeingroßerFilterH inmehrere
kleineFilterH zerlegtwerdenkann:
i
I∗H =I∗(H ∗H ∗...)=(...((I∗H )∗H )∗...)
1 2 1 2
Insbesonderebei2eindimensionalenFilterninx-undy-Richtung
(x/y-Separabilität),z.B
 
1
H x =[ 1 1 1 1 1 ] bzw. H y = 1 
1
ergibtsich
I(cid:48) =(I∗H )∗H =I∗(H ∗H )=I∗H
x y x y xy
 
1 1 1 1 1
z.B. H xy =H x ∗H y = 1 1 1 1 1  d.h.8statt15Operationen
1 1 1 1 1

LineareFilter FormaleEigenschaftenlinearerFilter NichtlineareFilter
| Beispiele | für separable | Filter |
| --------- | ------------- | ------ |
ZweidimensionaleFiltersind
separabel,wennsieals
äußeresProduktgeschrieben
werdenkönnen:
| H xy (i,j)=H | x (i)·H y (j) |     |
| ------------ | ------------- | --- |
Beispiel:Gaußfilter
e−x2 y2
| G (x,y) | = +           |     |
| ------- | ------------- | --- |
| xy      | 2 σ2          |     |
|         | 2 2           |     |
|         | = e− x ·e− y  |     |
|         | 2 σ 2 2 σ 2   |     |
|         | = G (x)·G (y) |     |
|         | x y           |     |
[Kienzleetal.,2002]

LineareFilter FormaleEigenschaftenlinearerFilter NichtlineareFilter
Dirac-Funktion
DieImpuls-oderDirac-Funktionδ istdasneutraleElementder
Faltung
I∗δ =I
Definition(zweidimensional,diskret):
(cid:26)
1 füri=j=0
δ(i,j)=
0 sonst.

LineareFilter FormaleEigenschaftenlinearerFilter NichtlineareFilter
| Dirac-Funktion | als neutrales          | Element       | der Faltung |
| -------------- | ---------------------- | ------------- | ----------- |
| Die Faltung    | mit der Impulsfunktion | ergibt wieder | das         |
| ursprüngliche  | Bild.                  |               |             |

LineareFilter FormaleEigenschaftenlinearerFilter NichtlineareFilter
Impulsantwort
Die Impulsfunktion als Input eines linearen Filters liefert die
| Filterfunktion | H als Ergebnis. |              |                     |
| -------------- | --------------- | ------------ | ------------------- |
| Ein Impuls     | charakterisiert | ein lineares | System vollständig! |

LineareFilter FormaleEigenschaftenlinearerFilter NichtlineareFilter
Übersicht
| 1 Lineare      | Filter        |                 |
| -------------- | ------------- | --------------- |
| 2 Formale      | Eigenschaften | linearer Filter |
| 3 Nichtlineare | Filter        |                 |

LineareFilter FormaleEigenschaftenlinearerFilter NichtlineareFilter
| Rauschunterdrückung | mit linearen | Filtern |
| ------------------- | ------------ | ------- |
Lineare Glättungsfilter reduzieren zwar das Rauschen im Bild,
aber gleichzeitig werden Kanten oder Linien verbreitert und im
Kontrast reduziert.

LineareFilter FormaleEigenschaftenlinearerFilter NichtlineareFilter
Nichtlineare Filter
NichtlineareFilterwerdensowielineareFilterübereineUmgebungR
desZielpixelsmiteinernichtlinearenFunktionf :R→Rberechnet:
I(cid:48)(u,v)=f(I(u,v),I(u+1,v),I(u−1,v),I(u,v+1),...)
z.B.Minimum-undMaximumfilter:
I(cid:48)(u,v) = min{I(u+i,v+j)|i,j∈R}
I(cid:48)(u,v) = max{I(u+i,v+j)|i,j∈R}

LineareFilter FormaleEigenschaftenlinearerFilter NichtlineareFilter
| Beispiel: | Minimum- | und | Maximumfilter | auf |     |
| --------- | -------- | --- | ------------- | --- | --- |
Salt-and-Pepper-Rauschen
| Minimumfilter | eliminiert    | weiße | Punkte und     | verbreitert | dunkle |
| ------------- | ------------- | ----- | -------------- | ----------- | ------ |
| Regionen,     | Maximumfilter | macht | das Gegenteil. |             |        |

LineareFilter FormaleEigenschaftenlinearerFilter NichtlineareFilter
Medianfilter
DerMedianfilterersetztjedenPixeldurchdenMedianseiner
UmgebungR.Bei2k+1aufsteigendsortiertenPixelnistderMedian
definiertals
|                                    | median{p | ,p ,...,p ,...,p | }=p ,  |         |
| ---------------------------------- | -------- | ---------------- | ------ | ------- |
|                                    |          | 0 1 k            | 2k k   |         |
| bei2kaufsteigendsortiertenPixeln{p |          | ,...,p           | }als(p | +p )/2. |
|                                    |          | 0                | 2k−1   | k−1 k   |

LineareFilter FormaleEigenschaftenlinearerFilter NichtlineareFilter
Beispiel: 3 × 3-Medianfilter

LineareFilter FormaleEigenschaftenlinearerFilter NichtlineareFilter
Vergleich linearer Glättungs- und Medianfilter
DerlineareFilterdämpftdasRauschen,machtaberdasBild
unscharf.
DerMedianfiltereliminiertSpitzen/Höhen,erzeugtörtlich
FleckenmitkonstanterIntensität.

LineareFilter FormaleEigenschaftenlinearerFilter NichtlineareFilter
Gewichteter Medianfilter
Grundidee:WertwirdindersortiertenListesooftwiederholt,wie
(cid:80)
seinGewichtist,d.h.dieListewirddadurchL= W(i,j)lang.
i,j∈R
Beispiel:

LineareFilter FormaleEigenschaftenlinearerFilter NichtlineareFilter
| Weitere | nichtlineare   | Filter... |     |     |     |
| ------- | -------------- | --------- | --- | --- | --- |
|         | Morphologische | Filter    |     |     |     |
Interest-Point-Detektoren
Volterra-Filter:
(cid:90)
|     | h(0)+  | h(1)(τ |     |     |     |
| --- | ------ | ------ | --- | --- | --- |
|     | y(t) = | )x(t−τ | )dτ |     |     |
|     |        | 1      | 1 1 |     |     |
R
(cid:90)
|     | +   | h(2)(τ ,τ )x(t−τ | )x(t−τ | )dτ dτ |     |
| --- | --- | ---------------- | ------ | ------ | --- |
|     |     | 1 2              | 1 2    | 1 2    |     |
R2
(cid:90)
|     | +   | h(3)(τ ,τ ,τ )x(t−τ | )x(t−τ | )x(t−τ )dτ dτ | dτ  |
| --- | --- | ------------------- | ------ | ------------- | --- |
|     |     | 1 2 3               | 1      | 2 3 1         | 2 2 |
R3
+···