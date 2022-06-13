# hangman game
from random_word import RandomWords
from icecream import ic


def validate_input(current_guess) -> str:
    """Ask the user to input a character. Repeat if getting invalid input.

    Returns:
        str: the valid character
    """
    valid_input = False
    while not valid_input:
        guess = str(input("Please enter a guess character: "))[0]
        if guess.lower().isalpha():
            if guess.lower() not in current_guess:
                valid_input = True
            else:
                print("Oops! You have already guessed this character! Try"
                      "again...")
        else:
            print("Oops! That was not a valid character! Try again...")
    return guess


def hangman_word(word) -> bool:
    """The hangman game: guessing word with the given word.

    Args:
        word (str): the word that will be guessed

    Returns:
        bool: True if guessing it correctly given 5 tries, False otherwise
    """
    score = 0
    history_guess = []
    current_guess = ['_' for c in word]
    while score < 5:
        guess_char = validate_input(current_guess)
        isTrue, current_guess = check_and_show(word, current_guess, guess_char)
        if not isTrue:
            score += 1
            print("Oops! You guessed wrongly!")
        if current_guess == word:
            print("You guessed correctly the word: You win!")
            return True
        history_guess.append(guess_char)
        print(f"The current word: {current_guess}")
        print(f"History of guess: {history_guess}")
        print(f"The current score: {score}")
    print(f"Out of guesses! You lose! The correct word is {word}")
    return False


def check_and_show(word, current_guess, guess_char) -> tuple[bool, str]:
    """Given a word and a character, check if the character is in the word.

    Args:
        word (str): the word to guess
        current_guess: the current phase of guessing, starting with all '_'
        guess_char (char): the guessed character

    Returns:
        tuple(bool, str): True if the character is contained in the word,
                            False otherwise, the string being returned is
                            the word with _ for hidden character
                            and the true character is the one that
                            has been revealed, e.g., m__h
    """
    word_show_list = [c for c in current_guess]
    if guess_char in word:
        nr_char = word.count(guess_char)
        indices_guess_char = []
        for i, c in enumerate(word):
            if c == guess_char:
                indices_guess_char.append(i)
        for ind in indices_guess_char:
            word_show_list[ind] = guess_char
        word_show = "".join(word_show_list)
        return (True, word_show)
    else:
        return (False, "".join(word_show_list))


def hangman_game() -> None:
    """The hanging man game with an internal or external database of words.
       Using the Python library `random-word`
    """

    random_word_instance = RandomWords()
    word = random_word_instance.get_random_word()
    hangman_word(word.lower())


if __name__ == "__main__":
    # hangman_word(word)
    banner = """
    ██╗  ██╗ █████╗ ███╗   ██╗ ██████╗       ███╗   ███╗ █████╗ ███╗   ██╗
    ██║  ██║██╔══██╗████╗  ██║██╔════╝       ████╗ ████║██╔══██╗████╗  ██║
    ███████║███████║██╔██╗ ██║██║  ███╗█████╗██╔████╔██║███████║██╔██╗ ██║
    ██╔══██║██╔══██║██║╚██╗██║██║   ██║╚════╝██║╚██╔╝██║██╔══██║██║╚██╗██║
    ██║  ██║██║  ██║██║ ╚████║╚██████╔╝      ██║ ╚═╝ ██║██║  ██║██║ ╚████║
    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝       ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝                                                                  
    """
    print(banner)
    hangman_game()
