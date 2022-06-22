""" The Higher-Lower game ASCII
"""
import random

from tomlkit import table
import art
import game_data
import utils
from prettytable import PrettyTable

LIVES = 5


def get_item(data) -> dict:
    """ Return a random entry from a list of data

    Args:
        data (list[dict]): list of data

    Returns:
        dict: an entry of data
    """
    return random.choice(data)


def correct_choice(dataA, dataB) -> tuple[str, dict]:
    """Return A if dataA has higher count, B otherwise, and A if they are the same

    Args:
        dataA (dict): data entry
        dataB (dict): data entry

    Returns:
        str: A (dataA) or B (dataB), depend on what has higher count 
        dict: the higher data entry
    """

    A_count, B_count = dataA['follower_count'], dataB['follower_count']
    if A_count >= B_count:
        return 'A', dataA
    return 'B', dataB


def HigherLowerGame(LIVES, data) -> None:
    score = 0
    lives = LIVES
    cur_data = get_item(data)
    data.remove(cur_data) # make sure this entry does not appear again
    game_should_continue = True
    player_choice = None # to save the last choice
    is_correct = None # to save the last choice
    while game_should_continue:
        utils.clear()
        print(art.LOGO)
        # print('==============================================================')
        # The PrettyTable
        ascii_table = PrettyTable(border=True, padding_width=1)
        art_A_fieldname = str("A".ljust(35))
        art_B_fieldname = str("B".ljust(35))
        art_C_fieldname = str("Record".ljust(15))
        ascii_table.field_names = [art_A_fieldname, art_B_fieldname, art_C_fieldname]
        ascii_table.align[art_A_fieldname] = 'l'
        ascii_table.align[art_B_fieldname] = 'l'
        ascii_table.align[art_C_fieldname] = 'l'
        # data entry for current data
        cur_descript = cur_data['description'].split(" ")[0]
        A_str = "\n" +\
                f"NAME      : {cur_data['name']}\n\n" +\
                f"FOLLOWERS : {cur_data['follower_count']}\n\n" +\
                f"CATEGORY  : {cur_descript}\n\n" +\
                f"COUNTRY   : {cur_data['country']}"
        # The Game Play
        # print(f'You have {lives} left!')
        new_data = get_item(data)
        data.remove(new_data) # make sure this entry does not appear again
        # data entry for new data
        new_descript = new_data['description'].split(" ")[0]
        B_str = "\n" +\
                f"NAME      : {new_data['name']}\n\n" +\
                f"FOLLOWERS : ????????\n\n" +\
                f"CATEGORY  : {new_descript}\n\n" +\
                f"COUNTRY   : {new_data['country']}"
        # the record column in the table
        C_str = "\n" +\
                f"LIVES        : {lives}\n\n" +\
                f"SCORES       : {score}\n\n" +\
                f"LAST CHOICE  : {player_choice} - {is_correct}\n\n"
        ascii_table.add_row([A_str, B_str, C_str])
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
        B_str = "\n" +\
                f"NAME      : {new_data['name']}\n\n" +\
                f"FOLLOWERS : {new_data['follower_count']}\n\n" +\
                f"CATEGORY  : {new_descript}\n\n" +\
                f"COUNTRY   : {new_data['country']}"
        C_str = "\n" +\
                f"LIVES        : {lives}\n\n" +\
                f"SCORES       : {score}\n\n" +\
                f"LAST CHOICE  : {player_choice} - {is_correct}\n\n"
        # table.field_names = [art_A_fieldname, art_B_fieldname, art_C_fieldname]
        ascii_table.add_row([A_str, B_str, C_str])
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
    HigherLowerGame(5, game_data.data)
