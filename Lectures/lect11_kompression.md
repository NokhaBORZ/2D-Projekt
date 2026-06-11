Kompression
2DComputerVision,VorlesungNo.11
Prof.Dr.M.O.Franz
HTWGKonstanz,FakultätfürInformatik
1/30

Übersicht
1 Lauflängencodierung
2 Entropiecodierung
3 KompressionvonBildernamBeispielJPEG
2/30

Übersicht
1 Lauflängencodierung
2 Entropiecodierung
3 KompressionvonBildernamBeispielJPEG
3/30

Kompression (Terminologie)
Code:Abbildungsvorschrift,diejedemZeicheneines
ZeichenvorratseindeutigeinZeichenodereineZeichenfolgeaus
einemmöglicherweiseanderenZeichenvorratzuordnet.
Datenkompression:CodierungvonDaten,sodasssichalle
(oderzumindestdiemeisten)InformationeninkürzererForm
darstellenlassen.
Redundanz:Datensindredundant,wennsieohne
Informationsverlustweggelassenwerdenkönnen.
VerlustfreieKompression:ausdenkomprimiertenDaten
könnenwiederexaktdieOriginaldatengewonnenwerden
(Redundanzreduktion).
VerlustbehafteteKompression:einTeilderInformationgeht
verloren;dieAlgorithmenversuchen,möglichstnur„unwichtige“
Informationenwegzulassen(Irrelevanzreduktion).
4/30

| Verlustfreie | Kompression | durch Lauflängencodierung |
| ------------ | ----------- | ------------------------- |
RedundanterBeispieltext:
AAAAAAAAAABBCDEEFFFFFFFFFFFFFGGGGGGGGGGGGGGGGG
Grundidee:jedeSequenzvonidentischenSymbolenwirddurchderen
Anzahlundggf.dasSymbolersetzt,d.h.eswerdennurdieStellen
markiert,andenensichdasSymbolinderNachrichtändert:
10A2B1C1D2E13F17G
17statt46Zeichen,allerdingssindmancheCodewörtergleichlang
| (BB | 2B)odersogarlänger(D | 1D),vgl. |
| --- | -------------------- | -------- |
| →   |                      | →        |
Maryhadalittlelamb.
→
1M1a1r1y1h1a1d1a1l1i2t1l1e1l1a1m1b1.
5/30

Schlecht für Text, aber gut für Binärbilder und Grafiken
[Wirtschaftswoche]
Lauflängencodierung(RLE)isteinfachunddahersehrschnell.
RLE-codierteBilderkönnendeutlichschnellervonPlattegelesenund
angezeigtwerdenalsunkomprimierteBilder.Eingesetztinden
BildformatenBMP,TARGA,PCXundfürFaxeundScans.
6/30

Sortierung nach Kanälen für RLE
[DVD-HQ]
DiehäufigeingesetztegepackteAnordnungderFarbkanäleeignet
sichnichtfürRLE.Daherwirdz.B.inTARGAbeimSpeichernindie
Komponentenanordnungumsortiert(nichtaberbeiBMP!).
7/30

Übersicht
1 Lauflängencodierung
2 Entropiecodierung
3 KompressionvonBildernamBeispielJPEG
8/30

Entropiecodierung
DieverlustfreieKompressionfunktioniertüberdieLängeder
einzelnenCodewörter:häufigeZeichenerhaltenkurzeCodes,seltene
ZeichenlangeCodes.
Informationsgehalt:istfüreinZeichena mitder
i
Wahrscheinlichkeitp(a) = p nachShannondefiniertals
i i
1
h(a) = log = log p
2 p − 2 i
i
Entropie:durchschnittlicherInformationsgehalteinesCodes
C = a ,a ,...
1 2
{ } 1
H(C) = p log
i 2 p
i
i
(cid:88)
Entropiecode:dieCodelängejedesSymbolsistumgekehrt
proportionalzumInformationsgehaltdescodiertenZeichens.
9/30

