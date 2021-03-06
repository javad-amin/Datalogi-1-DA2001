

"""
Stackbaserad kalkylator med omvänd polsk notation.
"""

import calcCommand

def main_function():
    # kommando-modulen vet vilka
    # globala kommandon som är giltiga
    globalCommands = calcCommand.getGlobalCommands()
    
    # berätta vad man kan göra
    calcCommand.printHelp()
    
    # Fortsätt för evigt (= tills kommandot 'sluta' ges)
    while True:
        # Hämta ett eller flera kommandon
        cmdString = input('calc > ').strip()
    
        # om ingenting matades in så börja om
        if cmdString == '':
            continue
    
        # men om någonting matades in så gör en lista av inmatningen
        cmdList = cmdString.split(' ')
    
        # om bara ett globalt kommando givits
        if len(cmdList) == 1 and cmdList[0] in globalCommands:
    
            # Hoppa ur kommando-slingan om kommandot är sluta
            if cmdList[0] == 'sluta':
                break
    
            # Skriv ut hjälptexten om kommandot är hjälp
            elif cmdList[0] == 'hjälp':
                calcCommand.printHelp()
    
            # annars kan kommandot bara vara 'töm'
            else:
                calcCommand.clearStack()
    
        # om kommandot inte är globalt eller användaren
        # givit mer än ett kommando (en kommandosekvens)
        else:
            try:
                # Skicka allt till kommandomodulen
                calcCommand.validate(cmdList)

                # Utför eventuella kommandon
                calcCommand.doCommands()
        
            # Fånga alla fel som uppstår och skriv ut dem
            except calcCommand.CalcError as ce:
                print(ce)

    print("Tack för denna gång!")

if __name__ == "__main__":
    main_function()

