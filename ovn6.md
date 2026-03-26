# Övning 6 grudat26
### Deadline: Tisdag 5/5 kl 19:00

Mål:
 - formulera och implementera rekursiva algoritmer
 - skriva och använda enkel BNF-syntax
 - konstruera och använda reguljära uttryck

**Vid övningen ska du vara beredd att muntligt presentera och diskutera dina lösningar och din programkod. Du ska också ha med en utskrift av din inlämning för kamratgranskning på övningen.**

- Gör (minst) en fil per uppgift och lägg filerna i katalogen <code>username-ovn6</code> i organisationen [grudat26 på KTH GitHub](https://gits-15.sys.kth.se/grudat26).
- Utgå från mallarna i [/grudat26/ovn0/](https://github.com/isakemma/grudat/tree/master/ovn0).
- Lösningar ska vara inlämnade före deadline.

Den här gången ska du testa vissa av dina lösningar på Kattis 
innan du lämnar in dem på ditt githubkonto. Om du inte gjorde övning 1 eller 4 behöver du först registrera dig på kursen.

1. Du får tillgång till Kattis genom att [logga in](https://kth.kattis.com/login) med ditt KTH-id.
2. Du måste också [registrera dig på grudat26](https://kth.kattis.com/courses/DD1327/grudat26/register) i Kattis. 



## 6.1 Dynamisk programmering
<!-- CC BY-SA 2.0: https://www.flickr.com/photos/bekathwia/5148701602 -->
![Knitting machine HACKED](https://github.com/isakemma/grudat/blob/master/knitting-machine-hacked.jpg)

[Hacking the Brother KH-930e Knitting Machine](https://www.youtube.com/watch?v=GhnTSWMMtdU)

En F-teknolog har kommit över en stickmaskin och ett parti garn och planerar att sticka och sälja halsdukar.

Efter en noggrann marknadsundersökning har teknologen sammanställt en tabell över priset på olika typer av halsdukar:
h[n] är det högsta priset på en halsduk som man kan sticka av n meter garn.

För att tjäna så mycket pengar som möjligt vill vi förstås hitta en optimal kollektion.
Följande rekursion beräknar den maximala inkomsten p(n) som man kan tjäna genom att sticka halsdukar av n meter garn:

> p(0) = 0,  
> p(n) = max<sub>1 &le; i &le; n</sub>(h[i] + p(n-i)) om n > 0.

- Förklara varför rekursionen fungerar.
- Implementera en rekursiv funktion som beräknar p(n). Glöm inte dokumentation och testkod.
- Beräkna p(5) när h[1] = 2, h[2] = 5, h[3] = 6, h[4] = 9 och h[n] = 0 när n > 4.
  Simulera beräkningen för hand och rita ett träd över alla funktionsanrop.
  (Det går bra med ett foto på ett handritat träd.)
- Förklara varför tidskomplexiteten för denna funktion är exponentiell.
- Förbättra tidskomplexiteten genom att skriva en version av programmet som cachar delresultat.
- Räkna ut en tabell över p(n) för n = 0, 1, 2, 3, 4, 5 (med samma h som ovan). Gör beräkningen för hand.
- Visa att tidskomplexiteten för den uppdaterade koden är O(n<sup>2</sup>).

[Tips om dynamisk programmering](https://www.youtube.com/watch?v=obslDoqkm7E) (video)



## 6.2 Reguljära uttryck (Kattis)

### Uppgift [grudatregex](https://kth.kattis.com/courses/DD1327/grudat26/assignments/gavufo/problems/grudatregex).

[Tips om reguljära uttryck](https://www.youtube.com/watch?v=NvKvCXac7sM) (video)

Dina funktioner måste ligga i en fil som heter regex.py, annars får du Run Time Error (“ImportError”) i Kattis.

Använd kodskelettet [regex.py](regex.py). Funktionerna i skelettet returnerar alla en tom sträng,
men de ska i din lösning returnera strängar som innehåller reguljära uttryck som löser deluppgifterna nedan.

De uttryck du konstruerar får vara högst 250 tecken långa (en generöst tilltagen gräns),
förutom i de två uppgifterna som tar en söksträng som indata.
Om du i någon av de andra uppgifterna returnerar ett för långt uttryck så får du Wrong Answer i Kattis.

I uppgifter där kravet är att hela strängen ska uppfylla något villkor så måste du använda
de speciella symbolerna ^ och $.

Kattis kommer att testa uppgifterna i ordning. När du är klar med första uppgiften
kan du alltså skicka in din lösning och se om du klarar alla testfall som hör
till första uppgiften, och så vidare.

### 6.2.1 Oktal sträng (första testfallet)
Skriv ett regex som matchar en sträng om och endast om den består av enbart oktala tal, dvs i talbasen 8.

### 6.6.2 ISIN (andra testfallet)
Vid publik fondhandel har alla värdeinstrument en ISIN-kod, som är en unik identifierare. Skriv ett regex som matchar en sträng om och endast om den uppfyller kraven för ett ISIN-nummer, som uppfyller följande regler [från ISIN-formatets definition](https://www.isin.org/isin-format/):

- Första två tecknen är bokstäver, versaler (motsvarar en landskod, men du behöver inte kolla att landskoden existerar)
- Följande nio tecken är alfanumeriska (versaler)
- Det sista tecknet är en kontrollsiffra (du behöver inte implementera stöd för att verifiera kontrollsiffran).

### 6.2.3 Alfabetiskt sorterad? (tredje testfallet)
Du läser en sträng och ska avgöra om alla tecken på plats i+x är större än eller lika med tecknet på plats i, för varje i och alla x $\geq$ 1.
Indata är strängar med små bokstäver. Skriv ett reguljärt uttryck som avgör om strängen uppfyller kravet!

### 6.2.4 Komplexa tal i python (fjärde testfallet)
Python har inbyggt stöd för komplexa tal som får en egen typ och som känns igen av imaginärdelen. Komplexa tal består av en realdel som skrivs som ett flyttal och en imaginärdel som skrivs som ett flyttal med j eller J direkt efter, t.ex. 2+5j eller -1-0.15J. 
Om realdelen är noll behöver den inte skrivas ut. Om den är positiv är det tillåtet att ha med ett plustecken före. Om imaginärdelen är 0 måste talet innehålla 0j eller 0J, annars tolkas plus och minus som operationer. Om imaginärdelen är 1j måste ettan skrivas ut av samma skäl. 

(Det här är en förenkling. Egentligen tillåts alla float-värden inklusive Infinity och NaN, och tal på exponentform, men dem behöver du inte matcha. I den här uppgiften tillåter vi inte heller .3j, utan kräver 0.3j för att uttrycka det talet. Du behöver inte heller kunna byta ordning på real- och imaginärdelen eller tillåta variabler som realdel, vilket Python skulle acceptera.) 
Skriv ett reguljärt uttryck som känner igen sådana här komplexa tal!

### 6.2.5 Mac-adress (femte testfallet)
(Grupper och referenser)

Uppgift: MAC-adress Alla nätverkskort har en unik identifierare som kallas MAC-adress. Din uppgift är att skriva ett reguljärt uttryck som matchar en giltig MAC-adress enligt följande regler:
Den består av sex grupper om två hexadecimala siffror (0-9, a-f, A-F).

Grupperna separeras antingen med kolon (:) eller bindestreck (-).
Viktigt: Blandade separatorer tillåts inte i samma adress. Om den första gruppen följs av ett kolon måste alla andra också göra det (t.ex. 01:23:45:67:89:ab eller 01-23-45-67-89-ab men inte 01-23-45:67:89-ab).


### 6.2.6 Sjörövarspråket (sjätte testfallet)
Skriv ett reguljärt uttryck som matchar alla strängar på sjörövarspråket uttryckt i versaler. Sjörövarspråket (eller rövarspråket) är ett påhittat kodspråk av Astrid Lindgren där varje konsonant byts ut mot konsonanten, följt av ett ’O’, följt av konsonanten igen. T.ex. blir RÖVARSPRÅKET till RORÖVOVARORSOSPOPRORÅKOKETOT. 
Skriv ett reguljärt uttryck som matchar alla strängar på sjörövarspråket uttryckt i versaler. Testtexterna innehåller inga andra tecken än versala svenska bokstäver och inga andra skiljetecken än `.,!?`  eller några whitespace förutom space (mellanslag).
### 
  
## Högrebetygsuppgift (värd 10 högrebetygspoäng): Mer dynamisk programmering

Uppdatera koden så att den inte bara beräknar den maximala inkomsten,
utan också ger en lista över halsdukar (garnåtgång och antal) som uppnår detta.
Om det finns flera möjliga lösningar så räcker det om du anger en.

## Högrebetygsuppgift (värd 10 högrebetygspoäng): Miniräknare med postfixnotation
Du ska tolka aritmetiska operationer på infixform som postfix med hjälp av en stack, och evaluera dem. Det finns tre kattisuppgifter till din hjälp, men du behöver också skriva egna tester (som kanske testar samma saker som Kattis). Gör det för varje bugg du rättar eller ny del av koden du lägger till! Det är funktionerna infixToPostfix och evalPostfix som huvudsakligen ska testas (du behöver lämna in utförliga tester av din stack denna gång, men antagligen ha dem för dig själv ändå).
Ett kodskelett finns i filen [miniraknare.py](miniraknare.py).
I den första uppgiften ska du bara tolka infix-uttryck som postfix.
I den andra uppgiften behöver du evaluera postfix-uttryck, och i den tredje uppgiften behöver du även felhantera indatat - det går förstås inte att evaulera indata på fel format på ett säkert sätt!

https://kth.kattis.com/courses/DD1327/grudat26/assignments/gavufo/problems/miniraknarepostfix
https://kth.kattis.com/courses/DD1327/grudat26/assignments/gavufo/problems/miniraknareevaluering
https://kth.kattis.com/courses/DD1327/grudat26/assignments/gavufo/problems/miniraknarefelhantering


