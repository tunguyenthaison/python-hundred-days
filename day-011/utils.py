""" Utilities for Blackjack game
"""
import random
from icecream import ic
from os import system, name

CARD_NAMES_VALUES = {
    'A': 11,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
}

CARD_CODES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
CARD_SHAPES = ['clubs', 'diamonds', 'hearts', 'spades']
DECK_OF_CARDS = []

for card_name_index in CARD_CODES:
    for card_shape_index in CARD_SHAPES:
        card_name = card_name_index + '-' + card_shape_index
        DECK_OF_CARDS.append(card_name)


def clear():
    """Clear the command promt
    """
    # for Window
    if name == 'nt':
        _ = system('cls')
    # for Mac and Linux
    else:
        _ = system('clear')


def get_value(card):
    """ Get value of a card from its name

    Args:
        card (str): name of card

    Returns:
        int: value
    """
    return CARD_NAMES_VALUES[card.split("-")[0]]


def draw(deck_of_cards) -> tuple[str, list[str]]:
    """ Draw a random card from the deck of card

    Args:
        deck_of_cards (list[str]): deck of card

    Returns:
        tuple: (str, list[str]), the card and the remaining deck
    """
    current_deck_of_cards = deck_of_cards.copy()
    # draw_card = np.random.choice(current_deck_of_cards, replace=False)
    draw_card = random.choice(current_deck_of_cards)
    current_deck_of_cards.remove(draw_card)
    return (draw_card, current_deck_of_cards)


def get_score(list_of_cards) -> tuple[str, int]:
    """Compute the score of a list of card

    Args:
        list_of_cards (list[str]): list of cards

    Returns:
        str: 'natural' or 'super' or 'None'
        int: str-super blackjack or natural blackjack and int-score
    """
    # blackjack_string = 'None'
    total_score = 0
    list_names = [card.split("-")[0] for card in list_of_cards]
    # edge case, natural blackjack (A+10) or super blackjack (A+A)
    if len(list_names) == 2 and 'A' in list_names:
        card_1, card_2 = list_names
        if (card_1 == "A" and get_value(card_2) == 10) or (card_2 == "A" and get_value(card_1) == 10):
            blackjack_string = 'natural'
            total_score = 21
        elif (card_1 == "A" and card_2 == 'A'):
            blackjack_string = 'super'
            total_score = 21
        else:
            blackjack_string = 'None'
            possible_scores = [x for x in score_all(list_names.copy()) if x <= 21]
            total_score = max(possible_scores) if len(possible_scores) > 0 else 0
    else:
        blackjack_string = 'None'
        possible_scores = [x for x in score_all(list_names.copy()) if x <= 21]
        # ic(possible_scores)
        total_score = max(possible_scores) if len(possible_scores) > 0 else 0
    return blackjack_string, total_score
      

def score_aces(number_of_aces) -> list[int]:
    """ Return all possible scores of aces

    Args:
        number_of_aces (int): number of aces

    Returns:
        list[int]: list of all possible scores
    """
    if number_of_aces == 0:
        return 0
    if number_of_aces == 1:
        return [1, 11]
    if number_of_aces == 2:
        return [2, 12, 22]
    if number_of_aces == 3:
        return [3, 13, 23, 33]
    if number_of_aces == 4:
        return [4, 14, 24, 34, 44]
    if number_of_aces > 4:
        return None


def score_all(list_of_cards_name) -> list[int]:
    """ Return all possible scores of a hand of cards

    Args:
        list_of_cards_name (str): list of cards name, 'A', '2', ... not including shape

    Returns:
        list[int]: list of scores
    """
    number_aces = list_of_cards_name.count('A')
    if number_aces == 0:
        return [sum([get_value(card) for card in list_of_cards_name])]
    for i in range(number_aces):
        list_of_cards_name.remove('A')
    remain_cards = list_of_cards_name
    remain_cards_score = sum([get_value(card) for card in remain_cards])
    return [remain_cards_score + score for score in score_aces(number_aces)]


if __name__ == "__main__":
    # drawed_card, remained_deck = draw(DECK_OF_CARDS)
    # print(len(remained_deck))
    # print(f"The drawed card is {drawed_card}")
    # print(f"The value of the drawed card is: {get_value(drawed_card)}")
    # print(score_all(['A','2', '10']))
    # print(get_score(['A-square','2-bl', '10-l', 'Q-p']))
    # print(get_score(['Q-clubs', 'J-hearts']))
    ic(get_score(['5-spades', '5-clubs', 'A-hearts']))