| Präfixfreie     | Codes |        |      |       |       |     |
| --------------- | ----- | ------ | ---- | ----- | ----- | --- |
| Beispielcode:A  |       | 11,B   | 00,C | 110,D | 011   |     |
|                 |       | →      | →    | →     | →     |     |
| Wiedecodiertman |       | 110011 | ? CD | oder  | ABA ? |     |
DasProblemisthier,dassderCode11einPräfixvon110ist.Füreine
eindeutigeDecodierungmusseinzusätzlichesTrennzeichenbzw.
Trennbitfolgeeingeführtwerden.
PräfixfreierCode:KeinCodewortistPräfixeinesanderen
Codewortesbzw.keinCodewortdarfdenBeginneinesanderen
Codewortesdarstellen.
| Beispiele:C |     |       | ,C             |     | ,C            | ,   |
| ----------- | --- | ----- | -------------- | --- | ------------- | --- |
|             | =   | 0,101 | = 0,10,110,111 |     | = 00,01,10,11 |     |
|             | 1 { | }     | 3 {            |     | } 4 {         | }   |
abernichtC
2 = 1,101
|     |     | { } |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
PräfixfreieCodeskönnenohnezusätzlicheTrennzeichendecodiert
werden.
10/30

Copyright Cambridge University Press 2003. On-screen viewing permitted. Printing not permitted. http://www.cambridge.org/0521642981
You can buy this book for 30 pounds or $50. See http://www.inference.phy.cam.ac.uk/mackay/itila/ for links.
5.1: Symbol codes 93
0
0
Example 5.4. The code C = 0,101 is a prefix code because 0 is not a prefix
1
{ }
0
of 101, nor is 101 a prefix of 0.
1
C 1 101
1
Example 5.5. Let C = 1,101 . This code is not a prefix code because 1 is a
2
{ }
prefix of 101.
Repräsentation eines präfixfreien Codes als Binärbaum
Example 5.6. The code C = 0,10,110,111 is a prefix code.
3
{ }
Copyright Cambridge University Press 2003. On-screen viewing permitted. Printing not permitted. http://www.cambridge.org/0521642981 0
0
Example 5.7. The code C = 00,01,10,11 is a prefix code.
You can buy this book for 30 pounds or $50. See http://www.inference.phy.cam4.ac.uk/mackay/itila/ for links.
{ }
0 10
C 3 1
Exercise 5.8. [1, p.104] Is C uniquely decodeable? 0 110
5.1: Symbol codes 2 931
1 111
Example 5.9. Consider exercise 4.1 (p.66) and figure 4.2 (p.69). Any weighing
strategy that identifies the odd ball and whether it is heavy or light can 0 00
0
0
Example 5.4. The code C 1 = 0,101beisviaewperdefiaxs caossdigenbinegcaautseern0airsyncootdea tporeefiacxh of the 24 possible states. 0 1 01
{ }
of 101, nor is 101 a prefix of 0T. his code is a prefix code. 0 C 0 10
1 4 1
C 1 101
1 1 11
Example 5.5. Let C = 1,101 T.hTehciosdceosdheoiusldnoatchaiepvreefiasx mcoudcehbceocmapurseess1ioisnaas possible
2
{ } Prefix codes can be[McrKeayp200r3]esented
prefix of 101. The expected length L(C,X) of a symbol code CC 1fo=r e0n,1s0e1m , bCl3e=X0,i1s0,110,111 ,C o4n=bin 00 a,r 0 y 1,t 1 r 0 e,e 1 s 1 . Complete prefix
{ } { } { }
codes correspond to binary trees
Example 5.6. The code C 3 = 0,10,110,111 is a prefix L co (C de , . X) = P(x)l(x). (5.5) with no unused branches. 1 C 1/3 1 0 is an
{ }
incomplete code.
x !∈A X 0 0
Example 5.7. The code C = 00,01,10,11 is a prefix code.
4
{ We may}also write this quantity as
0 10
C 3 1
Exercise 5.8. [1, p.104] Is C uniquely decodeable? 0 110
2 I 1
L(C,X) = p l (5.6)
i i 1 111
Example 5.9. Consider exercise 4.1 (p.66) and figure 4.2 (p.69). Any weii=g1hing
!
strategy that identifies the odd ball and whether it is heavy or light can 0 00
where I = .
X
be viewed as assigning a ternary code to|Aeac|h of the 24 possible states. 0 1 01 C 3 :
This code is a prefix codeE.xample 5.10. Let C 0 10
4 1 a c(a ) p h(p ) l
= a, b, c, d , i i i i i
A X { } 1 11 (5.7)
The code should achieve as much compression as p a o n s d sibleX = 1/ 2,1/ 4,1/ 8,1/ 8 , a 0 1/ 2 1.0 1
P { }
Prefix codes can be representbed 10 1/ 4 2.0 2
and consider the code C . The entropy of X is 1.75 bits, and the expected
3
The expected length L(C,X) of a symbol code C for ensemble X is on binary trees. Complete prcefix110 1/ 8 3.0 3
length L(C ,X) of this code is also 1.75 bits. The sequence of symbols
3
x=(acdbac) is encoded as c+(x) = 01101111001 c 1 o 0 d . e C s co is rr a es p p r o e n fi d x c to od b e inary trdees 111 1/ 8 3.0 3
3
L(C,X) an = d is the P re ( fo x r ) e l( u x n ) iq . uely decodeable. No ( t 5 i . c 5 e ) that w t i h t e h c n o o d u ew nu or s d ed le b n r g a t n h c s hes. C 1 is an
incomplete code.
satisxf
!∈
y
A
l
Xi
= log
2
(1/p
i
), or equivalently, p
i
=2
−
l i.
C C
4 5
We may also write this quantity as
Example 5.11. Consider the fixed length code for the same ensemble X, C . a 00 0
4
The expected length L(C 4 ,X) is 2 bits. b 01 1
I
c 10 00
L(C,X) = p l (5.6)
Example 5.12. Consiidier C . The expected length L(C ,X) is 1.25 bits, which
5 5 d 11 11
is less th! ia=n1 H(X). But the code is not uniquely decodeable. The se-
quence x=(acdbac) encodes as 000111000, which can also be decoded
where I = . C :
X 6
|A | as (cabdca).
C :
3
a c(a ) p h(p ) l
Example 5.10. Let i i i i i
Example 5.13. Consider the code C . The expected length L(C ,X) of this
6 a c(6a ) p h(p ) l
= a, b, c, d , i i i i ai 0 1/ 2 1.0 1
X code is 1.75 bits. The sequence of symbols x=(acdbac) is encoded as
A { } (5.7)
and X c+= (x) = 1/ 020 , 1 1/ 141 , 1 1 1 / 80 , 1 1 0 / 8011 , . a 0 1/ 2 1.0 b1 01 1/ 4 2.0 2
P { } b 10 1/ 4 2.0 c 2 011 1/ 8 3.0 3
and consider the code C 3 . The eIsntCr 6 opayporfefiXx icso1d.e7?5Ibtitiss,naont,dbtehceauesxepce(cat)ed= 0 is a p c refix 11 o 0 f bot 1 h / 8 c(b) 3.0 d 3 111 1/ 8 3.0 3
length L(C ,X) of this code isanadlsoc(c1)..75 bits. The sequence of symbols
3
d 111 1/ 8 3.0 3
x=(acdbac) is encoded as c+(x) = 0110111100110. C is a prefix code
3
and is therefore uniquely decodeable. Notice that the codeword lengths
satisfy l = log (1/p ), or equivalently, p =2 l i.
i 2 i i −
C C
4 5
Example 5.11. Consider the fixed length code for the same ensemble X, C . a 00 0
4
The expected length L(C ,X) is 2 bits. b 01 1
4
c 10 00
Example 5.12. Consider C . The expected length L(C ,X) is 1.25 bits, which
5 5 d 11 11
is less than H(X). But the code is not uniquely decodeable. The se-
quence x=(acdbac) encodes as 000111000, which can also be decoded
C :
6
as (cabdca).
a c(a ) p h(p ) l
i i i i i
Example 5.13. Consider the code C . The expected length L(C ,X) of this
6 6
a 0 1/ 2 1.0 1
code is 1.75 bits. The sequence of symbols x=(acdbac) is encoded as
b 01 1/ 4 2.0 2
c+(x) = 0011111010011.
c 011 1/ 8 3.0 3
Is C 6 a prefix code? It is not, because c(a) = 0 is a prefix of both c(b) d 111 1/ 8 3.0 3
and c(c).

