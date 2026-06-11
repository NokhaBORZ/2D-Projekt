Textur
2DComputerVision,VorlesungNo.12
Prof.Dr.M.O.Franz
HTWGKonstanz,FakultätfürInformatik
1/26

Übersicht
1 TexturenundihreAnwendungen
2 TexturanalysedurchFilterbänke
3 StatistikenvonBildmerkmalenundKlassifikation
2/26

Übersicht
1 TexturenundihreAnwendungen
2 TexturanalysedurchFilterbänke
3 StatistikenvonBildmerkmalenundKlassifikation
3/26

Texturen
lat.texere-weben,flechten
EsgibtkeineformaleDefinitionfür
Texturen(ca.10unterschiedliche
DefinitionsversucheinderLiteratur)
Menschenerkennenbestimmte
BildbereicheanhandderTextur(Fell,
Haare,...)
NichtalleBildbereicheenthalten
Texturen.
Arbeitsdefinition:TexturensindBildbereichemiteinereinheitlichen
lokalenBildeigenschaft.
4/26

Repräsentation von Texturen
TexturenbestehenausräumlichenAnordnungenvonmehroderweniger
variablenUntereinheiten(Textonen).
EineTexturwirddaherdefiniertdurch
ArtundWahrscheinlichkeitsverteilungderTextonen
RäumlicheKombinations-undAnordnungsregelnfürdieTextonen
EsgibtzweigrundsätzlichverschiedeneHerangehensweisen:
syntaktisch:TextonenwerdennachdenRegelneinerformalenSprache
kombiniert,TexturanalysedurcheinenParser(Voraussetzung:
Textonenmüsseneindeutigbestimm-undlokalisierbarsein,
deterministischeGrammatik⇒wenigpraxisrelevant)
statistisch:TexturenwerdenüberStatistikenvonBildmerkmalen
definiert.
5/26

Anwendung von Texturen
KlassifikationvonOberflächenundSzenen:
KlassifikationvonTexturen
BewertungvonOberflächen
IndizierungvonTextenundBildern
DetektionvonstrukturellenDefekteninOberflächen
HerstellungsfehlerinTextilien
Holzfehler
RisseinKacheln
Textursegmentierung
TerraintypeninLuft-undSatellitenbildern
GewebetypeninUltraschall-,Röntgen-,fMRI-Bildern
TexteinDokumenten
WeitereAnwendungen:
TextursyntheseinderComputergraphik
RekonstruktionvonOberflächen(shapefromtexture)
6/26

Texturanalyse
”Texturesynthesisexhausteduslongbeforewecouldexhaustit.”
[Forsyth&Ponce,2003]
DieTexturanalyseisteinerderBereichederBildverarbeitung,beidemes
nochanGrundlagenfehlt⇒esgibteinesehrgroßeAnzahlempirischerund
halbempirischerAnsätze.TypischerAufbaueinesSystemszurstatistischen
Texturanalyse:DetektionvonstrukturellenDefekten:
KlassifikationvonOberflächen,Segmentierung:
7/26

Übersicht
1 TexturenundihreAnwendungen
2 TexturanalysedurchFilterbänke
3 StatistikenvonBildmerkmalenundKlassifikation
8/26

| Detektion | von Textonen | mit Filtern |
| --------- | ------------ | ----------- |
Grundidee:DetektionvoneinfachenGrundelementenderTextur
durchdaranangepaßteFilter
9/26

| Filterantwort | auf verschiedenen | Texturen |
| ------------- | ----------------- | -------- |
10/26

Filterbänke
Probleme:
ArtundGrößederTextonensind
(meist)nichtbekannt.
Esgibtkeinenkanonischen
Texturkatalog.
⇒GenerischeFilter,ausdenensichalle
anderenBildelementeaufbauenlassen
(z.B.BlobsoderKanten)
⇒FiltersatzinverschiedenenGrößen
(Multiskalenansatz).
Tradeoff:AnzahlderunterscheidbarenTexturennimmtmitder
AnzahlderFilterzu,Laufzeitauch.
11/26

Multiskalenanalyse mit Gaußpyramide
1 GlättungjedesLevelsmit
Gaußfilter
1
| G = | e − 1 (x2+y2), | [Forsyth&Ponce,2003] |
| --- | -------------- | -------------------- |
| σ   | 2σ 2           |                      |
| 2π  | σ2             |                      |
Hochredundant!
↓
| 2 SubsamplingS | umFaktor2 |     |
| -------------- | --------- | --- |
2
↓
| I n+1 | = S G σ I n |     |
| ----- | ----------- | --- |
2
12/26

Multiskalenanalyse mit Laplacepyramide
1 BerechneGaußpyramide
↑
2 UpsamplingS umFaktor2
2
3 Differenzzwischenfeinund
grobaufgelöstemBild
L = I −S ↑I
n n 2 n+1
[Forsyth&Ponce,2003]
Bandpaßcharakteristik:Zerlegung
nachräumlichenFrequenzen,aber
keineOrientierungsanalyse
13/26

