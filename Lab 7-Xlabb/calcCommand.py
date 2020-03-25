"""
Kommandon för kalkylatorn.
"""

##
 # Läs in modulen för kö och stack
##
import queues

##
 # Datatyp för fel som uppstår i kalkylatorn
##
class CalcError(Exception):
    pass


##
 # listan med giltiga globala kommandon
 # dessa kan inte ingå i en kommandosekvens
##
commands = ['hjälp', 'sluta', 'töm']


##
 # listan med giltiga operatorer
##
operator = ['=', '+', '-', '*', '/', '^']

##
 # skapa kommandokön
##
Q = queues.fifoQueue()

##
 # skapa operandstacken
##
S = queues.stack()


def printHelp():
    """Utskrift av hjälptexten."""
    print('''
Mata in en sekvens med kommandon i omvänd polsk notation,
separerade med " ". Tillåtna kommandon är:
decimala tal (1, 1.2, ...)
'=' skriv ut värdet på stackens topp.
'+' addera stackens två översta värden.
'-' subtrahera stackens två översta värden.
'*' multiplicera stackens två översta värden.
'/' dividera stackens två översta värden.
'^' Upphöjer stackens överst värde till sista värde.

Därutöver kan man skriva
'sluta' för att avsluta sessionen
'hjälp' för att skriva ut denna text eller
'töm'   för att tömma kalkylatorns stack
''')


def getGlobalCommands():
    """
    Låter omgivande programdelar få del av
    programmets globala kommandon
    används av huvudprogrammet
    """
    return commands


def clearQueue():
    """
    Städning av kön
    används av funktionen validate
    """
    while not Q.empty():
        Q.dequeue()

def clearStack():
    while not S.empty():
        S.pop()


def validate(clist):
    """
    Kontrollerar att inmatningen endast innehåller
    tillåtna tal och operatorer.
    används av huvudprogrammet efter varje inmatning via tangentbordet
    """    
    for c in clist:
        if c in operator:  # köa operatorer
            Q.enqueue(c)
        elif c in commands: # inga globala kommandon tillåts här 
            clearQueue()
            raise CalcError("'" + c + "' är inte tillåtet i en kommandosekvens!")
        else:                # annars kan det bara vara
            try:
                x = float(c) # tal, som köas
                Q.enqueue(x)
            except ValueError:  # eller fel, som ger avbrott
                clearQueue()
                raise CalcError("Känner inte till något '" + c + "'-kommando!")

_calcPrint = __builtins__['print']

def atCalcPrint(pf):
    '''
    It takes in a funktion as argument and calls it at print command
    '''
    global _calcPrint
    _calcPrint = pf

def calcPrint(x):
    _calcPrint(x)

    
def doCommands():
    """
    Utför allt som finns i kommandokön.
    Anropas från huvudprogrammet efter varje validering.
    OBS att kön endast innehåller giltiga kommandon och tal
    eftersom validering av innehållet redan skett
    """
    # töm kön och utför vare kommando
    while not Q.empty():
        cmd = Q.dequeue()
        if cmd == '=':       # Visa vad stacken innehåller
            if S.empty():    # säg ifrån om den är tom
                raise CalcError('Stacken är tom')
            else:            # annars
                t = S.pop()  # hämta översta elementet
                calcPrint(t)     # skriv ut
                S.push(t)    # och lägg tillbaka

        elif cmd in operator: # försök utföra en beräkning
            performCalculation(cmd)
        else:                 # sista alternativet är
            S.push(cmd)       # ett tal, spara det i stacken


def performCalculation(c):
    """
    Försöker utföra en beräkning:
    * om stacken inte innehåller minst två operander,
    signaleras fel
    * annars hämtas två värden från stackens topp,
    beräkningen utförs och
    resultatet läggs tillbaka på stacken

    pre: stacken innehåller minst två värden och
    c är ett giltigt (aritmetiskt) kommando
    post: stacken innehåller resultatet av beräkningen
    används av: doCommand 
    """
    if S.empty():
        raise CalcError('Stacken är tom!')
    else:
        op1 = S.pop()
        if S.empty():
            S.push(op1)
            raise CalcError('Stacken innehåller bara en operand!')
        else:
            op2 = S.pop()
            res = None
            if c == '+':
                res = op2 + op1
            elif c == '-':
                res = op2 - op1
            elif c == '*':
                res = op2 * op1
            elif c == '/':
                try: 
                    res = op2 / op1
                except ZeroDivisionError as e:
                    clearStack()
                    raise CalcError('Division med noll ej definerad.')
            elif c == '^':
                res = op2 ** op1
            S.push(res)