Copyright Cambridge University Press 2003. On-screen viewing permitted. Printing not permitted. http://www.cambridge.org/0521642981
You can buy this book for 30 pounds or $50. See http://www.inference.phy.cam.ac.uk/mackay/itila/ for links.
| 5.5: Optimalsourcecodingwithsymbolcodes: |     |     |     | Huffmancoding |     |     |     | 99  |
| ---------------------------------------- | --- | --- | --- | ------------- | --- | --- | --- | --- |
TheHuffmancodingalgorithm Huffman-Codes
Wenowpresentabeautifullysimplealgorithmforfindinganoptimalprefix
code. Thetrickistoconstructthecodebackwards startingfromthetailsof
thecodewords;webuHildutffhembainna-rAytlrgeoerfriotmhmitsulseaves.
Algorithm5.4.Huffmancoding
1. Take thetwo lea1stMproobmabelenstyamnbeoslsBinitth=elaelptzhtaebest.BiTthdeseestwCoodesalgorithm.
symbolswillbegiventhelongestcodewords,whichwillhaveequal
length,anddiffe ronWlyäinhtlheedlaisetzdwigiet.iZeichenmitdergeringstenWahrscheinlichkeit
2
2. Combinethesetwosuynmdbowlseinitsoeaihsinngelensy0mubnold,a1ndimrepmeato.mentanenBitzu.
FassebeideZeichenzusammen,summiereihre
3
Sinceeachstepreducesthesizeofthealphabetbyone,thisalgorithmwill
Wahrscheinlichkeiten,setzedasmomentaneBiteineStelle
| haveassignedstringstoall |     | the                           | s y m b ol s a fte | r X|u−n 1       | st ep s .           |             |         |       |
| ------------------------ | --- | ----------------------------- | ------------------ | --------------- | ------------------- | ----------- | ------- | ----- |
|                          |     | w ei                          | t e r n a c h      | v o|Arn         | d g e h ezurückzu2. |             |         |       |
| Example5.15.             | Let | AX= a,                        | b, c,              | d, e            |                     |             |         |       |
|                          | and | PX= { 0.25,0.25,0.2,0.15,0.15 |                    | } .             |                     |             |         |       |
|                          |     | {                             |                    | }               |                     |             |         |       |
|                          | x   | step1                         | step2              | step3 step4     |                     |             |         |       |
|                          |     |                               |                    |                 |                     | ai pi h(pi) | li      | c(ai) |
|                          |     |                               |                    | 0               | 0                   |             |         |       |
|                          | a   | 0 . 2 5                       | 0 . 2 5 0          | . 2 5 " 0 . 5 5 | ! 1.0               |             |         |       |
|                          |     |                               | 0                  |                 | !                   | a 0 . 2 5   | 2 . 0 2 | 0 0   |
|                          | b   | 0 . 2 5                       | 0 . 2 5 0          | . 4 5 " 0 . 4 5 | 1                   |             |         |       |
|                          |     |                               | ! !                | "               |                     | b 0 . 2 5   | 2 . 0 2 | 1 0   |
|                          | c   | 0.2                           | 0.2 1              | "               |                     | c 0.2       | 2.3 2   | 11    |
|                          |     | 0                             |                    | "1              |                     |             |         |       |
|                          | d   | 0.15                          | 0.3 0.3            |                 |                     | d 0.15      | 2.7 3   | 010   |
!
|     | e   | 0.15 ! 1 |     |     |     | e 0.15 | 2.7 3 | 011 |
| --- | --- | -------- | --- | --- | --- | ------ | ----- | --- |
Thecodewordsarethenobtainedbyconcatenatingthebinarydigitsin Table5.5.Codecreatedbythe
[McKay2003]
reverse order: C = 00,10,11,010,011 . The codelengths selected Huffmanalgorithm.
|     |     | {   |     | }   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
by the Huffman algorithm (column 4 of table 5.5) are in some cases
longerandinsomecasesshorterthantheidealcodelengths,theShannon
information contents log 1/pi (column 3). Theexpected length of the 12/30
2
| codeisL=2.30bits,whereastheentropyisH=2.2855bits. |     |     |     |     | !   |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Ifatanypointthereismorethanonewayofselectingthetwoleastprobable
symbolsthenthechoicemaybemadeinanymanner–theexpectedlengthof
thecodewillnotdependonthechoice.
Exercise5.16.[3,p.105] Provethatthereisnobettersymbolcodeforasource
thantheHuffmancode.
Example5.17. WecanmakeaHuffmancodefortheprobabilitydistribution
| overthealphabetintroducedinfigure2.1. |                                                    |     |     | Theresultisshowninfig- |     |     |     |     |
| ------------------------------------- | -------------------------------------------------- | --- | --- | ---------------------- | --- | --- | --- | --- |
| ure5.6.                               | Thiscodehasanexpectedlengthof4.15bits;theentropyof |     |     |                        |     |     |     |     |
theensembleis4.11bits. Observethedisparitiesbetweentheassigned
| codelengthsandtheidealcodelengthslog |     |     |     | 1/pi . |     |     |     |     |
| ------------------------------------ | --- | --- | --- | ------ | --- | --- | --- | --- |
2
Constructingabinarytreetop-downissuboptimal
Inpreviouschapterswestudiedweighingproblemsinwhichwebuiltternary
orbinarytrees. Wenoticedthatbalancedtrees–onesinwhich,ateverystep,
thetwopossibleoutcomeswereascloseaspossibletoequiprobable–appeared
todescribethemostefficientexperiments. Thisgaveanintuitivemotivation
forentropyasameasureofinformationcontent.

