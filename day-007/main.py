# hangman game
from unittest import result
from random_word import RandomWords
from hangman_art import banner, hangman_stage
from prettytable import PrettyTable
from utils import clear

MAX_LIVES = 8


def validate_input(current_guess, history_guess) -> str:
    """Ask the user to input a character. Repeat if getting invalid input.
       This also checks if the letter they guess is already guessed before,
       as it is not a valid guess.

    Args:
        current_guess (str): the current word with correct characters revealed
        history_guess (list[str]): list of historical guesses

    Returns:
        str: the valid character
    """

    valid_input = False
    while not valid_input:
        while True:
            try:
                guess = str(input("Please enter a guess character: "))[0]
                break
            except IndexError:
                print("Oops! That was not a valid character! Try again...")
        if guess.lower().isalpha():
            if ((guess.lower() not in current_guess) and
                    (guess.lower() not in history_guess)):
                valid_input = True
            else:
                print("Oops! You have already guessed this character! Try"
                      " again...")
        else:
            print("Oops! That was not a valid character! Try again...")
    return guess


def hangman_round(word,
                  current_guess,
                  history_guess,
                  stage) -> tuple[bool, str, int]:
    """One single round of the hangman game. Given the current states of the
       game, guessing word with the given word, current guess, history, stage
       return True/False for guessing correctly or not, the new current_guess
       and the stage afterward and the guessed character.

    Args:
        word (str): the word that going to be guessed
        current_guess (str): current guess with correct letters revealed
        history_guess (list[str]): list of historical guessed letters
        stage (_type_): stage of lives, 0 - 7

    Returns:
        tuple[bool, str, int, str]: True/False for guessing correctly or not,
        the new current_guess and the stage afterward and the guessed character
    """
    guess_char = validate_input(current_guess, history_guess)
    isTrue, current_guess = check_and_show(word, current_guess, guess_char)
    if not isTrue:
        stage += 1
        print(f"Oops! You guessed wrongly! Letter {guess_char} is not"
              " in the word. You lose a life.")
    return (isTrue, current_guess, stage, guess_char)


def check_and_show(word, current_guess, guess_char) -> tuple[bool, str]:
    """Given a word and a character, check if the character is in the word.
       Return True/False and also the form of the word with
       revealed correct letters.

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
       Using the Python library `random-word` for generating a word to guess.
    """
    print(banner)
    random_word_instance = RandomWords()
    long_word = random_word_instance.get_random_word()
    while long_word is None:
        long_word = random_word_instance.get_random_word()
    if "-" in long_word:
        word = long_word.split("-")[0]
    else:
        word = long_word.split(" ")[0]
    # set up the game
    stage = 0
    history_guess = []
    current_guess = "".join(['_' for c in word])
    last_guess_bool = None
    last_guess_char = None
    while stage < MAX_LIVES:
        clear()
        print(banner)
        print('*************************************************************')
        print(f"Phh! The word is {word}")
        # make PrettyTable
        x = PrettyTable(border=True, padding_width=5)
        art_stage_fieldname = str("STAGE".ljust(15))
        art_infor_fieldname = str("INFO".ljust(35))
        x.field_names = [art_stage_fieldname, art_infor_fieldname]
        x.align[art_stage_fieldname] = "l"
        x.align[art_infor_fieldname] = "l"
        stage_str = hangman_stage[stage]
        infor_str = "\n\n" +\
                    f"GUESS      : {current_guess}\n\n" +\
                    f"HISTORY    : {''.join(history_guess)}\n\n" +\
                    f"STAGE      : {stage}\n\n" +\
                    f"LAST GUESS : {last_guess_char} - {last_guess_bool}"
        x.add_row([stage_str, infor_str])
        print(x)
        # print(hangman_stage[stage])
        # print(f"GUESS  : {current_guess}")
        # print(f"HISTORY: {history_guess}")
        # print(f"STAGE  : {stage}")
        # processing result of the round
        result_round = hangman_round(word, current_guess, history_guess, stage)
        isTrue, current_guess, stage, guess_char = result_round
        history_guess.append(guess_char)
        if current_guess == word:
            print(f"YOU WIN, THE WORD IS == {word} ==!")
            return
        last_guess_bool = isTrue
        last_guess_char = guess_char
    print(f"GAME OVER! YOU LOSE! THE WORD IS == {word} ==!")


if __name__ == "__main__":
    hangman_game()
