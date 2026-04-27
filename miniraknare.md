## **Hjälpsam extrainformation som planerades att gås igenom på föreläsning 9**

Denna uppgift är en lätt förkortad del av en uppgift i vår systerkurs DD1328. I den här uppgiften övar du på att använda datastrukturen stack för att hantera något som inte reguljära uttryck kan göra: hantera syntax och matcha parenteser. Du gör detta genom att implementera en miniräknare som använder postfixnotation i sin inre representation. Postfixnotation är en syntax för att skriva uttryck som gör det extra effektivt för datorn att evaluera dem, jämfört med den normala infixnotationen som du hittills använt i matematiken.

Denna miniräknare hanterar aritmetiska uttryck som består av en avgränsad mängd symboler: positiva heltal, operatorerna +, -, *, / samt höger- och vänsterparentes.

I normal infixform befinner sig operatorerna mellan operanderna, och parenteser används för att klargöra i vilken ordning operationerna ska utföras. Som vanligt har * och / högre prioritet än + och -, parenteser anger att uttryck däri utvärderas först, och om det finns flera operatorer med samma prioritet så utförs operationerna från vänster till höger. Exempel på infixform är: 

2 + 3 <br>
14 * (2 + 3)<br>
((3 + 5 * 1) / 8) * 14

I postfixform placeras operatorerna efter operanderna. Parenteser behövs ej, utan ordningen på operationerna framgår av notationen. Samma exempel på posfixform är:

2 3 + <br>
14 2 3 + * <br>
3 5 1 * + 8 / 14 * 

Miniräknaren behöver två algoritmer:

##### Algoritm 1:

Vi använder funktionen p för att specificera operatorernas prioritet: 

| op    | p(op) |
|:-------:|:-------:|
| +     | 1     |
| −     | 1     |
| ∗     | 2     |
| /     | 2     |

Givet ett infixuttryck $U_1 ,..., U_m$, där $U_i$ är antingen en operand (ett positivt heltal), en operator eller en parentes, så översätter algoritmen nedan uttrycket till postfixform. Algoritmen använder sig av en stack för att mellanlagra symboler $U_i$.

För i = 1 till m:<br>
&emsp;&emsp; Om $U_i$ är en operand: <br>
&emsp;&emsp; &emsp;&emsp; Skicka $U_i$ till output.<br>
&emsp;&emsp; Om $U_i$ är en vänsterparentes: <br>
&emsp;&emsp; &emsp;&emsp; Pusha $U_i$ till stacken.<br>
&emsp;&emsp; Om $U_i$ är en högerparentes: <br>
&emsp;&emsp; &emsp;&emsp; Poppa symboler från stacken och skicka dem till output tills <br>
&emsp;&emsp; &emsp;&emsp; en vänsterparentes ligger på toppen av stacken. Poppa denna vänsterparentes.<br>
&emsp;&emsp; Om $U_i$ är en operator: <br>
&emsp;&emsp; &emsp;&emsp; Låt oss kalla toppelementet på stacken för $t$. <br>
&emsp;&emsp; &emsp;&emsp; Poppa symboler från stacken och skicka dem till output ända <br>
&emsp;&emsp; &emsp;&emsp; tills: $p(t) < p(U_i)$ <br>
&emsp;&emsp; &emsp;&emsp; eller: $t$ är en vänsterparentes<br>
&emsp;&emsp; &emsp;&emsp; eller: stacken är tom.  <br>
&emsp;&emsp; &emsp;&emsp; Pusha $U_i$ till stacken<br>
Poppa återstående symboler från stacken och skicka dem till output.

**Exempel** på hur algoritmen arbetar med infixuttrycket ((3+5∗1)/8)∗14:

