Diskrete2D-Fouriertransformation Windowing BeispieleundAnwendungen DiskreteKosinustransformation(DCT)
Spektraltechniken
2D Computer Vision, Vorlesung No. 91
M. O. Franz
1
fallsnichtandersvermerkt,sinddieAbbildungenentnommenausBurger&Burge,2005.

Diskrete2D-Fouriertransformation Windowing BeispieleundAnwendungen DiskreteKosinustransformation(DCT)
Übersicht
| Diskrete | 2D-Fouriertransformation |     |
| -------- | ------------------------ | --- |
1
2 Windowing
| 3 Beispiele | und Anwendungen       |       |
| ----------- | --------------------- | ----- |
| 4 Diskrete  | Kosinustransformation | (DCT) |

Diskrete2D-Fouriertransformation Windowing BeispieleundAnwendungen DiskreteKosinustransformation(DCT)
Übersicht
| Diskrete | 2D-Fouriertransformation |     |
| -------- | ------------------------ | --- |
1
2 Windowing
| 3 Beispiele | und Anwendungen       |       |
| ----------- | --------------------- | ----- |
| 4 Diskrete  | Kosinustransformation | (DCT) |

Diskrete2D-Fouriertransformation Windowing BeispieleundAnwendungen DiskreteKosinustransformation(DCT)
Diskrete 1D-Fouriertransformation
Diskrete,periodischeSignalehabeneindiskretes,periodisches
Spektrum.
Geg.:diskretesSignalg(u)derLängeM(u=0,1,...,M 1).
−
Vorwärtstransformation(DFT):
1 M−1
|       | (cid:88) g(u)e−i2πm u |           |
| ----- | --------------------- | --------- |
| G(m)= | M                     | für 0 m<M |
| √M    |                       | ≤         |
u=0
InverseTransformation(DFT−1):
M−1
1 (cid:88)
| g(u)= | G(m)ei2πm u | 0 u<M |
| ----- | ----------- | ----- |
M für
| √M  |     | ≤   |
| --- | --- | --- |
m=0

Diskrete2D-Fouriertransformation Windowing BeispieleundAnwendungen DiskreteKosinustransformation(DCT)
| Diskrete | zweidimensionale | Fouriertransformation |     |
| -------- | ---------------- | --------------------- | --- |
Füreinezweidimensionale,periodischeFunktiong(u,v)derGröße
| M   | N   |     |     |
| --- | --- | --- | --- |
istdie2D-DFT
×
M−1N−1
1 (cid:88)(cid:88)
|     | G(m,n) = | g(u,v)e−i2πm | ue−i2πn v |
| --- | -------- | ------------ | --------- |
M N
√MN
u=0 v=0
M−1N−1
1 (cid:88)(cid:88)
|     |     | g(u,v)e−i2π(m | u+n v) |
| --- | --- | ------------- | ------ |
= M N
√MN
u=0 v=0
Inverse2D-DFT−1:
1 M−1N−1
|     |          | (cid:88)(cid:88) G(m,n)ei2πu | mei2πv n |
| --- | -------- | ---------------------------- | -------- |
|     | g(u,v) = |                              | M N      |
√MN
m=0 n=0
1 M−1N−1
|     |     | (cid:88)(cid:88) G(m,n)ei2π(m | u+n v) |
| --- | --- | ----------------------------- | ------ |
= M N
√MN
m=0 n=0

Diskrete2D-Fouriertransformation Windowing BeispieleundAnwendungen DiskreteKosinustransformation(DCT)
2D-Basisfunktionen
DiezweidimensionaleFunktiong(u,v)wirdbeschriebenalseine
gewichteteSummevonzweidimensionalen,komplexenFunktionen
DabeisindCM,N(u,v)undSM,N(u,v)zweidimensionaleCosinus-bzw.
| m,n | m,n |     |
| --- | --- | --- |
SinusfunktionenmithorizontalerWellenzahlmundvertikaler
Wellenzahln
|           | (cid:104) (cid:16)um | vn(cid:17)(cid:105) |
| --------- | -------------------- | ------------------- |
| CM,N(u,v) | 2π                   |                     |
| m,n       | = cos                | +                   |
M N
|           | (cid:104) (cid:16)um | vn(cid:17)(cid:105) |
| --------- | -------------------- | ------------------- |
| SM,N(u,v) | = sin 2π             | +                   |
| m,n       |                      | M N                 |
d.h.orientierteWellenfunktionen.

