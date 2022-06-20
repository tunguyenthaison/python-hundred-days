""" The Blackjack game in Terminal with ASCII art
"""
import arts
import utils
import random 
import numpy as np
from icecream import ic

CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def step(number_of_cards, current_deck, hand)->tuple[list[str], list[str]]:
    """ A withdrawing step, take random cards from the deckm update the deck and hand

    Args:
        number_of_cards (int): how many cards will be taken from the deck
        current_deck (list[str]): list of cards in deck
        hand (list[str]): list of cards in hand

    Returns:
        tuple[list[str], list[str]]: list of card in the deck and hand after the step
    """
    count = 0
    while count < number_of_cards:
        card, current_deck = utils.draw(current_deck)
        hand.append(card)
        count += 1
    return current_deck, hand


def compare_blackjack(player, computer) -> int:
    """ Compare the string representation of Blackjack

    Args:
        player (str): string represent blackjack, 'natural', 'super' or None
        computer (str): string represent blackjack, 'natural', 'super' or None

    Returns:
        int: -1 if the player loses, 0 if tie and 1 if the player wins and None 
        if either of them has blackjack
    """
    if player == computer:
        return 0
    if [player, computer] == ['natural', 'super']:
        return -1
    if [player, computer] == ['super', 'natural']:
        return 1
    if [player, computer] == ['natural', 'None']:
        return 1
    if [player, computer] == ['super', 'None']:
        return 1
    if [player, computer] == ['None', 'natural']:
        return -1
    if [player, computer] == ['None', 'super']:
        return -1
        

def blackjack_game() -> tuple[int, list[str], list[str]]:
    """ Blackjack game

    Returns:
        int: 1 if the player wins, 0 if ties, and -1 if the player loses
        list[str]: final hand of the player
        list[str]: final hand of the computer
    """
    current_deck = utils.DECK_OF_CARDS.copy()
    player_hand, computer_hand = [], []
    player_score, computer_score = 0, 0
    # withdraw 2 cards for player
    current_deck, player_hand = step(2, current_deck, player_hand)
    player_blackjack_string, player_score = utils.get_score(player_hand)
    # withdraw 2 cards for computer
    current_deck, computer_hand = step(2, current_deck, computer_hand)
    computer_blackjack_string, computer_score = utils.get_score(computer_hand)
    # Initial report of information to the screen
    print(f"Computer first card: {computer_hand[0]}, score {utils.get_value(computer_hand[0])}")

    # player_hand = ['9-hearts', '8-spades']
    # player_blackjack_string, player_score = utils.get_score(player_hand)
    # computer_hand = ['4-diamonds', '2-clubs']
    # computer_blackjack_string, computer_score = utils.get_score(computer_hand)

    ic(player_hand, player_blackjack_string, player_score)
    ic(computer_hand, computer_blackjack_string, computer_score)

    ic('=============== GET A0 =============== ')

    is_more = 'y'
    while is_more == 'y' and player_blackjack_string == 'None':
        is_more = input("Type 'y' to get another card, type 'n' to pass: ")
        if is_more == 'y':
            current_deck, player_hand = step(1, current_deck, player_hand)
            _, player_score = utils.get_score(player_hand)
        if player_score > 21:
            is_more = 'n'

        ic(type(player_blackjack_string))
        ic(player_hand, player_blackjack_string, player_score)
        ic(computer_hand, computer_blackjack_string, computer_score)

    ic('=============== GET A1 =============== ')

    # check if player has blackjack, the game is finished here
    if player_blackjack_string != 'None' or computer_blackjack_string != 'None':
        blackjack_result = compare_blackjack(player_blackjack_string, computer_blackjack_string)
        return blackjack_result, player_hand, computer_hand

    ic('=============== GET A2 =============== ')

    # computer analysis and get cards
    # the case player got 5 cards under 21
    if len(player_hand) == 5 and player_score <= 21:
        return 1, player_hand, computer_hand
    
    ic('=============== GET A3 =============== ')

    # the case the computer is lower than 15, not legal
    while computer_score < 15:
        current_deck, computer_hand = step(1, current_deck, computer_hand)
        _, computer_score = utils.get_score(computer_hand)

    ic('=============== GET A4 =============== ')   

    # keep withdrawing card if computer < player
    countc = 0
    while computer_score > 0 and computer_score < player_score:
        print(f'The step {countc}')
        ic('Now', len(current_deck))
        current_deck, computer_hand = step(1, current_deck, computer_hand)
        _, computer_score = utils.get_score(computer_hand)
        ic(computer_hand)
        ic(computer_score)


    print(f"Your final hand: {player_hand}, final score: {player_score}")
    print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")

    if player_score == 0:
        if computer_score == 0:
            print('Tie, both are over 21!')
            return 0, player_hand, computer_hand
        else:
            print('You are over 21! The computer wins!')
            return -1, player_hand, computer_hand
    else:
        if computer_score == 0:
            print('The computer is over 21! You win!')
            return 1, player_hand, computer_hand
        elif player_score == computer_score:
            print(f'Tie! You are both {player_score}!')
            return 0, player_hand, computer_hand
        elif player_score > computer_score:
            print('You win!')
            return 1, player_hand, computer_hand
        else:
            print('Computer wins!')
            return -1, player_hand, computer_hand


if __name__ == "__main__":
    utils.clear()
    print(blackjack_game())