| Histogramme |     | Punktoperationen |     | Histogrammausgleich |
| ----------- | --- | ---------------- | --- | ------------------- |
Punktoperationen
21
|     | 2D Computer | Vision, Vorlesung | No. |     |
| --- | ----------- | ----------------- | --- | --- |
M. O. Franz
1
fallsnichtandersvermerkt,sinddieAbbildungenentnommenausBurger&Burge,2005.

Histogramme Punktoperationen Histogrammausgleich
Überblick
1 Histogramme
2 Punktoperationen
3 Histogrammausgleich

| Histogramme |     | Punktoperationen |     | Histogrammausgleich |
| ----------- | --- | ---------------- | --- | ------------------- |
Histogramme
Histogramme: Häufigkeitsverteilungen
| Histogramme | in Bildern: | Häufigkeiten | einzelner |     |
| ----------- | ----------- | ------------ | --------- | --- |
Intensitätswerte im Bild

| Histogramme           | Punktoperationen |             | Histogrammausgleich |
| --------------------- | ---------------- | ----------- | ------------------- |
| Histogramm eines      | Grauwertbildes   |             |                     |
| Bei Intensitätswerten | I(u,v) ∈ [0,K    | −1] hat das |                     |
Histogramm K Einträge.
| Histogrammeintrag | h(i) is definiert     | als   |     |
| ----------------- | --------------------- | ----- | --- |
|                   | h(i) = |{(u,v)|I(u,v) | = i}| |     |

| Histogramme | Punktoperationen | Histogrammausgleich |
| ----------- | ---------------- | ------------------- |
Beispiel Histogrammvektor
HistogrammvektoreinesBildesmit16möglichenIntensitätswerten

| Histogramme   |            | Punktoperationen | Histogrammausgleich |
| ------------- | ---------- | ---------------- | ------------------- |
| Eigenschaften | und Nutzen | von Histogrammen |                     |
VölligunterschiedlicheBilderkönnenidentischeHistogramme
haben.
Histogrammzeigt
Belichtung
Kontrast
Dynamik
Bildfehler

| Histogramme | Punktoperationen | Histogrammausgleich |
| ----------- | ---------------- | ------------------- |
Belichtung
| Unterbelichtung | korrekt | Überbelichtung |
| --------------- | ------- | -------------- |

| Histogramme |     | Punktoperationen |     | Histogrammausgleich |
| ----------- | --- | ---------------- | --- | ------------------- |
Kontrast
Kontrast:genutzterIntensitätsbereichimBild,d.h.
|     |      | I        | −I  |     |
| --- | ---- | -------- | --- | --- |
|     | I −I | oder max | min |     |
max min
I mean

Histogramme Punktoperationen Histogrammausgleich
Dynamik
Dynamik:AnzahlverschiedenerIntensitätswerteimBild
DiemaximaleDynamikwirddannerreicht,wennallezwischen
I undI liegendenGrauwerteimBildvorkommen.
min max
Dynamikkannnichtnachträglicherhöhtwerden

| Histogramme | Punktoperationen | Histogrammausgleich |
| ----------- | ---------------- | ------------------- |
Bildfehler
| Sättigung | Löcher | Spitzen |
| --------- | ------ | ------- |

| Histogramme  |                     | Punktoperationen |       | Histogrammausgleich |
| ------------ | ------------------- | ---------------- | ----- | ------------------- |
| Auswirkungen | von Bildkompression |                  | - GIF |                     |

| Histogramme  |                     | Punktoperationen |        | Histogrammausgleich |
| ------------ | ------------------- | ---------------- | ------ | ------------------- |
| Auswirkungen | von Bildkompression |                  | - JPEG |                     |

| Histogramme        |            | Punktoperationen             |           | Histogrammausgleich |
| ------------------ | ---------- | ---------------------------- | --------- | ------------------- |
| Histogramme        | für Bilder | mit mehr                     | als 8 Bit |                     |
| Binning:Zählungder |            | Beispiel:B=256bei14-Bit-Bild |           |                     |
IntensitätswerteinBIntervallen
[a,a ]:
j j+1
| h(i)=|{(u,v)|a | ≤I(u,v)<a | .}| |     |     |
| -------------- | --------- | --- | --- | --- |
|                | j         | j+1 |     |     |
BeigleichgroßenBinsergibtsich
| eineIntervallgrößek | =K/Bmit |     |     |     |
| ------------------- | ------- | --- | --- | --- |
B
a =jk .
j B
Implementierung:
(cid:22) B (cid:23)
j= I(u,v)
K

