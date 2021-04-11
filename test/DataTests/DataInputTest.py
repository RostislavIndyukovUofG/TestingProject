import unittest

from src.Display.ConsoleInput import ConsoleInput
from src.Data.DataInputFile import DataInputFile
from src.Data.DataInputStub import DataInputStub
from src.Display.TestOutput import TestOutput
from src.Engine.Main import Main


class DataInputTest(unittest.TestCase):
    user_input = ConsoleInput(False)
    user_output = TestOutput()

    def test_readDataFromFoundFile(self):
        main = Main(DataInputFile(), self.user_input, self.user_output)
        main.setFilePath("../../resources/gameData.csv")
        main.initialiseHelperClasses()
        game_data_list = main.game_data.getGameDataList()
        game_name = game_data_list[0].getGameName()
        self.assertEqual('Anno 1701', game_name)

    def test_readDataFromMissingFile(self):
        main = Main(DataInputFile(), self.user_input, self.user_output)
        main.setFilePath("missing file")
        main.initialiseHelperClasses()
        output_message = "An error occurred when reading the file. Switching to stub data."
        self.assertEqual(output_message, self.user_output.output_list[-1])

    def test_readDataFromEmptyFile(self):
        main = Main(DataInputFile(), self.user_input, self.user_output)
        main.setFilePath("../../resources/emptyTestFile.csv")
        main.initialiseHelperClasses()
        output_message = "An error occurred when reading the file. Switching to stub data."
        self.assertEqual(output_message, self.user_output.output_list[-1])

    def test_readDataFromStub(self):
        main = Main(DataInputStub(), self.user_input, self.user_output)
        main.setFilePath("")
        main.initialiseHelperClasses()
        game_data_list = main.game_data.getGameDataList()
        game_name = game_data_list[0].getGameName()
        self.assertEqual("Xbox Video Game", game_name)


if __name__ == '__main__':
    unittest.main()
