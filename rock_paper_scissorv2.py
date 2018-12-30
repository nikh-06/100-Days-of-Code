from random import randint

# For the points of computer and player. Making a initial variable if player wins adding 1 to existing value 
score_player = 0 
score_computer = 0 
while True:
	password = input("Please Enter the password ?")
	if password == "nikh":
		
		print("You can now play game")

		# Maximum score one needs(player or computer) to win ie min value of score_player or score_computer to terminate the game 
		
		player_name = input("Please Enter your name ?")
		
		while True:

			# Defining Computer its move 

			number = randint(1,3)
			if number == 1 :
				computer_move = "rock"
			elif number == 2 :
				computer_move = "paper"
			else:
				computer_move = "scissor"

			# Logic of the game 

			if computer_move == "rock":
				player_move = input("Please Enter Your Move : ")
				
				if player_move == "scissor":
					print("Computer wins")
					score_computer += 1 
				
				elif player_move == "paper":
					print(f"{player_name} wins")
					score_player += 1 

				else:
					print("There is a Tie")

			
			elif computer_move == "paper":
				
				player_move = input("Please Enter Your Move : ")
				
				if player_move == "rock":
					print("Computer wins")
					score_computer += 1 

				elif player_move == "scissor":
					print(f"{player_name} wins")
					score_player += 1

				else:
					print("There is a Tie")

			
			else:

				player_move = input("Please Enter Your Move : ") 
				
				if player_move == "rock":
					print(f"{player_name} wins")
					score_player += 1

				elif player_move == "paper":
					print("Computer wins")
					score_computer += 1 

				else:
					print("There is a Tie")

			
			print(f" Computer :  {score_computer}  {player_name}  :  {score_player} ")		
			
			if score_player == 3 :
				print("PLAYER WINS")
				again = input(f"Do You Want to play again {player_name} ? (y/n)")
				if again == "y":
					# reseting player scores to zero 
					score_player = 0 
					score_computer = 0 
					continue
				else:
					print(f"Thanks for Playing {player_name} ")
					break
			
			elif score_computer == 3 :
				print("COMPUTER WINS")
				again = input("Do You Want to play again ? (y/n)")
				if again == "y":
					score_computer = 0 
					score_player = 0 
					# continue can be used kia jaa sakta he......... # loop se jub tuk exit nahi honge tub tuk ki break command na aajaaye 
				else:
					print("Thanks for Playing")
					break
			
			else: 	
				continue
	else:
		continue








