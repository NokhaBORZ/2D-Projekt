AuffindenvonBildregionen GeometrischeEigenschaftenbinärerBildregionen StatistischeEigenschaftenbinärerBildregionen
| Regionen | in Binärbildern |     |
| -------- | --------------- | --- |
81
| 2D Computer | Vision, Vorlesung | No. |
| ----------- | ----------------- | --- |
M. O. Franz
1
fallsnichtandersvermerkt,sinddieAbbildungenentnommenausBurger&Burge,2005.

AuffindenvonBildregionen GeometrischeEigenschaftenbinärerBildregionen StatistischeEigenschaftenbinärerBildregionen
Übersicht
| Auffinden | von Bildregionen |     |
| --------- | ---------------- | --- |
1
| 2 Geometrische | Eigenschaften | binärer Bildregionen |
| -------------- | ------------- | -------------------- |
| 3 Statistische | Eigenschaften | binärer Bildregionen |

AuffindenvonBildregionen GeometrischeEigenschaftenbinärerBildregionen StatistischeEigenschaftenbinärerBildregionen
Übersicht
| Auffinden | von Bildregionen |     |
| --------- | ---------------- | --- |
1
| 2 Geometrische | Eigenschaften | binärer Bildregionen |
| -------------- | ------------- | -------------------- |
| 3 Statistische | Eigenschaften | binärer Bildregionen |

AuffindenvonBildregionen GeometrischeEigenschaftenbinärerBildregionen StatistischeEigenschaftenbinärerBildregionen
Regionen in Binärbildern
Aufgaben:
AuffindenvonverbundenenRegionengleicherPixelfarbe
ExtraktionvonKonturen
RepräsentationderBildregionen
BeschreibungderRegionendurchgeeigneteKennzahlen

AuffindenvonBildregionen GeometrischeEigenschaftenbinärerBildregionen StatistischeEigenschaftenbinärerBildregionen
Auffinden von Bildregionen
Regionenmarkierung(regionlabelingodercoloring):
BestimmungderAnzahlderRegionenimBild
BestimmungderPositionderRegionenimBild
BestimmungderZugehörigkeitdereinzelnenPixelzuden
Bildregionen
Vorherfestzulegen:ArtderNachbarschaft(4eroder8er)⇒führtzu
unterschiedlichenRegionen.
ErgebnisderRegionenmarkierung:

AuffindenvonBildregionen GeometrischeEigenschaftenbinärerBildregionen StatistischeEigenschaftenbinärerBildregionen
| Regionenmarkierung | durch Flood | Filling (1) |
| ------------------ | ----------- | ----------- |
entsprichtrekursiverTiefensuchebeiGraphenalgorithmen.Vorsicht:
ErschöpfungdesStack-SpeichersbeigroßenRegionen

AuffindenvonBildregionen GeometrischeEigenschaftenbinärerBildregionen StatistischeEigenschaftenbinärerBildregionen
| Regionenmarkierung | durch Flood | Filling (2) |
| ------------------ | ----------- | ----------- |
entsprichtsequentiellerTiefensuchebeiGraphenalgorithmen.Dader
StackimHeapspeicherangelegtwird,bestehtprinzipiellkeine
Größenlimitierung.

AuffindenvonBildregionen GeometrischeEigenschaftenbinärerBildregionen StatistischeEigenschaftenbinärerBildregionen
| Regionenmarkierung | durch Flood | Filling (3) |
| ------------------ | ----------- | ----------- |
entsprichtsequentiellerBreitensuchebeiGraphenalgorithmen.
EbenfallskeineGrößenlimitierung,geringererSpeicherbedarf.

AuffindenvonBildregionen GeometrischeEigenschaftenbinärerBildregionen StatistischeEigenschaftenbinärerBildregionen
| Beispiel: | Flood Filling | (1) |
| --------- | ------------- | --- |

AuffindenvonBildregionen GeometrischeEigenschaftenbinärerBildregionen StatistischeEigenschaftenbinärerBildregionen
| Beispiel: | Flood Filling | (2) |
| --------- | ------------- | --- |

