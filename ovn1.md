# Övning 1 grudat26
### Deadline: Tisdag 24/3 kl 19:00
Mål:
- Systematiskt testa program för att upptäcka fel
- Använda abstraktion som ett verktyg för att förenkla programmeringen

**Vid övningen ska du vara beredd att muntligt presentera och diskutera dina lösningar och din programkod. Du ska också ha med en utskrift av din inlämning för kamratgranskning på övningen.**

- Gör (minst) en fil per uppgift och lägg filerna i katalogen <code>username-ovn1</code> i organisationen [grudat26 på KTH GitHub](https://gits-15.sys.kth.se/grudat26).
- Utgå från mallarna i [/grudat26/ovn0/](https://github.com/isakemma/grudat/tree/master/ovn0).
- Lösningar ska vara inlämnade före deadline.
- Du kommer att få återkoppling på din inlämning i form av ett **issue**, antingen att uppgiften är godkänd eller att den behöver kompletteras.
- Normalt kommer återkopplingen senast en vecka efter deadline.

För den länkade listan kan du bara använda programspråket Python. För den andra uppgiften väljer du själv vilket av programspråken Python, Go eller Java du vill använda.
**Observera att all kod på den här kursen ska dokumenteras och testas.**

## Betyg G

### 1.1 Testning av Länkade listor

En **lista** (array), ett antal element ordnade i en linjär struktur, är den kanske enklaste och mest grundläggande datastrukturen.

En **länkad lista** är en sekvens av listelement förbundna av pekare.
En länkad lista med tre heltal <code>[2,&nbsp;2,&nbsp;1]</code> ser ut så här:

<pre><code>     ----------        ----------        ------------
    |     |    |      |     |    |      |     |      |
--->|  2  |  -------->|  2  |  -------->|  1  | null |
    |     |    |      |     |    |      |     |      |
     ----------        ----------        ------------
</code></pre>

(Nullpekaren har olika namn i olika programspråk: <code>None</code>, <code>nil</code> eller <code>null</code>.)

Listelementen kan implementeras som objekt med två instansvariabler,
en variabel som innehåller värdet och en variabel som pekar på nästa element i listan.
I **pseudokod**:

<pre><code># A list element that stores a value of type T.
private ListElement:
    data T
    next ListElement
</code></pre>

<pre><code># A singly linked list of elements of type T.
public LinkedList:
    private first ListElement # first element in list
    private last ListElement  # last element in list
    private size int          # number of elements in list
   
    # Create an empty list.
    public new() LinkedList

    # Insert the given element at the beginning of this list.
    public void addFirst(element T)

    # Insert the given element at the end of this list.
    public void addLast(element T)

    # Return the first element of this list.
    # Return null if the list is empty.
    public getFirst() T

    # Return the last element of this list.
    # Return null if the list is empty.
    public getLast() T

    # Return the element at the specified position in this list.
    # Return null if index is out of bounds.
    public get(index int) T

    # Remove and returns the first element from this list.
    # Return null if the list is empty.
    public removeFirst() T

    # Remove all elements from this list.
    public clear()

    # Return the number of elements in this list.
    public size() int

    # Return a string representation of this list.
    # The elements are enclosed in square brackets ("[]").
    # Adjacent elements are separated by ", ".
    public string() string
</code></pre>

Den här gången ska du testa vissa av dina lösningar på Kattis
innan du lämnar in dem på ditt githubkonto.

1. Du får tillgång till Kattis genom att [logga in](https://kth.kattis.com/login) med ditt KTH-id.
2. Du måste också [registrera dig på grudat26](https://kth.kattis.com/courses/DD1327/grudat26/register) i Kattis. 
3. Om du gör uppgiften på workshop-passet, skapa en grupp i Kattis för uppgiften Workshop-problem med dina gruppkamrater så plagiatflaggas ni inte när ni skickar in samma kod.

Mer information om Kattis hittar du på [Kattis supportsidor](https://support.kattis.com/support/home).

- Skriv <b>utförlig testkod</b> för en pythonimplementation av ovanstående api med pythons inbyggda modul unittest. Alla publika metoder ska testas.
  Glöm inte att kontrollera beteendet även för den tomma listan! Se exemplet [github.com/isakemma/grudat/blob/master/ovn0/StackTest.py](https://github.com/isakemma/grudat/blob/master/ovn0/StackTest.py)

- Denna del (1.1) av hemuppgiften får lösas i grupp om du deltar i Workshop-passet den 19/3 kl 9-12.

- Du får hjälp att verifiera att du testat tillräckligt noga av Kattis. 

- Du kan arbeta iterativt och skicka in dina testfall till Kattis (https://kth.kattis.com/courses/DD1327/grudat26/assignments/m4m3pf/problems/kth.testthelist). Inga av testfallen i Kattis handlar om att alla element som lagras i listan har samma typ, eller om det exakta värdet, alltså behöver du inte kolla om det finns en specifik sträng eller ett specifikt tal som har sönder någon av implementationerna.


### 1.2 Egen listimplementation 

- Implementera en enkellänkad lista i form av en klass som innehåller funktionerna i ovanstående **pseudokod**.
  Du får inte ändra klassens gränssnitt, dvs du får inte ändra **signaturerna** eller **dokumentationskommentarerna**
  på de  publika metoderna eller lägga till några andra publika metoder. Klassen ska kunna testas med din färdiga testsvit.
  Jag rekommenderar att du testar den ofta medan du skriver den!
- Skicka in din färdiga lista tillsammans med din testsvit till ett annat Kattisproblem: (https://kth.kattis.com/courses/DD1327/grudat26/assignments/otf5na/problems/kth.testyourlist) så att vi kan se att dina tester körts på din lista.

- Beräkna den asymptotiska värstafallstiden för samtliga publika metoder i din implementation. (Gås igenom på föreläsning 2.)
  Uttryck tiden som en funktion av antalet element&nbsp;<i>n</i> i listan.


#### Tips

Ditt program ska bestå av två klasser:

- <code>LinkedList</code> är den publika delen av programmet,
- <code>ListElement</code> är en privat hjälpklass som implementerar ett element i den länkade listan.

Titta gärna på exempelmallarna för Stacken i övning 0. (De visar hur man kan skriva och testa en klass i Python men även Java och Go):

- [github.com/isakemma/grudat/blob/master/ovn0/stack.py](https://github.com/isakemma/grudat/blob/master/ovn0/stack.py)
- [github.com/isakemma/grudat/blob/master/ovn0/Stack.java](https://github.com/isakemma/grudat/blob/master/ovn0/Stack.java)
- [github.com/isakemma/grudat/blob/master/ovn0/stack.go](https://github.com/isakemma/grudat/blob/master/ovn0/stack.go)

[Tips och råd](https://www.youtube.com/watch?v=SH72Eyelbs4) (video)

### 1.3 Testreflektion (ca en A4-sida)
- Vilka sorters fel letar dina testfall efter? Vad är det sannolikt för fel på de testade implementationerna i Kattisproblemet? Räkna upp minst fem olika saker som måste ha varit felimplementerade!
- Hur fungerade det att skriva den länkade listan när du hade testfallen klara? Brukar du göra så?

