# Blackjack project

## Game's rules
* The deck is unlimited in size. 
* There are no jokers. 
* The Jack/Queen/King all count as 10.
* The the Ace can count as 11 or 1.
* Use the following list as the deck of cards:
* cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
* The cards in the list have equal probability of being drawn.
* Cards are not removed from the deck as they are drawn.
* The computer is the dealer.

## Strategy

- [x] Create a card deck.
- [x] A function to withdraw a card randomly from the deck.
    ```python
        draw(deck_of_cards) -> tuple[str, list[str]]
    ```
- [x] A function to read a hand of cards and return the best score
    ```python
        get_score(list_of_cards) -> tuple[str, int]
    ```
    This function uses the following helper functions:

    - `score_aces(number_of_aces) -> list[int]` to compute the possible scores of all `aces` in the hand, and 
    - `score_all(list_of_cards_name) -> list[int]` to compute all possible scores, including both aces and non-aces

    


## The game goes as follows:

1. Draw 2 cards for player (update hands, score, blackjack ...)
2. Draw 2 cards for computer (update hands, score, blackjack ...), review first card
3. Proceed to decice if blackjack happens, end game appropriately.
4. A loop for Player to continue draw 1 card (update hands, score ...) until stop.
5. Once the player stop, computer gets a loop to keep withdrawing 1 card until > 21 or > Player
6. Compare score, end game.


## Notes
* For simplicity, we make a list of integer going from 0-51 representing 52 cards. 
* Need to write code in a module fashion.
