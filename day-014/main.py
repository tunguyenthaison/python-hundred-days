""" The Higher-Lower game ASCII
"""
import random
import art
import game_data
import utils
from prettytable import PrettyTable

LIVES = 5


def get_item(data) -> dict:
    """ Return a random entry from a list of data

    Args:
        data (list[dict]): list of data, each entry of the list is a dictionary

    Returns:
        dict: an entry of data
    """
    return random.choice(data)


def correct_choice(data_a, data_b) -> tuple[str, dict]:
    """Return A if data_a has higher count, B otherwise, and A if they are the same

    Args:
        data_a (dict): data entry
        data_b (dict): data entry

    Returns:
        str: A (data_a) or B (data_b), depend on what has higher count
        dict: the higher data entry
    """

    count_a, count_b = data_a['follower_count'], data_b['follower_count']
    if count_a >= count_b:
        return 'A', data_a
    return 'B', data_b


def higher_lower_game(number_of_lives, data) -> None:
    """ The Higher-Lower Game: guessing number of Twitter followers

    Args:
        number_of_lives (int): number of guesses the player has
        data (list[dict]): list of data, each entry is a dictionary of type
            ```python
            {
                'name': 'Ariana Grande',
                'follower_count': 183,
                'description': 'Musician and actress',
                'country': 'United States'
            },
            ```
    """
    score = 0
    lives = number_of_lives

    game_should_continue = True
    player_choice = None # to save the last choice
    is_correct = None # to save the last choice
    while game_should_continue:
        cur_data = get_item(data)
        # data.remove(cur_data) # make sure this entry does not appear again
        new_data = get_item(data)
        # data.remove(new_data) # make sure this entry does not appear again

        # swwapping to make the game more interesting
        cur_data = new_data
        new_data = get_item(data)

        # the graphic part
        utils.clear()
        print(art.LOGO)
        # print('==============================================================')
        # The PrettyTable
        ascii_table = PrettyTable(border=True, padding_width=1)
        art_a_fieldname = str("A".ljust(35))
        art_b_fieldname = str("B".ljust(35))
        art_c_fieldname = str("Record".ljust(15))
        ascii_table.field_names = [art_a_fieldname, art_b_fieldname, art_c_fieldname]
        ascii_table.align[art_a_fieldname] = 'l'
        ascii_table.align[art_b_fieldname] = 'l'
        ascii_table.align[art_c_fieldname] = 'l'
        # data entry for current data
        cur_descript = cur_data['description'].split(" ")[0]
        a_str = "\n" +\
                f"NAME      : {cur_data['name']}\n\n" +\
                f"FOLLOWERS : {cur_data['follower_count']}\n\n" +\
                f"CATEGORY  : {cur_descript}\n\n" +\
                f"COUNTRY   : {cur_data['country']}"
        # The Game Play
        # print(f'You have {lives} left!')

        # data entry for new data
        new_descript = new_data['description'].split(" ")[0]
        b_str = "\n" +\
                f"NAME      : {new_data['name']}\n\n" +\
                "FOLLOWERS : ????????\n\n" +\
                f"CATEGORY  : {new_descript}\n\n" +\
                f"COUNTRY   : {new_data['country']}"
        # the record column in the table
        c_str = "\n" +\
                f"LIVES        : {lives}\n\n" +\
                f"SCORES       : {score}\n\n" +\
                f"LAST CHOICE  : {player_choice} - {is_correct}\n\n"
        ascii_table.add_row([a_str, b_str, c_str])
        print(ascii_table)
        # print(f"A. {cur_data['name']}, {cur_data['follower_count']} followers")
        # print("v.s.")
        # print(f"B. {new_data['name']}, ? followers")
        player_choice = input("Type A or B: ").upper()
        right_choice, right_data = correct_choice(cur_data, new_data)
        if player_choice.lower()[0] == right_choice.lower():
            # print('You guessed it correctly')
            # print(f"B. {new_data['name']}, {new_data['follower_count']} followers")
            score += 1
            is_correct = True
        else:
            # print('You guessed it wrongly')
            # print(f"B. {new_data['name']}, {new_data['follower_count']} followers")
            lives -= 1
            is_correct = False
        # update table
        ascii_table.clear_rows()
        b_str = "\n" +\
                f"NAME      : {new_data['name']}\n\n" +\
                f"FOLLOWERS : {new_data['follower_count']}\n\n" +\
                f"CATEGORY  : {new_descript}\n\n" +\
                f"COUNTRY   : {new_data['country']}"
        c_str = "\n" +\
                f"LIVES        : {lives}\n\n" +\
                f"SCORES       : {score}\n\n" +\
                f"LAST CHOICE  : {player_choice} - {is_correct}\n\n"
        # table.field_names = [art_a_fieldname, art_b_fieldname, art_c_fieldname]
        ascii_table.add_row([a_str, b_str, c_str])
        utils.clear()
        print(art.LOGO)
        # print('==============================================================')
        print(ascii_table)
        cur_data = right_data
        if lives == 0:
            game_should_continue = False
        _ = input("Type Enter to continue the game! ")
    print(f"Out of lives! You have {score} points!")


if __name__ == "__main__":
    higher_lower_game(5, game_data.data)
