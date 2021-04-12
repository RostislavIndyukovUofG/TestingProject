import unittest

from src.Display.ConsoleInput import ConsoleInput
from src.Data.DataInputFile import DataInputFile
from src.Data.DataInputStub import DataInputStub
from src.Display.TestOutput import TestOutput


class DataInputTest(unittest.TestCase):
    user_input = ConsoleInput(False)
    user_output = TestOutput()

    def test_readDataFromFoundFile(self):
        input_type = DataInputFile()
        file_data = input_type.getFileData("../../resources/gameData.csv", self.user_output)
        game_name = file_data[1][1]
        self.assertEqual('City Builder', game_name)

    def test_readDataFromMissingFile(self):
        input_type = DataInputFile()
        file_data = input_type.getFileData("missing file", self.user_output)
        output_message = "An error occurred when reading the file. Switching to stub data."
        self.assertEqual(output_message, self.user_output.output_list[-1])

    def test_readDataFromEmptyFile(self):
        input_type = DataInputFile()
        file_data = input_type.getFileData("../../resources/emptyTestFile.csv", self.user_output)
        output_message = "An error occurred when reading the file. Switching to stub data."
        self.assertEqual(output_message, self.user_output.output_list[-1])

    def test_readDataFromStub(self):
        input_type = DataInputStub()
        file_data = input_type.getFileData("", self.user_output)
        game_name = file_data[1][1]
        self.assertEqual("X-Destroyer Video Game", game_name)


if __name__ == '__main__':
    unittest.main()
