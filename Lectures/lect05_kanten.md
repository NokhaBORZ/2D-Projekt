| KantenundGradienten |        | FilterzurKantendetektion |     | Kantenschärfung |
| ------------------- | ------ | ------------------------ | --- | --------------- |
|                     | Kanten | und Konturen             |     |                 |
51
|     | 2D Computer | Vision, Vorlesung | No. |     |
| --- | ----------- | ----------------- | --- | --- |
M. O. Franz
1
fallsnichtandersvermerkt,sinddieAbbildungenentnommenausBurger&Burge,2005.

KantenundGradienten FilterzurKantendetektion Kantenschärfung
Übersicht
1 Kanten und Gradienten
2 Filter zur Kantendetektion
3 Kantenschärfung

KantenundGradienten FilterzurKantendetektion Kantenschärfung
Übersicht
1 Kanten und Gradienten
2 Filter zur Kantendetektion
3 Kantenschärfung

KantenundGradienten FilterzurKantendetektion Kantenschärfung
Kanten
KantenspieleneinedominanteRolleimmenschlichenSehen:
Bildinhaltistbereitserkennbar,wennnurwenigeKonturen
sichtbarsind(s.Karikaturen).
SubjektiverSchärfeeindruckeinesBildesstehtindirektem
ZusammenhangmitseinerKantenstruktur.
EinBildkann(beinahe)vollständigausKantenrekonstruiert
werden.

KantenundGradienten FilterzurKantendetektion Kantenschärfung
Kanten und Ableitungen
KantensindBildorte,andenensichdieIntensitätaufkleinemRaum
starkverändert.
DieIntensitätsänderungbezogenaufdieBilddistanzwirddurchdie
AbleitungderBildintensitätgemessen.IneinerDimension(z.B.
entlangeinerBildzeile):
df(u)
f(cid:48)(u)=
du

| KantenundGradienten |           | FilterzurKantendetektion |         | Kantenschärfung |
| ------------------- | --------- | ------------------------ | ------- | --------------- |
| Genäherte           | Ableitung | auf diskreten            | Gittern |                 |
Näherungdurchsog.endlicheDifferenzen(finitedifference
schemes),z.B.
df(u) 1
|     | ≈ (f(u+1)−f(u−1)) | symmetrischerGradient |     |     |
| --- | ----------------- | --------------------- | --- | --- |
du 2
df(u)
|     | ≈ f(u)−f(u−1) | Rückwärtsgradient |     |     |
| --- | ------------- | ----------------- | --- | --- |
du
df(u)
|     | ≈ f(u+1)−f(u) | Vorwärtsgradient |     |     |
| --- | ------------- | ---------------- | --- | --- |
du

| KantenundGradienten |           |     |     | FilterzurKantendetektion |     |     | Kantenschärfung |
| ------------------- | --------- | --- | --- | ------------------------ | --- | --- | --------------- |
| Partielle           | Ableitung |     | und | Gradient                 |     |     |                 |
PartielleAbleitung:AbleitungeinermehrdimensionalenFunktion(hier
dasBildI(u,v))entlangeinerderKoordinatenrichtungen
|     |     | ∂I      |     |            | ∂I      |        |     |
| --- | --- | ------- | --- | ---------- | ------- | ------ | --- |
|     |     | (u,v)=∂ |     | I(u,v) und | (u,v)=∂ | I(u,v) |     |
|     |     | ∂u      | u   |            | ∂v      | v      |     |
Gradient:VektorderpartiellenAbleitungen
|     |     |     |          | (cid:20) | (cid:21)   |     |     |
| --- | --- | --- | -------- | -------- | ---------- | --- | --- |
|     |     |     |          |          | ∂ I(u,v)   |     |     |
|     |     |     | ∇I(u,v)= |          | u          |     |     |
|     |     |     |          |          | ∂ v I(u,v) |     |     |
DerBetragdesGradienten
(cid:113)
|     |     |     | |∇I|= | (∂ I(u,v))2+(∂ | I(u,v))2 |     |     |
| --- | --- | --- | ----- | -------------- | -------- | --- | --- |
|     |     |     |       | u              | v        |     |     |
istunbhängigvonderOrientierungderBildstruktur.

KantenundGradienten FilterzurKantendetektion Kantenschärfung
Ableitungsfilter
Realisierungdes
symmetrischenGradienten
alsFilter:
H = [ −0.5 0 0.5 ]
x
= 0.5·[ −1 0 1 ]
   
