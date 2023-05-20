# Made by Joel
## CS 30
## RPG game


Enemy = 0
Spawn = 1
Escape = 2
Tile = 3
playermap = [[3, 0, 3, 0],
		    [2, 1, 3, 3],
		    [3, 0, 0, 3],
		    [0, 3, 0, 0]]


class Player(object):
	"""The player"""

	def __init__(self, name):
		self.name = name

	def movement(self):
		"""The player movement"""
		while True:
			print(room.userpos)
			movement = input("Use 'W', 'A', 'S', or 'D' to move around").lower()
			while True:
				if movement == 'w':
					x, y = (1, 0)
					break
				elif movement == 's':
					x, y = (-1, 0)
					break
				elif movement == 'a':
					x, y = (0, -1)
					break
				elif movement == 'd':
					x, y = (0, 1)
					break
				elif movement == 'something':
					try:
						print("You've found another one, why are you doing this?")
						break
					except:
						print("The doors are still closed to you, come back at a later time")
						with open("error.txt", "w") as file:
							file.write("You thought something was going to be here?")
				else:
					print("You can't go that way")
					break
			a = room.column + x
			b = room.row + y
			room.userpos = playermap[a][b]
			if room.userpos == 0:
				print("You've found an enemy")
			elif room.userpos == 1:
				print("Spawn Room")
			elif room.userpos == 2:
				print("You've successfuly escaped")
			elif room.userpos == 3:
				print("There's nothing of interest in this room")


class Room(object):

	def __init__(self, column, row):
		self.userpos = playermap[column][row]
		self.column = column  #Column/Row dictates player position in tilemap.
		self.row = row


Enemy = 0
Spawn = 1
Escape = 2
Tile = 3
playermap = [[3, 0, 3, 0],
		    [2, 1, 3, 3],
		    [3, 0, 0, 3],
		    [0, 3, 0, 0]]

room = Room( 0, 0)  #Player position for 'room' and 'Room' class
user = Player('Bryce')

def Map1():
	"""prints out the map to 'map.txt' """
	place = playermap
	with open("map.txt", "w") as file:
		file.write(f"{place}\n")

def main():  #Loads the rest of the program -- returns user position results.
	inp = input("Press any button to continue.: ")
	if inp != '':
		menu = input("")
		if menu == "Start":
			user.movement()
		elif menu == "Map":
			Map1()
			print("The map was printed to 'map.txt'\n")
		elif menu == "correct answer":
			print("Congratulations you found a something, can you find the other five")
		else:
			print("That's not the correct answer")

try:
	main()
except:
	with open("error.txt", "w") as file:
		file.write("Error\n")
else:
	with open("error.txt", "w") as file:
		file.write("No errors\n")