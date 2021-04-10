import unittest
from unittest.mock import MagicMock

from src.Data.DataInputStub import DataInputStub
from src.Display.ConsoleInput import ConsoleInput
from src.Display.TestOutput import TestOutput
from src.Engine.Main import Main


class MainTest(unittest.TestCase):
    input_type = DataInputStub()
    user_input = ConsoleInput(False)
    user_output = TestOutput()
    main = Main(input_type, user_input, user_output)

    data_list = [['GameID', 'Game Name', 'Price', 'Stock'],
                 ['1', 'Anno 1701', '8.99', '4'],
                 ['2', 'Metro 2033', '9.99', '5']]

    def test_setGameDataMock(self):
        DataInputStub.getFileData = MagicMock(return_value=self.data_list)
        self.main.setGameDataAndHeader()
        self.assertEqual(2, len(self.main.game_data.game_data_list))

    def test_setHeaderMock(self):
        DataInputStub.getFileData = MagicMock(return_value=self.data_list)
        self.main.setGameDataAndHeader()
        self.assertEqual(self.data_list[0], self.main.header)

    def test_displayInitialMessage(self):
        self.main.displayInitialMessage()
        self.assertEqual("Welcome to the Game Store.", self.user_output.output_list[-1])


if __name__ == '__main__':
    unittest.main()