|Infix-input |  Stack (toppen åt höger)    |       Postfix-output |
|:----:|:----:|:----:|
|((3+5∗1)/8)∗14  |    tom      |     tom                       | 
|(3+5∗1)/8)∗14   |     (       |    tom                        |  
| 3+5∗1)/8)∗14   |       ((    |      tom                      |
|  +5∗1)/8)∗14   |     ((      |        3                      |
|   5∗1)/8)∗14   |    ((+      |         3                     |
|   ∗1)/8)∗14    |    ((+      |           3 5                 |
|    1)/8)∗14    |   ((+∗      |          3 5                  |
|     )/8)∗14    |   ((+∗      |           3 5 1               |
|     /8)∗14     |    (        |          3 5 1 ∗ +            |
|        8)∗14   |     (/      |          3 5 1 ∗ +            |
|         )∗14   |     (/      |           3 5 1 ∗ + 8         |
|          *14   |     tom     |           3 5 1 ∗ + 8 /       |
|           14   |     *       |          3 5 1 ∗ + 8 /        |
|        tom     |     ∗       |          3 5 1 ∗ + 8 / 14     |
|        tom     |     tom     |         3 5 1 ∗ + 8 / 14 ∗    |

##### Algoritm 2:

Givet ett postfixuttryck V1 . . . Vn, där Vi är antingen en operand (ett positivt heltal) eller en operator, så evaluerar algoritmen uttrycket och returnerar dess värde.

För i = 1 till n: <br>
&emsp;&emsp; Om $V_i$ är en operand: <br>
&emsp;&emsp;&emsp;&emsp; Pusha $V_i$ till stacken.<br>
&emsp;&emsp; Om $V_i$ är en operator:  <br>
&emsp;&emsp;&emsp;&emsp; Tillämpa $V_i$ på de två toppelementen i stacken. Resultatet är <br>
&emsp;&emsp;&emsp;&emsp; en ny operand, som pushas till stacken. <br>
Poppa det återstående elementet i stacken och skicka till output.

**Exempel** på hur algoritmen arbetar med infixuttrycket 3 5 1 * + 8 / 14 *:

|Postfix-input |  Stack (toppen åt höger)    |    Eval-output      |
|:---:|:---:|:---:|
|3 5 1 * + 8 / 14 *|tom|tom|
|5 1 * + 8 / 14 *|3|tom|
|    1 * + 8 / 14 *   |    3 5 |tom|
 |     * + 8 / 14 *    |   3 5 1 |tom|
 |      + 8 / 14 *    |   3 5 |tom|
 |         8 / 14 *   |    8 |tom|
 |           / 14 *    |   8 8 |tom|
  |            14 *    |   1 |tom|
  |               *    |   1 14 |tom|
 |            tom    |  14|tom|
|		tom |		   tom      |              14 |

#### Tolka korrekta infixuttryck och evaluera dem 

**Din uppgift är nu att i Python implementera din egen postfixminiräknare som tar in infixuttryck**, omvandlar dem till postfixform med Algoritm 1, evaluerar dem med Algoritm 2, och skriver ut svaret. De centrala datastrukturerna i din algoritm är två stackar, en för Algoritm 1 och en för Algoritm 2.

Till din hjälp har du ett kodskelett (nedan), som innehåller en lämplig struktur för funktioner och datastrukturer, samt funktionalitet för att läsa aritmetiska uttryck som programmet läst in via standard input. 
Kodskelettet innehåller funktionen readInfix och skelett till funktionerna infixToPostfix, evalPostfix, top, pop och push som behövs för implementationen. Skapa sen de ytterligare funktioner och variabler du vill ha i ditt program.

Komplettera skelettet tillsammans med kommentarer så att läsaren förstår hur din implementation fungerar. Lämna in din kod på vanligt sätt i github men testa den också på Kattis!

Så här ska körningar från din miniräknare se ut (fyra exempel). De fetstilta raderna markerar den input som körningen gäller. (Lägg märke till mellanslagen mellan alla tecken i indatat)

&emsp;&emsp; **( ( 3 + 5 * 1 ) / 8 ) * 14** <br>
&emsp;&emsp; Postfixnotation: 3 5 1 * + 8 / 14 *<br>
&emsp;&emsp; Resultat: 14

&emsp;&emsp; **4 * 3 - 2** <br>
&emsp;&emsp; Postfixnotation: 4 3 * 2 -<br>
&emsp;&emsp; Resultat: 10

&emsp;&emsp; **( 3 + 4 ) / 7 + ( 8 / 4 - 9 / 3 )** <br>
&emsp;&emsp; Postfixnotation: 3 4 + 7 / 8 4 / 9 3 / - +<br>
&emsp;&emsp; Resultat: 0

&emsp;&emsp; **( ( ( 120 / 5 + 6 ) / 10 * 5 ) + 36 - 1 ) / 25** <br>
&emsp;&emsp; Postfixnotation: 120 5 / 6 + 10 / 5 * 36 + 1 - 25 /<br>
&emsp;&emsp; Resultat: 2


Det finns Kattis-uppgifter som krävs för att få godkänt, men du behöver även själv kontrollera att din kod fungerar korrekt. Notera att Kattis är känsligt för hur input läses in, använd gärna input(), och att du endast skriver ut det som efterfrågas i uppgiften. Du kan lämna in hur många gånger som helst. Efter varje inlämning kan du se under "Debugging hints" vilken typ av input ditt program inte klarade. 
Du hittar Kattis-uppgifterna här: [https://kth.kattis.com/courses/DD1327/
](https://kth.kattis.com/courses/DD1327/grudat26/assignments/gavufo), uppgift E, F och G.

**Kodskelettet finns nedan**, komplettera det med egna funktioner/metoder (samt ändra de ofullständiga metoderna givna) för att lösa problemet

```python
class Stack:
    """
    Denna klass implementerar en stack av element. 
    Stacken används med funktionerna push, pop och top. 
    """

    def __init__(self) -> None:
        """
        Skapa en tom stack.
        :param data: lista med stackens element.
        """
        self._data = []

    def push(self, item):
        """
        Lägg till ett element item på stacken.
        (Detta görs genom att lägga till elementet sist i data.)
        """
        self._data...

    def pop(self):
        """
        Ta bort ett element från stacken och returnera det.
        (Detta görs genom att ta bort det sista elementet i data och returnera
        det. Tänk på hur du hanterar försök att poppa från en tom stack?)
        """
        return self._data...

    def top(self):
        """
        Returnera det sista elementet i stacken.
        (Detta görs genom att returnera det sista elementet i. Tänk på hur du 
        hanterar försök att titta på toppelementet i en tom stack?)
        """
        return self._data...

    

def readInFix():
    """
    Funktion som omvandlar en sträng med input till ett lista av 
    aritmetiska symboler. (Tänk på att kontrollera att elementen 
    i listan alla är godkända symboler.)
    Exempel: 2 + 3, 14 * ( 2 + 3 ), ( ( 3 + 5 * 1 ) / 8 ) * 14
    Godkända operander: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
    Godkända operatorer: '*', '+', '-', '/' samt parenteser
    :param arit_input: en sträng med ett aritmetiskt uttryck. 
    :return: en lista med ett aritmetiskt uttryck.
    """
    ...
    arit_input = str(input())
    arit_list = arit_input.split(', ')
    ...
    
    return arit_list

def infixToPostfix(i_array):
    """
    Översättning av ett uttryck från infix- till postfixformat
    :param i_array: en lista med ett infixuttryck.
    :return: en lista med ett postfixuttryck.
    """
    ...
    
def evalPostfix(p_array):
    """
    Evaluering av ett uttryck på postfixformat
    :param p_array: en lista med ett postfixuttryck.
    :return: ett resultat.
    """
    ...
    
def main():
    infix_list = readInFix()
    ...
    
if __name__ == "__main__":
    main()
```

#### Felhantering

Implementationen ovan förutsätter att all input är giltiga infixuttryck, och så fungerar ju inte världen alltid. Om uttrycket inte garanteras innehålla endast tillåtna tecken, dvs positiva heltal och tecknen +, -, *, /, ) och ( kommer programmet krascha eller fungera felaktigt (beroende på din implementation).

Utöka funktionen readInfix så att den hanterar all möjlig input! Om ett uttryck är felaktigt ska miniräknaren klaga på det genom att skriva "Invalid Infix". 


#### Enhetstestning

Notera att Kattisuppgifterna gör enhetstestning av er kod. I denna uppgift kommer du alltså duplicera vad den gör. Syftet är att du ska visa att du har omdöme att skriva relevanta tester själv.

Din uppgift här är att utöka programmet med minst 5 enhetstester vardera av funktionerna infixToPostfix och evalPostfix. Testerna ska fånga så många tänkbara fel som möjligt i parsningen av stackarna, tex prioritetsordning av operatorer, felaktig hantering av parenteser, eller felaktig hantering av tal med flera siffror. 

Enhetstesterna ska följa de principer vi gått igenom, dvs vara automatiska och oberoende av användaren, och bara skriva ut meddelanden när något i implementationen är fel. Du behöver inte testa stacken denna gång och det går bra att anta att uttrycken är syntaktiskt korrekta och bara testa implementationen av algoritmerna.

#### **Redovisning**
Förbered dig för redovisningen!Det är mycket som ingår i den här uppgiften och du kommer inte att presentera allt på en gång.

Vid den muntliga redovisningen kan läraren att be dig testa miniräknaren med nya uttryck. Det kan vara bra om du förberett dig med att rita upp stackarna för något av de fyra körexemplen, likt dem i exemplen för algoritm 1 och algoritm 2!

Infixuttryck kan vara felaktiga på många sätt och det är bra om du för en given inputsträng kan avgöra varifrån klagomålet kommer och vad det var som var fel, även om det inte behöver skrivas ut på Kattisuppgiften eller i din inlämning!
Tänk ut tre felaktiga input och hur de hanteras av programmet (dvs var det avgörs att de är felaktiga)!

Var beredd på att förklara vilka sorters fel dina enhetstester letar efter!

---