Diskrete2D-Fouriertransformation Windowing BeispieleundAnwendungen DiskreteKosinustransformation(DCT)
2D-Basisfunktionen CM,N(u,v) (1)
m,n

Diskrete2D-Fouriertransformation Windowing BeispieleundAnwendungen DiskreteKosinustransformation(DCT)
2D-Basisfunktionen CM,N(u,v) (2)
m,n

Diskrete2D-Fouriertransformation Windowing BeispieleundAnwendungen DiskreteKosinustransformation(DCT)
2D-Basisfunktionen CM,N(u,v) (3)
m,n

Diskrete2D-Fouriertransformation Windowing BeispieleundAnwendungen DiskreteKosinustransformation(DCT)
2D-Basisfunktionen CM,N(u,v) (4)
m,n

Diskrete2D-Fouriertransformation Windowing BeispieleundAnwendungen DiskreteKosinustransformation(DCT)
| Implementierung | der zweidimensionalen | DFT |
| --------------- | --------------------- | --- |
Umformungder2D-DFT
d.h.HintereinanderausführungzweiereindimensionalerDFTs.

Diskrete2D-Fouriertransformation Windowing BeispieleundAnwendungen DiskreteKosinustransformation(DCT)
Darstellung der Fouriertransformierten in 2D
StatteinBilddesReal-undeinesdesImaginärteilszuzeigen,wird
häufigderBetrag G(m,n) derDFTdargestellt
| |
(Amplitudenspektrum),oftauchlogarithmiert.
DadietransformiertenBilderrellwertigsind,istdasAmplituden-
spektrumsymmetrischzumUrsprung,d.h.
G(m,n) = G( m, n)
| | | − − |
ÜblicherweisewirddaherderUrsprungzentriertdargestellt.Dies
geschiehtdurcheineUmordnungderQuadrantenunterderNutzung
dieserSymmetrieeigenschaft.

Diskrete2D-Fouriertransformation Windowing BeispieleundAnwendungen DiskreteKosinustransformation(DCT)
Zentrierte Darstellung

Diskrete2D-Fouriertransformation Windowing BeispieleundAnwendungen DiskreteKosinustransformation(DCT)
| Darstellung | als logarithmiertes | Intensitätsbild |
| ----------- | ------------------- | --------------- |

Diskrete2D-Fouriertransformation Windowing BeispieleundAnwendungen DiskreteKosinustransformation(DCT)
| Frequenz und | Orientierung |     |
| ------------ | ------------ | --- |
(cid:113)
EffektiveFrequenzinWellenrichtung:ˆf (cid:0)m(cid:1)2 (cid:0)n(cid:1)2
= 1 +
(m,n) τ M N
(cid:0)n, m(cid:1)
| Orientierung:ψ | =arctan 2 | bzw. |
| -------------- | --------- | ---- |
| (m,n)          | N         | M    |
(m,n)= ˆf(Mcosψ,Nsinψ)
±
RichtungswinkelinBildundSpektrumsindnurbeiquadratischen
| Bilderngleich. | KorrekturdurchquadratischeSkalierungdes |     |
| -------------- | --------------------------------------- | --- |
⇒
Spektrums.

Diskrete2D-Fouriertransformation Windowing BeispieleundAnwendungen DiskreteKosinustransformation(DCT)
| Geometrische | Korrektur | des 2D-Spektrums |
| ------------ | --------- | ---------------- |

Diskrete2D-Fouriertransformation Windowing BeispieleundAnwendungen DiskreteKosinustransformation(DCT)
| Frequenzlimits | und Aliasing | in 2D |
| -------------- | ------------ | ----- |
EffektiveAbtastfrequenzistamgeringstenentlangder
Koordinatenachsen,amhöchstenentlangderDiagonalen.

Diskrete2D-Fouriertransformation Windowing BeispieleundAnwendungen DiskreteKosinustransformation(DCT)
Übersicht
| Diskrete | 2D-Fouriertransformation |     |
| -------- | ------------------------ | --- |
1
2 Windowing
| 3 Beispiele | und Anwendungen       |       |
| ----------- | --------------------- | ----- |
| 4 Diskrete  | Kosinustransformation | (DCT) |

