# Kompletteringsuppgifter för övning 1-2 (grudat26)
### Lämnas in i omtentaperioden (senast fredag 10/4 kl 19:00)

- Lös bara uppgifter för delar du blivit underkänd på och lämna in svaren i katalogen för den ordinarie övningen i organisationen [grudat26 på KTH GitHub](https://gits-15.sys.kth.se/grudat26).
- Utgå från mallarna i [/grudat26/ovn0/](https://github.com/isakemma/grudat/tree/master/ovn0).
- Lösningar ska vara inlämnade före deadline.
- Du kommer att få återkoppling på din inlämning på samma sätt som tidigare, antingen att uppgiften är godkänd eller att den behöver kompletteras.
- Normalt kommer återkopplingen senast på onsdagen veckan efter inlämning.


## Övning 1
Gör uppgifterna för den ordinarie övning 1, inklusive båda Kattisuppgifterna.

## Övning 2
### 2.1 Ordoquiz
Gör quiz i Canvas om ordobegreppet: [Ordoquiz](https://canvas.kth.se/courses/62593/assignments/375399/).

### 2.2 Kö
Implementera datastrukturen Kö.

Du kan ha användning av din länkade lista från övning 1. 
Visa att du kan testa systematiskt (det är inte ok att överlåta det målet till AI - dina tester ska övertyga dig om att du är klar!).

Följande metoder ska finnas:

- Skapa en tom kö.
- Lägg till ett nytt element. (Kalla den enqueue(x)).
- Undersök om ett element finns i kön (Kalla den exist(x)).
- Hämta första värdet ur kön (Kalla den dequeue()).
- Returnera antalet element i kön.
- Kontrollera dubbletter (Hur många element av varje sort finns det i kön? Returnera en lista som är sorterad i första hand på antal och i andra hand på värde. Kalla den duplicates()). Du kan med fördel använda biblioteksfunktioner för sortering!
- Returnerar en sträng med alla element i köordning, separerade med mellanslag.

*Ange tidskomplexiteten i värstafall för samtliga operationer.*
