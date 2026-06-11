Einführung RadiometrieundPhotometrie Lichtquellen Beleuchtung
Bildentstehung
| 2D Computer | Vision, Vorlesung | No. 11 |
| ----------- | ----------------- | ------ |
| Prof.       | Dr. M. O. Franz   |        |
mfranz@htwg-konstanz.de
1
fallsnichtandersvermerkt,sinddieAbbildungenentnommenausHaußecker,1999.

Einführung RadiometrieundPhotometrie Lichtquellen Beleuchtung
Überblick
1 Einführung
2 Radiometrie und Photometrie
3 Lichtquellen
4 Beleuchtung

Einführung RadiometrieundPhotometrie Lichtquellen Beleuchtung
Übersicht
1 Einführung
2 Radiometrie und Photometrie
3 Lichtquellen
4 Beleuchtung
3/34

Einführung RadiometrieundPhotometrie Lichtquellen Beleuchtung
| Vorlesung |     | 2D  | Computer |     | Vision |     |     |     |
| --------- | --- | --- | -------- | --- | ------ | --- | --- | --- |
Ziele:
|     | Die        | Grundlagen |                  | der | automatischen                | Verarbeitung |           | von |
| --- | ---------- | ---------- | ---------------- | --- | ---------------------------- | ------------ | --------- | --- |
|     | Bildern    |            | mit Rechnern     |     | für Automatisierungsaufgaben |              |           | in  |
|     | Industrie, |            | Medizin          | und | Wirtschaft                   | kennenlernen |           |     |
|     | Digitale   |            | Bildverarbeitung |     | anhand                       | einfacher    | Beispiele | zu  |
praktizieren
Aufbau:
| 2   | SWS | Vorlesung, |     | anschließend | 2   | SWS praktische |     | Übungen in |
| --- | --- | ---------- | --- | ------------ | --- | -------------- | --- | ---------- |
Python.
4/34

Einführung RadiometrieundPhotometrie Lichtquellen Beleuchtung
Bildverarbeitung
Definition:
AutomatischeAuswertungvonKamerabildernzurDurchführungvon
Meß-undSteuerungaufgaben.Insbesonderewirdversucht,Aspekte
dervisuellenIntelligenzdesMenschenzuautomatisieren.
DieBildverarbeitungwirdoftmitBildbearbeitungverwechselt
(d.h.interaktiveVerbesserungdesBildesdurchdenMenschen).
ZielderBildverarbeitungistes,dieseProzessezu
automatisieren.
Computergraphikgehtumgekehrtvor:Bilderwerdennicht
analysiertsondernsythetisiert.
OftwirddieBildverarbeitungaufgeteiltindiebildnahe,
pixelbasierteVorverarbeitungundMerkmalsextraktionunddas
eigentlicheRechnersehen(ComputerVision),das
ObjekterkennungunddreidimensionaleRekonstruktionumfaßt.
5/34

Einführung RadiometrieundPhotometrie Lichtquellen Beleuchtung
| Beispiel: | Qualitätskontrolle | in der Produktlinie |
| --------- | ------------------ | ------------------- |
[Diehl/Massen]
6/34

Einführung RadiometrieundPhotometrie Lichtquellen Beleuchtung
| Beispiel:   | Schrifterkennung | (Optical | Character |
| ----------- | ---------------- | -------- | --------- |
| Recognition | - OCR)           |          |           |
7/34

Einführung RadiometrieundPhotometrie Lichtquellen Beleuchtung
| Beispiel:    | Objekterkennung | (Kategorie,       | Position, |
| ------------ | --------------- | ----------------- | --------- |
| Ausrichtung, | Anzahl,         | Konfiguration...) |           |
[Diehl/Massen]
8/34

Einführung RadiometrieundPhotometrie Lichtquellen Beleuchtung
| Beispiel: | Medizinische | Bildverarbeitung |
| --------- | ------------ | ---------------- |
[Diehl/Massen]
9/34