Diskrete2D-Fouriertransformation Windowing BeispieleundAnwendungen DiskreteKosinustransformation(DCT)
Auswirkungen der Periodizität
DieimpliziteAnnahmeeinesperiodischenBildesführtzu
breitbandigenSignalenentlangderKoordinatenachsendurchdie
DiskontinuitätenandenBildrändern.

Diskrete2D-Fouriertransformation Windowing BeispieleundAnwendungen DiskreteKosinustransformation(DCT)
Windowing
ZurReduktionderdurchdiePeriodizitätverursachtenArtefaktewird
dasgesamteBildvorderDFTmiteinerFensterfunktionmultipliziert:
˜g(u,v)=g(u,v) w(u,v)
·
DieFensterfunktionwirdsogewählt,daßsiemöglichstgleichmäßig
andenRänderngegen0abfälltunddamitdieDiskontinuitätenan
denBildrändernunterdrückt.
Aber:MultiplikationimBildraumführtzuFaltungdesSpektrumsmit
derDFTderFensterfunktionimFrequenzraum.
Tradeoff:Jesteilerw(u,v)anddenBildrändernabfällt,destogrößer
istderBildanteil,derzumSpektrumbeiträgt,aberdestostärkersind
dieRand-Artefakte,unddestostärkerwirddasSpektrum”verwischt”.

Diskrete2D-Fouriertransformation Windowing BeispieleundAnwendungen DiskreteKosinustransformation(DCT)
| Rechteckiges | und elliptisches | Fenster |
| ------------ | ---------------- | ------- |

Diskrete2D-Fouriertransformation Windowing BeispieleundAnwendungen DiskreteKosinustransformation(DCT)
| Gauß- und | Supergauß(n | = 6)-Fenster |
| --------- | ----------- | ------------ |

Diskrete2D-Fouriertransformation Windowing BeispieleundAnwendungen DiskreteKosinustransformation(DCT)
Cos2- und Bartlett-Fenster

Diskrete2D-Fouriertransformation Windowing BeispieleundAnwendungen DiskreteKosinustransformation(DCT)
Hanning- und Parzen-Fenster

Diskrete2D-Fouriertransformation Windowing BeispieleundAnwendungen DiskreteKosinustransformation(DCT)
| Beispiel: | Auswirkung | der Fensterfunktion | (1) |
| --------- | ---------- | ------------------- | --- |

Diskrete2D-Fouriertransformation Windowing BeispieleundAnwendungen DiskreteKosinustransformation(DCT)
| Beispiel: | Auswirkung | der Fensterfunktion | (2) |
| --------- | ---------- | ------------------- | --- |

Diskrete2D-Fouriertransformation Windowing BeispieleundAnwendungen DiskreteKosinustransformation(DCT)
Übersicht
| Diskrete | 2D-Fouriertransformation |     |
| -------- | ------------------------ | --- |
1
2 Windowing
| 3 Beispiele | und Anwendungen       |       |
| ----------- | --------------------- | ----- |
| 4 Diskrete  | Kosinustransformation | (DCT) |

Diskrete2D-Fouriertransformation Windowing BeispieleundAnwendungen DiskreteKosinustransformation(DCT)
Beispiel: Skalierung

Diskrete2D-Fouriertransformation Windowing BeispieleundAnwendungen DiskreteKosinustransformation(DCT)
| Beispiel: | periodisches | Bildmuster |
| --------- | ------------ | ---------- |

Diskrete2D-Fouriertransformation Windowing BeispieleundAnwendungen DiskreteKosinustransformation(DCT)
Beispiel: Drehung

Diskrete2D-Fouriertransformation Windowing BeispieleundAnwendungen DiskreteKosinustransformation(DCT)
| Beispiel: | gerichtete, | längliche | Strukturen |
| --------- | ----------- | --------- | ---------- |

Diskrete2D-Fouriertransformation Windowing BeispieleundAnwendungen DiskreteKosinustransformation(DCT)
| Beispiel: | Natürliche | Bilder (1) |
| --------- | ---------- | ---------- |