AuffindenvonBildregionen GeometrischeEigenschaftenbinärerBildregionen StatistischeEigenschaftenbinärerBildregionen
Sequentielle Regionenmarkierung
Verfahrenläuftin2Schrittenab:
1 Schritt1-VorläufigeMarkierung:BeimerstenDurchlaufwerden
alleLabelsausderlinken/oberenNachbarschaftübernommen.
GleichzeitigwerdendasAufeinandertreffenvonRegionenmit
unterschiedlichenLabels(Kollisionen)gespeichert.
2 Schritt2-AuflösungderKollisionen:Zusammenhängende
Regionenwerdenmiteinanderverschmolzen.
HäufigeingesetztwegenmoderatemSpeicherbedarf,Verschmelzung
derRegionenistaberkomplex.

AuffindenvonBildregionen GeometrischeEigenschaftenbinärerBildregionen StatistischeEigenschaftenbinärerBildregionen
| Sequentielle | Regionenmarkierung: | Schritt 1 |
| ------------ | ------------------- | --------- |

AuffindenvonBildregionen GeometrischeEigenschaftenbinärerBildregionen StatistischeEigenschaftenbinärerBildregionen
| Beispiel: | Vorläufige | Markierung | (1) |
| --------- | ---------- | ---------- | --- |

AuffindenvonBildregionen GeometrischeEigenschaftenbinärerBildregionen StatistischeEigenschaftenbinärerBildregionen
| Beispiel: | Vorläufige | Markierung | (2) |
| --------- | ---------- | ---------- | --- |

AuffindenvonBildregionen GeometrischeEigenschaftenbinärerBildregionen StatistischeEigenschaftenbinärerBildregionen
| Beispiel: | Vorläufige | Markierung | (3) |
| --------- | ---------- | ---------- | --- |

AuffindenvonBildregionen GeometrischeEigenschaftenbinärerBildregionen StatistischeEigenschaftenbinärerBildregionen
| Sequentielle | Regionenmarkierung: | Schritt 2 |
| ------------ | ------------------- | --------- |

AuffindenvonBildregionen GeometrischeEigenschaftenbinärerBildregionen StatistischeEigenschaftenbinärerBildregionen
| Sequentielle | Regionenmarkierung: | Schritt 2 |
| ------------ | ------------------- | --------- |

AuffindenvonBildregionen GeometrischeEigenschaftenbinärerBildregionen StatistischeEigenschaftenbinärerBildregionen
Beispiel: fertige Regionenmarkierung

AuffindenvonBildregionen GeometrischeEigenschaftenbinärerBildregionen StatistischeEigenschaftenbinärerBildregionen
Übersicht
| Auffinden | von Bildregionen |     |
| --------- | ---------------- | --- |
1
| 2 Geometrische | Eigenschaften | binärer Bildregionen |
| -------------- | ------------- | -------------------- |
| 3 Statistische | Eigenschaften | binärer Bildregionen |

AuffindenvonBildregionen GeometrischeEigenschaftenbinärerBildregionen StatistischeEigenschaftenbinärerBildregionen
Formmerkmale
Merkmal(Feature)einerRegion:Numerischeoderkategorielle
Kenngröße,dieausBildpunkten(PositionundWerte)berechnetwird.
MehrereMerkmalewerdenineinemMerkmalsvektor
zusammengefaßt.
Merkmalesollten
einfachzuberechnen,
invariantgegenüberirrelevantenVeränderungen(z.B.
Rotationen,Verschiebungen,Skalierungen)sein.
EineRegionRineinemBinärbildkannalszweidimensionale
VerteilungvonVordergrundpunktenx =(u,v)beschriebenwerden:
i i i
R={x ,x ,...,x }={(u ,v ),(u ,v ),...,(u ,v )}
1 2 N 1 1 2 2 N N

AuffindenvonBildregionen GeometrischeEigenschaftenbinärerBildregionen StatistischeEigenschaftenbinärerBildregionen
| Geometrische | Eigenschaften |     | - Umfang |
| ------------ | ------------- | --- | -------- |
Umfanghängtvom
Nachbarschaftstypab:
bei4er-Nachbarschaftenist
derUmfangi.A.größerals
derreale.
einebessereNäherungwird
durchdie8er-Nachbarschaft
erreicht.
|       | M−1      | (cid:26) |                                  |
| ----- | -------- | -------- | -------------------------------- |
|       | (cid:88) |          | 1 Horizontal-undVertikalsegmente |
| U(R)= | l(c) mit | l(c)= √  |                                  |
i
2 Diagonalsegemente
i=0
Umfangwirddamitimmernochleichtüberschätzt,daherKorrektur
umFaktor0.95:
M−1
(cid:88)
|     |     | U(R)≈0.95 | l(c) |
| --- | --- | --------- | ---- |
i
i=0