| Histogramme                 | Punktoperationen | Histogrammausgleich |
| --------------------------- | ---------------- | ------------------- |
| Histogramme von Farbbildern |                  |                     |

| Histogramme |            | Punktoperationen |     | Histogrammausgleich |
| ----------- | ---------- | ---------------- | --- | ------------------- |
| Kumulatives | Histogramm |                  |     |                     |
i
(cid:88)
|     | H(i) = | h(j) bzw. | H(i) = H(i−1)+h(i) |     |
| --- | ------ | --------- | ------------------ | --- |
j=0

Histogramme Punktoperationen Histogrammausgleich
Überblick
1 Histogramme
2 Punktoperationen
3 Histogrammausgleich

Histogramme Punktoperationen Histogrammausgleich
Punktoperationen
Punktoperationf:jederneuePixelwerthängtausschließlichvom
altenPixelwertab,unabhängigvonanderenPixelwertenimBild
I (u,v)←f(I (u,v),u,v).
neu alt
HomogenePunktoperation:f istunabhängigvondenBildkoordinaten
I (u,v)←f(I (u,v)).
neu alt
Beispiele:
ÄnderungvonKontrastundHelligkeit
AnwendungbeliebigerHelligkeitskurven
InvertierenundAddierenvonBildern
Schwellwertbildung
Gammakorrektur
RealisierungoftüberLookup-Tabellen(LUTs)

| Histogramme |                      |                | Punktoperationen |                 | Histogrammausgleich |
| ----------- | -------------------- | -------------- | ---------------- | --------------- | ------------------- |
| Änderung    | der                  | Bildintensität |                  |                 |                     |
|             | Kontraständerung:    |                | f c (a) = 1.5·a  |                 |                     |
|             | Helligkeitsänderung: |                | f b (a) = a+10   |                 |                     |
|             | Beschränkung         | (clamping):    | if (a            | > 255) a = 255; | bzw. if (a <        |
0) a = 0;
|     | Invertieren: | f inv (a) | = a max −a    |             |           |
| --- | ------------ | --------- | ------------- | ----------- | --------- |
|     | Schwellwert: | f (a)     | = a 0 für a < | a und f (a) | = a 1 für |
|     |              | th        |               | th th       |           |
a ≥ a
th

| Histogramme           | Punktoperationen | Histogrammausgleich |
| --------------------- | ---------------- | ------------------- |
| Schwellwertoperation: | Binarisierung    |                     |

| Histogramme |                         | Punktoperationen |       | Histogrammausgleich |
| ----------- | ----------------------- | ---------------- | ----- | ------------------- |
| Verlust von | Bildinformation/Dynamik |                  | durch |                     |
Pixeloperationen

Histogramme Punktoperationen Histogrammausgleich
Alpha-Blending
I(cid:48)(u,v)=αI (u,v)+
BG
(1−α)I (u,v)
FG

| Histogramme |     | Punktoperationen |     |     | Histogrammausgleich |
| ----------- | --- | ---------------- | --- | --- | ------------------- |
Automatische Kontrastanpassung
| Einfache   | Kontrastanpassung: |              | Dehne und | verschiebe |                |
| ---------- | ------------------ | ------------ | --------- | ---------- | -------------- |
| Histogramm | so, daß            | dunkelster   | Pixel a   | auf a ,    | hellster Pixel |
|            |                    |              |           | low min    |                |
| a high     | auf Maximalwert    | a max fällt: |           |            |                |
a −a
|     |                   |           | max    | min      |      |
| --- | ----------------- | --------- | ------ | -------- | ---- |
|     | f (a)             | = (a−a    | )      |          |      |
|     | ac                |           | low a  | −a       |      |
|     |                   |           | high   | low      |      |
|     | Problem: einzelne | Ausreißer | können | gesamtes | Bild |
beeinflussen.

| Histogramme  |                   | Punktoperationen |                  | Histogrammausgleich |
| ------------ | ----------------- | ---------------- | ---------------- | ------------------- |
| Automatische | Kontrastanpassung |                  | und Invertierung |                     |
(Beispiel)