| Orientierte | Pyramiden |     |
| ----------- | --------- | --- |
Gaborfilter
| sym      | y)e− | 1 (x2+y2) |
| -------- | ---- | --------- |
| G =cos(k | x+k  | 2σ 2      |
| σ        | x y  |           |
| asym     | y)e− | 1 (x2+y2) |
| G =sin(k | x+k  | 2σ 2      |
| σ        | x y  |           |
analysierenorientierteStrukturen
bestimmterGröße.
Texturanalysesystemehaben4-11Skalen,
[Simoncellietal.1992]
2-18Orientierungen
14/26

Übersicht
1 TexturenundihreAnwendungen
2 TexturanalysedurchFilterbänke
3 StatistikenvonBildmerkmalenundKlassifikation
15/26

Statistiken von Bildmerkmalen
DieMerkmalsextraktionmitFilterbänkenliefertfürjedenFilterund
jedenPixelderTextureinereellwertigeFilterantwort.
TexturwirddurchdiespezifischeVerteilungderFilterantwortenin
einemTestfenstercharakterisiert.
EswerdenKennzahlen(Statistiken)benötigt,diedieVerteilungder
Filterantwortenbeschreiben.
EinfachsterAnsatz:Mittlere
quadratischeFilterantwortüber
Testfenster,ergibteinen
MerkmalsvektormitkElementen(bei
kFiltern).
Alternative:MittelwertundVarianz
derFilterantwort(2k-dimensionaler
Merkmalsvektor).
16/26

| Ranking | von Texturen | nach Distanz | der Merkmalsvektoren |
| ------- | ------------ | ------------ | -------------------- |
[Maetal.,1996]
17/26

Strukturelle Statistiken
Problem:Mittelwert,VarianzodermittlerequadratischeAntwort
sagennichtsüberdieräumlicheVerteilungderFilterantwortenaus⇒
StrukturelleStatistikennotwendig
sindnurStatistikenersterundzweiterOrdnung.Menschenbenutzen
auchStatistikenhöhererOrdnung,umTexturenzuunterscheiden.
Ansätze:
BestimmungderKovarianzderFilterantwortf(x,y)imTestfenster
C (x,y)=E[(f(x ,y )−f ¯)(f(x,y)−f ¯)]
f 0 0
seltenrobust,meistwerdennureinigespeziellgewählteTerme
geschätzt.
HistogrammederlokalenVerteilungineinerkleinenNachbar-schaft
(co-occurrence-Matrizen)bzw.darausberechneteKenn-werte
(Entropie,Energie,maximaleWahrscheinlichkeit,...),ebenfallsselten
robust.
18/26

Klassifikation
NachdemdieVerteilungderFilterantwortendurch
entsprechendeStatistikencharakterisiertist,mußalsletzter
SchritteineEntscheidung(Klassifikation)getroffenwerden.
JenachProblemstellungmüsseneinerodermehrere
KlassifikatorenamhandvonBeispielentrainiertwerden:
DetektionvonDefekten:einKlassifikatorfürdieEntscheidung
Defektvorhandenbzw.nichtvorhanden
Segmentierung/Oberflächenklassifikation:fürnTexturklassen
werdenn(onevs.rest)oder 1n(n−1)Klassifikatoren(onevs.one)
2
undggf.eineArbitrierungsstufebenötigt.
MöglicheKlassifikatoren:
einfachsteMöglichkeit(häufigausreichend):empirisch
bestimmterSchwellwertbzw.Winnertakesall
NeuronaleNetze(Standardpakete)
Supportvektormaschinen(freiimInternetverfügbar)
....
19/26

Zusammenfassung
TexturensindBildbereichemiteinereinheitlichenlokalen
Bildeigenschaft.InderPraxiswerdenTexturenüberStatistiken
vonBildmerkmalendefiniert.
EintypischesTexturklassifikationssystembestehtaus3Stufen:
1.Merkmalsextraktion;2.BerechnungstatistischerKennzahlen
fürdieVerteilungderMerkmale;3.Klassifikation.
MerkmalsextraktiongeschiehthäufigüberFilteralsDetektoren
fürlokaleBildstrukturen,oftinFormeinerorientierten
Pyramide.
AlsStatistikreichenoftMittelwerteundVarianzender
Filterantworten,alsKlassifikatoreinfacheSchwellwerteoder
Winner-takes-all-Architekturen.BessereKlassifikationsleistung
erreichenStandardverfahrenwieneuronaleNetzeoderSVM.
20/26

Bewertung von Oberflächen
[Silven,2000]
[Pannekamp,2005]
21/26

Herstellungsfehler in Textilien
[Chetverikov&
Hanbury,2001]
22/26

Astlöcher in Holzplatten
[Silvenetal.,
2000]
23/26

| Segmentierung | von Gewebe | in der medizinischen |
| ------------- | ---------- | -------------------- |
Bildgebung
[Glatardetal.,2004]
24/26

| Segmentierung | von Text | in Dokumenten |
| ------------- | -------- | ------------- |
[Jainetal.,1992]
25/26

| Klassifikation | von Terraintypen | in Satellitenbildern |
| -------------- | ---------------- | -------------------- |
[INRIA,2005]
26/26