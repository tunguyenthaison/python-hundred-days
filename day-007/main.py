
from unicodedata import name

def validate_input(current_guess) -> str:
    """Ask the user to input a character. Repeat if getting invalid input.

    Returns:
        str: the valid character
    """
    valid_input = False
    while not valid_input:
        while True:
            try:
                guess = str(input("Please enter a guess character: "))[0]
                break
            except ValueError:
                print("Oops! That was not a valid number! Try again...")
        if guess.lower().isalpha():
            valid_input = True
    return guess                


def hangman(word) -> bool:
    """_summary_

    Args:
        word (_type_): _description_

    Returns:
        bool: _description_
    """
    score = 0
    current_guess = ['_' for c in word]
    while score < 5:
        guess_char = validate_input()
        while guess_char in current_guess:  # if repeating a character already guessed then it is an invalid guess
            print(f"Chatacter {guess_char} has already guessed, please enter a different character")  
            guess_char = validate_input()
        isTrue, current_guess = check_and_show(word, current_guess, guess_char)
        if not isTrue or guess_char 
            score += 1
        if current_guess == word:
            print("You guessed correctly the word: You win!")
            return True
        print(f"The current word: {current_guess}")
        print(f"The current score: {score}")
    print("Out of guesses! You lose!")
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
        for char_count in range(0, nr_char):
            ind_char = word.index(guess_char, nr_char)
            word_show_list[ind_char] = guess_char
            word_show = "".join(word_show_list)
        return (True, word_show)
    else:
        return (False, "".join(word_show_list))


if __name__ == "__main__":
    # hangman()
    word = 'recitation'
    # current_guess = ['_' for c in word]
    # isTrue, word_show = check_and_show(word, current_guess, 'c')
    # print(word_show)
    hangman(word)

