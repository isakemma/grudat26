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
  - använda abstraktion som ett verktyg för att förenkla programmeringen

  
## Betyg E

### 2.1 Ordo-notation
Ordna funktionerna i följande lista i växande ordning med
avseende på tillväxtstakt. Funktionen <i>f(n)</i> ska alltså
komma före funktionen <i>g(n)</i> i listan om
<i>f(n)</i> är <i>O</i>(<i>g(n)</i>).

<ul>
<li><i>f<sub>1</sub>(n)</i>&nbsp;=&nbsp;<i>n</i><sup>1.7</sup>/2
</li>
<li><i>f<sub>2</sub>(n)</i>&nbsp;=&nbsp;<i>n</i>&nbsp;log&nbsp;log&nbsp;<i>n</i> (dvs <i>n</i> gånger logaritmen för logaritmen av <i>n</i>)
</li>
<li><i>f<sub>3</sub>(n)</i>&nbsp;=&nbsp;10<sup><i>n</i></sup>
</li>
<li><i>f<sub>4</sub>(n)</i>&nbsp;=&nbsp;<i>n</i>&nbsp;log&nbsp;<i>n</i>
</li>
<li><i>f<sub>5</sub>(n)</i>&nbsp;=&nbsp;<i>n</i>&nbsp;+100
</li>
<li><i>f<sub>6</sub>(n)</i>&nbsp;=&nbsp;2<sup><i>n</i></sup>
</li>
</ul>

Vilka av följande påståenden är sanna? Motivera dina svar.

<ul>
<li><i>n</i>(<i>n</i>&nbsp;+&nbsp;1)&nbsp;/&nbsp;2 = <i>O</i>(<i>n</i><sup>3</sup>)</li>
<li><i>n</i>(<i>n</i>&nbsp;+&nbsp;1)&nbsp;/&nbsp;2 = <i>O</i>(<i>n</i><sup>2</sup>)</li>
<li><i>n</i>(<i>n</i>&nbsp;+&nbsp;1)&nbsp;/&nbsp;2 = &Theta;(<i>n</i>)</li>
<li><i>n</i>(<i>n</i>&nbsp;+&nbsp;1)&nbsp;/&nbsp;2 = &Omega;(<i>n</i>)</li>
<li>Om <i>f<sub>1</sub>(n)</i>&nbsp;=&nbsp;<i>n</i> och <i>f<sub>2</sub>(n)</i>&nbsp;=någon annan funktion av <i>n</i> gäller alltid antingen att <i>f<sub>1</sub>(n)</i>&nbsp;=&nbsp;<i>O</i>(<i>f<sub>2</sub>(n)</i>)</li> eller att <i>f<sub>2</sub>(n)</i>&nbsp;=&nbsp;<i>O</i>(<i>f<sub>1</sub>(n)</i>)?</li>
</ul>

[Video om ordo-notation](https://www.youtube.com/watch?v=rZvpB4Ip2_M)

  
### 2.2 Datastruktur - prioritetskö

Implementera en prioritetskö som lagrar textsträngar. Implementera den som en min-heap på listform, dvs skapa inga noder eller pekare utan basera heapen på en lista.

- Gör ett tydligt API med publika dokumenterade metoder.
- Skriv utförlig testkod.
- Använd koden för den länkade listan i övning&nbsp;1 som mall.

Följande metoder ska finnas:

- Skapa en tom prioritetskö.
- Lägg till ett nytt element. (Kalla den insert(x)) (eller insert(x, prio) om du vill kunna styra prioriteter)
- Ta ut bästa elementet (med lägst värde på prioriteten) (kalla den extract_min()).
- Returnera antalet element i prioritetskön.
- Returnera hela prioritetskön som en sträng i indexordning från implementationen (inte i prioritetsordning).

*Ange tidskomplexiteten i värstafall för samtliga operationer.*

[Tips och råd (fast när uppgiften var att bygga ett träd, nu är den lite mindre komplex)](https://www.youtube.com/watch?v=NCzRttSCeH4) (Video)

## Högrebetygsuppgift (värd 10 högrebetygspoäng)

### 2.3 Datastruktur - Treap

Skapa ett randomiserat binärt sökträd, en treap, som håller sig balanserat även om värdena som ska lagras kommer i sorterad ordning. Sättet den gör det är att försöka imitera treapens villkor om "föräldern är bättre än barnen" men inte med avseende på värdena som lagras utan med avseende på slumptal som associeras med värdena.

- Gör ett tydligt API med publika dokumenterade metoder.
- Skriv utförlig testkod.
- Använd koden för den länkade listan i övning&nbsp;1 som mall för ditt träd.

Följande metoder ska finnas:

- Skapa ett tomt träd.
- Lägg till ett nytt element. (Kalla den insert(x))
- Undersök om ett element finns i trädet (Kalla den exist(x))
- Returnera antalet element i trädet.
- Returnerar en sträng med alla element i bokstavsordning, separerade med mellanslag.

Kom ihåg att skriva tester och docstrings!

(Ledning: Det kan vara svårt att skriva bra tester på internt tillstånd i trädet. Två möjligheter är att lägga till en publik metod som returnerar trädets maxhöjd och testa den, eller att prestandatesta trädet. Vi vill undvika linjära samband mellan storlek och tid om trädet är balanserat!)

Det finns problem i Kattis som hanterar binära sökträd, några är samlade i  https://kth.kattis.com/courses/DD1327/grudat26/assignments/m74qag. Dessa är inte obligatoriska men kan ge lite hjälp med att skriva ett balanserat sökträd. Notera att alla problemen kräver något slags styrprogram som *använder* ditt träd för att lösa den specifika uppgiften. Problemet bst ställer t.ex. specifika krav på att summera och skriva antal traverserade nivåer i trädet genom alla inserts i ett givet testfall! 
