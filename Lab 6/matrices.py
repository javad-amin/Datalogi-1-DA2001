

"""
`matrix.py` - matrisfunktioner.
"""
# from gauss import gauss_elim



def deep_copy(matrix):
	"""
	Retuns a deep copy of a matrix
	Matrix has to be inputed as a list with m elements/rows
	and n element in each of the m elements /columns
	"""
	result= []
	for el in matrix:
		if isinstance(el,list):
			result.append(deep_copy(el))
		else:
			result.append(el)
	return result


def identity(n):
	"""
	Återsänd en n*n-identitetsmatris.
	(En identitetsmatris har 1:or på diagonalen,
	och övriga element är 0.)
	"""
	pass

def inverse(A):
	"""
	Återsänd matrisinversen av A.
	(A måste vara kvadratisk).
	"""
	n = len(A)
	B = identity(n)
	inv = gauss_elim(A, B)
	return inv

def vandermonde(xs):
	"""
	`xs` är en kolumnvektor (n*1-matris).
	Återsänd en Vandermonde-matris skapad från `xs`.
	D.v.s. för varje `x` i `xs` finns en rad
	[ 1, x, x**2, ..., x**(n-1) ]
	där `n` är längden av `xs`.
	"""
	pass


def interpolate(xs, ys):
	"""
	`xs` och `ys` är kolumnvektorer (n*1-matriser).
	De representerar koordinater för punkter i planet.
	Återsänd koefficienterna `cs` (som en kolumnvektor)
	för polynomet av grad n-1 som passerar genom punkterna.
	Alla x-koordinater måste vara unika,
	annars ges felet SingularMatrix.
	"""
	v = vandermonde(xs)
	coeffs = gauss_elim(v, ys)
	return coeffs


	
	"""
	A function which changes the first element of the second 
	column of a given matrix to 42
	"""
def another_evil_function(mtx):
	mtx[0][1] = 42
	"""
	A function which is only included in the main file 
	with the purpose of testing the codes
	"""
def main_function():
	my_matrix = [ [ 1, 2, 3 ],
				[ 4, 5, 6 ] ]
	cpy = deep_copy(my_matrix)

	another_evil_function(cpy)
	print(my_matrix) 
	# prints [[1, 2, 3],[4, 5, 6]]

	another_evil_function(my_matrix)
	print(my_matrix) 
	# prints [[1, 42, 3],[4, 5, 6]]

if __name__ == "__main__":
	main_function()