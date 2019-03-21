#DICE GAME CREATED A PROCEDURAL PARADIGM
# = + |

import random
#Games Variables
max_score = 20
dice_values = [1,2,3,4,5,6]

player_one_score = 0
player_two_score = 0
active_player = "player1"

while player_one_score < max_score and player_two_score < max_score:
	user_press = input("Press R: ")
	dice_value = random.choice(dice_values)
	if user_press == "r" or user_press == "R":
		if active_player == "player1":
			player_one_score += dice_value
			active_player = "player2"
			print(f"PLAYER ONE ROLLING DICE. DICE VALUE: {dice_value}")
		else:
			player_two_score += dice_value
			active_player = "player1"
			print(f"PLAYER TWO ROLLING DICE. DICE VALUE: {dice_value}")
	else:
		print("Press the right key")

	if player_one_score > max_score or player_two_score > max_score:
		print(f" Player one scored: {player_one_score} points.... Player two scored: {player_two_score} points")
		user_response = input("Do You want to play again? (Y/N) ")
		if user_response == "y" or user_response == "Y":
			player_one_score = 0
			player_two_score = 0
		else user_response == "n" or user_response == "N":
			print(f"Game Over... Thanks")
		# else:
		# 	print("Invalid Key Selected")
		# 	user_response = input("Do You want to play again? (Y/N) ")

