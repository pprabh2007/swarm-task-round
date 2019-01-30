class Node:

	def __init__ (self, parent=None, position=None):
		
		self.parent = parent
		self.position = position
		self.g = 0
		self.h = 0
		self.f = 0

	def __eq__(self, other):
		return self.position==other.position

def isValid(position):
	return position[0]>=0 and position[1]>=0 and position[0]<10 and position[1]<10

def isBlocked(grid, position):
	return grid[position[0]][position[1]] == 1

def isDestination(point, dest):
	return point.position == dest.position

def checkMove(first, second):
	if first is not None:
		x = second.position[0]-first.position[0]
		y = second.position[1]-first.position[1]
		if [x,y] == [-1,-1]:
			return 1
		if [x,y] == [-1,0]:
			return 2
		if [x,y] == [-1,1]:
			return 3
		if [x,y] == [0,1]:
			return 4
		if [x,y] == [1,1]:
			return 5
		if [x,y] == [1,0]:
			return 6
		if [x,y] == [1,-1]:
			return 7
		if [x,y] == [0,-1]:
			return 8

def aStarSearch(grid, start, dest):

	open_list = []
	closed_list = []

	start_node = Node(None, start)
	dest_node = Node(None, dest)

	start_node.g=start_node.h=start_node.g = 0
	dest_node.g=dest_node.h=dest_node.g = 0

	open_list.append(start_node)

	while len(open_list)>0:

		current_node = open_list[0]
		current_node_index = 0

		for index, node in enumerate (open_list):
			if node.f < current_node.f:
				current_node = node
				current_node_index = index

		open_list.pop(current_node_index)
		closed_list.append(current_node)

		#Destination is here!
		if current_node == dest_node:
			path = []
			moves = []
			temp = current_node

			while temp is not None:
				path.append(temp.position)
				moves.append(checkMove(temp.parent, temp))
				temp = temp.parent
			moves.pop(-1)

			return [path[::-1], moves[::-1]]


		children = []

		for new_position in [(-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1)]:

			new_node_position = (current_node.position[0]+new_position[0], current_node.position[1]+new_position[1])

			if not isValid(new_node_position):
				continue
			if isBlocked(grid, new_node_position):
				continue

			new_node = Node(current_node, new_node_position)
			children.append(new_node)

		for child in children:

			for present in closed_list:
				if present==child:
					continue

			child.g = current_node.g + 1
			child.h = ((child.position[0] - dest_node.position[0]) ** 2) + ((child.position[1] - dest_node.position[1]) ** 2)
			child.f = child.g + child.h

			for present in open_list:
				if child==present and child.f>present.f:
					continue

			open_list.append(child)

def generateGrid(obstacle_pos):
	grid = [[0 for j in range(10)] for i in range(10)]
	for obstacle in obstacle_pos:
		row_min = min(obstacle[0][0], obstacle[1][0])
		col_min = min(obstacle[0][1], obstacle[1][1])
		row_max = max(obstacle[0][0], obstacle[1][0])
		col_max = max(obstacle[0][1], obstacle[1][1])
		for row in range(row_min, row_max+1):
			for col in range(col_min, col_max+1):
				grid[row][col] = 1

	return grid

def main():
	
	obstacle_pos = [ [[1,1],[3,3]], [[4,4],[8,8]] ]
	grid = generateGrid(obstacle_pos)

	for i in range(10):
		for j in range(10):
			print(str(grid[i][j]), end=" ")
		print("")

	start = (0,0)
	dest = (9,9)    

	solution = aStarSearch(grid, start, dest)
	print(solution)

if __name__ == '__main__':
    main()