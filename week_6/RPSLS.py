"""
Write a program that plays Rock, Paper, Scissors, Lizard, Spock.

Rules of the game:
- rock blunts scissors and crushes lizard
- paper covers rock and disproves Spock
- scissors cuts paper and decapitates lizard
- lizard eats paper and poisons Spock
- Spock vaporizes rock and smashes scissors

Your program should:
- Take in user input for their move
- Check if the input is valid
- Generate a random move for the computer
- Determine who won the round
- Output the winner
- Bonus: Keep the game going until the user quits

All the needed packages are imported for you.

@author: Alexandra DeLucia
"""
from random import randint

# Define the rules of the game
instructions_string = """
    Welcome to Rock, Paper, Scissors, Lizard, Spock! 
    Rules of the game:
    - rock blunts scissors and crushes lizard
    - paper covers rock and disproves Spock
    - scissors cuts paper and decapitates lizard
    - lizard eats paper and poisons Spock
    - Spock vaporizes rock and smashes scissors
    
    Possible moves are rock, paper, scissors, lizard, and Spock.
    """


# Define any functions you need here



# Separate our main from the rest of the file
# All the main logic will go here
if __name__ == "__main__":
    # 1. Print the rules of the game
    print(instructions_string)
