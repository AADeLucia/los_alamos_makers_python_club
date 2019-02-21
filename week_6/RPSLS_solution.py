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


# Define the possible moves for the game
possible_moves = ["rock", "paper", "scissors", "lizard", "spock"]
computer_move = {0: "rock", 1: "paper", 2: "scissors", 3: "lizard", 4: "spock"}
# Define the winning moves for each move
# move : [list moves the move beats]
winning_moves = {"rock": ["scissors", "lizard"], "paper": ["rock", "spock"], "scissors": ["paper", "lizard"], "lizard": ["paper", "spock"], "spock": ["rock", "scissors"]}

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


def get_computer_move():
    """
    Generates a random move for the computer
    
    string : computer move
        One of: rock, paper, scissors, lizard, spock
    """
    return computer_move[randint(0, 4)]


def determine_winner(user_move, computer_move):
    """
    Returns the outcome of the match
    
    Parameters
    ----------
    user_move : string
        user's move. One of: rock, paper, scissors, lizard, spock
    computer_move : string
        computer's move. One of: rock, paper, scissors, lizard, spock
    
    Returns
    --------
    string : "draw", "user", or "computer"
        The winner of the match
    """
    if user_move == computer_move:
        return "draw"
    if computer_move in winning_moves[user_move]:
        return "user"
    else:
        return "computer"
    

# Separate our main from the rest of the file
if __name__ == "__main__":
    # 1. Print the rules of the game
    print(instructions_string)
    
    # 2. Accept and validate user input
    while True:
        # Take in user input
        user_move = input("Enter your move: ")

        # Move on if move is valid
        user_move = user_move.lower()
        if user_move in possible_moves:
            print("You picked {}".format(user_move))
            break
        else:
            print("Sorry, that is not a possible move. Please pick a valid move.")
    
    # Get computer move
    computer_move = get_computer_move()
    print("The computer picked {}".format(computer_move))
    
    # Determine winner
    winner = determine_winner(user_move, computer_move)
    
    if winner == "draw":
        print("The match was a draw.")
    elif winner == "user":
        print("Congrats, you won!")
    elif winner == "computer":
        print("Computer won. Humanity is lost.")
    print("\n")
    
    
        
        