import random

a = ["Rock","Paper","Scissor"]

comp = random.choice(a)

def rock_paper():
    user = input(": ")
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

rock_paper()

