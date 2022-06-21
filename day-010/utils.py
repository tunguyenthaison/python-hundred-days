# utilities for Calculator
from os import system, name

def clear():
    """Clear the command promt
    """
    # for Window
    if name == 'nt':
        _ = system('cls')
    # for Mac and Linux
    else:
        _ = system('clear')


def validate_float(promt_msg, error_msg) -> float:
    """Ask the user to input a float. Repeat if getting invalid input.

    Args:
        promt_msg (str): message to use for the input
        error_msg (str): message to dislay for invalid input
    Returns:
        float: the valid float
    """
    while True:
        try:
            number = float(input(f"{promt_msg}"))
            break
        except ValueError:
            print(error_msg)
    return number


def validate_operation(promt_msg, error_msg) -> str:
    """Ask the user to input an operation [+, -, *, /]. Repeat if getting invalid input.

    Args:
        promt_msg (str): message to use for the input
        error_msg (str): message to dislay for invalid input
    Returns:
        str: the valid operation in [+, -, *, /]
    """
    valid_input = False 
    while not valid_input:
        operation = input(f"{promt_msg}")[0]
        if operation in ["+", "-", "*", "/"]:
            valid_input = True
        else:
            print(error_msg)
    return operation


def compute(number1, number2, operation) -> tuple[bool, float]:
    """Compute with two float numbers, operation is +, -, * or /

    Args:
        operation (str): one of [+, -, *, /]
        number1 (float): the first number
        number2 (float): the second number

    Returns:
        bool: the operation is successful or not, use for divide by 0
        float: (first number) operation (second number)
    """
    if operation == "+":
        return (True, number1 + number2)
    if operation == "-":
        return (True, number1 - number2)
    if operation == "*":
        return (True, number1 * number2)
    if operation == "/":
        if number2 != 0:
            return (True, number1 / number2)
        return (False, 0)
