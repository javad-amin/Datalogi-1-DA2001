import morse as m


def translate_to_morse(character):
    '''
    Överätter ett tecken till morse.
    Argumentet är ett tecken.
    Retunerar en morse enligt teckenlexikon.
    '''
    if character is ' ':
        return ' ' 
    else:
        character = character.upper()
        return m.char_dictionary[character] + ' '

def translate_to_char(morse):
    '''
    Överätter en morse till ett tecken.
    Argumentet är ett morse sträng.
    Retunerar ett tecken enligt morselexikon.
    '''
    if morse is '':
        return ' '   
    else:
        return m.morse_dictionary[morse]
        

def translate_input(input_lst):
	'''
	Översätter indata lista till morse/tecken.
	Tar in en sträng som argument.
	Returnerar översätningen som en lista.
	'''
	translation_char = []
	translation_morse =[]
	Error_char = []
	Error_morse = []
	input_lst_char = input_lst.split(' ')[:]
	input_lst_morse = [ch for ch in input_lst][:]
	for i in range(len(input_lst_char)):
		try:
			translation_char.append(translate_to_char(input_lst_char[i]).lower())
		except Exception: 
			Error_char.append("'{}'  är inte ett morsetecken.".format(input_lst_char[i]))
	for i in range(len(input_lst_morse)):
		try:
			translation_morse.append(translate_to_morse(input_lst_morse[i]))
		except Exception: 
			Error_morse.append("'{}' kan inte översättas till morse.".format(input_lst_morse[i]))
	if Error_char != [] and Error_morse != []:
		print('Fel: ')
		for e in set(Error_char):
			print(e)
		for e in set(Error_morse):
			print(e)
	elif Error_char != [] and Error_morse == []:
		return translation_morse
	else:
		result = [translation_char]
		for i in range(len(m.special_charachter)):
			temp_translation = ''.join(result[i]).split(m.special_charachter[i])
			temp_list = []
			for index in range(len(temp_translation)):
				if len(temp_translation[index]) > 0:
					temp_list.append(m.upcase_first_letter(temp_translation[index]))
				else:
					temp_list.append(temp_translation[index])	
			temp_list = m.special_charachter[i].join(temp_list)
			temp_list = [ch for ch in temp_list]
			result.append(temp_list)
		result = result[len(result) - 1]
		return result
		