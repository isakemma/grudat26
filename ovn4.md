# Övning 4 grudat26 
### Deadline: Tisdag 21/4 kl 19:00

Mål:
 - jämföra algoritmer med avseende på tids- och minnesåtgång
 - beskriva och implementera olika algoritmer för sökning och sortering
   
**Vid övningen ska du vara beredd att muntligt presentera och diskutera dina lösningar och din programkod. Du ska också ha med en utskrift av din inlämning för kamratgranskning på övningen.**

- Gör (minst) en fil per uppgift och lägg filerna i katalogen <code>username-ovn4</code> i organisationen [grudat26 på KTH GitHub](https://gits-15.sys.kth.se/grudat26).
- Utgå från mallarna i [/grudat26/ovn0/](https://github.com/isakemma/grudat/tree/master/ovn0).
- Lösningar ska vara inlämnade före deadline.

Du väljer själv vilket av programspråken Python, Go eller Java du vill använda.
**Observera att all kod på den här kursen ska dokumenteras och testas.**

## Betyg G

### 1 Tidskomplexitet för rekursiva funktioner

#### Teori

Beräkna **tidskomplexiteten** för funktionerna 

Du behöver visa hur beräkningen ser ut, inte bara svaret!

[Tips och råd om att räkna ut tidskomplexitet för rekursiva funktioner](https://www.youtube.com/watch?v=sorlJiiWDRA) (video)

#### Praktik

Gör en **benchmark** där du mäter tiden för att exekvera de här funktionerna.
Uppgiften ska göras i **Python** och du ska mäta tiden, till exempel med funktionen <code>time.time</code>:

<pre><code>start = time.time()
funktion1(n)
print(n, time.time() - start) # elapsed time
</code></pre>

Testa för n = 10, 100, 1,000, 10,000, 100,000 och 1,000,000. Vid behov kan du också testa större tal, eller kanske fler datapunkter.
Presentera resultaten av tidmätningarna i en **tabell** eller i en **graf**.

#### Diskussion

Skriv en **diskussionsdel** där du försöker förstå och förklara eventuella skillnader mellan teori och praktik.


### 2 Linjärtidssortering av små tal

**Implementera**, **dokumentera** och **testa** en algoritm som sorterar heltalen x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>n</sub>.
För samtliga tal x<sub>i</sub> gäller att 0 &le; x<sub>i</sub> &le; k.

Analysera tidskomplexiteten. Din algoritm ska ha värstafallstidskomplexitet O(n+k).
För vilka värden på k blir algoritmen linjär?

<b>Tips:</b> räkna hur många element det finns av varje sort.

## Betyg VG

### 3 Sortering med kända restriktioner
