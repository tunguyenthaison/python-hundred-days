"""Calculator in the terminal with ASCII art
"""
import utils
import arts


def calculator() -> None:
    """ The calculator in terminal program
    """
    print(arts.LOGO)
    run_program =  True
    memory = None
    is_cont = True
    while run_program:
        if is_cont:
            memory = calculator_step(memory)
        else:
            memory = calculator_step(None)
        valid_input = False
        while not valid_input:
            is_cont_input = input(f"Type 'y' to continue calculating with {memory}, "
                                  "or type 'n' to start a new calculation, "
                                  "or type 'e' to exit the program: ")
            if is_cont_input.lower() in ['y', 'n', 'e']:
                valid_input = True
            else:
                print("Not a valid input! Try again!")
        if is_cont_input == 'n':
            is_cont = False
        elif is_cont_input == 'e':
            run_program = False


def calculator_step(memory) -> float:
    """A step of the calculator

    Args:
        memory (float): the previous result

    Returns:
        float: the new result
    """
    if memory is None:
        memory = utils.validate_float("What's the first number?: ", "Invalid input, try again!")
    print("+\n-\n*\n/")
    operation = utils.validate_operation("Pick an operation: ", "Invalid operation, try again!")
    valid_computation = False
    while not valid_computation:
        number_next = utils.validate_float("What's the next number?: ", "Invalid input, try again!")
        (valid_computation, result) = utils.compute(memory, number_next, operation)
    print(f"{memory} {operation} {number_next} = {result}")
    return result


if __name__ == "__main__":
    calculator()
