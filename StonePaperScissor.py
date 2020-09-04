import random

comp_list = ["Rock","Paper","Scissor"]

while True:
	#creating input and initializing
	user = input("Please choose an option :").lower().capitalize()
	if user not in comp_list:
		print("Invalid input ,please try again ")
		continue
	comp = random.choice(comp_list)
	print(f"You choose {user}")
	print(f"Computer choose {comp}")
	#main program
	if user == "Rock" and comp == "Paper":
		print("Comp wins")
	elif user == "Rock" and comp == "Scissor":
		print("User wins")
	elif user == "Rock" and comp == "Rock":
		print("Draw")
	elif user == "Paper" and comp == "Paper":
		print("Draw")   
	elif user == "Paper" and comp == "Scissor":
		print("Comp wins")
	elif user == "Paper" and comp == "Rock":
		print("User wins")
	elif user == "Scissor" and comp == "Paper":
		print("User wins")
	elif user == "Scissor" and comp == "Scissor":
		print("Draw")
	elif user == "Scissor" and comp == "Rock":
		print("Comp wins")
	print("\n")
	replay = input("Want to play again ? (y/n)")
	if "y" in replay:
		continue
	else:
		print("\n")
		print("Thanks for playing !")
		exit()	
   