CopHyrighut Caffmbmridge aUninvers-ityC Preoss d200e3. Onf-sücreren veiewningg pelrmiitstedc. Phrinteing nMot peromitnted.o httpg://wrwaw.cmambrmidge.eorg/0521642981
You can buy this book for 30 pounds or $50. See http://www.inference.phy.cam.ac.uk/mackay/itila/ for links.
| 100 |     |     |     |     |     | 5—SymbolCodes |
| --- | --- | --- | --- | --- | --- | ------------- |
ai pi log2p 1 li c(ai) Fi g u r e 5. 6 . H u ff Zm a un rc o Bd e e forrethcehnung
|          | i          |     |     | a   | E n g l i sh | l a ng u a g e e ns e m b l e |
| -------- | ---------- | --- | --- | --- | ------------ | ----------------------------- |
| a 0.0575 | 4.1 4 0000 |     |     | n   |              |                               |
(monogramstatmistiücs)s.sendie
| b 0.0128 | 6.3 6 001000 |     |     | b   |     |                 |
| -------- | ------------ | --- | --- | --- | --- | --------------- |
| c 0.0263 | 5.2 5 00101  |     |     | g   |     | Wahrscheinlich- |
| d 0.0285 | 5.1 5 10000  |     |     | c   |     |                 |
s
| e 0.0913      | 3.5 4 1100         |     |     |     |     | keitenaller    |
| ------------- | ------------------ | --- | --- | --- | --- | -------------- |
| f 0.0173      | 5.9 6 111000       |     | −   |     |     |                |
| g 0.0133      | 6.2 6 001001       |     |     | d   |     | Zeichenbekannt |
| h 0.0313      | 5.0 5 10001        |     |     | h   |     |                |
|               |                    |     |     | i   |     | sein.          |
| i 0.0599      | 4.1 4 1001         |     |     |     |     |                |
| j 0.0006      | 10.7 10 1101000000 |     |     | k   |     |                |
| k 0 . 0 0 8 4 | 6 . 9 7 1 0 1 0    | 000 |     | x   |     |                |
|               |                    |     |     | y   |     | Huffman-Codes  |
| l 0 . 0 3 3 5 | 4 . 9 5 1 1 1 0    | 1   |     | u   |     |                |
| m 0 . 0 2 3 5 | 5 . 4 6 1 1 0 101  |     |     |     |     | sindoptimal.   |
| n 0 . 0 5 9 6 | 4 . 1 4 0 0 0 1    |     |     | o   |     |                |
e
| o 0.0689      | 3.9 4 1011        |        |     |     | j   |              |
| ------------- | ----------------- | ------ | --- | --- | --- | ------------ |
| p 0.0192      | 5.7 6 111001      |        |     |     | z   | JedesZeichen |
| q 0 . 0 0 0 8 | 1 0 . 3 9 1 1 0 1 | 0 0001 |     |     |     |              |
| r 0 . 0 5 0 8 | 4 . 3 5 1 1 0 1   | 1      |     | q   |     | mussdurch    |
v
| s 0 . 0 5 6 7 | 4 . 1 4 0 0 1 1 |     |     | w   |     |               |
| ------------- | --------------- | --- | --- | --- | --- | ------------- |
| t 0 . 0 7 0 6 | 3 . 8 4 1 1 1 1 |     |     |     |     | ganzzahlige   |
| u 0.0334      | 4.9 5 10101     |     |     | m   |     |               |
|               |                 |     |     | r   |     | AnzahlBits    |
| v 0.0069      | 7.2 8 11010001  |     |     | f   |     |               |
| w 0.0119      | 6.4 7 1101001   |     |     | p   |     | repräsentiert |
| x 0.0073      | 7.1 7 1010001   |     |     |     |     |               |
l
| y 0.0164 | 5.9 6 101001       |     |     | t   |     | werden. |
| -------- | ------------------ | --- | --- | --- | --- | ------- |
| z 0.0007 | 10.4 10 1101000001 |     |     |     |     |         |
| – 0.1928 | 2.4 2 01           |     |     |     |     |         |
[McKay2003]
Itisnotthecase,however,thatoptimalcodescanalwaysbeconstructed
byagreedytop-downmethodinwhichthealphabetissuccessivelydivided
intosubsetsthatareasnearaspossibletoequiprobable. ai pi Greedy Huffman
13/30
Example5.18. Findtheoptimalbinarysymbolcodefortheensemble: a .01 000 000000
|     |                                          |             |      |        | b   | .24 001 01     |
| --- | ---------------------------------------- | ----------- | ---- | ------ | --- | -------------- |
|     |                                          |             |      |        | c   | .05 010 0001   |
|     | AX= a,                                   | b, c, d, e, | f, g |        | d   | .20 011 001    |
|     | PX= { 0.01,0.24,0.05,0.20,0.47,0.01,0.02 |             | }.   | (5.24) |     |                |
|     | {                                        |             | }    |        | e   | .47 10 1       |
|     |                                          |             |      |        | f   | .01 110 000001 |
Noticethatagreedytop-downmethodcansplitthissetintotwosub- g .02 111 00001
| sets | a,b,c,d and e,f,g | whichbothhaveprobability1/2,andthat |     |     |     |     |
| ---- | ----------------- | ----------------------------------- | --- | --- | --- | --- |
| {    | } {               | }                                   |     |     |     |     |
a,b,c,d canbedividedintosubsets a,b and c,d ,whichhaveprob- Table5.7.Agreedily-constructed
| { ability1/4;soagreedytop-downmethodgivesthecodeshowninthe | }   | { } | { } |     |     |     |
| ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
codecomparedwiththeHuffman
thirdcolumnoftable5.7,whichhasexpectedlength2.53.TheHuffman code.
codingalgorithmyieldsthecodeshowninthefourthcolumn,whichhas
| expectedlength1.97. |     |     |     | !   |     |     |
| ------------------- | --- | --- | --- | --- | --- | --- |
5.6 DisadvantagesoftheHuffmancode
TheHuffmanalgorithmproducesanoptimalsymbolcodeforanensemble,
butthisisnottheendofthestory.Boththeword‘ensemble’andthephrase
‘symbolcode’needcarefulattention.
Changingensemble
Ifwewishtocommunicateasequenceofoutcomesfromoneunchangingen-
semble,thenaHuffmancodemaybeconvenient. Butoftentheappropriate

