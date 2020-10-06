from random import choice

from string import ascii_uppercase as base_letters

def random_grid():
    grid = []
    for _ in range(9):
        grid.append(choice(base_letters))
    return grid
