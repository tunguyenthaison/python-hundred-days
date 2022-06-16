"""The secret auction program
"""
from tomlkit import key
from utils import LOGO, validate_number, clear
from icecream import ic


def auction_input() -> dict[str: int]:
    """ The input part of the secret auction program

    Returns:
        dict[str: int]: (key, value) = (name, bid value)
    """
    print(LOGO)
    print("Welcome to the secret auction program!")
    all_bids = {}
    is_done = False
    while not is_done:
        clear()
        print(LOGO)
        print(f"Number of bidders: {len(all_bids)}")
        name = input("What is your name?: ")
        bid = validate_number("What is your bid? ", "Oops, not a valid bid, try again...")
        all_bids[name] = bid

        # getting valid yes/no to continue to other bidder
        valid_yesno = False
        while not valid_yesno:
            is_continue = input("Are there any other bidders? Type 'yes' or 'no': ")[0]
            if is_continue in ['y', 'n']:
                valid_yesno = True
        # stop the while loop
        if is_continue == 'n':
            is_done = True
    return all_bids


def auction() -> dict[str: int]:
    """ The secret auction program

    Returns:
        dict[str: int]: (key, value) = (name, bid value) with only one bidder
    """
    all_bids_dict = auction_input()
    ic("Got here")
    ic(all_bids_dict)
    ic(all_bids_dict.values())
    max_bid_value = max(list(all_bids_dict.values()))
    ic(max_bid_value)
    max_bids_dict = {key: value for (key, value) in all_bids_dict.items() if value == max_bid_value}
    while len(max_bids_dict) > 1:
        print("There is a tie, enter a new round of bidding for those who are tie only!")
        for bidder in max_bids_dict.keys():
            new_bid = validate_number(f"Please enter a new bid for {bidder}: ",
                                        "Oops, not a valid bid, try again.")
            max_bids_dict[bidder] = new_bid
            ic(bidder, new_bid)
        max_bid_value = max(list(max_bids_dict.values()))
        temp_dict = {key: value for (key, value) in max_bids_dict.items() if value == max_bid_value}
        max_bids_dict = temp_dict
        ic(max_bids_dict)
    return max_bids_dict

if __name__ == "__main__":
    result = list(auction().items())
    key, value = result[0]
    print(f"The max bidder is {key}, with value {value}!")
