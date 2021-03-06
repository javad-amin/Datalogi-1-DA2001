from tree import Tree

def print_filetree(tree):
	"""
	Print the filetree `tree` in prefix order.
	Prepend the file/directory name with N spaces, and "|-",
	where N is the level of the file in the file tree.
	"""
	def inner(tree, num_spaces):
		"""
		Print the filetree `filetree`. The current level should use
		`num_spaces` many spaces.
		Do a preorder traversal.
		"""
		print(" "*num_spaces, end="")
		print('|-{}'.format(tree.get_value()))
		for i in range(tree.num_children()):
			inner(tree.get_child(i), num_spaces + 1)
	
	inner(tree, 0)

def example_tree():
	ft = Tree("/")
	for directory in ["bin", "boot", "dev", "etc", "home", "proc"]:
		t = Tree(directory)
		ft.add_child(t)
		if directory == "home":
			for user in ["pelle", "stina", "tjorven"]:
				u = Tree(user)
				t.add_child(u)
				if user == "tjorven":
					d = Tree("sudata")
					u.add_child(d)
					for labb in range(3,8):
						d.add_child(Tree("labb{}".format(labb)))
	return ft

def test():
	ft = example_tree()
	print()                    
	print_filetree(ft)

if __name__ == "__main__":
	test()