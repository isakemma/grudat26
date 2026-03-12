# Övning 3 grudat26 - Rekursiva algoritmer, induktionsbevis och loopinvarianter

Mål:
- Avgöra korrekthet för iterativa och rekursiva algoritmer
- Formulera och implementera rekursiva algoritmer
- Jämföra algoritmer med avseende på tids- och minnesåtgång

### Deadline: Fredag 4/4 kl 12:00

**Vid övningen ska du vara beredd att muntligt presentera och diskutera dina lösningar och din programkod. Du ska också ha med en utskrift av din inlämning för kamratgranskning på övningen.**

- Gör (minst) en fil per uppgift och lägg filerna i katalogen <code>username-ovn3</code> i organisationen [grudat26 på KTH GitHub](https://gits-15.sys.kth.se/grudat26).
- Utgå från mallarna i [/grudat26/ovn0/](https://github.com/isakemma/grudat/tree/master/ovn0).
- Lösningar ska vara inlämnade före deadline.

Du väljer själv vilket av programspråken Python, Go eller Java du vill använda.
**Observera att all kod på den här kursen ska dokumenteras och testas.**

## Betyg G
### 3.1 Bevisa korrekthet med induktion 
Bevisa med induktion att följande funktion som bygger ett palindrom är korrekt. 
Var noga med att namnge den egenskap du bevisar och använda både funktionens beteende (utskrift snarare än returvärde) och ditt induktionsantagande i beviset!

```python=
def palindrome(inputString):
    """Function that creates a palindrome from an input string 
    by appending all characters but the last in reverse order.
    Prints the string one character at each line. 
    
    Example: For input "lion" the printout should be:
    l
    i
    o
    n
    o
    i
    l"""
    character = inputString[0]
    if len(inputString) > 1:
        print(character)
        palindrome(inputString[1:])
    print(character)
```

### Tips
- Läs hela uppgiften, gör det som efterfrågas! Tex krävs ingen egen kod, men beviset måste relatera till koden som anges!
- Var tydlig med när du använder ett basfall eller ett induktionsantagande! Var tydlig med vilken egenskap du bevisar!

Nu har vi bevisat att algoritmidén är rätt. Detta är ett annat paradigm än testning - testningen gäller själva implementationen. 

> Beware of bugs in the above code; I have only proved it correct, not tried it.

&ndash; Donald Knuth

[Video om induktion](https://www.youtube.com/watch?v=x8dmvJIF-MI)

### 3.2 Implementera rekursiv funktion
Skriv en rekursiv funktion som tar ett binärträd (från övning 2) med heltalsvärden samt ett heltal som indata och räknar hur många av värdena i trädet som är större än indatavärdet! Skriv tester på att din funktion fungerar som avsett. Du behöver inte testa trädet denna gång eftersom du gjorde det i förra hemuppgiften!

### 3.3 Typvärde

[Typvärdet](https://sv.wikipedia.org/wiki/Typv%C3%A4rde) (mode)
i ett statistiskt datamaterial är det värde som förekommer flest gånger.

- Skriv en funktion som beräknar typvärdet för en vektor med heltal.
  Om flera värden är lika vanliga skall funktionen ge det minsta av dem.
- Tidskomplexiteten för din algoritm ska vara *O*(*n*&nbsp;log&nbsp;*n*). Motivera din komplexitet!

Det är fritt fram att använda de datastrukturer och algoritmer
som finns i standardbiblioteken för Python, Java eller Go.
Det är bra att kunna sitt standardbibliotek och det är bra praxis att använda en färdig vältestad funktion
snarare än att skriva den själv.

Med det sagt, så får man inte använda https://docs.python.org/3/library/statistics.html#statistics.multimode,
som ju nästan löser uppgiften direkt.
Observera också att det inte framgår av Python-dokumentationen vilken tidskomplexitet denna funktion har.


## Betyg VG
### 3.4 Negativt och positivt

- Skriv en effektiv funktion som ändrar ordningen på en vektor med tal så att de negativa talen kommer först.
  Vektorn ska inte sorteras, du behöver endast samla alla negativa tal för sig.
- Skriv en **loopinvariant** som förklarar hur koden fungerar.
- Räkna också ut tidskomplexiteten för din algoritm. Visa/motivera uträkningen. Algoritmen måste ha *O*(*n*) tidskomplexitet.
- Det räcker med förväntad (expected) tid, men värstafall går förstås också bra.

Algoritmen ska vara **in-place** ([Wikipedia: In-place algorithm](https://en.wikipedia.org/wiki/In-place_algorithm)),
dvs använda högst *O*(1) extra utrymme. *Du får inte använda någon sorteringsalgoritm.*

[Video om loopinvarianter](https://www.youtube.com/watch?v=vVdDyI1PIUU)

På engelska skiljer man på **average** time complexity där man väger samman tiderna för alla möjliga indata och  **expected** time complexity där algoritmen använder sig av slump för att göra värstafallsbeteendet extremt osannolikt. Vi har sett två exempel på expected time hittils i kursen: hashtabeller och treapar. På svenska finns det tyvärr ingen tydlig och bra terminologi.

Så här skriver Wikipedia om [Average-case complexity](https://en.wikipedia.org/wiki/Average-case_complexity):

> Average-case analysis requires a notion of an "average" input to an algorithm,
> which leads to the problem of devising a probability distribution over inputs.
> Alternatively, a randomized algorithm can be used.
> The analysis of such algorithms leads to the related notion of an expected complexity.