−0.5 −1
H y = 0 =0.5 0 
0.5 1

KantenundGradienten FilterzurKantendetektion Kantenschärfung
Übersicht
1 Kanten und Gradienten
2 Filter zur Kantendetektion
3 Kantenschärfung

| KantenundGradienten |     |     |     |     | FilterzurKantendetektion |     |     | Kantenschärfung |
| ------------------- | --- | --- | --- | --- | ------------------------ | --- | --- | --------------- |
Prewitt-Operator
GradientenfilterhabenHochpaßeigenschaftenundverstärken
dadurchdasBildrauschen.DaherwirdbeimPrewitt-Operatorüber
jeweils3Zeilenbzw.Spaltengemittelt:
|     |     |       |      |    |     |        |      |    |
| --- | --- | ------ | ---- | --- | --- | ------ | ----- | --- |
|     |     |        | −1 0 | 1   |     |        | −1 −1 | −1  |
|     |     | H P = | −1   |     |     | H P = |       |     |
|     |     | x      | 0    | 1  | und | y      | 0 0   | 0  |
|     |     |        | −1 0 | 1   |     |        | 1 1   | 1   |
DerPrewitt-Operatoristseparabel:
|     |     |        |     |     |       |     |              |   |
| --- | --- | -------- | --- | --- | ----- | --- | ------------ | --- |
|     |     | 1        |     |     |       |     |              | −1  |
|     | H P | = 1 ∗[ | −1  | 0 1 | ] und | H P | =[ 1 1 1 ]∗ | 0  |
|     | x   |          |     |     |       | y   |              |     |
|     |     | 1        |     |     |       |     |              | 1   |
d.h.zuerstGlättungüberBoxfilter,dannAbleitung(oderumgekehrt).
|     |     |     |     |          |     | (cid:20) | (cid:21) |     |
| --- | --- | --- | --- | -------- | --- | -------- | -------- | --- |
|     |     |     |     |          | 1   | HP∗I     |          |     |
|     |     |     |     | ∇I(u,v)≈ |     | x        |          |     |
HP∗I
|     |     |     |     |     | 6   | y   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

| KantenundGradienten |     |     |     | FilterzurKantendetektion |     |     | Kantenschärfung |
| ------------------- | --- | --- | --- | ------------------------ | --- | --- | --------------- |
Sobel-Operator
ÄhnlichwiePrewitt-Operator,abermitstärkererGewichtungder
zentralenZeilebzw.Spalte
|     |     |        |     |        |         |     |    |
| --- | --- | ------- | --- | ------- | -------- | --- | --- |
|     |     | −1      | 0   | 1       | −1       | −2  | −1  |
|     | H   | S = −2 | 0   | 2  und | H S = 0 | 0   | 0  |
|     |     | x       |     |         | y        |     |     |
|     |     | −1      | 0   | 1       | 1        | 2   | 1   |
DerSobel-Operatoristebenfallsseparabel:
|     |       |    |     |     |         |     |   |
| --- | ------ | --- | --- | --- | ------- | --- | --- |
|     |        | 1   |     |     |         |     | −1  |
|     | H S = | ∗[ | −1  | ]   | H S =[  | ]∗ |     |
|     | x      | 2   | 0   | 1   | und y 1 | 2 1 | 0  |
|     |        | 1   |     |     |         |     | 1   |
d.h.GlättungmitstärkererGewichtungderMitte.
|     |     |     |          |     | 1 (cid:20) HS∗I (cid:21) |     |     |
| --- | --- | --- | -------- | --- | ------------------------ | --- | --- |
|     |     |     | ∇I(u,v)≈ |     | x                        |     |     |
|     |     |     |          |     | 8 HS∗I                   |     |     |
y

| KantenundGradienten       |               | FilterzurKantendetektion |        |           | Kantenschärfung |
| ------------------------- | ------------- | ------------------------ | ------ | --------- | --------------- |
| Kantenstärke              | und -richtung |                          |        |           |                 |
| SkalierteGradientenwerte: |               | D (u,v)=H                | ∗I und | D (u,v)=H | ∗I              |
|                           |               | x                        | x      | y         | y               |
(cid:113)
|     | Kantenstärke: | E(u,v)= | D (u,v)2+D | (u,v)2 |     |
| --- | ------------- | ------- | ---------- | ------ | --- |
|     |               |         | x          | y      |     |
D (u,v)
|     |     |     | Φ(u,v)=tan−1 | y   |     |
| --- | --- | --- | ------------ | --- | --- |
LokaleKantenrichtung:
D (u,v)
x

