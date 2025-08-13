import random

player = input("Enter your choice (rock, paper, scissors): ")
choices = ["rock", "paper", "scissors"]


def get_computer_choice():
    return random.choice(choices)

def determine_winner(player, computer):
    if player == computer:  
        return "It's a tie!"    
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "You lose!"

computer1 = get_computer_choice()

print(determine_winner(player, computer1))
print("Computer chose: \n#\n#\n#\n#\n##", computer1)