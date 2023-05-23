# Made by Joel
## CS 30
## RPG game

import time
import Inventory


class fighting():

	def __init__(self):
		print("")

	def Enemy(self):
		"""fighting an enemy"""
		try:
			player_hp = 24
			enemy_hp = 25
			while (player_hp >= 1):
				while (enemy_hp >= 1):
					atk = input(" Attacks: \n Slash \n Kick \n Stomp \n Run \n")
					if atk == "Slash":
						# Slash attack on the enemy
						enemy_hp -= 5
						print("Your attack did 5 damage")
						print("Enemy health: " + str(enemy_hp))
						player_hp -= 5
						print("You got Slashed for 5 damage")
						print("Player health: " + str(player_hp))
					elif atk == "Run":
						# Try to run away
						time.sleep(2)
						print("You couldn't get away")
						print("You Died")
						time.sleep(86400)
					elif atk == "yeet":
						enemy_hp -= 5000
					elif atk == "Kick":
						# Kick attack on the enemy
						enemy_hp -= 6
						print("Your attack did 6 damage")
						print("Enemy health: " + str(enemy_hp))
						player_hp -= 6
						print("You got Kicked for 6 damage")
						print("Player health: " + str(player_hp))
					elif atk == "Stomp":
						# Stomp attack on the enemy
						enemy_hp -= 3
						print("Your attack did 3 damage")
						print("Enemy health: " + str(enemy_hp))
						player_hp -= 3
						print("You got Stomped for 3 damage")
						print("Player health: " + str(player_hp))
					else:
						print("Your attack failed")
				if player_hp <= 0:
					# The player dies
					print("You Died")
					time.sleep(86400)
				elif enemy_hp <= 0:
					# The enemy dies
					print("You've killed the enemy \nYou got a object")
					input("press enter to continue")
					Inventory.pick()
					return
		except:
			# tells you there's an error
			print("There was an error running the 'enemy' code")
		else:
			print("\n \n")
		finally:
			# prints the inventory and that the file worked to "enemys.txt"
			with open("enemys.txt", "w") as file:
				file.write("The enemy file worked\n")
			with open("enemys.txt", "a") as file:
				file.write(f"{Inventory.Inv()}\n")
