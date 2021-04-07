import unittest

from src.Data.DataInputFile import DataInputFile
from src.Display.TestInput import TestInput
from src.Display.TestOutput import TestOutput
from src.Engine.Basket import Basket
from src.Engine.CommandHandler import CommandHandler
from src.Engine.Game import Game
from src.Engine.Main import Main


class CommandHandlerTest(unittest.TestCase):
    input_type = DataInputFile()
    user_input = TestInput()
    user_output = TestOutput()

    game = Game("1", "Anno 1701", 8.99, 4)

    # handleCommand

    def test_handleValidListCommandOutput(self):
        main = Main(self.input_type, self.user_input, self.user_output)
        main.initialiseHelperClasses()
        main.user_input.input_list = ["list", "exit"]
        basket = Basket(self.user_input, self.user_output, main.game_data)
        main.game_data.game_data_list.append(self.game)
        command_handler = CommandHandler(self.user_input, self.user_output, basket, main.game_data)
        close = command_handler.handleUserCommands()
        print(main.user_output.getOutputList()[-2])
        self.assertEqual("Stock:\t4", main.user_output.getOutputList()[-2])


if __name__ == '__main__':
    unittest.main()