Arithmetisches Codieren (1)
ÄhnlichwiebeiHuffman-Codesbrauchtmanbeimarithmetischen
CodiereneinprobabilistischesModell,d.h.dieWahrscheinlichkeitenp für
i
jedesZeichena.StattdieEingabeZeichenfürZeichenzucodieren,wird
i
hierdiegesamteSequenzalseinereelleFließkommazahlzwischen0und1
dargestellt.
Beispiel: AAABBBAC mitp =0.5,p =0.375,p =0.125.
A A C
1 FürjedeStelleteiltderCodiererdasmomentaneIntervall
entsprechenddenWahrscheinlichkeitenauf,alsozuerstdas
Anfangsintervall[0,1[indieIntervalle[0,0.5[,[0.5,0.875[,[0.875,1[.
2 DasersteZeichenistA,alsowirdalsnächstesIntervalldaszuA
gehörigeIntervall[0,0.5[nachdemgleichenSchemaunterteilt,alsoin
[0,0.25[,[0.25,0.4325[,[0.4325,0.5[.
3 WeitereIntervalleebenso:3.Symbol:[0,0.125[,4.Symbol:
[0.0625,0.109375[,usw.biszum8.Symbol:derCodemusshierin
[0.0956878662109375,0.0958251953125[liegen,d.h.wirübertragenz.B.
0.0957.
14/30

Arithmetisches Codieren (2)
[DVD-HQ]
DerDecodierergehtumgekehrtvor(AnzahlZeichenN =8undp müssen
i
vorherübertragenwordensein):
1 DerCode0.0957liegtin[0,0.5[,alsoistdas1.ZeichenA.
2 DerCode0.0957liegtin[0,0.25[,alsoistdas2.ZeichenA.
3 DerCode0.0957liegtin[0,0.125[,alsoistdas3.ZeichenA.
4 DerCode0.0957liegtin[0.0625,0.109375[,alsoistdas4.ZeichenB.
5 usw.bisN =8erreichtist.
15/30

| Arithmetisches |     | Codieren | (3) |     |
| -------------- | --- | -------- | --- | --- |
Gesucht:Intervall[u,v[derLängepfürdieEingabesequenzx x ...x .
1 2 N
| QundR:linkebzw,rechteIntervallgrenzevonx |     |     |     | innerhalb[0,1[ |
| ---------------------------------------- | --- | --- | --- | -------------- |
n
AlgorithmusfürArithmetischesCodieren
| u   | := 0   |            |             |             |
| --- | ------ | ---------- | ----------- | ----------- |
| v   | := 1.0 |            |             |             |
| p   | := v   | − u        |             |             |
| for | n=1    | to N:      |             |             |
|     | i =    | Index      | des Symbols | in x_n      |
|     | Q =    | Summiere   | p_j von     | j=1 bis i−1 |
|     | R =    | Summiere   | p_j von     | j=1 bis i   |
|     | v      | := u + p∗R |             |             |
|     | u      | := u + p∗Q |             |             |
|     | p      | := v − u   |             |             |
16/30

Entropiecodierung bei Bildern
ArithmetischesCodierenistebenfallsnahezuoptimal(maximal
2BitmehralsderInformationsgehaltdesInputs).
ImGegensatzzuHuffman-Codeswirdnichtzeichenweise
codiert,sonderndiegesamteSequenz.Dadurchmussnicht
jedesZeichenmiteinerganzzahligenBitfolgecodiertwerden,
waseinhöhereKompressionsrateerlaubt(v.a.wennviele
ZeicheneineniedrigenInformationsgehalthaben).
ArithmetischesCodierenistallerdingsdeutlichrechenintensiver
alsdieHuffman-Codierung.
WährendRLEaufFotografienmeistwenigerals5%Ersparnis
bringt,kommtEntropiecodierunginKombinationmitanderen
Verfahrenverlustfreiaufbiszu50%.
Huffman-Codierungwirdu.a.beidenBildformatenPNGund
JPEGeingesetzt,arithmetischesCodierenoptionalinJPEG.
17/30

Übersicht
1 Lauflängencodierung
2 Entropiecodierung
3 KompressionvonBildernamBeispielJPEG
18/30

JPEG (Überblick)
[Umlauf]
VerlustbehaftetesKompressionsverfahren,entwickelt1991-1993
durchdieJointPhotographicExpertsGroup(ISO-10918).
19/30

| Schritt | 1: Wechsel | des Farbraums | nach |     |
| ------- | ---------- | ------------- | ---- | --- |
YC C
b r
|     |     | UmrechnungindasYP | P -SchemanachCCIR601: |     |
| --- | --- | ----------------- | --------------------- | --- |
b r
|     |     | Y = | 0.299R+0.587G+0.114B |                |
| --- | --- | --- | -------------------- | -------------- |
|     |     | P = | 0.168736R            | 0.331264G+0.5B |
|     |     | b   | −                    | −              |
|     |     | P = | 0.5R 0.418688G       | 0.081312B      |
|     |     | r   | −                    | −              |
DadieRGB-WertebereitsimBereich[0,255]vorliegen,
|     |     | müssendieP -undP | -Komponentenlediglichverschoben |     |
| --- | --- | ---------------- | ------------------------------- | --- |
|     |     | b                | r                               |     |
werden:
|     |     | Y = 0.299R+0.587G+0.114B |           |                |
| --- | --- | ------------------------ | --------- | -------------- |
|     |     | C = 128                  | 0.168736R | 0.331264G+0.5B |
b
|     |     |              | −         | −         |
| --- | --- | ------------ | --------- | --------- |
|     |     | C = 128+0.5R | 0.418688G | 0.081312B |
r
|     |     |     | −   | −   |
| --- | --- | --- | --- | --- |
DieKomponentenliegennunwiederumimWertebereich
[0,255].BeiderUmrechnungdesFarbraumsentstehendie
[Wikipedia]
üblichenRundungsfehler.
20/30

Schritt 2: Unterabtastung der Chromakanäle
DasmenschlicheAugenimmtdieChromakanälemiteinerdeutlich
geringerenAuflösungwahralsdenLuminanzkanal.Daherwerdenin
JPEGdieChromakanälenachdemSchema4:2:0unterabgetastet
(A:B:Cbedeutet:beieinem2 A-ArraywerdenBWerteinderersten
×
ZeileundCWerteinderzweitenReiheübernommen):
[Umlauf]
JederChromakanalwirdnurmiteinemViertelderAuflösung
abgetastet,daherhalbiertsichdasgesamteDatenvolumen(allerdings
verlustbehaftet).DieabgetastetenWerteerhältmandurchMittelung
überdieNachbarn(BoxfilteralsTiefpass).
21/30

| Schritt | 3: Transformationscodierung |                    | mit  | der DCT          |
| ------- | --------------------------- | ------------------ | ---- | ---------------- |
|         |                             | JedeKomponente(Y,C | undC | )desBildeswirdin |
b r
8 8-Blöckeeingeteilt.DasBildmussdazuggf.
ve×rgrößertwerden.
|     |     | JederBlockI | wirdzentriert,d.h.I | =I 128. |
| --- | --- | ----------- | ------------------- | ------- |
−
AnwendungderDCTaufjedenBlockergibteinen
8 8-BlockvonDCT-Koeffizienten
×
7 7
1
|     |     | G(m,n) | = I(u,v)c | c     |
| --- | --- | ------ | --------- | ----- |
|     |     |        | 4         | m n · |
u=0 v=0
(cid:88)(cid:88)
|     |     |     | cos πm(2u+1) | cos πm(2v+1) |
| --- | --- | --- | ------------ | ------------ |
|     |     |     | 16           | 16           |
DieDCTkonzentriertdiegesamteSignalenergiein (cid:0) (cid:1) (cid:0) (cid:1)
wenigenKoeffizienten(z.B.wirdeineinfarbigerBlock
nurdurcheineneinzigenKoeffizientendargestellt.)
[Umlauf]
AuchhiergibtesRundungsfehler.
22/30

Beispiel DCT
[Umlauf]
23/30

Schritt 4: Quantisierung
DieDCT-Koeffizientenwerdendurchdie
Quantisierungsmatrixgeteilt(elementweisedividiert)und
danachaufdienächstliegendeGanzzahlgerundet:
G(m,n)
GQ(m,n) = round
Q(m,n)
(cid:18) (cid:19)
JekleinerderEintragindieQuantisierungsmatrix,desto
genauerwirdderDCT-Koeffizientrepräsentiert.
DurchdieRundungfindeteineIrrelevanzreduktionstatt.Die
QuantisierungsmatrixistsowohlfürdieQualitätalsauchfürdie
Kompressionsrateverantwortlich.
DieQuantisierungsmatrixorientiertsichanderEmpfindlichkeit
desAugesfürdieentsprechendenOrtsfrequenzen.Fürgrobe
StrukturenistdasAugeempfindlicher,dahersinddie
QuantisierungswertefürdieseFrequenzenkleineralsdiefür
hoheFrequenzen.
24/30

Beispiel: Quantisierungsmatritzen
[Umlauf]
25/30

Beispiel: Quantisierung
[Umlauf]
26/30

Schritt 5: Verlustfreie Kompression
Die64quantisiertenKoeffizienten
werdenanhandderFrequenz
sortiert.
DieDifferenzender
DC-Komponentenentlangdes
Zickzackmusterswerden
Huffman-codiert.
DieAC-Komponentenwerden
wahlweiseHuffman-oder
arithmetischcodiert.
[Umlauf]
27/30

| Beispiel: | Speicherplatz | für verschiedene | Kompressionraten |
| --------- | ------------- | ---------------- | ---------------- |
28/30

| Beispiel: | von links | nach rechts | abnehmende | Qualitätsstufen |
| --------- | --------- | ----------- | ---------- | --------------- |
[Wikipedia]
29/30

JPEG: Vor- und Nachteile
Vorteile:
HoheKompressionsraten
WirdvonfastallenSystemenunBildverarbeitungsprogrammen
unterstützt.
Nachteile:
SchlechteKompressionbeischarfenBildkanten(eher
ungeeignetfürZeichnungen)
VerlustbehafteteKompression
Block-Artefakte
Nichtidempotent:dasÖffnenundanschließendeSpeichern
einerJPEG-Dateiführtzueinerneuenverlustbehafteten
Kompression.
30/30