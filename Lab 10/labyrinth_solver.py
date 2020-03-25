from labyrinth_test import *


BLOCKED = "#"
VISITED = "."

##########################################
######### DFS solution ###################
##########################################


def dfs_solve(string):
	labyrinth = [ list(row) for row in string.split("\n") if row != "" ]
	num_rows = len(labyrinth)
	num_cols = len(labyrinth[0])

	def is_inside(pos):
		"""True if `pos` is a position inside the picture,
		i.e. it is valid coordinates.
		"""
		row, col = pos
		return 0 <= row and row < num_rows and \
			0 <= col and col < num_cols
	directions = [(0,-1), (0,1), (1,0), (-1,0)]

	def add(pos, direction):
		"""Vector addition of `pos` with `direction`."""
		posx, posy = pos
		dirx, diry = direction
		return posx+dirx, posy+diry

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

	def get_image():
		"""
		Retrieve the labyrinth as a string (input format).
		Can be used for debugging.
		"""
		return "\n".join("".join(row) for row in picture)

	GOAL = (num_rows-1, num_cols-1)
	
	def inner(pos, camefrom):
		"""
		Do a depth-first expansion of the node `pos`.
		"""
		labyrinth[pos[0]][pos[1]] = VISITED
		if pos == GOAL:
			return [pos], True
		for neighbour in neighbours(pos):
			if neighbour != camefrom and is_inside(neighbour):
				if labyrinth[neighbour[0]][neighbour[1]] != BLOCKED and labyrinth[neighbour[0]][neighbour[1]] != VISITED:
					way, success = inner(neighbour, pos)
					if success == True:
						return [pos]+way, True
		return None, False
	
	way, success = inner((0,0), None)
	return way



##########################################
######### Tests ##########################
##########################################


def draw_path(string, way):
	labyrinth = [ list(row) for row in string.split("\n") if row != "" ]
	for row, col in way:
		labyrinth[row][col] = "x"
	return "\n".join("".join(row) for row in labyrinth)


def do_dfs_test(labyrinth):
	print()
	way = dfs_solve(labyrinth)
	print(draw_path(labyrinth, way))
	

def dfs_test():
	do_dfs_test(labyrinth_small)
	do_dfs_test(labyrinth_small2)

def dfs_test_cycles():
	do_dfs_test(labyrinth_small)
	do_dfs_test(labyrinth_small2)
	do_dfs_test(labyrinth_small3)

if __name__ == "__main__":
	print(dfs_solve(labyrinth_small_3))
