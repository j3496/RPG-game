# Made by Joel
## CS 30
## RPG game

import time

x = 0
y = 0

Enemy = 0
Spawn = 1
Escape = 2
Tile = 3
map = [[3, 0, 3, 0],
	   [2, 1, 3, 3],
	   [3, 0, 0, 3],
       [0, 3, 0, 0]]

playermap = [
 "Tile", "Enemy", "Tile", "Enemy", "Escape", "Spawn", "Tile", "Tile", "Tile",
 "Enemy", "Enemy", "Tile", "Enemy", "Tile", "Enemy", "Enemy"
]

class Player(object):
	"""The player"""

	def __init__(self, name):
		"""Initates the code"""
		self.name = name

	def movement(self):
		"""The player movement"""
		while True:
			movement = input("Use 'W', 'A', 'S', or 'D' to move around ").lower()
			while True:
				global x
				global y
				if movement == 'w':
					y += 1
					print("You moved forward ")
					break
				elif movement == 's':
					y -= 1
					print("You moved backwords ")
					break
				elif movement == 'a':
					x -= 1
					print("You moved left ")
					break
				elif movement == 'd':
					x += 1
					print("You moved right ")
					break
				elif movement == 'something':
					try:
						print("You've found another one, why are you doing this? ")
						break
					except:
						print("The doors are still closed to you, come back at a later time")
						with open("error.txt", "w") as file:
							file.write("You thought something was going to be here?")
					else:
						print("Why")
				else:
					print("You can't go that way")
					break
			a = room.x + x
			b = room.y + y
			room.userpos = map[a][b]
			if room.userpos == 0:
				# Description an function for the 'enemy' tile
				print("You've found an enemy ")
			elif room.userpos == 1:
				# Description for the 'spawn room'
				print("Spawn Room ")
			elif room.userpos == 2:
				# Description and function for the 'escape' tile
				print("You've successfuly escaped ")
				time.sleep(31536000)
			elif room.userpos == 3:
				# Description for the 'room' tile
				print("There's nothing of interest in this room ")


class Room(object):
	"""tracks the players position"""

	def __init__(self, x=4, y=4):
		self.userpos = map[x][y]
		self.x = x
		self.y = y


room = Room( 0, 0)
# Player position for 'room' and 'Room' class
user = Player('P1')
# Defines the user as a player


def Map1():
	"""prints out the map to 'map.txt'"""
	place = playermap
	with open("map.txt", "w") as file:
		file.write(f"{place}\n")


def main():
	# Loads the rest of the program -- returns user position results.
	inp = input("Press any button to continue.: ")
	if inp != '':
		menu = input("input 'Start' to start the game \n'Map' to print map to 'map.txt' \n")
		if menu == "Start":
			user.movement()
		elif menu == "Map":
			Map1()
			print("The map was printed to 'map.txt' \n")
		elif menu == "correct answer":
			print("Congratulations you found a something, can you find the other five ")
		else:
			print("That's not the correct answer ")


try:
	# Checks the "main" function for errors
	main()
except:
	# Prints out that there was an error to "error.txt", if there's an error
	with open("error.txt", "w") as file:
		file.write("Error\n")
else:
	# Prints that there were no errors to "error.txt", if there's no errors
	with open("error.txt", "w") as file:
		file.write("No errors\n")
