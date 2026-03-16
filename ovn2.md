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



[Video om ordo-notation](https://www.youtube.com/watch?v=rZvpB4Ip2_M)

### 2.2 Tidskomplexitet för algoritm

[Video om tidskomplexitet](https://www.youtube.com/watch?v=x04gACtJHX0)
  
### 2.3 Datastruktur

[Tips och råd](https://www.youtube.com/watch?v=NCzRttSCeH4) (Video)

## Högrebetygsuppgift (värd 10 högrebetygspoäng)

### 2.4 Treap

Modifiera uppgift 2.3 så att du får ett randomiserat binärt sökträd i stället för ett obalanserat träd. Uppdatera tidskomplexiteterna för operationerna där det behövs. Kom ihåg att testa och dokumentera! Alla tester av det obalanserade trädet ska fortfarande gå igenom. 
(Ledning: Det kan vara svårt att skriva bra tester på internt tillstånd i trädet. Två möjligheter är att lägga till en publik metod som returnerar trädets maxhöjd och testa den, eller att prestandatesta trädet. Vi vill undvika linjära samband mellan storlek och tid om trädet är balanserat!)

Det finns problem i Kattis som hanterar binära sökträd, t.ex. https://open.kattis.com/problems/bst. Det ingår inte i kursen men kan ge lite hjälp med att skriva ett balanserat sökträd. Dock har detta problem sina egna givna modifikationer i trädets funktionalitet/insert-metod!
