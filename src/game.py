from helpers import random_grid


# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods

class Game():

    def __init__(self):
        self.grid = random_grid()


    def is_valid(self, word):
        if len(word) != 9:
            return False
        for letter in word:
            if letter not in self.grid:
                return False
        return True
