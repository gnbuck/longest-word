import requests

from helpers import random_grid

# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods


class Game():

    def __init__(self):
        self.grid = random_grid()


    def is_valid(self, word):
        for letter in word:
            if letter not in self.grid:
                return False
        response = requests.get(f"https://wagon-dictionary.herokuapp.com/{word}")
        if response.json()["found"] is not True:
            return False
        return True