| Histogramme |                                                    | Punktoperationen |               |     | Histogrammausgleich |
| ----------- | -------------------------------------------------- | ---------------- | ------------- | --- | ------------------- |
| Robuste     | Kontrastanpassung                                  |                  | mit Quantilen |     |                     |
| Seis        | ,s derAnteilderPixel,derinDunkel-bzw.Hellsättigung |                  |               |     |                     |
low high
übergehendarf,AistdieFlächedesBildesinPixeln.
|     | Quantile:         | ˆa = min{i|H(i)≥As |        | }        |      |
| --- | ----------------- | ------------------ | ------ | -------- | ---- |
|     |                   | low                |        | low      |      |
|     | ˆa                | = min{i|H(i)≤A(1−s |        | )}       |      |
|     |                   | high               |        | high     |      |
|     | Problem: einzelne | Ausreißer          | können | gesamtes | Bild |
beeinflussen.

| Histogramme | Punktoperationen | Histogrammausgleich |
| ----------- | ---------------- | ------------------- |
Linearer Histogrammausgleich
Ziel:BilddurchhomogenePunktoperationsoverändern,daßesein
gleichverteiltesHistogrammaufweist.GleichverteilteGrauwerte
habentheoretischdenhöchstenInformationsgehalt.

| Histogramme     |                        |                  |                  | Punktoperationen    |            |                    | Histogrammausgleich |
| --------------- | ---------------------- | ---------------- | ---------------- | ------------------- | ---------- | ------------------ | ------------------- |
| Näherungsweiser |                        |                  | linearer         | Histogrammausgleich |            |                    |                     |
|                 | Homogene               | Punktoperationen |                  |                     | können     | Histogrammeinträge |                     |
|                 | nur verschieben        |                  | oder             | zusammenfügen,      |            | nicht              | aber trennen.       |
|                 | Die Histogrammeinträge |                  |                  | werden              | so         | verschoben,        | daß sich            |
|                 | näherungsweise         |                  | ein keilförmiges |                     | Histogramm |                    | ergibt.             |

| Histogramme  |                          | Punktoperationen |     | Histogrammausgleich |
| ------------ | ------------------------ | ---------------- | --- | ------------------- |
| Häufigkeiten | und Wahrscheinlichkeiten |                  |     |                     |
SummederHistogrammeinträgeergibtdieBildflächeinPixeln:
(cid:88)
h(i)=A
i
NormalisiertesHistogramm(Wahrscheinlichkeitsverteilung):
h(i)
p(i)=
(cid:80)
h(k)
k
mit
(cid:88)
p(i)=1.
i
Diskrete(kumulative)Verteilungsfunktion:
|     |       | i i               |      |     |
| --- | ----- | ----------------- | ---- | --- |
|     |       | (cid:88) (cid:88) | h(j) |     |
|     | P(i)= | p(j)=             |      |     |
(cid:80)
h(k)
|     |     | j=0 j=0 | k   |     |
| --- | --- | ------- | --- | --- |
mit
K−1
(cid:88)
|     | P(0)=0 | und P(K−1)= | p(j)=1 |     |
| --- | ------ | ----------- | ------ | --- |
j=0

| Histogramme   |                | Punktoperationen | Histogrammausgleich |
| ------------- | -------------- | ---------------- | ------------------- |
| Ableitung der | Punktoperation |                  |                     |
FundamentaltheoremfürtransformierteZufallsvariablen(s.Papoulis,
1991)
WirdeineZufallsvariableamitWahrscheinlichkeitsverteilungp(a)mit
derPunkttransformationa(cid:48) =f(a)transformiert,soerhältmandie
neueWahrscheinlichkeitsverteilung
p(a)
p(a(cid:48))=
|d
f(a)|
da
FürdiePunktoperationmitderkumulativenVerteilungsfunktion
(cid:90) a
|     | a(cid:48) =f(a)= | p(x)dx |     |
| --- | ---------------- | ------ | --- |
0
erhältman
|     | d         | p(a)              |     |
| --- | --------- | ----------------- | --- |
|     | f(a)=p(a) | und p(a(cid:48))= | =1, |
|     | da        | p(a)              |     |
alsoeineGleichverteilungderGrauwerte.

| Histogramme |                | Punktoperationen |     |                     | Histogrammausgleich |
| ----------- | -------------- | ---------------- | --- | ------------------- | ------------------- |
| Homogene    | Punktoperation |                  | für | Histogrammausgleich |                     |
|             |                | (cid:90) a       |     | (cid:22)            | (cid:23)            |
K−1
| ideal: | f(a)= | p(w)dw | praktisch: | f (a)= H(a) |     |
| ------ | ----- | ------ | ---------- | ----------- | --- |
|        |       |        |            | eq          | A   |
0