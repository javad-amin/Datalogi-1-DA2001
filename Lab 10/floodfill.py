from floodfill_test import *

def floodfill_dfs(new_color, pos, image):
	"""
	Colour the region in `image` contain containing `pos` 
	with `new_color`.
	"""
	picture = [ list(row) for row in image.split("\n") if row != "" ]
	num_rows = len(picture)
	num_cols = len(picture[0])
	r, c = pos
	old_color = picture[r][c]

	def is_inside(pos):
		"""True if `pos` is a position inside the picture,
		i.e. it is valid coordinates.
		"""
		row, col = pos
		return 0 <= row and row < num_rows and \
			0 <= col and col < num_cols
	
	directions = [(0,1), (0,-1), (1,0), (-1,0)]

	def add(pos, direction):
		"""Vector addition of `pos` with `direction`."""
		posx, posy = pos
		dirx, diry = direction
		return posx+dirx, posy+diry

	def get_image():
		"""Retrieve the image as a string."""
		return "\n".join("".join(row) for row in picture)

	def neighbours(pos):
		"""
		Retrieve a list of neigbours (visited or unvisited)
		of the position `pos`. All coordinates are valid.
		"""
		nbs = []
		for direction in directions:
			nb = add(pos, direction)
			if is_inside(nb):
				nbs.append(nb)
		return nbs

	
	def dfs(pos):
		"""
		Do a depth-first expansion of the node `pos`.
		"""
		if picture[pos[0]][pos[1]] == old_color:
			picture[pos[0]][pos[1]] = new_color
		for neighbour in neighbours(pos):
			if picture[neighbour[0]][neighbour[1]] != new_color:
				if picture[neighbour[0]][neighbour[1]] == old_color:
					dfs(neighbour)
		return picture

	dfs(pos)
	return get_image()


def test_dfs():
	print()
	print(floodfill_dfs("#", (2, 30), test_image))


##########################################
######### BFS solution ###################
##########################################

def floodfill_bfs(new_color, pos, image):
	"""
	Colour the region in `image` contain containing `pos` 
	with `new_color`.
	"""
	picture = [ list(row) for row in image.split("\n") if row != "" ]
	num_rows = len(picture)
	num_cols = len(picture[0])
	r, c = pos
	old_color = picture[r][c]

	def is_inside(pos):
		"""True if `pos` is a position inside the picture,
		i.e. it is valid coordinates.
		"""
		row, col = pos
		return 0 <= row and row < num_rows and \
			0 <= col and col < num_cols
	
	directions = [(0,1), (0,-1), (1,0), (-1,0)]

	def add(pos, direction):
		"""Vector addition of `pos` with `direction`."""
		posx, posy = pos
		dirx, diry = direction
		return posx+dirx, posy+diry

	def get_image():
		"""Retrieve the image as a string."""
		return "\n".join("".join(row) for row in picture)

	def neighbours(pos):
		"""
		Retrieve a list of neigbours (visited or unvisited)
		of the position `pos`. All coordinates are valid.
		"""
		nbs = []
		for direction in directions:
			nb = add(pos, direction)
			if is_inside(nb):
				nbs.append(nb)
		return nbs

	
	def bfs():
		"""
		Do a breadth-first expansion from the start position.
		"""
		Q = []
		picture[pos[0]][pos[1]] = new_color
		Q.append(pos)
		while len(Q) > 0:
			e = Q.pop(0)
			for neighbour in neighbours(e):
				if picture[neighbour[0]][neighbour[1]] == old_color:
					picture[neighbour[0]][neighbour[1]] = new_color
					Q.append(neighbour)
		return picture
	
	bfs()
	return get_image()


def test_bfs():
	print()
	print(floodfill_bfs("#", (2, 30), test_image))

if __name__ == "__main__":
	test_dfs()
	test_bfs()
