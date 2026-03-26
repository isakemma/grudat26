class Stack:
    """
    Denna klass implementerar en stack av element. 
    Stacken används med funktionerna push, pop och top. 
    Du kan utgå ifrån exemplet i ovn0 för en stack, men ge metoderna dessa namr!
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
    arit_list = arit_input.split(' ')
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
