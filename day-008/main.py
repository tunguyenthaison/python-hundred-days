from utils import alphabet_list, banner, validate_direction
from icecream import ic


def encrypt_v2(text, shift) -> str:
    """Take a text and shift every letter to `shift` characters
    in the alphabet (using lambda function).

    Args:
        text (str): text to be encrypted
        shift (int): number of characters to shift

    Returns:
        str: text after being shifted
    """
    shift_c = (lambda c: alphabet_list[(alphabet_list.index(c) + shift) %
               len(alphabet_list)])
    return_text = "".join([shift_c(c) for c in text])
    return return_text


def encrypt_v1(text, shift) -> str:
    """Take a text and shift every letter to `shift` characters
       in the alphabet.

    Args:
        text (str): text to be encrypted
        shift (int): number of characters to shift

    Returns:
        str: text after being shifted
    """
    text_shifted = ""
    for c in text:
        idx = alphabet_list.index(c)
        idx_shifted = (idx + shift) % len(alphabet_list)
        text_shifted += alphabet_list[idx_shifted]
    return(text_shifted)


def decrypt(text, shift) -> str:
    """Take a shifted text and un-shift every letter to
    `shift` characters in the alphabet.

    Args:
        text (str): text to be decrypted
        shift (int): number of characters to shift

    Returns:
        str: text after being un-shifted
    """
    return encrypt_v1(text, -shift)


def CeasarCipher():
    """The Ceasar Cipher program in command line
    """
    print(banner)
    text = input("Please input the word: ")
    shift = int(input("Please input the amount of shift: "))
    direction = validate_direction()
    if direction == 'e':
        encrypt_text = encrypt_v1(text, shift)
        print(f"The encrypted word is: {encrypt_text}")
    else:
        decrypt_text = decrypt(text, shift)
        print(f"The decrypted word is: {decrypt_text}")


if __name__ == "__main__":
    CeasarCipher()
