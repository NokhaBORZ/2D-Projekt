DetektionvonEckpunkten Hough-TransformationfürGeraden Hough-TransformationfürKreiseundEllipsen
| Detektion | von Eckpunkten | und einfachen |
| --------- | -------------- | ------------- |
Kurven
61
| 2D  | Computer Vision, Vorlesung | No. |
| --- | -------------------------- | --- |
|     | M. O. Franz                |     |
1
fallsnichtandersvermerkt,sinddieAbbildungenentnommenausBurger&Burge,2005.

DetektionvonEckpunkten Hough-TransformationfürGeraden Hough-TransformationfürKreiseundEllipsen
Übersicht
Detektion von Eckpunkten
1
| 2 Hough-Transformation | für Geraden    |          |
| ---------------------- | -------------- | -------- |
| 3 Hough-Transformation | für Kreise und | Ellipsen |

DetektionvonEckpunkten Hough-TransformationfürGeraden Hough-TransformationfürKreiseundEllipsen
Übersicht
Detektion von Eckpunkten
1
| 2 Hough-Transformation | für Geraden    |          |
| ---------------------- | -------------- | -------- |
| 3 Hough-Transformation | für Kreise und | Ellipsen |

DetektionvonEckpunkten Hough-TransformationfürGeraden Hough-TransformationfürKreiseundEllipsen
Eckpunkte
EckpunkteinBildernsinddieBasisfüreineVielzahlvon
Anwendungen:
VerfolgungvonObjekteninaufeinanderfolgendenVideobildern
(tracking)
ZuordnungvonBildstruktureninStereoaufnahmen
ReferenzpunktezurgeometrischenVermessungmiteinemoder
vielenBildern
KalibrierungvonKameras
alsAnkerpunktebeiderSegmentierungvonObjekteninseine
Teile
EckpunktesindrobusteMerkmale:siebleibenineinembreiten
BereichvonAnsichtswinkelnundBeleuchtungsbedingungen
detektierbar.

DetektionvonEckpunkten Hough-TransformationfürGeraden Hough-TransformationfürKreiseundEllipsen
Detektion von Eckpunkten
Kanten:Bildbereiche,indenenderGradientineinerRichtunghoch
undsenkrechtdazuniedrigist.
Eckpunkte:Bildbereiche,indenenderGradientinmehralseiner
Richtunghochist.
GewünschteEigenschaften:
UnterscheidungvonwichtigenundunwichtigenEckpunkten
ZuverlässigesAuffindenvonEckpunktenunterBildrauschen
GenaueLokalisierungderEckpunkte
MöglichstwenigRechenaufwand
UnabhängigvonderOrientierungderEcken

DetektionvonEckpunkten Hough-TransformationfürGeraden Hough-TransformationfürKreiseundEllipsen
Harris-Detektor (1)
PartielleBildableitunginhorizontalerundvertikalerRichtung:
∂I ∂I
∂ I(u,v)= (u,v) und ∂ I(u,v)= (u,v)
x ∂x y ∂y
DarausBerechnungderlokalenStrukturmatrix:
(cid:18) ∂ I2 ∂ I∂ I (cid:19)
M = x x y
∂ I∂ I ∂ I2
x y y
GewichteteMittelungvonM mitGaußfilterH :
σ
(cid:18) ∂ I2∗H ∂ I∂ I∗H (cid:19) (cid:18) A C (cid:19)
M = x σ x y σ =
∂ I∂ I∗H ∂ I2∗H C B
x y σ y σ
Eigenwerte:
(cid:114)
tr(M) tr(M)2 1 (cid:112)
λ = ± −detM = (A+B± A2−2AB+B2+4C2)
1,2
2 4 2

DetektionvonEckpunkten Hough-TransformationfürGeraden Hough-TransformationfürKreiseundEllipsen
| Harris-Detektor (2) |     |     |
| ------------------- | --- | --- |
InterpretationderEigenwerte(beidesindpositiv):Eigenwerte
codierendieKantenstärke,EigenvektorendieKantenrichtung.
InuniformenBildregionenistMnahean0anddamitauchλ
1 1
| undλ ⇒λ =0,λ | =0. |     |
| ------------ | --- | --- |
2 1 2
2 AnKantenistderGradientnursenkrechtzurSprungkante
größerals0,entlangderKanteister0⇒λ >0,λ =0.
1 2
AnEckpunktenistderGradientinmehralseinerRichtung
3
| größerals0⇒λ | >0,λ >0. |     |
| ------------ | -------- | --- |
1 2
StattderEigenwertewird”Eckenstärke”mit
Empfindlichkeitsparameterα∈[0.04..0.06]berechnet:
| Q(u,v)=detM−αtr(M)2 | =λ λ −α(λ | +λ )2 =(AB−C2)−α(A+B)2 |
| ------------------- | --------- | ---------------------- |
|                     | 1 2       | 1 2                    |
Eckenwerdendetektiert,wennQ(u,v)einenSchwellwert
überschreitet.

