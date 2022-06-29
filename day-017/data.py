""" Script to get new questions from Open Trivia API everytimne a new user plays
"""
import requests
import json
import re
from icecream import ic 


def get_questions_bank(url_API='https://opentdb.com/api.php?amount=10&type=boolean', amount=10, type='boolean') -> list:
    """ Get json data from the API, use `re` to change the amount in the API url

    Args:
        url_API (str): API url
        amount (int): number of questions, default to 10
        type (str): type of questions, dafault to 'boolean'

    Returns:
        list: data in format list[dict]
    """
    url_API = re.sub("[1-9][0-9]", str(amount), url_API, 1)
    response_API = requests.get(url_API)
    return response_API.json()['results']


if __name__ == "__main__":
    print(get_questions_bank(amount=2))
