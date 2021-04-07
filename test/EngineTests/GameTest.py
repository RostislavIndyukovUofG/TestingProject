import unittest

from src.Display.TestOutput import TestOutput
from src.Engine.Game import Game


class GameTest(unittest.TestCase):
    user_output = TestOutput()

    game = Game("1", "Anno 1701", 8.99, 4)
    game2 = Game("2", "Metro 2033", 9.99, 5)
    game3 = Game("3", "Assassin's Creed Brotherhood", 26.99, 7)

    def test_reduceStock(self):
        game = Game("1", "Anno 1701", 8.99, 4)
        game.reduceStock()
        self.assertEqual(3, game.stock)

    def test_reduceStockFrom0(self):
        game = Game("1", "Anno 1701", 8.99, 0)
        game.reduceStock()
        self.assertEqual(0, game.stock)

    def test_reduceMultipleStocks(self):
        game = Game("1", "Anno 1701", 8.99, 4)
        game2 = Game("2", "Metro 2033", 9.99, 5)
        game3 = Game("3", "Assassin's Creed Brotherhood", 26.99, 7)
        game.reduceStock()
        game2.reduceStock()
        game3.reduceStock()
        self.assertEqual(6, game3.stock)

    def test_displayGameDetails(self):
        self.game.displayGameDetails(self.user_output)
        self.assertIn("Stock", self.user_output.output_list[-1])

    def test_displayMultipleGameDetails(self):
        self.game.displayGameDetails(self.user_output)
        self.game2.displayGameDetails(self.user_output)
        self.game3.displayGameDetails(self.user_output)
        self.assertIn("7", self.user_output.output_list[-1])

    def test_displayGame(self):
        self.game.displayGame(self.user_output)
        self.assertIn("Anno", self.user_output.output_list[-1])

    def test_displayMultipleGames(self):
        self.game.displayGame(self.user_output)
        self.game2.displayGame(self.user_output)
        self.game3.displayGame(self.user_output)
        game_name = "Assassin's Creed Brotherhood"
        self.assertIn(game_name, self.user_output.output_list[-1])


if __name__ == '__main__':
    unittest.main()