DetektionvonEckpunkten Hough-TransformationfürGeraden Hough-TransformationfürKreiseundEllipsen
| Harris-Detektor | (3) |     |     |     |
| --------------- | --- | --- | --- | --- |
”Eckenstärke”:
|                          | Q(u,v)=detM−αtr(M)2 |                       |                 | )2  |
| ------------------------ | ------------------- | --------------------- | --------------- | --- |
|                          |                     | =λ                    | 1 λ 2 −α(λ 1 +λ | 2   |
| 1 UniformeBildregionen:λ |                     | 1 =0,λ 2 =0⇒Q(u,v)=0. |                 |     |
| Kanten:λ                 | >0,λ =0⇒Q(u,v)=−αλ2 |                       | <0              |     |
| 2                        | 1 2                 |                       | 1               |     |
| 3 Eckpunkte:λ            | >λ >0.⇒             |                       |                 |     |
1 2
| Q(u,v)=λ | λ −α(λ | +λ )2 >λ2−2αλ2 | =(1−2α)λ2,d.h.für |     |
| -------- | ------ | -------------- | ----------------- | --- |
|          | 1 2 1  | 2 2            | 2                 | 2   |
1
| α<  | istQnuranEckpunktenechtpositiv. |     |     |     |
| --- | ------------------------------- | --- | --- | --- |
2
UmrobustgegenRauschenzusein,wirdsicherheitshalberein
Schwellwert>0(typisch:25000)eingeführt,abdemeinEckpunkt
markiertwird.

DetektionvonEckpunkten Hough-TransformationfürGeraden Hough-TransformationfürKreiseundEllipsen
| Harris-Detektor: | Algorithmus | (1) |
| ---------------- | ----------- | --- |

DetektionvonEckpunkten Hough-TransformationfürGeraden Hough-TransformationfürKreiseundEllipsen
| Harris-Detektor: | Algorithmus | (2) |
| ---------------- | ----------- | --- |

DetektionvonEckpunkten Hough-TransformationfürGeraden Hough-TransformationfürKreiseundEllipsen
Harris-Detektor: Parameterwerte

DetektionvonEckpunkten Hough-TransformationfürGeraden Hough-TransformationfürKreiseundEllipsen
Harris-Detektor: Beispiel

DetektionvonEckpunkten Hough-TransformationfürGeraden Hough-TransformationfürKreiseundEllipsen
Übersicht
Detektion von Eckpunkten
1
| 2 Hough-Transformation | für Geraden    |          |
| ---------------------- | -------------- | -------- |
| 3 Hough-Transformation | für Kreise und | Ellipsen |

DetektionvonEckpunkten Hough-TransformationfürGeraden Hough-TransformationfürKreiseundEllipsen
Kantenverfolgung
KantendetektorenproduziereneineVielzahlvonirrelevanten
Kanten,zusätzlichsinddiewichtigenKantenoft
unzusammenhängend.
Kantenverfolgungistdahereinschwieriges,nochnichtgelöstes
Problem(Verzweigungen,VerschmelzungvonKantenusw.).
Hier:SuchenacheinfachengeometrischenKonturen,diesich
durchparametrisierteFormelnbeschreibenlassen.

DetektionvonEckpunkten Hough-TransformationfürGeraden Hough-TransformationfürKreiseundEllipsen
Hough-Transformation
MitderHough-Transformationlassensichbeliebige,
parametrisierbareFormeninPunktverteilungenlokalisieren(z.B.
Geraden,Kreise,Ellipsen).Sieistdaherbesondersgeeignetzur
DetektionkünstlicherObjekte.

DetektionvonEckpunkten Hough-TransformationfürGeraden Hough-TransformationfürKreiseundEllipsen
| Beispiel | für eine | parametrisierbare |     | Form: Gerade |
| -------- | -------- | ----------------- | --- | ------------ |
ZweidimensionaleGeradengleichung:
y=kx+d
2Parameter:Steigungkundy-Achsenabschnittd.FüreineGerade,
| diedurch2Punktep |     | =(x ,y   | )undp =(x | ,y )gilt |
| ---------------- | --- | -------- | --------- | -------- |
|                  |     | 1 1      | 1 2       | 2 2      |
|                  |     | y =kx +d | und y =kx | +d       |
|                  |     | 1 1      | 2         | 2        |

DetektionvonEckpunkten Hough-TransformationfürGeraden Hough-TransformationfürKreiseundEllipsen
Parameterraum
Ziel:AuffindenderGeradenmitParameternkundd,aufdenen
möglichstvielePunkteliegen.
DieHough-Transformationsuchtimvonkundd gebildeten
zweidimensionalenParameterraumalleGeraden,diedurcheinen
gegebenenPunktp =(x ,y )laufen.
0 0 0

DetektionvonEckpunkten Hough-TransformationfürGeraden Hough-TransformationfürKreiseundEllipsen
| Geraden          | im Bild- | und Parameterraum | (1) |
| ---------------- | -------- | ----------------- | --- |
| BeliebigeGeradeL |          | durchp :          |     |
j 0
L : y =kx +d
|                                              |     | j 0 j 0 j |           |
| -------------------------------------------- | --- | --------- | --------- |
| ImParameterraumistdieMengeallerGeradendurchp |     |           | ebenfalls |
0
eineGerade:
|     |     | d j =−x 0 k j +y 0 . |     |
| --- | --- | -------------------- | --- |
FürbeliebigePunktegiltalsofolgendeBeziehung:

DetektionvonEckpunkten Hough-TransformationfürGeraden Hough-TransformationfürKreiseundEllipsen
| Geraden | im Bild- | und Parameterraum | (2) |
| ------- | -------- | ----------------- | --- |
WennsichnGeradenimParameterraumanPosition(k(cid:48),d(cid:48))
schneiden,dannliegenaufderentsprechendenGeradeny=k(cid:48)x+d(cid:48)
imBildrauminsgesamtnBildpunkte.

DetektionvonEckpunkten Hough-TransformationfürGeraden Hough-TransformationfürKreiseundEllipsen
Akkumulator-Array
Akkumulator-Array:DiskreteRepräsentationdesParameterraumes.
GrundideederHough-Transformation:Fürjedengefundenen
| Bildpunktp | werdendieZählerimAkkumulator-Arrayentlangder |     |
| ---------- | -------------------------------------------- | --- |
0
| Geradend | =−x k +y | um1erhöht. |
| -------- | -------- | ---------- |
|          | j 0 j    | 0          |

DetektionvonEckpunkten Hough-TransformationfürGeraden Hough-TransformationfürKreiseundEllipsen
| Eine bessere | Geradenparametrisierung |     |     |
| ------------ | ----------------------- | --- | --- |
Problem:VertikaleGeradenhabenSteigungk=∞.
| HessescheNormalform: |     | xcosθ+ysinθ | =r  |
| -------------------- | --- | ----------- | --- |
√
| mit0≤θ | <π und−r | ≤r≤r mitr | = 1 M2+N2. |
| ------ | -------- | --------- | ---------- |
|        | max      | max       | max 2      |

DetektionvonEckpunkten Hough-TransformationfürGeraden Hough-TransformationfürKreiseundEllipsen
Hough-Algorithmus für Geraden

DetektionvonEckpunkten Hough-TransformationfürGeraden Hough-TransformationfürKreiseundEllipsen
Programmbeispiel

DetektionvonEckpunkten Hough-TransformationfürGeraden Hough-TransformationfürKreiseundEllipsen
| Beispiel | Hough-Transformation | in  |
| -------- | -------------------- | --- |
Hesse-Parameterraum

DetektionvonEckpunkten Hough-TransformationfürGeraden Hough-TransformationfürKreiseundEllipsen
Auswertung des Akkumulator-Arrays
Problem:DieSinuskurvenschneidensichnichtgenauaneinem
Punkt,sondernineinerRegion.DieLokalisierungderMaximaist
daherderschwierigsteTeilderHough-Transformation.
AnsatzA:Schwellwerte.AlleAkkumulatorzellenunterhalbeines
Schwellwerteswerdenverworfen.Dieübrigenwerdenmiteiner
morphologischenClosing-Operationbereinigt(s.nächsteVorlesung)
undanschließendderSchwerpunktderRegionenbestimmt(s.
übernächsteVorlesung).
AnsatzB:Non-Maximum-Supression.AlleNicht-Maximawerden
verworfen,d.h.alleZellen,derenEinträgenichtgrößeralsdiealler
Nachbarnsind.AnschließendwerdendiegrößtenWertemiteiner
Schwellwertoperationgefunden.

DetektionvonEckpunkten Hough-TransformationfürGeraden Hough-TransformationfürKreiseundEllipsen
| Beispiel: | Auswertung | des Akkumulator-Arrays |
| --------- | ---------- | ---------------------- |

DetektionvonEckpunkten Hough-TransformationfürGeraden Hough-TransformationfürKreiseundEllipsen
Bias-Problem
Problem:Gewichteiner
Geradenbestimmtsichaus
ihrerLänge,aberweitvom
Bildzentrumhatesoftzuwenig
PlatzfürlangeGeraden⇒
bestimmteTeiledes
Akkumulator-Arrayshaben
nichtdiegleiche
Füllwahrscheinlichkeitwie
andere(Bias).
Ansatz:NormierungmitderAnzahln [θ,r]derüberhaupt
max
möglichenGeraden
Acc[θ,r]
Acc(cid:48)[θ,r]= ,
n [θ,r]
max
Bestimmungvonn [θ,r]übervollständigoderzufälliggefülltesBild.
max

DetektionvonEckpunkten Hough-TransformationfürGeraden Hough-TransformationfürKreiseundEllipsen
Erweiterungen der Hough-Transformation
EndpunktevonBildgeraden.DasnachträglicheAufsuchenvon
Endpunktenistaufwendigundwenigrobust.BeimFüllendes
Akkumulator-Arrayskannmanhierzudiejeweilsmaximalen
bzw.minimalenx/y-KoordinatenderPunktemitspeichern,d.h.
Acc[θ,r]=(count,start ,start ,end ,end )
x y x y
BerücksichtigungvonKantenstärkeund-orientierung.Stattden
Akkumulatorum1zuerhöhen,kannstattdessendie
Kantenstärkeaufaddiertwerden.WenndieOrientierungbekannt
ist,müssennurdiedamitkompatiblenZellenmitder
entsprechendenWinkelkoordinatehochgezähltwerden.
HierachischeHough-Transformation.ZuerstSucheingrob
gerastertemParameterraum,dannfeinereAbtastungumdie
Maximaherum.

DetektionvonEckpunkten Hough-TransformationfürGeraden Hough-TransformationfürKreiseundEllipsen
Übersicht
Detektion von Eckpunkten
1
| 2 Hough-Transformation | für Geraden    |          |
| ---------------------- | -------------- | -------- |
| 3 Hough-Transformation | für Kreise und | Ellipsen |

DetektionvonEckpunkten Hough-TransformationfürGeraden Hough-TransformationfürKreiseundEllipsen
| Parametrisierung | von Kreisen | und Ellipsen |
| ---------------- | ----------- | ------------ |
Kreisehängennichtnurvon2,sondernvon3Parameternab:x-und
y-Position(¯x,¯y)desMittelpunktsundRadiusρ:
|     | (u−¯x)2+(v−¯y)2 | =ρ2 |
| --- | --------------- | --- |
WirbenötigendahereindreidimensionalesAkkumulator-Array,um
Kreise(undKreisbögen)zufinden.

DetektionvonEckpunkten Hough-TransformationfürGeraden Hough-TransformationfürKreiseundEllipsen
”Brute-Force”-Ansatz
GesuchtwirdwiederdieMengeallerKreise,diedurcheinen
gegebenenBildpunktp(u,v)gehen.LeiderproduziertdieseMenge
keineeinfachzuberechnendenKurvenimParameterraum.
”Brute-Force”-Ansatz:TestefürjedeZelleimAkkumulator-Array(d.h.
jedenParametersatz),oberdieKreisgleichungerfüllt:

DetektionvonEckpunkten Hough-TransformationfürGeraden Hough-TransformationfürKreiseundEllipsen
| Einfache | Kurven für | fixen Radius | ρ   |
| -------- | ---------- | ------------ | --- |
1
| FüreinenfixenRadiusρ |     | liegenalleMittelpunktevonKreisendurch |     |
| -------------------- | --- | ------------------------------------- | --- |
1
einenPunktp(u,v)ebenfallsaufeinemKreismitRadiusρ und
1
Mittelpunktp(u,v).

DetektionvonEckpunkten Hough-TransformationfürGeraden Hough-TransformationfürKreiseundEllipsen
Hough-Transformation für Kreise
FürjedenneuenPunktp(u,v)mußalsonichtdergesamte
Parameterraumdurchsuchtundgetestetwerden,sondernjeweilsein
KreismitMittelpunktp(u,v)undRadiusρinjederRadius-Ebeneρ
hochgezähltwerden.

DetektionvonEckpunkten Hough-TransformationfürGeraden Hough-TransformationfürKreiseundEllipsen
Hough-Transformation für Ellipsen
Ellipsenhängenvon5Parameternab:x-undy-Position(¯x,¯y)des
MittelpunktsundzweiDurchmessera,bundOrientierungα,d.h.wir
benötigeneinen5-dimensionalenParameterraum.Bei128
Auflösungsschrittenergibtdas235 Akkumulatorzellen,alsobei
4-Byte-Integerzellen128GB.
⇒nichtpraktikabel!(⇒verallgemeinerteHough-Transformation).