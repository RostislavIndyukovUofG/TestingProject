import unittest

from src.Display.TestInput import TestInput
from src.Display.TestOutput import TestOutput
from src.Engine.CommandHandler import CommandHandler
from src.Engine.Game import Game
from src.Engine.GameData import GameData


class CommandHandlerTest(unittest.TestCase):
    user_input = TestInput()
    user_output = TestOutput()

    game = Game({"Game Id": "1", "Game Name": "Anno 1701", "Price": 8.99, "Stock": 4})
    game2 = Game({"Game Id": "2", "Game Name": "Metro 2033", "Price": 9.99, "Stock": 5})
    game3 = Game({"Game Id": "3", "Game Name": "Assassin's Creed Brotherhood", "Price": 26.99, "Stock": 7})

    game_data = GameData(user_input, user_output)
    game_data.game_data_list = [game, game2, game3]
    command_handler = CommandHandler(user_input, user_output, game_data)
    basket = command_handler.basket

    def test_handleValidListCommandOutput(self):
        self.user_input.setInputList(["list", "exit"])
        close = self.command_handler.handleUserCommands()
        self.assertIn("Stock", self.user_output.getOutputList()[-2])

    def test_handleInvalidListCommandOutput(self):
        output_message = "Invalid command. Type help to see available commands."

        self.user_input.setInputList(["list 1", "exit"])
        close = self.command_handler.handleUserCommands()
        self.assertEqual(output_message, self.user_output.getOutputList()[-2])

    def test_handleValidAddCommand(self):
        self.user_input.setInputList(["add 1", "exit"])
        self.basket.setBasketList([])
        basket_size = len(self.basket.getBasketList())
        close = self.command_handler.handleUserCommands()
        self.assertEqual(basket_size + 1, len(self.basket.getBasketList()))

    def test_handleValidAddCommandOutput(self):
        self.user_input.setInputList(["add 1", "exit"])
        self.basket.setBasketList([])
        close = self.command_handler.handleUserCommands()
        self.assertEqual("Game added successfully.", self.user_output.getOutputList()[-2])

    def test_handleInvalidAddCommand(self):
        self.user_input.setInputList(["add", "exit"])
        self.basket.setBasketList([])
        basket_size = len(self.basket.getBasketList())
        close = self.command_handler.handleUserCommands()
        self.assertEqual(basket_size, len(self.basket.getBasketList()))

    def test_handleOutOfBoundsAddCommand(self):
        self.user_input.setInputList(["add -1", "exit"])
        self.basket.setBasketList([])
        basket_size = len(self.basket.getBasketList())
        close = self.command_handler.handleUserCommands()
        self.assertEqual(basket_size, len(self.basket.getBasketList()))

    def test_handleInvalidAddCommandOutput(self):
        self.user_input.setInputList(["add", "exit"])
        self.basket.setBasketList([])
        close = self.command_handler.handleUserCommands()
        output_message = "Invalid command. Type help to see available commands."
        self.assertEqual(output_message, self.user_output.getOutputList()[-2])

    def test_handleValidRemoveCommand(self):
        self.basket.updateBasket(self.game_data.getGameDataList()[0], "add")
        self.user_input.setInputList(["remove 1", "exit"])
        basket_size = len(self.basket.getBasketList())
        close = self.command_handler.handleUserCommands()
        self.assertEqual(basket_size - 1, len(self.basket.getBasketList()))

    def test_handleValidRemoveCommandOutput(self):
        self.basket.updateBasket(self.game_data.getGameDataList()[0], "add")
        self.user_input.setInputList(["remove 1", "exit"])
        close = self.command_handler.handleUserCommands()
        self.assertEqual("Game removed successfully.", self.user_output.getOutputList()[-2])

    def test_handleInvalidRemoveCommand(self):
        self.user_input.setInputList(["remove 1", "exit"])
        self.basket.setBasketList([])
        basket_size = len(self.basket.getBasketList())
        close = self.command_handler.handleUserCommands()
        self.assertEqual(basket_size, len(self.basket.getBasketList()))

    def test_handleInvalidRemoveCommandOutput(self):
        self.user_input.setInputList(["remove 1", "exit"])
        self.basket.setBasketList([])
        close = self.command_handler.handleUserCommands()
        self.assertEqual("Game not in basket.", self.user_output.getOutputList()[-2])

    def test_handleOutOfBoundsRemoveCommandOutput(self):
        self.user_input.setInputList(["remove -1", "exit"])
        self.basket.setBasketList([])
        close = self.command_handler.handleUserCommands()
        output_message = "Invalid game id. Type list to view the available games."
        self.assertEqual(output_message, self.user_output.getOutputList()[-2])

    def test_handleValidBasketCommandOutput(self):
        self.user_input.setInputList(["basket", "exit"])
        self.basket.setBasketList([])
        self.basket.calcualateBasketTotal()
        close = self.command_handler.handleUserCommands()
        self.assertEqual("\nTotal: £0.0", self.user_output.getOutputList()[-2])

    def test_handleValidPurchaseCommand(self):
        self.basket.updateBasket(self.game_data.getGameDataList()[0], "add")
        self.user_input.setInputList(["purchase", "exit"])
        close = self.command_handler.handleUserCommands()
        output_message = "\nThank you for your purchase!\n"
        self.assertIn(output_message, self.user_output.getOutputList()[-2])

    def test_handleValidPurchaseCommandWithEmptyBasketOutput(self):
        self.user_input.setInputList(["purchase", "exit"])
        self.basket.setBasketList([])
        close = self.command_handler.handleUserCommands()
        self.assertEqual("Your basket is emtpy.", self.user_output.getOutputList()[-2])

    def test_handleInvalidPurchaseCommand(self):
        self.user_input.setInputList(["purchase 1", "exit"])
        basket_size = len(self.basket.getBasketList())
        close = self.command_handler.handleUserCommands()
        self.assertEqual(basket_size, len(self.basket.getBasketList()))

    def test_handleInvalidPurchaseCommandOutput(self):
        self.user_input.setInputList(["purchase 1", "exit"])
        close = self.command_handler.handleUserCommands()
        output_message = "Invalid command. Type help to see available commands."
        self.assertEqual(output_message, self.user_output.getOutputList()[-2])

    def test_handleValidHelpCommandOutput(self):
        self.user_input.setInputList(["help", "exit"])
        close = self.command_handler.handleUserCommands()
        self.assertIn("leave program", self.user_output.getOutputList()[-2])

    def test_handleInvalidHelpCommandOutput(self):
        self.user_input.setInputList(["help 1", "exit"])
        close = self.command_handler.handleUserCommands()
        output_message = "Invalid command. Type help to see available commands."
        self.assertIn(output_message, self.user_output.getOutputList()[-2])

    def test_handleValidExitCommandOutput(self):
        self.user_input.setInputList(["exit"])
        close = self.command_handler.handleUserCommands()
        self.assertIn("Closing program.", self.user_output.getOutputList()[-1])

    def test_handleInvalidExitCommandOutput(self):
        self.user_input.setInputList(["exit 1", "exit"])
        close = self.command_handler.handleUserCommands()
        output_message = "Invalid command. Type help to see available commands."
        self.assertIn(output_message, self.user_output.getOutputList()[-2])

    def test_handleValidCommandAlternative(self):
        self.user_input.setInputList(["e"])
        close = self.command_handler.handleUserCommands()
        self.assertIn("Closing program.", self.user_output.getOutputList()[-1])

    def test_handleValidCommandWithSpaces(self):
        self.user_input.setInputList(["      exit      "])
        close = self.command_handler.handleUserCommands()
        self.assertIn("Closing program.", self.user_output.getOutputList()[-1])

    def test_handleMultipleCommandsWithSpaces(self):
        self.user_input.setInputList(["ad 1", "add 1", " buy", "e"])
        close = self.command_handler.handleUserCommands()
        self.assertIn("Closing program.", self.user_output.getOutputList()[-1])


if __name__ == '__main__':
    unittest.main()
