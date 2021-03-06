import item

width = 10
height = 10

class Coord():
	def __init__(self, in_coord, item=None):
		self.coord = in_coord
		self.has = item

	def __str__(self):
		return str(self.coord)

	def __repr__(self):
		return str(self.has)

	def place(self, in_item):
		self.has = in_item

class Room():
	def __init__(self, characters, width, height):
		self.characters = characters
		self.coord_dict = {}
		self.width = width
		self.height = height
		
		# Fill the room with coordinates that have no item
		for i in range(height):
			for j in range(width):
				self.coord_dict[(i, j)] = Coord((i, j))

		# Make a single sample box at 1 down, 5 right
		single_box = item.Item('box', '☐')
		self.coord_dict[(1, 5)].place(single_box)
	
	def __repr__(self):
		# FIX THIS REPR
		# room = (' '*10 + '\n') * 10 + ''.join([str(character.location) + '\n' for character in self.characters])

		board = []  # start with an empty list
		for i in range(height):  # loop over the rows
			board.append([])  # append an empty row
			for j in range(width):  # loop over the columns
				board[i].append(' ') 
		
		# print out the board
		for i in range(height):
			for j in range(width):
				# if we're at the player location, print the player icon
				if i == self.width and j == self.height:
					print('👵', end=' ')
				else:
					print(board[self.width][self.height], end=' ')  # otherwise print the board square
			print()