Einführung RadiometrieundPhotometrie Lichtquellen Beleuchtung
Beispiel: Luftbildauswertung
[Diehl/Massen]
10/34

Einführung RadiometrieundPhotometrie Lichtquellen Beleuchtung
Inhalte der Vorlesung
IndieserVorlesungwirdnurklassischebildnaheund
pixelbasierteVorverarbeitungundMerkmalsextraktion
behandelt,dadiesedieGrundvoraussetzungfüralle
weitergehendenTechnikenbilden.
GrundlagenderKlassifikationundObjekterekennenungwerden
inVorlesungArtificialIntelligencebehandelt.
DieVerarbeitungvondreidimensionalenPunktwolkenwirdinder
Vorlesung3DComputerVisionbehandelt.
FortgeschritteneMethodendesRechnersehens(Computer
Vision)istGegenstandeinergleichnamigenVorlesungim
Master-StudiengangInformatik(MSI).
FortgeschritteneTechnikendesmaschinellenLernensundDeep
LearningwerdenindergleichnamigenVorlesungimMSI
vermittelt.
11/34

Einführung RadiometrieundPhotometrie Lichtquellen Beleuchtung
Themen der Vorlesung
Bildentstehungund-aufnahme
Punktoperationen
Filter
KanteninBildern
DetektionvonEckpunktenundeinfachenKurven
MorphologischeFilterung
RegionenbasierteVerfahren
Spektraltechniken
Farbräume
Bildkompression
Texturen
12/34

Einführung RadiometrieundPhotometrie Lichtquellen Beleuchtung
Literatur
W.Burger&M.J.Burge:DigitaleBildverarbeitung.Springer
2006.
GutverständlicheEinführung,decktbisaufBildentstehungund-aufnahmedenVorlesungsstoffkomplettab.
B.Jähne:DigitaleBildverarbeitung.Springer2005.
HäufigaktualisiertesStandardwerk,gehtimUmfangüberdieVorlesunghinaus.Nichtganzsoleicht
zugänglich,aberlohnend.
R.C.Gonzalez&R.E.Woods:DigitalImageProcessing.
Addison-Wesley,1993.
HäufigzitiertesStandardwerk.DecktVorlesungsstoffab,gehtaberanmanchenStellenweitdarüberhinaus.
13/34

Einführung RadiometrieundPhotometrie Lichtquellen Beleuchtung
Übersicht
1 Einführung
2 Radiometrie und Photometrie
3 Lichtquellen
4 Beleuchtung
14/34

Einführung RadiometrieundPhotometrie Lichtquellen Beleuchtung
Radiometrie und Photometrie
Radiometrie:TeilgebietderPhysik,
dassichmitderMessungvon
Strahlungbefaßt.
Photometrie:MessungvonStrahlung,
wobeijedeStrahlungskomponentemit
derwellenlängenabhängigen
Empfindlichkeitdesmenschlichen
Augesgewichtetwird.
PhysikalischgesehensindKameras
Strahlungsmeßinstrumente.
LichtisteineFormder
elektromagnetischenStrahlung,
gekennzeichnetdurchseineFrequenz
bzw.Wellenlänge.
15/34

Einführung RadiometrieundPhotometrie Lichtquellen Beleuchtung
Radiometrische Größen
Strahlungsleistung(oder-fluß):Φ= dQ [W =J/s∗]
dt
SpezifischeAusstrahlung(derQuelle):M = dΦ [W/m2]
dS
Bestrahlungsstärke(desEmpfängers):E= dΦ [W/m2]
dS
∗ wirdoftauchinPhotonenprosgemessen.IndiesemFallmußdieWattzahl
durchdieEnergiehν eineseinzelnenPhotonsgeteiltwerden.
16/34

Einführung RadiometrieundPhotometrie Lichtquellen Beleuchtung
Winkel in der Fläche und Raumwinkel, Strahlstärke
Raumwinkel(inSteradiant):
FlächeAaufEinheitskugel
EbenerWinkel:Bogenlänges
A
normiertdurchAbstandrbzw. Ω=
r2
BogenlängeaufEinheitskreis
Strahlstärke:
s
θ =
r dΦ
I = [W/sr]
dΩ
17/34

