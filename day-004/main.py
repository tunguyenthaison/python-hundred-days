import random
from os import system, name

def validate_input_game()->int:
    """Ask the user to input either 0, 1 or 2. Repeat if getting invalid input.

    Returns:
        int: 0, 1, or 2 as the valid choice of the user
    """
    valid_input = False
    while not valid_input:
        while True:
            try:
                player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
                break
            except ValueError:
                print("Oops! That was not a valid number! Try again...")
        if player_choice in [0, 1, 2]:
            valid_input = True
    return player_choice


def validate_input_yesno()->bool:
    """Ask the user to input either Yes or No. Repeat if getting invalid input to continue the game or not.

    Returns:
        bool: True if Yes, False if No
    """
    valid_input = False
    while not valid_input:
        cont = input("Play another round? Yes or No: ")
        if cont[0].lower() in ['y', 'n']:
            valid_input = True
    return (cont[0].lower() == 'y')


def RockPaperScissors_round()->int:
    """A round of Rock, Paper, Scissors game

    Returns:
        int: 1 if player win, -1 if computer win
    """
    
    rock = '''
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
            ______)
            _______)
            _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    '''
    
    game_dict = {
        0: rock,
        1: paper,
        2: scissors,
    }
    choice_names = {
        0: 'rock',
        1: 'paper',
        2: 'scissors',
    }
    
    exit_round = False 
    while exit_round is False:
        player_choice = validate_input_game()
        print(f"You play: {choice_names[player_choice]}\n" + game_dict[player_choice])
        computer_choice = random.randint(0, 2)
        print(f"Computer play: {choice_names[computer_choice]}\n" + game_dict[computer_choice])
        if player_choice == computer_choice:
            print("Tie! Go again!")
        else:
            exit_round = True
            if (player_choice < computer_choice):
                if abs(player_choice - computer_choice) == 1:
                    print("Computer win!")
                    return -1
                else:
                    print("You win! 🎉")
                    return 1
            else: # player_choice > computer_choice
                if abs(player_choice - computer_choice) == 1:
                    print("You win! 🎉")
                    return 1
                else:
                    print("Computer win!")
                    return -1
                

def RockPaperScissors():
    banner = '''
     █████╗ ███████╗ ██████╗██╗██╗                                                                                                       
    ██╔══██╗██╔════╝██╔════╝██║██║                                                                                                       
    ███████║███████╗██║     ██║██║                                                                                                       
    ██╔══██║╚════██║██║     ██║██║                                                                                                       
    ██║  ██║███████║╚██████╗██║██║                                                                                                       
    ╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝╚═╝                                                                                                       
                                                                                                                                        
    ██████╗  ██████╗  ██████╗██╗  ██╗██████╗  █████╗ ██████╗ ███████╗██████╗ ███████╗ ██████╗██╗███████╗███████╗ ██████╗ ██████╗ ███████╗
    ██╔══██╗██╔═══██╗██╔════╝██║ ██╔╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔════╝██╔════╝██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔════╝
    ██████╔╝██║   ██║██║     █████╔╝ ██████╔╝███████║██████╔╝█████╗  ██████╔╝███████╗██║     ██║███████╗███████╗██║   ██║██████╔╝███████╗
    ██╔══██╗██║   ██║██║     ██╔═██╗ ██╔═══╝ ██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗╚════██║██║     ██║╚════██║╚════██║██║   ██║██╔══██╗╚════██║
    ██║  ██║╚██████╔╝╚██████╗██║  ██╗██║     ██║  ██║██║     ███████╗██║  ██║███████║╚██████╗██║███████║███████║╚██████╔╝██║  ██║███████║
    ╚═╝  ╚═╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝
    '''
    print(banner)
    print("Welcome to the Rock, Paper, Scissors game!")
    player_scores = 0
    computer_scores = 0
    isContinue = True
    number_round = 0
    while isContinue:
        number_round += 1
        # clear the command promt
        clear()
        print(banner)
        print(f"Round {number_round} of the game: ")
        score = RockPaperScissors_round()
        if score == 1:
            player_scores += 1
        else:
            computer_scores += 1
        
        #  Validate input from user
        isContinue = validate_input_yesno()
        
    print("-----------------------------------------------------------")
    print(f"Game end! Your scores: {player_scores} v.s. Computer scores: {computer_scores}")


def clear():
    """Clear the command promt 
    """
    # for Window
    if name == 'nt':
        _ = system('cls')
    # for Mac and Linux
    else:
        _ = system('clear')
        
        
if __name__ == "__main__":
    RockPaperScissors()
