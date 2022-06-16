""" utilities for auction()
"""
from os import system, name
from prettytable import PrettyTable

LOGO = '''
                         ___________
                         \\         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''


def clear():
    """Clear the command promt
    """
    # for Window
    if name == 'nt':
        _ = system('cls')
    # for Mac and Linux
    else:
        _ = system('clear')


def validate_number(promt_msg, error_msg) -> int:
    """Get input from user as a integer

    Args:
        promt_msg (str): message to use for the input
        error_msg (str): message to dislay for invalid input

    Returns:
        int: the valid integer
    """
    valid_input = False
    while not valid_input:
        while True:
            try:
                number = int(input(f"{promt_msg}"))
                break
            except ValueError:
                print(f"{error_msg}")
        if number >= 0:
            valid_input = True
    return number


