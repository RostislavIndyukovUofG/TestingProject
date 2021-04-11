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
        file_path = "../../resources/gameData.csv"
        main.file_path = file_path
        main.initialiseHelperClasses()
        game_name = main.game_data.game_data_list[0].game_name
        self.assertEqual('Anno 1701', game_name)

    def test_readDataFromMissingFile(self):
        main = Main(DataInputFile(), self.user_input, self.user_output)
        file_path = "missing file"
        main.file_path = file_path
        main.initialiseHelperClasses()
        output_message = "An error occurred when reading the file. Switching to stub data."
        self.assertEqual(output_message, self.user_output.output_list[-1])

    def test_readDataFromEmptyFile(self):
        main = Main(DataInputFile(), self.user_input, self.user_output)
        file_path = "../../resources/emptyTestFile.csv"
        main.file_path = file_path
        main.initialiseHelperClasses()
        output_message = "An error occurred when reading the file. Switching to stub data."
        self.assertEqual(output_message, self.user_output.output_list[-1])

    def test_readDataFromStub(self):
        main = Main(DataInputStub(), self.user_input, self.user_output)
        main.file_path = ""
        main.initialiseHelperClasses()
        game_name = main.game_data.game_data_list[0].game_name
        self.assertEqual("Xbox Video Game", game_name)


if __name__ == '__main__':
    unittest.main()
