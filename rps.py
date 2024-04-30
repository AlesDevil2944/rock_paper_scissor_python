"""
import random

x = random.randint(1, 10)

print(x)
"""
"""
import random 

print("Welcome to Rock, Paper, Scissors")
 
play = ["rock", "paper", "scissor"]

computer = play[random.randint(1,3)] 
 
player = False

while player == False: 
    player = input("Choose your rock, paper, scissor?: ") 
    if player == computer: 
        print("draw!") 
    elif player == "rock": 
        if computer == "paper": 
            print("You lose!", computer, "covers", player) 
        else: 
            print("You win!", player, "smashes", computer) 
    elif player == "paper": 
        if computer == "scissor": 
            print("You lose!", computer, "cuts", player) 
        else: 
            print("You win!", player, "covers", computer) 
    elif player == "scissor": 
        if computer == "rock": 
            print("You lose...", computer, "smashes", player) 
        else: 
            print("You win!", player, "cuts", computer) 
    else: 
        print("That's not a valid play. Check the spelling!") 
    player = False 
    computer = play[random.randint(1,3)]
"""

import random
"""
user at start will have 3 lifes
everytime user loose a game life get removed
if lifes becomes zero then game will be cover



"""
print("Welcome to Rock, Paper, Scissors")

lives = 3
user_score = 0
comp_score = 0

while lives > 0:

    user = int(input("Enter following choice\n1 : Rock\n2 : Paper\n3 : Scissors\n"))
    comp = random.randint(1, 3)

    if user == 1:

        if comp == 1:
            print("Draw")
        elif comp == 2:
            print("Comp Wins")
            lives -= 1
            comp_score += 1
        elif comp == 3:
            print("User Wins")
            user_score += 1
            
    elif user == 2:

        if comp == 1:
            print("Comp Wins")
            user_score += 1
        elif comp == 2:
            print("Draw")
        elif comp == 3:
            print("Comp Wins")
            lives -= 1
            comp_score += 1
            
    elif user == 3:

        if comp == 1:
            print("Comp Wins")
            lives  -= 1
            comp_score += 1
        elif comp == 2:
            print("User Wins")
            user_score += 1
        elif comp == 3:
            print("Draw")
            
    print("user_score : ", user_score,)
    print("comp_score : ", comp_score)
    
    print("Game Over")

    if comp_score > user_score:
        print("comp_wins!")
    else:
        print("user wins")

  