Diskrete2D-Fouriertransformation Windowing BeispieleundAnwendungen DiskreteKosinustransformation(DCT)
| Beispiel: | Natürliche | Bilder (2) |
| --------- | ---------- | ---------- |

Diskrete2D-Fouriertransformation Windowing BeispieleundAnwendungen DiskreteKosinustransformation(DCT)
Beispiel: Druckmuster

Diskrete2D-Fouriertransformation Windowing BeispieleundAnwendungen DiskreteKosinustransformation(DCT)
Anwendungen der DFT
FilterungimSpektralraum:beisehrgroßenN N-Filtermasken
×
aufM M-BildernsindO(M2N2)Operationennotwendig,FFT
×
undinverseFFTbenötigenO(MlogM)OperationenplusM2
Multiplikationen,unabhängigvonderFiltergrößeN.
KorrelationbeiTemplateMatching:Korrelationistidentischzur
linearenFaltungmitgespiegelterFensterfunktion Anwendung
⇒
beiderSuchenachgroßenObjekten.
EntfernungderUnschärfedurchinverseFilterung:Ein
unscharfesBildenstehtdurchFaltungmitderPunktverwa-
schungsfunktionderOptik,d.h.MultiplikationderDFTdes
BildesmitderDFTderPVF(Modulationstransferfunktion,MTF)
EntfernungdurchDivisiondurchMTF.
⇒

Diskrete2D-Fouriertransformation Windowing BeispieleundAnwendungen DiskreteKosinustransformation(DCT)
Übersicht
| Diskrete | 2D-Fouriertransformation |     |
| -------- | ------------------------ | --- |
1
2 Windowing
| 3 Beispiele | und Anwendungen       |       |
| ----------- | --------------------- | ----- |
| 4 Diskrete  | Kosinustransformation | (DCT) |

Diskrete2D-Fouriertransformation Windowing BeispieleundAnwendungen
Diskrete2D-Fouriertransformation Windowing BeispieleundAnwendungen DiskreteKosinustransformation(DCT)
Darstellung als logarithmiertes Intensitätsbild
Bildkompression mithilfe des Spektrums
DasSpektrumeinesBildesisteinBeispiel
füreinesparse(dt.spärlich,sparsam)
Repräsentation:nurwenigeKoeffizienten
sinddeutlichgrößeralsNull.Dadurch
eignetsichdasSpektrumzur
Bildkompression.
Allerdingserzeugtdie
Fouriertransformationi.A.ein
komplexwertigesSpektrum,dasaufgrund
seinerSpiegelsymmetrieredundantist.
FürdieKompressionbrauchenwireineVarianteder
FouriertransformationohneredundantesSpektrum:diediskrete
Kosinusformation(DCT).

Diskrete2D-Fouriertransformation Windowing BeispieleundAnwendungen DiskreteKosinustransformation(DCT)
Diskrete 1D-Kosinustransformation
Geg.:diskretesSignalg(u)derLängeM(u=0,1,...,M 1).
−
Vorwärtstransformation:
|       | (cid:114) | M−1      |       | (cid:18) | (cid:19)  |
| ----- | --------- | -------- | ----- | -------- | --------- |
|       | 2         | (cid:88) |       | m(2u+1)  |           |
| G(m)= |           | g(u)     | c cos | π        | für 0 m<M |
|       | M         |          | m     | 2M       |           |
· ≤
u=0
InverseTransformation:
|       | (cid:114) | M−1      |       | (cid:18) | (cid:19)  |
| ----- | --------- | -------- | ----- | -------- | --------- |
|       | 2         | (cid:88) |       | m(2u+1)  |           |
| g(u)= |           | G(m)     | c cos | π        | für 0 u<M |
|       | M         |          | m     | 2M       |           |
· ≤
m=0
(cid:26) √1
für m=0
|     |     | mit | c = | 2   |     |
| --- | --- | --- | --- | --- | --- |
|     |     |     | m   | 1   |     |
sonst.
Beachte:dasDCT-Spektrumistreinreellwertig!

