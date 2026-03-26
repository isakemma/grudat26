# Övning 3 grudat26 - Rekursiva algoritmer, induktionsbevis och loopinvarianter

Mål:
- Avgöra korrekthet för iterativa och rekursiva algoritmer
- Formulera och implementera rekursiva algoritmer
- Jämföra algoritmer med avseende på tids- och minnesåtgång

### Deadline: Tisdag 14/4 kl 19:00

**Vid övningen ska du vara beredd att muntligt presentera och diskutera dina lösningar och din programkod. Du ska också ha med en utskrift av din inlämning för kamratgranskning på övningen.**

- Gör (minst) en fil per uppgift och lägg filerna i katalogen <code>username-ovn3</code> i organisationen [grudat26 på KTH GitHub](https://gits-15.sys.kth.se/grudat26).
- Utgå från mallarna i [/grudat26/ovn0/](https://github.com/isakemma/grudat/tree/master/ovn0).
- Lösningar ska vara inlämnade före deadline.

Du väljer själv vilket av programspråken Python, Go eller Java du vill använda.
**Observera att all kod på den här kursen ska dokumenteras och testas.**

## Betyg E
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
Utöka din länkade lista från övning 1 med en metod larger(x) som tar en parameter x och räknar hur många av elementen i listan som är större än  inparametern x. Metoden ska använda en *rekursiv* (inte iterativ) hjälpfunktion. Skriv tester så att din nya metod fungerar som avsett om din lista har 0, 1 eller många element. Du behöver inte bifoga tester av resten av listan, för dem har du redan lämnat in i övning 1.


## Högrebetygsuppgift (värd 10 högrebetygspoäng)
### PRELIMINÄR 3.3 Designa med invarianter

- Skriv en effektiv funktion som tar två listor A och B av tal som båda är sorterade i stigande ordning som indata och avgör om det finns ett tal ifrån A och ett tal ifrån B som precis har summan *s*.
- Skriv en **loopinvariant** som förklarar hur koden fungerar.
- Räkna också ut tidskomplexiteten för din algoritm. Visa/motivera uträkningen. Algoritmen måste vara linjär i indatas storlek.

Algoritmen ska vara **in-place** ([Wikipedia: In-place algorithm](https://en.wikipedia.org/wiki/In-place_algorithm)),
dvs använda högst *O*(1) extra utrymme. *Du får inte använda någon sorteringsalgoritm.*

[Video om loopinvarianter](https://www.youtube.com/watch?v=vVdDyI1PIUU)






