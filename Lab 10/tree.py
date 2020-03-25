class Tree:
	"""
	A datatype for representing trees.
	"""
	def __init__(self, value : str):
		"""
		Constructor:
		Tree(value) -> new tree with no children
		Argument `value` must be a string.
		"""
		self.__value = value
		self.__children = []

	def get_value(self):
		"""
		Retrieve the value of this node.
		"""
		return self.__value

	def add_child(self, c : "Tree"):
		"""
		Add `c` as a child to this node.
		"""
		self.__children.insert((self.num_children()), c)

	def get_child(self, idx : int):
		"""
		Retrieve child number `idx`.
		Children are numbered in the order they were added.
		Indexing starts with 0, i.e.
		0 <= idx < self.num_children()
		"""
		return self.__children[idx]

	def num_children(self):
		"""
		Returns the number of children of this node.
		"""
		return len(self.__children)
			
class BinaryTree:
	def __init__(self, value : str):
		"""
		Constructor:
		Tree(value) -> new tree with no children (no left and right subtree).
		Argument `value` must be a string.
		"""
		self.__value = value
		self.__left = None
		self.__right = None

	def get_value(self):        
		"""
		Retrieve the value of this node.
		"""
		return self.__value
		
	def set_left(self, child : "BinaryTree"):
		"""
		Set the left subtree to `child` (must be a BinaryTree).
		"""
		if self.__left == None:
			self.__left = child
		else:
			print('There is already a node in the left side.')

	def set_right(self, child : "BinaryTree"):
		"""
		Set the right subtree to `child` (must be a BinaryTree).
		"""
		if self.__right == None:
			self.__right = child
		else:
			print('There is already a node in the right side.')

	def get_left(self):
		"""
		Retrieve the left subtree of this node.
		"""    
		return self.__left

	def get_right(self):
		"""
		Retrieve the right subtree of this node.
		"""
		return self.__right

	def has_left(self):
		"""
		Returns `True` if this node has a left child/subtree, `False` otherwise.
		"""
		return self.__left != None

	def has_right(self):
		"""
		Returns `True` if this node has a left child/subtree, `False` otherwise.
		"""
		return self.__right != None

		