AuffindenvonBildregionen GeometrischeEigenschaftenbinärerBildregionen StatistischeEigenschaftenbinärerBildregionen
| Geometrische                            | Eigenschaften |     | - Fläche          |     |
| --------------------------------------- | ------------- | --- | ----------------- | --- |
| DieFlächeberechnetsicheinfachalsAnzahlN |               |     | derBildpunkteinR: |     |
A(R)=N =|R|,
kannauchnäherungsweisebeizusammenhängendenRegionenaus
| dergeschlossenenKontur{c |     | ,c ,...c | }={(x | ,y ),(x ,y ),...} |
| ------------------------ | --- | -------- | ----- | ----------------- |
|                          |     | 0 1      | M−1   | 0 0 1 1           |
(GaußscheFlächenformelfürPolygone)berechnetwerden:
|     | (cid:12)   |     |     | (cid:12) |
| --- | ---------- | --- | --- | -------- |
|     | 1(cid:12)M | −1  |     | (cid:12) |
(cid:88)
|     | A(R)= (cid:12) | xy          | −x        | y(cid:12) |
| --- | -------------- | ----------- | --------- | --------- |
|     | 2(cid:12)      | i (i+1)modM | (i+1)modM | i(cid:12) |
|     | (cid:12)       |             |           | (cid:12)  |
i=0
erlaubtBerechnungderFlächeausChainCodes.
UmfangundFlächesindinvariantgegenüberVerschiebungenund
Drehungen,jedochvariantgegenüberSkalierungen.

AuffindenvonBildregionen GeometrischeEigenschaftenbinärerBildregionen StatistischeEigenschaftenbinärerBildregionen
Geometrische Eigenschaften - Kompaktheit und
Rundheit
DieKompaktheiteinerRegionbeschreibtdieBeziehungvonUmfang
undFläche:k= A(R) .FürKreisergibtsichk= 1 ⇒Normierungauf
U(R)2 4π
KreisergibtRundheit:
A(R)
C=4π .
U(R)2
InvariantgegenüberVerschiebung,DrehungundSkalierung.

AuffindenvonBildregionen GeometrischeEigenschaftenbinärerBildregionen StatistischeEigenschaftenbinärerBildregionen
| Geometrische  | Eigenschaften | - Bounding | Box und |
| ------------- | ------------- | ---------- | ------- |
| konvexe Hülle |               |            |         |
BoundingBoxbezeichnetdasminimaleachsenparalleleRechteck,
dasallePunkteeinerRegioneinschließt.
KonvexeHülle:KleinstesPolygon,daseineRegionumfaßt.
Konvexität:VerhältnisderUmfängevonkonvexerHülleundRegion
Dichte:FlächenverhältnisvonHülleundRegion

AuffindenvonBildregionen GeometrischeEigenschaftenbinärerBildregionen StatistischeEigenschaftenbinärerBildregionen
Übersicht
| Auffinden | von Bildregionen |     |
| --------- | ---------------- | --- |
1
| 2 Geometrische | Eigenschaften | binärer Bildregionen |
| -------------- | ------------- | -------------------- |
| 3 Statistische | Eigenschaften | binärer Bildregionen |

AuffindenvonBildregionen GeometrischeEigenschaftenbinärerBildregionen StatistischeEigenschaftenbinärerBildregionen
Statistische Eigenschaften
Schwerpunkt(⇒PositionderRegion):
|     | 1 (cid:88) |       | 1 (cid:88) |     |
| --- | ---------- | ----- | ---------- | --- |
|     | ¯x=        | u und | ¯y=        | v   |
|     | |R|        | i     | |R|        | i   |
|     | (ui,vi)∈R  |       | (ui,vi)∈R  |     |
Momente:
|        | (cid:88) I(u,v)upvq |      | (cid:88)     | upvq |
| ------ | ------------------- | ---- | ------------ | ---- |
| m pq = |                     | bzw. | m pq =       |      |
|        | (u,v)∈R             |      | (u,v)∈Rbinär |      |
z.B.
|        | (cid:80) | (cid:80) u0v0 |     |     |
| ------ | -------- | ------------- | --- | --- |
| A=|R|= | 1=       | =m 00         |     |     |
(cid:80)
| ¯x= 1 | u1v0 =   | m10   |     |     |
| ----- | -------- | ----- | --- | --- |
| |R    | |        | m     |     |     |
|       | (cid:80) | 0 0   |     |     |
| ¯y= 1 | u0v1 =   | m 0 1 |     |     |
| |R|   |          | m00   |     |     |

