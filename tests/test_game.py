import unittest

from string import ascii_uppercase as base_letters

from src.game import Game

class TestGame(unittest.TestCase):

    def test_game_initialization(self):
        new_game = Game()
        grid = new_game.grid
        self.assertIsInstance(grid, list)
        self.assertEqual(len(grid), 9)
        for letter in grid:
            self.assertIn(letter, base_letters)
    
    def test_is_valid(self):
        new_game = Game()
        grid = new_game.grid
        false_grid = grid.copy()[:6]
        self.assertTrue(new_game.is_valid(grid))
        self.assertFalse(new_game.is_valid(false_grid))

    def test_unknown_word(self):
        new_game = Game()
        new_game.grid = "KWIENFUQW"
        self.assertIs(new_game.is_valid("FEUN"), False)