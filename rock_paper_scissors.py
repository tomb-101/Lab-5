import random

def rock_paper_scissors_game():
    """
    Plays a Rock-Paper-Scissors game between the user and the computer.
    
    The user is prompted to enter 'rock', 'paper', or 'scissors'.
    The computer randomly chooses one of the three options.
    The winner is determined based on the standard rules of the game.
    The game continues until the user decides to quit by entering 'quit'.
    """
    
    computer=["Rock", "Paper", "Scissors"]

    while True:
        comp_choice=random.choice(computer)
        print("Rock, Paper, Scissors? Case sensitive. (or type quit to exit)\n")
        user_input=input()
        if user_input=="quit":
            print("\nExiting game.")
            break
        elif user_input==computer[computer.index(user_input)] and comp_choice==computer[(computer.index(user_input))-1]:
            print(f"You win, {user_input} beats {computer[(computer.index(user_input))-1]}.\n")
        elif user_input==computer[computer.index(user_input)] and comp_choice==computer[(computer.index(user_input))]:
            print("It's a draw.\n")
        else:
            print(f"{computer[computer.index(user_input)]} does not beat {comp_choice}. You lose this round.\n")

# Run the game
rock_paper_scissors_game()
