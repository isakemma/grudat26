# Övning 2 grudat26
### Deadline: Tisdag 31/3 kl 19:00

**Vid övningen ska du vara beredd att muntligt presentera och diskutera dina lösningar och din programkod. Du ska också ha med en utskrift av din inlämning för kamratgranskning på övningen.**

- Gör (minst) en fil per uppgift och lägg filerna i katalogen <code>username-ovn2</code> i organisationen [grudat26 på KTH GitHub](https://gits-15.sys.kth.se/grudat26).
- Utgå från mallarna i [/grudat26/ovn0/](https://github.com/isakemma/grudat/tree/master/ovn0).
- Lösningar ska vara inlämnade före deadline.

Du väljer själv vilket av programspråken Python, Go eller Java du vill använda.
**Observera att all kod på den här kursen ska dokumenteras och testas.**

Mål:
  - systematiskt testa program för att upptäcka fel
  - designa och dokumentera programpaket som andra programmerare kan använda
  - jämföra algoritmer med avseende på tids- och minnesåtgång
  - implementera och konstruera algoritmer för grundläggande datastrukturer

  
## Betyg G

### 2.1 Ordo-notation

Ordna funktionerna i följande lista i växande ordning med
avseende på tillväxtstakt. Funktionen <i>f(n)</i> ska alltså
komma före funktionen <i>g(n)</i> i listan om
<i>f(n)</i> är <i>O</i>(<i>g(n)</i>).

<ul>
<li><i>f<sub>1</sub>(n)</i>&nbsp;=&nbsp;<i>n</i><sup>1.5</sup>
</li>
<li><i>f<sub>2</sub>(n)</i>&nbsp;=&nbsp;10<sup><i>n</i></sup>
</li>
<li><i>f<sub>3</sub>(n)</i>&nbsp;=&nbsp;<i>n</i>&nbsp;log&nbsp;<i>n</i>
</li>
<li><i>f<sub>4</sub>(n)</i>&nbsp;=&nbsp;<i>n</i>&nbsp;+100
</li>
<li><i>f<sub>5</sub>(n)</i>&nbsp;=&nbsp;2<sup><i>n</i></sup>
</li>
</ul>

Vilka av följande påståenden är sanna? Motivera dina svar.

<ul>
<li><i>n</i>(<i>n</i>&nbsp;+&nbsp;1)&nbsp;/&nbsp;2 = <i>O</i>(<i>n</i><sup>3</sup>)</li>
<li><i>n</i>(<i>n</i>&nbsp;+&nbsp;1)&nbsp;/&nbsp;2 = <i>O</i>(<i>n</i><sup>2</sup>)</li>
<li><i>n</i>(<i>n</i>&nbsp;+&nbsp;1)&nbsp;/&nbsp;2 = &Theta;(<i>n</i><sup>3</sup>)</li>
<li><i>n</i>(<i>n</i>&nbsp;+&nbsp;1)&nbsp;/&nbsp;2 = &Omega;(<i>n</i>)</li>
<li>Om du har två funktioner, <i>f<sub>1</sub>(n)</i>&nbsp;=&nbsp;<i>n</i> och <i>f<sub>2</sub>(n)</i>&nbsp;=någon annan funktion av <i>n</i>, gäller då alltid antingen att <i>f<sub>1</sub>(n)</i>&nbsp;=&nbsp;<i>O</i>(<i>f<sub>2</sub>(n)</i>)</li> eller att <i>f<sub>2</sub>(n)</i>&nbsp;=&nbsp;<i>O</i>(<i>f<sub>1</sub>(n)</i>)?</li>
</ul>


[Video om ordo-notation](https://www.youtube.com/watch?v=rZvpB4Ip2_M)

### 2.2 Prefixsumma

Indata är en heltalsvektor <i>A</i> med <i>n</i>&nbsp;element.
Vi vill beräkna en vektor <i>B</i>, där <i>B</i>[i]&nbsp;=
<i>A</i>[0]&nbsp;+&nbsp;<i>A</i>[1]&nbsp;+&nbsp;...&nbsp;+&nbsp;<i>A</i>[i].
Här är en enkel algoritm som löser problemet.

<pre><code><b>for</b> i = 0 <b>to</b> n-1
    B[i] = 0
    <b>for</b> j = 0 <b>to</b> i
        B[i] += A[j]
</code></pre>

- Beräkna tidskomplexiteten för denna algoritm och uttryck den på
  formen&nbsp;<i>O</i>(<i>f(n)</i>), där funktionen&nbsp;<i>f(n)</i>
  är så liten och enkel som möjligt.

- Visa att tidskomplexiteten också är &Omega;(<i>f(n)</i>). (Tidskomplexiteten för just denna implementation, använd definitionen!)

- Hitta på en algoritm med bättre asymptotisk tidskomplexitet.
  Beskriv algoritmen i pseudokod och ange dess
  tidskomplexitet med Θ-notation.
  
[Video om tidskomplexitet](https://www.youtube.com/watch?v=x04gACtJHX0)
  
### 2.3 Binärt sökträd

Implementera ett *obalanserat* binärt sökträd som lagrar textsträngar.

- Gör ett tydligt API med publika dokumenterade metoder.
- Skriv utförlig testkod.
- Använd koden för den länkade listan i övning&nbsp;1 som mall för ditt träd.

Följande metoder ska finnas:

- Skapa ett tomt träd.
- Lägg till ett nytt element. (Kalla den insert(x))
- Undersök om ett element finns i trädet (Kalla den exist(x))
- Returnera antalet element i trädet.
- Returnerar en sträng med alla element i bokstavsordning, separerade med mellanslag.

*Ange tidskomplexiteten i värstafall för samtliga operationer.*


[Tips och råd](https://www.youtube.com/watch?v=NCzRttSCeH4) (Video)

## Högrebetygsuppgift (värd 10 högrebetygspoäng)

### 2.4 Treap

Modifiera uppgift 2.3 så att du får ett randomiserat binärt sökträd i stället för ett obalanserat träd. Uppdatera tidskomplexiteterna för operationerna där det behövs. Kom ihåg att testa och dokumentera! Alla tester av det obalanserade trädet ska fortfarande gå igenom. 
(Ledning: Det kan vara svårt att skriva bra tester på internt tillstånd i trädet. Två möjligheter är att lägga till en publik metod som returnerar trädets maxhöjd och testa den, eller att prestandatesta trädet. Vi vill undvika linjära samband mellan storlek och tid om trädet är balanserat!)

Det finns problem i Kattis som hanterar binära sökträd, t.ex. https://open.kattis.com/problems/bst. Det ingår inte i kursen men kan ge lite hjälp med att skriva ett balanserat sökträd. Dock har detta problem sina egna givna modifikationer i trädets funktionalitet/insert-metod!
