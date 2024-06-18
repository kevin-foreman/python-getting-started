# Rock, Paper, Scissors Game (never-ending fun!)

from random import randint

# Moves
moves = ["rock", "paper", "scissors"]

# Loop
while True:
    computer = moves[randint(0, 2)]
    