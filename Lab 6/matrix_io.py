

"""
`matrix_io.py` - Inmatning och utskrift av matris. 
Funktioner för läsning av matris från stdin (standard input)
och utskrift till stdout (standard output).
Med följande textformat för matriser:

m n
e e e e e e e
e e e e e e e
e e e e e e e

"""

def read_matrix():
	"""
	Läser in en matris från stdin.
	Först mattar man in m som radvektors längd och sedan n som radvrktors längd
	Sedan mattar man in varje radvektor en gång för sig
	"""
	mstr, nstr = input().split()
	m = int(mstr)
	n = int(nstr)
	matris = []
	for rad_idx in range(m):
		rad_med_tal = input().split() 
		rad_med_tal_formatted = []
		for el in rad_med_tal:
			rad_med_tal_formatted.append(format(float(el), ".2f"))
		matris.append(rad_med_tal_formatted)
	return matris

def write_matrix(matris):
	"""Skriver matrisen till stdout."""
	m, n = len(matris), len(matris[0])
	print(m, n)
	for rad_idx in range(m):
		tal_i_denna_rad = matris[rad_idx]
		print(" ".join(tal_i_denna_rad))

	"""
	A function which is only included in the main file 
	with the purpose of testing the codes
	"""
def tests_function():
	write_matrix(read_matrix())
	
if __name__ == "__main__":
	tests_function()

