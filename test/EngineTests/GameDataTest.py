import unittest

from src.Display.ConsoleInput import ConsoleInput
from src.Display.TestOutput import TestOutput
from src.Engine.Game import Game
from src.Engine.GameData import GameData


class GameDataTest(unittest.TestCase):
    user_input = ConsoleInput(False)
    user_output = TestOutput()

    game = Game("1", "Anno 1701", 8.99, 4)
    game2 = Game("2", "Metro 2033", 9.99, 5)
    game3 = Game("3", "Assassin's Creed Brotherhood", 26.99, 7)

    game_data = GameData(user_input, user_output)
    game_data.game_data_list = [game, game2, game3]

    def test_displayGameData(self):
        self.game_data.displayGameData()
        self.assertIn("Stock", self.user_output.output_list[-1])

    def test_getGameFromGameId(self):
        game = self.game_data.getGameFromGameId("1")
        self.assertEqual(self.game, game)

    def test_getMissingGameFromGameId(self):
        game = self.game_data.getGameFromGameId("-1")
        self.assertEqual(None, game)

    def test_getMultipleGamesFromGameId(self):
        game = self.game_data.getGameFromGameId("1")
        game2 = self.game_data.getGameFromGameId("2")
        game3 = self.game_data.getGameFromGameId("3")
        self.assertEqual(self.game3, game3)


if __name__ == '__main__':
    unittest.main()
