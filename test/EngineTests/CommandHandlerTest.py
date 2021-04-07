import unittest

from src.Data.DataInputStub import DataInputStub
from src.Display.TestInput import TestInput
from src.Display.TestOutput import TestOutput
from src.Engine.Game import Game
from src.Engine.Main import Main


class CommandHandlerTest(unittest.TestCase):
    input_type = DataInputStub()
    user_input = TestInput()
    user_output = TestOutput()

    main = Main(input_type, user_input, user_output)
    main.initialiseHelperClasses()

    # handleCommand

    def test_handleValidListCommandOutput(self):
        self.main.user_input.input_list = ["list", "exit"]
        close = self.main.command_handler.handleUserCommands()
        self.assertIn("Stock", self.main.user_output.getOutputList()[-2])

    def test_handleInvalidListCommandOutput(self):
        self.main.user_input.input_list = ["list 1", "exit"]
        close = self.main.command_handler.handleUserCommands()
        output_message = "Invalid command. Type help to see available commands."
        self.assertEqual(output_message, self.main.user_output.getOutputList()[-2])

    def test_handleValidAddCommand(self):
        self.main.user_input.input_list = ["add 1", "exit"]
        self.main.basket.basket_list = []
        basket_size = len(self.main.basket.basket_list)
        close = self.main.command_handler.handleUserCommands()
        self.assertEqual(basket_size + 1, len(self.main.basket.basket_list))

    def test_handleValidAddCommandOutput(self):
        self.main.user_input.input_list = ["add 1", "exit"]
        self.main.basket.basket_list = []
        close = self.main.command_handler.handleUserCommands()
        self.assertEqual("Game added successfully.", self.main.user_output.getOutputList()[-2])

    def test_handleInvalidAddCommand(self):
        self.main.user_input.input_list = ["add", "exit"]
        self.main.basket.basket_list = []
        basket_size = len(self.main.basket.basket_list)
        close = self.main.command_handler.handleUserCommands()
        self.assertEqual(basket_size, len(self.main.basket.basket_list))

    def test_handleOutOfBoundsAddCommand(self):
        self.main.user_input.input_list = ["add -1", "exit"]
        self.main.basket.basket_list = []
        basket_size = len(self.main.basket.basket_list)
        close = self.main.command_handler.handleUserCommands()
        self.assertEqual(basket_size, len(self.main.basket.basket_list))

    def test_handleInvalidAddCommandOutput(self):
        self.main.user_input.input_list = ["add", "exit"]
        self.main.basket.basket_list = []
        close = self.main.command_handler.handleUserCommands()
        output_message = "Invalid command. Type help to see available commands."
        self.assertEqual(output_message, self.main.user_output.getOutputList()[-2])

    def test_handleValidRemoveCommand(self):
        self.main.basket.updateBasket(self.main.game_data.game_data_list[0], "add")
        self.main.user_input.input_list = ["remove 1", "exit"]
        basket_size = len(self.main.basket.basket_list)
        close = self.main.command_handler.handleUserCommands()
        self.assertEqual(basket_size - 1, len(self.main.basket.basket_list))

    def test_handleValidRemoveCommandOutput(self):
        self.main.basket.updateBasket(self.main.game_data.game_data_list[0], "add")
        self.main.user_input.input_list = ["remove 1", "exit"]
        close = self.main.command_handler.handleUserCommands()
        self.assertEqual("Game removed successfully.", self.main.user_output.getOutputList()[-2])

    def test_handleInvalidRemoveCommand(self):
        self.main.user_input.input_list = ["remove 1", "exit"]
        self.main.basket.basket_list = []
        basket_size = len(self.main.basket.basket_list)
        close = self.main.command_handler.handleUserCommands()
        self.assertEqual(basket_size, len(self.main.basket.basket_list))

    def test_handleInvalidRemoveCommandOutput(self):
        self.main.user_input.input_list = ["remove 1", "exit"]
        self.main.basket.basket_list = []
        close = self.main.command_handler.handleUserCommands()
        self.assertEqual("Game not in basket.", self.main.user_output.getOutputList()[-2])

    def test_handleOutOfBoundsRemoveCommandOutput(self):
        self.main.user_input.input_list = ["remove -1", "exit"]
        self.main.basket.basket_list = []
        close = self.main.command_handler.handleUserCommands()
        output_message = "Invalid game id. Type list to view the available games."
        self.assertEqual(output_message, self.main.user_output.getOutputList()[-3])

    def test_handleValidBasketCommandOutput(self):
        self.main.user_input.input_list = ["basket", "exit"]
        self.main.basket.basket_list = []
        self.main.basket.calcualateBasketTotal()
        close = self.main.command_handler.handleUserCommands()
        self.assertEqual("Basket total: £0.0", self.main.user_output.getOutputList()[-2])

    def test_handleValidPurchaseCommand(self):
        self.main.basket.updateBasket(self.main.game_data.game_data_list[0], "add")
        self.main.user_input.input_list = ["purchase", "exit"]
        close = self.main.command_handler.handleUserCommands()
        self.assertIn("Xbox Video Game", self.main.user_output.getOutputList()[-2])

    def test_handleValidPurchaseCommandWithEmptyBasketOutput(self):
        self.main.user_input.input_list = ["purchase", "exit"]
        self.main.basket.basket_list = []
        close = self.main.command_handler.handleUserCommands()
        self.assertEqual("Your basket is emtpy.", self.main.user_output.getOutputList()[-2])

    def test_handleInvalidPurchaseCommand(self):
        self.main.user_input.input_list = ["purchase 1", "exit"]
        basket_size = len(self.main.basket.basket_list)
        close = self.main.command_handler.handleUserCommands()
        self.assertEqual(basket_size, len(self.main.basket.basket_list))

    def test_handleInvalidPurchaseCommandOutput(self):
        self.main.user_input.input_list = ["purchase 1", "exit"]
        close = self.main.command_handler.handleUserCommands()
        output_message = "Invalid command. Type help to see available commands."
        self.assertEqual(output_message, self.main.user_output.getOutputList()[-2])

    def test_handleValidHelpCommandOutput(self):
        self.main.user_input.input_list = ["help", "exit"]
        close = self.main.command_handler.handleUserCommands()
        self.assertIn("leave program", self.main.user_output.getOutputList()[-2])

    def test_handleInvalidHelpCommandOutput(self):
        self.main.user_input.input_list = ["help 1", "exit"]
        close = self.main.command_handler.handleUserCommands()
        output_message = "Invalid command. Type help to see available commands."
        self.assertIn(output_message, self.main.user_output.getOutputList()[-2])

    def test_handleValidExitCommandOutput(self):
        self.main.user_input.input_list = ["exit"]
        close = self.main.command_handler.handleUserCommands()
        self.assertIn("Closing program.", self.main.user_output.getOutputList()[-1])

    def test_handleInvalidExitCommandOutput(self):
        self.main.user_input.input_list = ["exit 1", "exit"]
        close = self.main.command_handler.handleUserCommands()
        output_message = "Invalid command. Type help to see available commands."
        self.assertIn(output_message, self.main.user_output.getOutputList()[-2])

    def test_handleValidCommandAlternative(self):
        self.main.user_input.input_list = ["e"]
        close = self.main.command_handler.handleUserCommands()
        output_message = "Invalid command. Type help to see available commands."
        self.assertIn("Closing program.", self.main.user_output.getOutputList()[-1])

    def test_handleValidCommandWithSpaces(self):
        self.main.user_input.input_list = ["      exit      "]
        close = self.main.command_handler.handleUserCommands()
        output_message = "Invalid command. Type help to see available commands."
        self.assertIn("Closing program.", self.main.user_output.getOutputList()[-1])

    def test_handleMultipleCommandsWithSpaces(self):
        self.main.user_input.input_list = ["ad 1", "add 1", " buy", "e"]
        close = self.main.command_handler.handleUserCommands()
        output_message = "Invalid command. Type help to see available commands."
        self.assertIn("Closing program.", self.main.user_output.getOutputList()[-1])


if __name__ == '__main__':
    unittest.main()