Diskrete2D-Fouriertransformation Windowing BeispieleundAnwendungen DiskreteKosinustransformation(DCT)
Basisfunktionen der DCT
WiebeiderDFTgehtauchbeiderDCTkeineInformationverloren.
WarumkommtdieDCTohneSinustermeaus?Vergleichedie
FrequenzenderBasisfunktionen:
(cid:16) mu(cid:17)
DFT: CM(u)=cos 2π Frequenz:m/M
m M
(cid:18) (cid:19)
m(2u+1)
DCT: DM(u)=cos π
m 2M
(cid:18) (cid:19)
m(u+0.5)
=cos 2π Frequenz:1m/M
2M 2
DieFrequenzensindbeiderDCTalsonurhalbsogroßundliegen
daherdoppeltsodichtimSpektrum.DamitbrauchtmanbeiderDCT
doppeltsovieleKosinusfunktionenwiebeiderDFT,aberdafürkeine
Sinusfunktionen.

1 3 E i n f u¨ h r u n g in C8 m(u)=cos 2π mu S8 m(u)=sin 2π mu
|                              | `   | 8 ´ | ` 8 | ´   |     |     |     |     |     |     |
| ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Sp e kt r a l t e c h n i ke | n   |     |     |     |     |     |     |     |     |     |
m=0
|     | CD8 |     | Sin8 |     |     |     |     |     |     |     |
| --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
A b b i l d u n g 1 3 D .1 is 1 krete2 0-F(uo)uriertransformation Window 0g(u) BeispieleundAnwendungen DiskreteKosinustransformation(DCT)
Dis kr et e B a s isf u n k t i o n e n C M m ( u ) u n d 1 1
| S M m ( u ) fu¨ r d i e S i g n a l l ¨a n g e M = | 8                  |     |     |     |     |     |     |     |     |     |
| -------------------------------------------------- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| undWellenzahlenm=0...3.BJe-eis0.5piel:             | Basisfunkt0i.5onen |     |     |     |     |     |     |     |     |     |
|                                                    |                    |     | DFT | und | DCT |     |     |     |     |     |
derderPlotszeigtsowohldiedis- u u D8 D8 15.1EindimensionaleDCT
kretenFunktionswerte(durchrunde 1 2 3 4 5 6 7 8 1 2 3 4 5 6 7 8 0(u) m=0 4(u) m=4
| Punktemarkiert)wieauchdiezu-      |      |     |      |     | 1   |     | 1   |     |                     |                             |
| --------------------------------- | ---- | --- | ---- | --- | --- | --- | --- | --- | ------------------- | --------------------------- |
| geh¨origekontinuierlicheFunktion. | !0.5 |     | !0.5 |     |     |     |     |     | Abbildung15.1       |                             |
|                                   |      |     |      |     |     |     |     |     | D C T - B a s is fu | nk tio n en D M 0 (u ) .. . |
|                                   | !1   |     | !1   |     | 0.5 |     | 0.5 |     | D M ( u ) f u¨ r M  | = 8 . Je de rd er P l ots   |
7
|     |     |     |     |     |     |     | u   |     | u zeigtsowohldiediskretenFunktions- |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------- | --- |
1 2 3 4 5 6 7 8 1 2 3 4 5 6 7 8 werte(alsdunklePunkte)wieauch
|     |         |     | m=1     |     | !0.5        |     | !0.5        |     | diezugeh¨origekontinuierlicheFunk- |                                         |
| --- | ------- | --- | ------- | --- | ----------- | --- | ----------- | --- | ---------------------------------- | --------------------------------------- |
|     |         |     |         |     |             |     |             |     | t i o n . Im V e rg                | le ic h m it d e n B a s i s f u nk -   |
|     | C8 1(u) |     | S8 1(u) |     | !1          |     | !1          |     |                                    |                                         |
|     |         |     |         |     |             |     |             |     | t i o n en de r D                  | F T ( A bb .1 3 . 11 – 1 3 . 1 2 ) is t |
|     | 1       |     | 1       |     |             |     |             |     | zuerkennen,dassalleFrequenzender   |                                         |
|     |         |     |         |     | D8 1(u) m=1 |     | D8 5(u) m=5 |     | DCT-Basisfunktionenhalbiertund     |                                         |
|     | 0.5     |     | 0.5     |     |             |     |             |     |                                    |                                         |
|     |         |     |         |     | 1           |     | 1           |     | u m 0 . 5 E in h ei                | te n p h a s e n v e r s ch ob e n      |
1 2 3 4 5 6 7 8 u 1 2 3 4 5 6 7 8 u s i nd . A l le D C T - Ba s is f u n k t i o n en s in d
|     |      |     |      |     | 0.5 |     | 0.5 |     | alsou¨berdieDistanzvon2M=16 |     |
| --- | ---- | --- | ---- | --- | --- | --- | --- | --- | --------------------------- | --- |
|     | !0.5 |     | !0.5 |     |     |     |     |     |                             |     |
(anstattu¨berMbeiderDFT)Ein-
|     | !1  |     | !1  |     | 1 2 3 4 | 5 6 7 | 8 u 1 2 3 4 | 5 6 7 8 | u heitenperiodisch. |     |
| --- | --- | --- | --- | --- | ------- | ----- | ----------- | ------- | ------------------- | --- |
|     |     |     |     |     | !0.5    |       | !0.5        |         |                     |     |
|     |     |     |     |     | !1      |       | !1          |         |                     |     |
m=2
|     | C8 2(u) |         | S8 2(u)   |       |             |       |             |         |     |     |
| --- | ------- | ------- | --------- | ----- | ----------- | ----- | ----------- | ------- | --- | --- |
|     |         |         |           |       | D8 2(u) m=2 |       | D8 6(u) m=6 |         |     |     |
|     | 1       |         | 1         |       |             |       |             |         |     |     |
|     |         |         |           |       | 1           |       | 1           |         |     |     |
|     | 0.5     |         | 0.5       |       |             |       |             |         |     |     |
|     |         |         |           |       | 0.5         |       | 0.5         |         |     |     |
|     |         |         | u         | u     |             |       |             |         |     |     |
|     | 1 2 3 4 | 5 6 7 8 | 1 2 3 4 5 | 6 7 8 |             |       | u           |         | u   |     |
|     | !0.5    |         | !0.5      |       | 1 2 3 4     | 5 6 7 | 8 1 2 3 4   | 5 6 7 8 |     |     |
|     | !1      |         | !1        |       | !0.5        |       | !0.5        |         |     |     |
|     |         |         |           |       | !1          |       | !1          |         |     |     |
|     |         |         | m=3       |       | D8 3(u) m=3 |       | D8 7(u) m=7 |         |     |     |
|     | C8 3(u) |         | S8 3(u)   |       |             |       |             |         |     |     |
|     |         |         |           |       | 1           |       | 1           |         |     |     |
|     | 1       |         | 1         |       |             |       |             |         |     |     |
|     |         |         |           |       | 0.5         |       | 0.5         |         |     |     |
|     | 0.5     |         | 0.5       |       |             |       |             |         |     |     |
|     |         |         |           |       |             |       | u           |         | u   |     |
|     |         |         | u         | u     | 1 2 3 4     | 5 6 7 | 8 1 2 3 4   | 5 6 7 8 |     |     |
|     | 1 2 3 4 | 5 6 7 8 | 1 2 3 4 5 | 6 7 8 | !0.5        |       | !0.5        |         |     |     |
|     | !0.5    |         | !0.5      |       |             |       |             |         |     |     |
|     | !1      |         | !1        |       | !1          |       | !1          |         |     |     |
Natu¨rlichexistierenauchschnelleAlgorithmenzurBerechnungder
DCTundsiekannaußerdemmithilfederFFTmiteinemZeitaufwand
322
|     |     |     |     | von | (Mlog M)realisiertwerden[49,p.152].1DieDCTwirdh¨aufigin |     |     |     |     |     |
| --- | --- | --- | --- | --- | ------------------------------------------------------- | --- | --- | --- | --- | --- |
|     |     |     |     |     | O 2                                                     |     |     |     |     |     |
derBildkompressioneingesetzt,insbesondereimJPEG-Verfahren,wobei
die Gr¨oße der transformierten Teilbilder auf 8 8 fixiert ist und die
×
Berechnungdaherweitgehendoptimiertwerdenkann.
|     |     |     |     |     | 1ZurNotation ()s.Anhang1.3. |     |     |     |     |     |
| --- | --- | --- | --- | --- | --------------------------- | --- | --- | --- | --- | --- |
O
357

