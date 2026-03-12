# Övning 5 grudat26
### Deadline: Fredag 18/4 kl 12:00

Mål:
 - modellera problem med grafer och implementera algoritmer för grafsökning
 - skriva och använda enkel BNF-syntax
 - implementera och konstruera algoritmer för grundläggande datastrukturer (VG)

**Vid övningen ska du vara beredd att muntligt presentera och diskutera dina lösningar och din programkod. Du ska också ha med en utskrift av din inlämning för kamratgranskning på övningen.**

- Gör (minst) en fil per uppgift och lägg filerna i katalogen <code>username-ovn5</code> i organisationen [grudat26 på KTH GitHub](https://gits-15.sys.kth.se/grudat26).
- Utgå från mallarna i [/grudat26/ovn0/](https://github.com/isakemma/grudat/tree/master/ovn0).
- Lösningar ska vara inlämnade före deadline.

[Grafer 101](https://www.youtube.com/watch?v=8BWts5Ule2I) (video)



## Individuellt projekt

Observera att en första version av API och övrig dokumentation till
det [individuella projektet](https://github.com/isakemma/grudat/blob/master/ovn7.md)
ska vara klar redan till denna övning.

[Tips om projektet](https://www.youtube.com/watch?v=dzo3TO_v0uk) (video)

## Betyg G

### 5.1 Rita grafer

- Rita alla enkla sammanhängande grafer med hörnen 1, 2, 3, 4, där samliga hörn har gradtal 1.
- Rita alla enkla sammanhängande grafer med hörnen 1, 2, 3, 4, där samliga hörn har gradtal 2.
- Rita alla enkla sammanhängande grafer med hörnen 1, 2, 3, 4, där samliga hörn har gradtal 3.

### 5.2 Räkna kanter

- Hur många kanter kan det som mest finnas i en graf med n stycken hörn?
- Hur många kanter kan det som mest finnas i en enkel graf med n stycken hörn?
- Hur många kanter kan det som mest finnas i ett träd med n stycken hörn?

Motivera dina svar.

### 5.3 DFS och BFS

![Connected graph with 6 nodes](http://yourbasic.org/algorithms/graph2.png)

- Besök noderna i den här grafen i DFS- och BFS-ordning med start i nod 1.
  I vilken ordning besöks noderna i de två fallen?
  Du kan anta att grannarna till en nod besöks i nummerordning.

- Tidskomplexiteten för DFS blir i vissa fall mycket bättre om man använder närhetslistor i stället för en närhetsmatris.
Varför då? 
- För vilken typ av grafer blir den asymptotiska tidskomplexiteten för DFS den samma för båda datastrukturerna?

### 5.4 Syntax, enkel
Vi har en BNF-syntax för fågelljud enligt följande:

	<LJUD> :== PIP | TI | TJI
	<FRAS> :== <LJUD> | TJI <LJUD> | <LJUD><FRAS> TJIRRP

Vilka av följande uttryck följer fågelljudssyntaxen? Visa **hur** de ljud som var ok följer syntaxen! 
1. PIPPIPPIP (PIP-PIP-PIP)
2. PIPTJIRRP (PIP-TJIRRP)
3. TJITITJIRRP (TJI-TI-TJIRRP)
4. TITJITITJIRRP (TI-TJI-TI-TJIRRP)
5. TJIRRP
6. TITIPIP (TI-TI-PIP)
7. TJITITI (TJI-TI-TI)
8. PIP
9. TITJITITJIRRPTJIRRP (TI-TJI-TI-TJIRRP-TJIRRP)


## Betyg VG

### 5.5 En provisorisk strategi?

En ny pandemi har nått landet finns i två helt olika varianter som det rekordsnabbt har utvecklats var sitt vaccin för. Båda skyddar fullständigt både från sjukdom och från att smitta andra, men bara mot den variant de är utvecklade för. Biverkningarna blir svåra om någon tar båda vaccinen, och smittskyddsläkaren i ett landsting skissar på en vaccinationsstrategi. Hen tror att om vaccin administreras så att inget par av vuxna personer (barn inkluderas alltså inte) som umgås med varandra kan smitta den andra med någon av varianterna så är vi hemma. Designa en algoritm som avgör om denna strategi är möjlig!

Modellera problemet med en graf där varje hörn motsvarar en en person.
Grafen har kanter mellan de hörn som motsvarar personer som umgås med varandra.
Algoritmen ska baseras på en metodisk genomgång av grafen med BFS eller DFS.

- Beskriv din algoritm i pseudokod.
- Beräkna också tidskomplexiteten.
