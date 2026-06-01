
# Komplettering för missad övning 3-6
Lämnas in och redovisas under omtentaperioden. Redovisningstider kommer att finnas för någon dag, troligen 8-10 juni. 

## Övning 3
### 3.1 Induktionsbevis för kod och implementation av rekursiv funktion.
Implementera en rekursiv sorteringsmetod (en som inte finns i kod eller pseudokod i kursens material) och visa med induktion att den gör rätt. Kom ihåg tester!

### Tips:
Var tydlig med när du använder ett basfall eller ett induktionsantagande! Var tydlig med vilken egenskap du bevisar!

## Övning 4
### 4.1 Teori
Beräkna **tidskomplexiteten** för följande två okommenterade rekursiva funktioner:

<pre><code>def funk1(n):
	if n == 0:
		return 1
	x = funk1(n//3)
	if n%2 == 0:
		return x*x
	elif n%3 == 0:
		return x+3
	return 3*x
</code></pre>

<pre><code>def funk2(lista):
	n = len(lista)
	if n == 0:
		return 0
	if n == 1:
		return lista[-1]
	return funk2(lista[:n//2]) + funk2(lista[n//2:])
</code></pre>

Du behöver visa hur beräkningen ser ut, inte bara svaret!

[Tips och råd om att räkna ut tidskomplexitet för rekursiva funktioner](https://www.youtube.com/watch?v=sorlJiiWDRA) (video)

### 4.2 Praktik

Implementera en sorteringsalgoritm med kvadratisk värstafallskomplexitet och en med optimal värstafallskomplexitet. För att implementera två sorteringsalgoritmer är det ok att använda källor på internet (men du måste hänvisa till dem!).  Gör ett **benchmark** där du mäter tiden för att exekvera de båda algoritmerna.
Du ska mäta tiden "maskinellt", till exempel i **Python** med funktionen <code>time.time</code>:

<pre><code>start = time.time()
sorteringsalg(n)
print(n, time.time() - start) # elapsed time
</code></pre>

Testa för olika data av storlek n = 10, 100, 1,000, 10,000, 100,000 och 1,000,000. Försök att hitta ett par olika probleminstanser av varje storlek som avslöjar algoritmernas svaga och starka sidor!
Presentera resultaten av tidmätningarna i en **tabell** eller i en **graf**.

### 4.3 Diskussion

Skriv en **diskussionsdel** där du försöker förstå och förklara eventuella skillnader mellan teori (kvadratisk eller n log n) tidskomplexitet och dina faktiska mätresultat.

## Övning 5
### 5.1 Graftraversering
<!-- Constructed by csacademy graph editor -->
[graph.png](https://github.com/isakemma/grudat/blob/master/graph.png)


- Besök noderna i den inlänkade grafen i DFS- och BFS-ordning med start i nod 1 respektive nod 2.
  I vilken ordning besöks noderna i de fyra fallen?
  Du kan anta att grannarna till en nod besöks i nummerordning.

- Tidskomplexiteten för DFS blir i vissa fall mycket bättre om man använder närhetslistor i stället för en närhetsmatris.
Varför då? 
- För vilken typ av grafer blir den asymptotiska tidskomplexiteten för DFS den samma för båda datastrukturerna?

### 5.2 Syntax, enkel
Vi har bytt ut våra fåglar mot får och har en BNF-syntax för bräkanden enligt följande:

	<LJUD> :== B<ÄN> | M<ÄN> | BU<ÄN>
  	<ÄN> :== Ä | Ä<ÄN>
	<FRAS> :== <LJUD> | <LJUD> HÄ| <LJUD><FRAS> ÄÄH

Vilka av följande uttryck följer bräksyntaxen? Visa **hur** de ljud som var ok följer syntaxen! 

1. BÄÄÄH
2. BÄH
3. BÄBÄÄÄH
4. MÄÄÄÄÄÄÄÄÄ
5. BÄMÄMÄBUHÄ
6. BÄÄÄÄHÄ

## Övning 6
### 6.1 Reguljära uttryck
Skriv en flervalsfråga om reguljära uttryck med icketriviala svarsalternativ (ska kräva viss eftertanke för att se vilket/vilka som är rätt) och berätta vilken aspekt av reguljära uttryck som frågan belyser.

### 6.2 Jordgubbsförsäljning

Inför midsommarafton vill du hjälpa din lokala jordgubbsförsäljare att maximera sin inkomst, givet en ekonomisk prognos. Enligt prognosen är literpriset på jordgubbar l(d) kronor för varje antal dagar d som är kvar till midsommar. Försäljaren har n liter jordgubbar. Varje dag kommer hen att kunna sälja hur mycket jordgubbar som helst, men av det som blir över kommer 10 % att mögla eller bli dåliga. Vilken är den maximala inkomsten som försäljaren kan få av sina n liter jordgubbar?

Följande rekursion beräknar den maximala inkomsten p(n, d) som man kan ha fått i slutet av dagen när det är d dagar kvar till midsommar:

> p(n,0) = n*l(0),
> p(0,d) = 0, 
> p(n, d) = max<sub>1 &le; a &le; n</sub>(al[d] + p(0.9*(n-i), d-1)) om n, d > 0.

Jordgubbarna säljs bara i hela liter, så vi avrundar neråt när vi räknar bort de skämda bären.

- Förklara varför rekursionen fungerar.
- Implementera en rekursiv funktion som beräknar p(n,d). Glöm inte dokumentation och testkod.
- Beräkna p(10,4) när l[0] = 50, l[1] = 42, l[2] = 35, l[3] = 29, l[4] = 27 och l[i] = 25 när i > 4.
  Simulera beräkningen för hand och rita ett träd över dina funktionsanrop (du behöver inte rita upp hela trädet, men se till att det som gör trädet obekvämt stort kommer fram! Det går bra med ett foto på ett handritat träd.)
- Förklara varför tidskomplexiteten för denna funktion är exponentiell.
- Förbättra tidskomplexiteten genom att skriva en version av programmet som cachar delresultat.
- Räkna ut en tabell över p(n,d) för n = 0, 1, 2, 3, 4, 5 (med samma dagar och priser som ovan). Gör beräkningen för hand.
- Visa vad tidskomplexiteten är för den uppdaterade koden.

[Tips om dynamisk programmering](https://www.youtube.com/watch?v=obslDoqkm7E) (video)
