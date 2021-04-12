import unittest
from unittest.mock import MagicMock

from src.Data.DataInputFile import DataInputFile
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
                 ['1', 'City Builder', '8.99', '4'],
                 ['2', 'Survivalist', '9.99', '5']]

    def test_setGameDataMock(self):
        DataInputStub.getFileData = MagicMock(return_value=self.data_list)
        self.main.setGameData()
        self.assertEqual(2, len(self.main.game_data.getGameDataList()))

    def test_displayInitialMessage(self):
        self.main.displayInitialMessage()
        self.assertEqual("Welcome to the Game Store.", self.user_output.getOutputList()[-1])

    def test_setDataFromFoundFile(self):
        main = Main(DataInputFile(), self.user_input, self.user_output)
        main.setFilePath("../../resources/gameData.csv")
        main.setGameData()
        game_data_list = main.game_data.getGameDataList()
        game_name = game_data_list[0].getGameName()
        self.assertEqual('City Builder', game_name)

    def test_setDataFromMissingFile(self):
        main = Main(DataInputFile(), self.user_input, self.user_output)
        main.setFilePath("missing file")
        main.setGameData()
        output_message = "An error occurred when reading the file. Switching to stub data."
        self.assertEqual(output_message, self.user_output.output_list[-1])

    def test_setDataFromEmptyFile(self):
        main = Main(DataInputFile(), self.user_input, self.user_output)
        main.setFilePath("../../resources/emptyTestFile.csv")
        main.setGameData()
        output_message = "An error occurred when reading the file. Switching to stub data."
        self.assertEqual(output_message, self.user_output.output_list[-1])

    def test_setDataFromStub(self):
        main = Main(DataInputStub(), self.user_input, self.user_output)
        main.setGameData()
        game_data_list = main.game_data.getGameDataList()
        game_name = game_data_list[0].getGameName()
        self.assertEqual("X-Destroyer Video Game", game_name)


if __name__ == '__main__':
    unittest.main()
