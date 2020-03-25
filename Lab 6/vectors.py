

"""
`vectors.py` - funktioner för vanliga vektoroperationer.
Användbara för t.ex. Gauss-eliminering.
"""



def add_vectors(v1, v2):
	"""Addera vektorerna v1 och v2.
	Ändrar inte på v1 och v2."""
	result= [el1 + el2 for el1, el2 in zip(v1,v2)]
	return result

	
def subtract_vectors(v1, v2):
	"""Subtrahera vektorerna v1 och v2.
	Ändrar inte på v1 och v2."""
	result= [el1 - el2 for el1, el2 in zip(v1,v2)]
	return result


	
def multiply_vector_by(v, scalar):
	"""Multiplicera vektorn `v` med skalären `scalar`.
	Ändrar inte på v."""
	result = [el*scalar for el in v]
	return result
	
def divide_vector_by(v, scalar):
	"""Dividera vektorn `v` med skalären `scalar`.
	Ändrar inte på v."""
	result = [el/scalar for el in v]
	return result

	"""
	A function which is only included in the main file 
	with the purpose of testing the codes
	"""
def tests_function():
	v1 = [ 1, 2, 3 ]
	v2 = [ 1, 1, 1 ]
	print("add_vectors(v1, v2) , expeced result [2, 3, 4]")
	print(add_vectors(v1, v2))
	print("subtract_vectors(v1, v2) , expeced result [0, 1, 2]")
	print(subtract_vectors(v1, v2))
	print("multiply_vector_by(v1, v3) , expeced result [3, 6, 9]")
	print(multiply_vector_by(v1, 3))
	print("subtract_vectors(v12 2) , expeced result [0.5, 0.5, 0.5]")
	print(divide_vector_by(v2, 2))
	
if __name__ == "__main__":
	tests_function()