Diskrete2D-Fouriertransformation Windowing BeispieleundAnwendungen DiskreteKosinustransformation(DCT)
| Zweidimensionale |     |     | DCT |     |     |     |     |
| ---------------- | --- | --- | --- | --- | --- | --- | --- |
Füreinezweidimensionale,periodischeFunktiong(u,v)derGröße
M N istdie2D-DCT
×
|     |     | 2 M−1N−1 |     |     | (cid:18) m(2u+1) | (cid:19) (cid:18) | m(2v+1) (cid:19) |
| --- | --- | -------- | --- | --- | ---------------- | ----------------- | ---------------- |
(cid:88)(cid:88)
| G(m,n) | =   |     | g(u,v)c | m cos | π   | c n cos π |     |
| ------ | --- | --- | ------- | ----- | --- | --------- | --- |
|        |     | √MN |         |       | 2M  |           | 2N  |
u=0 v=0
|     |     | 2c c M−1N−1          |        |       |       |     |     |
| --- | --- | -------------------- | ------ | ----- | ----- | --- | --- |
|     |     | m n (cid:88)(cid:88) |        | DM(u) | DN(v) |     |     |
|     | =   |                      | g(u,v) |       |       |     |     |
|     |     | √MN                  |        | · m   | · n   |     |     |
u=0 v=0
Inverse2D-DCT:
|     |     | 2 M−1N−1 |     |     | (cid:18) m(2u+1) | (cid:19) (cid:18) | m(2v+1) (cid:19) |
| --- | --- | -------- | --- | --- | ---------------- | ----------------- | ---------------- |
(cid:88)(cid:88)
| g(u,v) | =   |     | G(m,n)c | cos | π   | c cos π |     |
| ------ | --- | --- | ------- | --- | --- | ------- | --- |
|        |     | √MN |         | m   | 2M  | n       | 2N  |
u=0 v=0
M−1N−1
|     |     | 2 (cid:88)(cid:88) |        |     | DM(u) DN(v) |     |     |
| --- | --- | ------------------ | ------ | --- | ----------- | --- | --- |
|     | =   |                    | G(m,n) | c   | c           |     |     |
|     |     | √MN                |        | · m | m · n       | n   |     |
u=0 v=0
Die2D-DCTistalsoebenfallsseparabel.

