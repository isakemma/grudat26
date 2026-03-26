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

## Betyg E

### PRELIMINÄR - 4.1 Tidskomplexitet för rekursiva funktioner

#### Teori

Beräkna **tidskomplexiteten** för följande funktioner:  
```python=
# Binärsökning och quicksort implementerade från kursboken yourbasic.org 
def findA(v, val, start, stop):
    l = stop - start
    if l == 0:
        return start
    elif l == 1:
        if val <= v[start]:
            return start
        else:
            return start + 1
    mid = start + l//2
    if val <= v[mid-1]:
        return findA(v, val, start, mid)
    return findA(v, val, mid, stop)
    ```
```python=
def findB(v, val):
    if len(v) == 0:
        return 0
    elif len(v) == 1:
        if val <= v[0]:
            return 0
        else:
            return 1
    mid = len(v) //2
    if val <= v[mid-1]:
        return findB(v[:mid], val)
    return mid + findB(v[mid:], val)
```
```python=
def quicksortA(v, start, stop):
    if start < stop:
        pivot = partition(v, start, stop) 
        print(v[start:stop])
        quicksortA(v, start, pivot-1) 
        quicksortA(v, pivot+1, stop)
```
```python=
def quicksortB(v):
    start, stop = 0, len(v)-1
    if start < stop:
        pivot = partition(v, 0, len(v)-1) 
        quicksortB(v[:pivot-1]) 
        quicksortB(v[pivot+1:])
```



 Notera skillanderna mellan de båda exemplen och fundera på vad den kan innebära! Du behöver visa hur beräkningen ser ut, inte bara svaret! Det går bra med förväntad eller värstafalls-komplexitet och ska uttryckas med big-O notation.

[Tips och råd om att räkna ut tidskomplexitet för rekursiva funktioner](https://www.youtube.com/watch?v=sorlJiiWDRA) (video)
Beware of bugs! But you do not have to fix them right now.

#### Praktik

Gör ett **benchmark** där du mäter tiden för att exekvera de här funktionerna.
Uppgiften ska göras i **Python** och du ska mäta tiden, till exempel med funktionen <code>time.time</code>:

<pre><code>start = time.time()
n = [random.randint(0, 1000) for _ in range(10000)]
find1(n, 50)
print(n, time.time() - start) # elapsed time
</code></pre>

Testa för n av längd 10, 100, 1,000, 10,000, 100,000 och 1,000,000. Vid behov kan du också testa större tal, eller kanske fler längder på listan. Eftersom exemplet använder slumpdata kan det vara bra att lägga mätningarna i en loop och ta medelvärdet, speciellt för quicksort!

För att göra mätningarna på quicksort behöver ni en funktion partition. Det går bra att använda en från kurslitteraturen eller internet, exempelvis nedanstående förenklade geeksforgeeks.org, men du måste kunna förklara vad varje del gör och varför de gör så!
```python=
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
```
Presentera resultaten av tidmätningarna i en **tabell** eller i en **graf**.

#### Diskussion

Skriv en **diskussionsdel** där du försöker förstå och förklara eventuella skillnader mellan teori och praktik.


### 4.2 Linjärtidssortering av små tal

**Implementera**, **dokumentera** och **testa** en algoritm som sorterar heltalen x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>n</sub>.
För samtliga tal x<sub>i</sub> gäller att 0 &le; x<sub>i</sub> &le; k.

Analysera tidskomplexiteten. Din algoritm ska ha värstafallstidskomplexitet O(n+k).
För vilka värden på k blir algoritmen linjär?

<b>Tips:</b> räkna hur många element det finns av varje sort.

## Högrebetygsuppgift (värd 10 högrebetygspoäng)

### 4.3 Sortering med vissa restriktioner

Lös uppgiften Sort of sorting på Kattis. Besvara följande frågor skriftligt och skriv in en länk till Kattisinskickningen!
- Vad är det lämpligt att använda för slags sortering här? 
- Varför? 
- Vad blir komplexiteten för din lösning?

Lägg dina egna testfall i en separat fil som du inte skickar in till Kattis - den här gången är det inte dina tester som testas.

(https://open.kattis.com/problems/sortofsorting)