Einführung RadiometrieundPhotometrie Lichtquellen Beleuchtung
Spektrale und radiometrische Größen
DiebisherbesprochenenradiometrischenGrößenignorierendie
VerteilungderWellenlängendesLichts,z.B:rotesLichtwird
genausobehandeltwieblauesLicht,obwohlKamerasauf
beidesunterschiedlichreagieren.
ManbetrachtetdaheroftspektraleGrößen,beiderdie
radiometrischenGrößennurinnerhalbeinesinfinitesimalen
Wellenlängenbereichsdλgemessenwerden,z.B.diespektrale
StrahlungsleistungfüreinegegebeneWellenlängeλ
dΦ
Φ = [W/m]
λ dλ
DieradiometrischenGrößenerhältmanausdenspektralen
GrößendurchIntegrationüberdasgesamteSpektrum,z.B.
(cid:90) ∞
Φ= Φ dλ
λ
0
18/34

Einführung RadiometrieundPhotometrie Lichtquellen Beleuchtung
| Hellempfindlichkeitsgrad | des menschlichen | Auges |
| ------------------------ | ---------------- | ----- |
V(λ):helladaptiertesAuge(Zapfen-photopisch)
V(cid:48)(λ):dunkeladaptiertesAuge(Stäbchen-skotopisch)
19/34

Einführung RadiometrieundPhotometrie Lichtquellen Beleuchtung
Photometrische Größen
PhotometrischeGrößensindsodefiniert,daßsieden
HelligkeitseindruckdesmenschlichenAugeswiedergeben.
AnalogzudenradiometrischenGrößenwerdendie
photometrischenGrößendurchAufintegrierenderspektralen
Größengebildet,allerdingsgewichtetmitdemspektralen
HellempfindlichkeitsgradV(λ),z.B.
(cid:90) ∞
Φ =K Φ V(λ)dλ,
v m λ
0
mitdemProportionalitätsfaktor(”Photometrisches
StrahlungsäquivalentfürdasTagessehen”)
DasphotometrischeAnalogezurStrahlstärkeI,dieLichtstärke
I ,wirdinderSI-BasiseinheitCandela(cd)gemessen(damitist
v
K =683cd·sr·W−1).DasAnalogezurStrahlungsleistungΦist
m
derLichtstromΦ ,gemesseninLumenlm=cd·sr.
v
20/34

Einführung RadiometrieundPhotometrie Lichtquellen Beleuchtung
Zusammenfassung: radiometrische und
photometrische Größen
. .
Strahlungsleistung[W=Js−1]=Φ=Lichtstrom[lm]
. .
Strahlungsenergie[J=Ws]=Q=Lichtmenge[lms]
. .
Spez.Ausstrahlung[Wm−2]=M=Spez.Lichtausstrahlung[lmm−2]
.
Bestrahlungsstärke[Wm−2]=Beleuchtungsstärke[lmm−2 =lx]
. .
Strahlstärke[Wsr−1]=I=Lichtstärke[cd=lmsr−1]
. .
Bestrahlung[Jm−2]=H=Belichtung[lmsm−2 =lxs]
21/34

Einführung RadiometrieundPhotometrie Lichtquellen Beleuchtung
Übersicht
1 Einführung
2 Radiometrie und Photometrie
3 Lichtquellen
4 Beleuchtung
22/34

Einführung RadiometrieundPhotometrie Lichtquellen Beleuchtung
| Spektrale | spezifische | Ausstrahlung | des Sonnenlichts |
| --------- | ----------- | ------------ | ---------------- |
23/34

Einführung RadiometrieundPhotometrie Lichtquellen Beleuchtung
Künstliche Beleuchtungsquellen
Glühlampen
Glimm-undBogenentladungslampen
Leuchtstofflampen
Leuchtdioden(LEDs)
Laser
Infrarot-(IR)-undUltraviolett-(UV)-Quellen
24/34