Diskrete2D-Fouriertransformation Windowing BeispieleundAnwendungen DiskreteKosinustransformation(DCT)
Beispielspektren für DFT und DCT
15Diediskrete Original DFT DCT
Kosinustransformation(DCT)
Abbildung15.2
Vergleichzwischenzweidimensionaler
DFTundDCT.BeideTransformatio-
nenmachenoffensichtlichBildstruk-
turenin¨ahnlicherWeisesichtbar.
ImreellwertigenDCT-Spektrum
(rechts)liegenalleKoeffizienten
innureinemQuadrantenbeisam-
menunddiespektraleAufl¨osungist
doppeltsohochwiebeiderDFT
(Mitte).DasDFT-Leistungsspektrum
istwieu¨blichzentriertdargestellt,
derUrsprungdesDCT-Spektrums
liegthingegenlinksoben.Inbei-
denF¨allensinddielogarithmischen
WertedesSpektrumsdargestellt.
Tats¨achlichexistierenzahlreiche¨ahnlicheTransformationen,vondenen
einige,wieetwadiediskreteKosinustransformation,ebenfallssinusoide
Funktionen als Basis verwenden, w¨ahrend andere etwa – wie z.B. die
Hadamard-Transformation(auchalsWalsh-Transformationbekannt)–
aufbin¨aren0/1-Funktionenaufbauen[16,48].
AlledieseTransformationensindglobaler Natur,d.h.,dieGr¨oßeje-
desSpektralkoeffizientenwirdingleicherWeisevonallenSignalwerten
beeinflusst,unabh¨angigvonihrerr¨aumlichenPositioninnerhalbdesSig-
nals. EineSpitze im Spektrum kann daherauseinem lokalbegrenzten
EreignismithoherAmplitudestammen,genausogutaberauchauseiner
breiten,gleichm¨aßigenWellemitgeringerAmplitude.GlobaleTransfor-
mationensinddaherfu¨rdieAnalysevonlokalenErscheinungenvonbe-
360