from tree import BinaryTree

OPERATORS = ['+', '-', '*', '/']

def parse_postfix(string):
	def inner(lst):
		if lst[0] in OPERATORS:
			op2, rest = inner(lst[1:])
			assert len(rest) > 0
			op1, skip = inner(rest)
			bt = BinaryTree(lst[0])
			bt.set_left(op1)
			bt.set_right(op2)
			return bt, skip
		else:
			bt = BinaryTree(lst[0])
			return bt, lst[1:]
	tree, empty = inner(string[::-1].split(" "))
	assert empty == []
	return tree


def scheme_syntax(tree):
	"""
	Return a string representation of the syntax tree `tree` 
	in prefix notation and with parentheses,
	like Scheme-notation.
	"""
	result = tree.get_value()
	if result in OPERATORS:
		result = '(' + result
	if tree.has_left() == True:
		result += ' ' + scheme_syntax(tree.get_left())
	if tree.has_right() == True:
		result += ' ' + scheme_syntax(tree.get_right()) + ')'
	return result

def infix_syntax(tree):
	"""
	Return a string representation of the syntax tree `tree` 
	in infix notation and with parentheses,
	like mathematical notation with many parentheses.
	"""
	result = tree.get_value()
	if tree.has_left() == True:
		result = '(' + infix_syntax(tree.get_left()) + ' ' + result + ' '
	if tree.has_right() == True:
		result = result + infix_syntax(tree.get_right()) + ')'
	return  result

def test():
	print(scheme_syntax(parse_postfix("3 2 +")))
	print(scheme_syntax(parse_postfix("3 2 + 7 -")))
	
	print(infix_syntax(parse_postfix("3 2 +")))
	print(infix_syntax(parse_postfix("3 2 + 7 -")))

if __name__ == "__main__":
	test()