Einführung RadiometrieundPhotometrie Lichtquellen Beleuchtung
| Spektrale | spezifische | Ausstrahlung | verschiedener |
| --------- | ----------- | ------------ | ------------- |
Lichtquellen
25/34

Einführung RadiometrieundPhotometrie Lichtquellen Beleuchtung
Glühlampen
BreitesEmissionspektrumim
sichtbarenundIR-Bereich
BeiHalogenlampenverhindert
eineFüllungmitHalogenendie
AblagerungvonDampfausder
Glühwendel
DadieHelligkeitvonder
Temperaturabhängt,glättetdie
Glühlampeschnelle
Schwankungeninder
Stromversorgung(kHz),
langsameSchwankungen
werdenwiedergegebenmitbis
zu10%derGesamtintensität.
26/34

Einführung RadiometrieundPhotometrie Lichtquellen Beleuchtung
Leuchtstofflampen
IneinemGaswerdenIonen
beschleunigtunderzeugenbeim
AufschlagaufdieElektrode
Elektronen,diewiederum
beschleunigtdasGasdurch
StoßzumLeuchtenanregen.
DasEmissionsspektrumwirdvon
Liniendominiert,oftim
UV-Bereich.
[Franz]
InLeuchtstoffröhrenistder SchnelleBeleuchtungs-
Glasmantelmiteinem schwankungenbei
fluoreszentenMaterial Standard-Stromquellen,
ausgekleidet,daßdasUV-Licht gleichmäßigeBeleuchtung
insichtbaresLichtumwandelt. erfordertspeziellehochfrequente
Stromquellen.
27/34

Einführung RadiometrieundPhotometrie Lichtquellen Beleuchtung
Leuchtdioden
KleineBaugröße,unabhängig
vonderemittiertenIntensität
Kanningroßflächige
Anordnungenbeliebiger
BandartigesEmissionspektrum
Formgebrachtwerden.
(außerbeiweißenLEDs)
SehrschnelleAntwortzeit,
HoheLichtausbeute,geringe
sehrhellbeigepulster
Leistungsaufnahme
Ansteuerung
28/34

Einführung RadiometrieundPhotometrie Lichtquellen Beleuchtung
Übersicht
1 Einführung
2 Radiometrie und Photometrie
3 Lichtquellen
4 Beleuchtung
29/34

Einführung RadiometrieundPhotometrie Lichtquellen Beleuchtung
Die radiometrische Kette
30/34

Einführung RadiometrieundPhotometrie Lichtquellen Beleuchtung
Reflektionstypen
| a.: Spiegelnde | Reflektion |               |           |
| -------------- | ---------- | ------------- | --------- |
| b.: Diffuse    | Reflektion | (Lambertscher | Strahler) |
c.: Subsurface-Reflektion
31/34

Einführung RadiometrieundPhotometrie Lichtquellen Beleuchtung
| Beleuchtungsmodell | nach Phong |     |     |
| ------------------ | ---------- | --- | --- |
Drei Komponenten:
| (a) Ambienter  | Anteil: homogener  | Anteil, erzeugt | durch z.B. |
| -------------- | ------------------ | --------------- | ---------- |
| Himmel oder    | andere ausgedehnte | Lichtquellen    |            |
| (b) Diffuser   | Anteil             |                 |            |
| (c) Spiegelnde | Reflektion         |                 |            |
32/34

Einführung RadiometrieundPhotometrie Lichtquellen Beleuchtung
Beleuchtungstypen
| Gerichtete  | DiffuseBeleuchtung | Rückwärtige |
| ----------- | ------------------ | ----------- |
| Beleuchtung |                    | Beleuchtung |
Hellfeldbeleuchtung
|     | Dunkelfeldbeleuchtung | Telezentrische |
| --- | --------------------- | -------------- |
Beleuchtung
33/34

Einführung RadiometrieundPhotometrie Lichtquellen Beleuchtung
Beleuchtungstypen (Beispiel)
GerichteteBeleuchtung RückwärtigeBeleuchtung
34/34