| KantenundGradienten |     | FilterzurKantendetektion |     |     | Kantenschärfung |
| ------------------- | --- | ------------------------ | --- | --- | --------------- |
Roberts-Operator
Extremkleine2×2-FiltermitgeringerRichtungsselektivität
|     | (cid:20) | (cid:21) | (cid:20) | (cid:21) |     |
| --- | -------- | -------- | -------- | -------- | --- |
|     |          | 0 1      | −1       | 0        |     |
|     | HR =     | und      | HR =     |          |     |
|     | 1 −1     | 0        | 2        | 0 1      |     |

KantenundGradienten FilterzurKantendetektion Kantenschärfung
Kompass-Operatoren
Tradeoff:jespezifischereinFilterKantenvonanderenBildstrukturen
unterscheidet,destoengeristderWinkelbereich,aufdener
anspricht.
Kirsch-Operator:
Nur4der8Filtermüssen
tatsächlichberechnetwerden,
dennHK bisHK sindbisauf
4 7
dasVorzeichenidentischmit
HK bisHK.
0 3
Deramstärksten(positiv)
reagierendeFilterjbestimmt
dieKantenrichtung
π
ΦK(u,v) j.
4

KantenundGradienten FilterzurKantendetektion Kantenschärfung
Kantendetektion mit der zweiten Ableitung
DiebisherigenKantenoperatorenmessennurdieersteAbleitung.
ProblematischsinddabeiKantenmiteinemlangsamen
Helligkeitswechsel,diesichdamitnichtgenaulokalisierenlassen.
Alternative:Bestimmungdes
Nulldurchgangsderzweiten
Ableitung.
DadiezweiteAbleitungnoch
empfindlichergegenRauschen
ist,mußdasBildgleichzeitig
geglättetwerden.

| KantenundGradienten |     |     | FilterzurKantendetektion |     |     | Kantenschärfung |
| ------------------- | --- | --- | ------------------------ | --- | --- | --------------- |
Laplace-Operator
Laplace-Operator:SpurderHesse-MatrixderzweitenAbleitungen
|     |           | ∂2f    | ∂2f      |           |        |     |
| --- | --------- | ------ | -------- | --------- | ------ | --- |
|     | ∇2f(x,y)= | (x,y)+ | (x,y)=∂2 | f(x,y)+∂2 | f(x,y) |     |
|     |           | ∂x2    | ∂y2      | xx        | yy     |     |
DiskreteNäherungfürzweiteAbleitung:
 
1
|     | ∂ 2 ≈H | L =[ 1 | −2 1 ] und | ∂ 2 ≈H L | = −2 |    |
| --- | ------ | ------ | ---------- | -------- | ----- | --- |
|     | x x    | x      |            | y y y    |       |     |
1
AddiertergibtsichderzweidimensionaleLaplace-Filter
|     |     |     |    |    |     |     |
| --- | --- | --- | --- | --- | --- | --- |
0 1 0
|     |     | HL =H | L+H L = 1 | −4 1  |     |     |
| --- | --- | ----- | ---------- | ------ | --- | --- |
|     |     |       | x y        |        |     |     |
0 1 0
Nichtseparabel,aberberechenbarüber
|     |     | I∗HL =I∗(HL+HL)=I∗HL+I∗HL |     |     |     |     |
| --- | --- | ------------------------- | --- | --- | --- | --- |
|     |     |                           | x y | x   | y   |     |

| KantenundGradienten | FilterzurKantendetektion | Kantenschärfung |
| ------------------- | ------------------------ | --------------- |
Beispiel: Laplace-Operator
Nulldurchgangmarkiert
genaueKantenposition.

KantenundGradienten FilterzurKantendetektion Kantenschärfung
Canny-Operator (1)
Ziele:
GuteDetektion:möglichstalleKantendetektieren,ohnezuviel
Clutter.
GuteLokalisation:minimaleDistanzzwischendetektierterund
echterKante
KlareAntwort:nureineAntwortproKante
DeroptimaleFilterwurdevonCannydurchVariationsrechnung
abgeleitet.
Vorgehensweise:
1.GlättungdesBildesmitGaußfilterderBreiteσ:bestimmt
RauschempfindlichkeitundBreitederzudetektierendenKanten.
2.Differenzierung:MeistPrewitt-OperatoroderAbleitungender
(cid:112)
Gaußfunktion,darausKantenstärke D (u,v)2+D (u,v)2
x y

