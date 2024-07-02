# Rock, Paper, Scissors Game (never-ending fun!)

from random import randint

# Moves
moves = ["rock", "paper", "scissors"]

# Loop
while True:
    computer = moves[randint(0,2)]
    player = input("rock, paper, or scissors? (or end the game) ").lower()
    if player == "end the game":
        print("The game has ended.")
        break
    # if player selection matches
    elif player == computer:
        print("Tie!")
    # if player selection is Rock, win, lose, or tie    
    elif player == "rock":
        if computer == "paper":
            print("You lose!", computer, "beats", player)
        else:
            print("You win!", player, "beats", computer)
    # if player selection is Paper, win, lose, or tie        
    elif player == "paper":
        if computer == "scissors":
            print("You lose!", computer, "beats", player)
        else:
            print("You win!", player, "beats", computer)