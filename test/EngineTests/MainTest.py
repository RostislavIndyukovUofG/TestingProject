import unittest

from src.Data.DataInputFile import DataInputFile
from src.Data.DataInputStub import DataInputStub
from src.Display.ConsoleInput import ConsoleInput
from src.Display.TestOutput import TestOutput
from src.Engine.Main import Main


class MainTest(unittest.TestCase):
    user_input = ConsoleInput(False)
    user_output = TestOutput()

    def test_displayInitialMessage(self):
        main = Main(DataInputStub(), self.user_input, self.user_output)
        main.displayInitialMessage()
        self.assertEqual("Welcome to the Game Store.", self.user_output.getOutputList()[-1])

    def test_setGameDataFromFoundFile(self):
        main = Main(DataInputFile(), self.user_input, self.user_output)
        main.setFilePath("../../resources/gameData.csv")
        main.setGameData()
        game_data_list = main.game_data.getGameDataList()
        game_name = game_data_list[0].getGameName()
        self.assertEqual('City Builder', game_name)

    def test_setGameDataFromMissingFile(self):
        main = Main(DataInputFile(), self.user_input, self.user_output)
        main.setFilePath("missing file")
        main.setGameData()
        output_message = "An error occurred when reading the file. Switching to stub data."
        self.assertEqual(output_message, self.user_output.output_list[-1])

    def test_setGameDataFromEmptyFile(self):
        main = Main(DataInputFile(), self.user_input, self.user_output)
        main.setFilePath("../../resources/emptyTestFile.csv")
        main.setGameData()
        output_message = "An error occurred when reading the file. Switching to stub data."
        self.assertEqual(output_message, self.user_output.output_list[-1])

    def test_setGameDataFromStub(self):
        main = Main(DataInputStub(), self.user_input, self.user_output)
        main.setGameData()
        game_data_list = main.game_data.getGameDataList()
        game_name = game_data_list[0].getGameName()
        self.assertEqual("X-Destroyer Video Game", game_name)

    def test_setGameDataFromStubListLength(self):
        main = Main(DataInputStub(), self.user_input, self.user_output)
        main.setGameData()
        self.assertEqual(3, len(main.game_data.getGameDataList()))


if __name__ == '__main__':
    unittest.main()