AuffindenvonBildregionen GeometrischeEigenschaftenbinärerBildregionen StatistischeEigenschaftenbinärerBildregionen
| Statistische | Eigenschaften |     | - zentrale | Momente |     |
| ------------ | ------------- | --- | ---------- | ------- | --- |
Momentesindi.A.nichtverschiebungsinvariant⇒Verscheibungdes
UrsprungsandenSchwerpunkt:zentraleMomente
| (cid:88) |                      |     |        | (cid:88)         |     |
| -------- | -------------------- | --- | ------ | ---------------- | --- |
| µ =      | I(u,v)(u−¯x)p(v−¯y)q |     | bzw. µ | = (u−¯x)p(v−¯y)q |     |
| pq       |                      |     | pq     |                  |     |
| (u,v)∈R  |                      |     |        | (u,v)∈Rbinär     |     |
DiezentralenMomentehängenvonderGrößederRegionab.Eine
SkalierungumdenFaktorsergibt
(cid:88)
| µ (s·R)=s2 |     | I(u,v)sp(u−¯x)psq(v−¯y)q |     | =sp+q+2µ | (R) |
| ---------- | --- | ------------------------ | --- | -------- | --- |
| pq         |     |                          |     |          | pq  |
(u,v)∈R
GrößeninvarianteMomenteerhältmanNormalisierungmitderFläche
| A=m | =µ : |     |     |     |     |
| --- | ---- | --- | --- | --- | --- |
00 00
µ pq
µ¯ =
pq µ(p+q+2)/2
00

AuffindenvonBildregionen GeometrischeEigenschaftenbinärerBildregionen StatistischeEigenschaftenbinärerBildregionen
Statistische Eigenschaften - Orientierung
Orientierung:RichtungderHauptachse(Achsemitminimalem
Drehmoment)
1 2µ
θ = tan−1 11
2 µ −µ
20 02
(RichtungdesEigenvektorszumgrößtenEigenwertdes
Trägheitstensors)

AuffindenvonBildregionen GeometrischeEigenschaftenbinärerBildregionen StatistischeEigenschaftenbinärerBildregionen
| Statistische | Eigenschaften | - Exzentrizität |
| ------------ | ------------- | --------------- |
Exzentrizität:MaßfürdasGrößenverhältnisderbeidenHauptachsen
(µ −µ )2+4µ2
|     | E= 20 | 02 11 ∈[0,1] |
| --- | ----- | ------------ |
(µ 20 +µ 02 )2
BeirundenObjektenistEnahean0,beilänglichenObjektennahe
an1.

AuffindenvonBildregionen GeometrischeEigenschaftenbinärerBildregionen StatistischeEigenschaftenbinärerBildregionen
Statistische Eigenschaften - Hu-Momente
NormalisiertezentraleMomentesindzwarskalierungs-und
verschiebungsinvariant,aberi.A.nichtrotationsinvariant.
Hu-Momente(zusätzlichrotationsinvariant):
meistlogarithmiertwegengroßenWertebereichs.

AuffindenvonBildregionen GeometrischeEigenschaftenbinärerBildregionen StatistischeEigenschaftenbinärerBildregionen
Projektionen
|         | M−1         |         | N−1      |
| ------- | ----------- | ------- | -------- |
|         | (cid:88)    |         | (cid:88) |
| P (v )= | I(u,v ) und | P (u )= | I(u ,v)  |
| hor 0   | 0           | vert 0  | 0        |
|         | u=0         |         | v=0      |
NützlichzurAnalysevonstrukturiertenBildern,z.B.zurDetektionvon
ZeilenundeinzelnenBuchstaben,oderschnellenSchätzungder
Orientierung.