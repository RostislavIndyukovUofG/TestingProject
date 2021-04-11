import unittest

from src.Display.TestOutput import TestOutput
from src.Engine.Game import Game


class GameTest(unittest.TestCase):
    user_output = TestOutput()

    game = Game({"Game Id": "1", "Game Name": "Anno 1701", "Price": 8.99, "Stock": 4})
    game2 = Game({"Game Id": "2", "Game Name": "Metro 2033", "Price": 9.99, "Stock": 5})
    game3 = Game({"Game Id": "3", "Game Name": "Assassin's Creed Brotherhood", "Price": 26.99, "Stock": 7})

    def test_reduceStock(self):
        game_details = {"Game Id": "1", "Game Name": "Anno 1701", "Price": 8.99, "Stock": 4}
        game = Game(game_details)
        game.reduceStock()
        self.assertEqual(3, game.getStock())

    def test_reduceStockFrom0(self):
        game_details = {"Game Id": "1", "Game Name": "Anno 1701", "Price": 8.99, "Stock": 0}
        game = Game(game_details)
        game.reduceStock()
        self.assertEqual(0, game.getStock())

    def test_reduceMultipleStocks(self):
        game_details = {"Game Id": "1", "Game Name": "Anno 1701", "Price": 8.99, "Stock": 4}
        game_details2 = {"Game Id": "2", "Game Name": "Metro 2033", "Price": 9.99, "Stock": 5}
        game_details3 = {"Game Id": "3", "Game Name": "Assassin's Creed Brotherhood", "Price": 26.99, "Stock": 7}
        game = Game(game_details)
        game2 = Game(game_details2)
        game3 = Game(game_details3)
        game.reduceStock()
        game2.reduceStock()
        game3.reduceStock()
        self.assertEqual(6, game3.getStock())

    def test_displayGameDetails(self):
        self.game.displayGameDetails(self.user_output)
        self.assertIn("Stock", self.user_output.getOutputList()[-1])

    def test_displayGameDetailsWithStock0(self):
        game_details = {"Game Id": "1", "Game Name": "Anno 1701", "Price": 8.99, "Stock": 0}
        game = Game(game_details)
        output_list_size = len(self.user_output.getOutputList())
        game.displayGameDetails(self.user_output)
        self.assertEqual(output_list_size, len(self.user_output.getOutputList()))

    def test_displayMultipleGameDetails(self):
        self.game.displayGameDetails(self.user_output)
        self.game2.displayGameDetails(self.user_output)
        self.game3.displayGameDetails(self.user_output)
        self.assertIn("7", self.user_output.getOutputList()[-1])

    def test_displayGame(self):
        self.game.displayGame(self.user_output)
        self.assertIn("Anno", self.user_output.getOutputList()[-1])

    def test_displayMultipleGames(self):
        game_name = "Assassin's Creed Brotherhood"
        self.game.displayGame(self.user_output)
        self.game2.displayGame(self.user_output)
        self.game3.displayGame(self.user_output)
        self.assertIn(game_name, self.user_output.getOutputList()[-1])


if __name__ == '__main__':
    unittest.main()