KantenundGradienten FilterzurKantendetektion Kantenschärfung
Canny-Operator (2)
3.UnterdrückungvonNichtmaxima:Zuerstwerdenlokale
MaximaderKantenstärkegesucht,abersenkrechtzurKante,
nichtentlangderKante.DazuwirdlokaldieGradientenrichtung
Φ(u,v)=tan−1(D (u,v)/D (u,v))bestimmtundalleMaxima,die
y x
nichtgrößeralsbeidesenkrechtenNachbarnsind,unterdrückt.
4.Schwellwertbildung:ZurVerhinderungvonunterbrochenen
Liniengibtes2Schwellwerteθ undθ :Maximaunterθ werden
1 2 1
verworfen,überθ beibehalten.FürWertedazwischengibtes
2
Hysterese:WennmindestenseinNachbarakzeptiertwurde,
wirddaslokaleMaximumebenfallsübernommen.θ undθ
1 2
werdenoftanhanddesHistogrammsderFilterantworten
gewählt.

| KantenundGradienten | FilterzurKantendetektion | Kantenschärfung |
| ------------------- | ------------------------ | --------------- |
Beispiel: Canny-Operator

| KantenundGradienten |               | FilterzurKantendetektion | Kantenschärfung |
| ------------------- | ------------- | ------------------------ | --------------- |
| Vergleich           | verschiedener | Kantendetektoren         |                 |
Kriterien:
Menge von
”irrelevanten”
Kantenelementen
Zusammenhang der
dominanten Kanten
Klare Lokalisierbarkeit
der Kanten

KantenundGradienten FilterzurKantendetektion Kantenschärfung
Von Kanten zu Konturen
Konturverfolgung:AusgehendvoneinemBildpunkthoher
KantenstärkewirdKonturpixelweiseinbeideRichtungen
verfolgt.
Problem:Konturenkönnensichteilen,kreuzen,verschwinden,
verdecktseinoderzusammenlaufen.
SinnvolleKontureninGraubildernerfordern
Segmentieralgorithmenoder
Konturvervollständigungsmechanismen,umLückeninKanten
zuüberbrücken.
KonturverfolgungwirdmeistinBinärbildernangewandt
(Vorlesunginca.3Wochen)
WenndieArtderKonturvorherbekanntist(z.B.Kreiseoder
DreieckebeiVerkehrsschildern),reicheneinfacheKantenbilder
alsInputaus.

KantenundGradienten FilterzurKantendetektion Kantenschärfung
Übersicht
1 Kanten und Gradienten
2 Filter zur Kantendetektion
3 Kantenschärfung

KantenundGradienten FilterzurKantendetektion Kantenschärfung
Kantenschärfung mit dem Laplace-Filter
Grundidee:Überhöhungder
KantendurchSubtraktionder
zweitenAbleitungläßtdasBild
schärfererscheinen.
Vorgehensweise:
I(cid:48) =I−wHL∗I
wbestimmtdieStärkeder
Schärfung.
Achtung:Schärfungverstärkt
auchdasBildrauschen-evtl.
vorherigeGlättungnotwendig.

| KantenundGradienten |                 | FilterzurKantendetektion | Kantenschärfung |
| ------------------- | --------------- | ------------------------ | --------------- |
| Beispiel:           | Kantenschärfung | mit Laplace              |                 |

| KantenundGradienten                                      |            | FilterzurKantendetektion |         | Kantenschärfung |
| -------------------------------------------------------- | ---------- | ------------------------ | ------- | --------------- |
| Unscharfe                                                | Maskierung | (unsharp                 | masking | - USM)          |
| 1 ErzeugungeinergeglättetenVersiondesBildes(z.B.miteinem |            |                          |         |                 |
Gaußfilter)
| 2 SubtraktiondergeglättetenVersionvomOriginalbild: |     |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- |
M =I−I∗H
ErgebnisheißtMaske.
| 3 AdditiondergewichtetenMaskezumOriginalbild |     |     |     |     |
| -------------------------------------------- | --- | --- | --- | --- |
I(cid:48) I+aM
=
= (1+a)I−aI∗H
| akontrolliertdenSchärfungsgrad(a∈[0.2,4]),Breiteσ |     |     |     | des |
| ------------------------------------------------- | --- | --- | --- | --- |
GaußfiltersdieRauschempfindlichkeit.
OftgibteszusätzlicheinenMindestwertfürdenBildkontrast,abdem
einSchärfungvorgenommenwird.

