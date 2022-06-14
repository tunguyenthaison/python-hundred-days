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
