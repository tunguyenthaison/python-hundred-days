""" The Higher-Lower game ASCII
"""
import art
import game_data
import random
import utils

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
    game_should_continue = True
    while game_should_continue:
        utils.clear()
        print(art.LOGO)
        print('==============================================================')
        print(f'You have {lives} left!')
        new_data = get_item(data)
        print(f"A. {cur_data['name']}, {cur_data['follower_count']} followers")
        print("v.s.")
        print(f"B. {new_data['name']}, ? followers")
        player_choice = input("Type A or B: ")
        right_choice, right_data = correct_choice(cur_data, new_data)
        if player_choice.lower()[0] == right_choice.lower():
            print('You guessed it correctly')
            print(f"B. {new_data['name']}, {new_data['follower_count']} followers")
            score += 1
        else:
            print('You guessed it wrongly')
            print(f"B. {new_data['name']}, {new_data['follower_count']} followers")
            lives -= 1
        cur_data = right_data
        if lives == 0:
            game_should_continue = False
    print(f"Out of lives! You have {score} points!")
    
if __name__ == "__main__":

    HigherLowerGame(5, game_data.data)