| KantenundGradienten |                 | FilterzurKantendetektion | Kantenschärfung |
| ------------------- | --------------- | ------------------------ | --------------- |
| Beispiel:           | Kantenschärfung | mit USM                  |                 |

| KantenundGradienten |                |     | FilterzurKantendetektion |     |     |     | Kantenschärfung |
| ------------------- | -------------- | --- | ------------------------ | --- | --- | --- | --------------- |
| Laplace-            | und USM-Filter |     |                          |     |     |     |                 |
Laplace-FilteristeigentlicheinSpezialfalldesUSM-Filters:
|     |        |      |    |       |    |             |     |
| --- | ------- | ----- | --- | ------ | --- | ------------ | --- |
|     | 0 1     | 0     | 0 1 | 0      | 0 0 | 0            |     |
| HL  | = 1 −4 | 1 = | 1 1 | 1 −5 | 0 1 | 0 =5(HˆL−δ) |     |
|     | 0 1     | 0     | 0 1 | 0      | 0 0 | 0            |     |
Laplace-Schärfung
|     |     | I(cid:48) | = I−wHL∗I       |     |     |     |     |
| --- | --- | --------- | --------------- | --- | --- | --- | --- |
|     |     |           | = I−5w(HˆL∗I−I) |     |     |     |     |
|     |     |           | = I+5w(I−HˆL∗I) |     |     |     |     |
|     |     |           | = I+5wM         |     |     |     |     |
entsprichtUSM-Schärfungmit
|     |     |     |    |    |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | 0 1 | 0   |     |     |     |
HˆL 1
|     |     | =   |  1 1 | 1  und | a=5w |     |     |
| --- | --- | --- | ----- | ------- | ---- | --- | --- |
5
|     |     |     | 0 1 | 0   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |

| KantenundGradienten |                    |               | FilterzurKantendetektion |             |          |           | Kantenschärfung |
| ------------------- | ------------------ | ------------- | ------------------------ | ----------- | -------- | --------- | --------------- |
| Ausblick:           | Schärfung          |               | mit plausiblen           |             | Details  |           |                 |
| Die bisherigen      |                    | Techniken     | schärfen                 | zwar        | Kanten,  | können    | aber            |
| keine               | verlorengegangenen |               | Details                  | hinzufügen. |          |           |                 |
| Grundidee:          |                    | Details       | werden aus               | einer       | großen   | Datenbank | von             |
| Bildausschnitten    |                    | herausgesucht |                          | bzw.        | zwischen | ihnen     | so              |
interpoliert, daß sie möglichst gut an die unscharfen Stellen
passen.
| Hier: | KPCA-Bildmodell |     | (Kim | et al., 2005). |     |     |     |
| ----- | --------------- | --- | ---- | -------------- | --- | --- | --- |

| KantenundGradienten |            | FilterzurKantendetektion |            | Kantenschärfung |
| ------------------- | ---------- | ------------------------ | ---------- | --------------- |
| Anwendung           | auf Bilder | von                      | Gesichtern |                 |
| Original            | 20×20      |                          | PCA        | KPCA            |
[Kimetal.,2005]

| KantenundGradienten            | FilterzurKantendetektion | Kantenschärfung |
| ------------------------------ | ------------------------ | --------------- |
| Trainingsbilder für Bildmodell |                          |                 |
[Kimetal.,2005]

| KantenundGradienten |             | FilterzurKantendetektion | Kantenschärfung |
| ------------------- | ----------- | ------------------------ | --------------- |
| Schärfung           | natürlicher | Bilder                   |                 |
(a)Original
(300×500),
(b)Input(90×150),
(c)Nearest-Neigbour-
Rekonstruktion,
(d)KPCA
Rekonstruktion.
[Kimetal.,2005]

| KantenundGradienten |             |     | FilterzurKantendetektion | Kantenschärfung |
| ------------------- | ----------- | --- | ------------------------ | --------------- |
| Schärfung           | natürlicher |     | Bilder (Ausschnitt)      |                 |
Interpolation/ Nearest
|     | Original | Input |     | KPCA |
| --- | -------- | ----- | --- | ---- |
Schärfung Neighbour
[Kimetal.,2005]