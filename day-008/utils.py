# utilities for Ceasar-cipher
import string
from os import system, name

alphabet_string = string.ascii_lowercase
alphabet_list = list(alphabet_string)

banner = """
╔═╗┌─┐┌─┐┌─┐┌─┐┬─┐  ╔═╗┬ ┬┌─┐┬ ┬┌─┐┬─┐
║  ├┤ ├─┤└─┐├─┤├┬┘  ║  └┬┘├─┘├─┤├┤ ├┬┘
╚═╝└─┘┴ ┴└─┘┴ ┴┴└─  ╚═╝ ┴ ┴  ┴ ┴└─┘┴└─
"""


def clear():
    """Clear the command promt
    """
    # for Window
    if name == 'nt':
        _ = system('cls')
    # for Mac and Linux
    else:
        _ = system('clear')


def validate_direction() -> str:
    """Ask the user to input a direction. Repeat if getting invalid input.

    Returns:
        str: the valid direction
    """
    valid_input = False
    while not valid_input:
        direction = str(input("Please enter 'encrypt' (e)"
                              "or 'decrypt' (d): ")[0])
        if direction.lower() in ['e', 'd']:
            valid_input = True
        else:
            print("Oops! That was not a valid choice! Try again...")
    return direction
