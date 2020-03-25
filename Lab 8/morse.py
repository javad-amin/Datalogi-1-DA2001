import morse_io as mio

def readfile(file):
	'''
	Öppnar valfri fil
	Tar in en fil som argument. 
	Retunerar en sträng.
	'''
	try:
		fh = open(file, 'r', encoding="utf8") # Öppnar och läser en fil med utf-8 encoding
		file = fh.read() #Läser inhåller av filen som en sträng
		fh.close() # Stänger filen.
		return file
	except:
		print('Fel: \n Filen morse.d kunde inte hittas.') # Felhantering ifall filen hittas inte

def ismorselength(string):
	'''
	Predikat som kontrollerar om ett tecken är en morselängd.
	Tar in en morsträng som ett argument.
	Retunerar Sant/Falskt om ett tecken är morselängd.
	Den returnerar en felmeddelande ifall det finns 3 nummer i rad i infilen.
	'''    
	three_char = string[0:3] 
	if three_char[0].isdigit() and three_char[1].isdigit() and three_char[2].isdigit():
		raise ValueError('\n \'{}\' från infilen är felaktig, kan inte ha 3 nummer i rad.'.format(three_char))
	elif three_char[2].isdigit():
		return False
	elif three_char[1].isdigit(): 
		return True
	else:
		return False
    
def findchar(string):
    '''
    Procedur som hittar alla tecken från en morsesträng.
    Tar in en morsträng som argument.
    Retunerar alla tecken som en lista.
    '''     
    characters = []
    for i in range(len(string) - 3):
        if ismorselength(string[i:i+3]):
            characters.append(string[i])
    return characters

def findmorse(string):
	'''
	Procedur som hittar alla morse från en morsesträng.
	Tar in en morsträng som argument.
	Retunerar alla morse som en lista.
	Returnerar felmeddelande i fall en morse i filen innehåller felaktig tecken.
	'''       
	characters = []
	allowed_morse = ['-', '.']
	for i in range(len(string) - 3):
		if ismorselength(string[i:i+3]):
			characters.append(string[i+2:i+2+int(string[i+1])])
	for e in characters:
		for i in range(len(e)):
			if e[i] in allowed_morse:
				continue
			else:
				raise ValueError('\n \'{}\' från infilen innehåller felaktig tecken.'.format(e))
	return characters

def morsedictionary(char_list, morse_list):
    '''
    Procedur som skapar en morselexikon.
    Tar in en morselista och en teckenlista som argument.
    Skapar ett morselexikon av listorna.
    '''       
    result = {}
    for i in range(len(char_list)):
        result[morse_list[i]] = char_list[i]
    return result

def chardictionary(char_list, morse_list):
    '''
    Procedur som skapar en teckenlexikon.
    Tar in en morselista och en teckenlista som argument.
    Skapar ett teckenlexikon av listorna.
    '''       
    result = {}
    for i in range(len(morse_list)):
        result[char_list[i]] = morse_list[i]
    return result

def upcase_first_letter(s):
	'''
	Procedur som kapitaliserar första tecken i en sträng.
	Detta procedure ändrar inte på resten av strängen.
	'''
	if len(s) == 1:
		return s[0].upper()
	else:
		return s[0].upper() + s[1:]

def capital_letter_fix(lst):
	'''
	Den splitrar på varje speciell tecken och utför funktionen upcase_first_letter.
	Tar in en lista som argument.
	Returnerar en bearbetad lista.
	'''
	result = [lst]
	for i in range(len(SPECIAL_CHARS)):
		temp_translation = ''.join(result[i]).split(SPECIAL_CHARS[i])
		temp_list = []
		for index in range(len(temp_translation)):
			if len(temp_translation[index]) > 0:
				temp_list.append(upcase_first_letter(temp_translation[index]))
			else:
				temp_list.append(temp_translation[index])	
		temp_list = SPECIAL_CHARS[i].join(temp_list)
		temp_list = [ch for ch in temp_list]
		result.append(temp_list)
	result = result[len(result) - 1]
	return result

def translate_to_morse(character):
    '''
    Överätter ett tecken till morse.
    Argumentet är ett tecken.
    Retunerar en morse enligt teckenlexikon.
    '''
    if character is ' ': # En mellanslag översättas som mellanslag
        return ' ' 
    else:
        character = character.upper()
        return CHAR_DICTIONARY[character] + ' '

def translate_to_char(morse):
    '''
    Överätter en morse till ett tecken.
    Argumentet är ett morse sträng.
    Retunerar ett tecken enligt morselexikon.
    '''
    if morse is '':
        return ' '   
    else:
        return MORSE_DICTIONARY[morse]
        

def translate_input(input_lst):
	'''
	Översätter indata lista till morse/tecken.
	Tar in en sträng som argument.
	Returnerar översätningen som en lista.
	'''
	translation_char = [] #Baslistan för översättning översättning från morse to tecken
	translation_morse =[] #Baslistan för  översättning översättning från tecken to morse
	Error_char = [] #Baslista för felmeddelande "översättning från morse to tecken"
	Error_morse = [] #Baslista för felmeddelande "översättning från tecken to morse"
	input_lst_char = input_lst.split(' ')[:]  
	# En lista kopia separerad med varje ord "morse" som ett element
	input_lst_morse = [ch for ch in input_lst][:]
	# En lista kopia separerad med varje tecken som ett element
	for i in range(len(input_lst_char)):
		try: # försöker översäta varje morse för sig och sen lägger till den till baslistan
			translation_char.append(translate_to_char(input_lst_char[i]).lower())
		except Exception: # Sparar fel för översättning försöket i fellistan "Error_char"
			Error_char.append("'{}'  är inte ett morsetecken.".format(input_lst_char[i]))
	for i in range(len(input_lst_morse)):
		try: # försöker översäta varje tecken för sig och sen lägger till den till baslistan
			translation_morse.append(translate_to_morse(input_lst_morse[i]))
		except Exception: # Sparar fel för översättning försöket i fellistan "Error_morse" 
			Error_morse.append("'{}' kan inte översättas till morse.".format(input_lst_morse[i]))
	if Error_char != [] and Error_morse != []:
		print('Fel: ') # Ifall båda försöket innehåller fel då skrivs ut felmeddelande
		for e in set(Error_char):
			print(e)
		for e in set(Error_morse):
			print(e)
	elif Error_char != [] and Error_morse == []:
		return translation_morse 
		# Ifall bara översätning från morse till tecken skapar felmeddelande
		# då skrivs ut översätning från tecken till morse och felmeddelandet skippas.
	else:
		# Ifall ingen felmeddelande finns
		# då skrivs ut översätning från morse till tecken och felmeddelandet skippas.
		return capital_letter_fix(translation_char)


if __name__ == "__main__":
	

	# Globala Variabler
	GLOBAL_FILE = readfile('morse.d')
	if GLOBAL_FILE != None:
		CHAR_LIST = findchar(GLOBAL_FILE)
		MORSE_LIST = findmorse(GLOBAL_FILE)
		MORSE_DICTIONARY = morsedictionary(CHAR_LIST, MORSE_LIST)
		CHAR_DICTIONARY = chardictionary(CHAR_LIST, MORSE_LIST)
	SPECIAL_CHARS = ['. ', '? ', '! ']

	#Kod för att köra programmet
	while GLOBAL_FILE != None:
		try:	
			print(mio.write_output(translate_input(mio.read_input())))
		except TypeError:
			pass
		except KeyboardInterrupt:
			print("Du valde att avsluta. Hej då!")
			break
		except EOFError:
			print("Du valde att avsluta. Hej då!")
			break