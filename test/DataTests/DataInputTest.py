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
        main.setDataFilePath(file_path)
        main.setGameDataAndHeader()
        game_name = main.getGameData()[0].getGameName()
        self.assertEqual('Anno 1701', game_name)

    def test_readDataFromMissingFile(self):
        main = Main(DataInputFile(), self.user_input, self.user_output)
        file_path = "missing file"
        main.setDataFilePath(file_path)
        main.setGameDataAndHeader()
        output_message = "An error occurred. Switching to stub data."
        self.assertEqual(output_message, self.user_output.getOutputList()[-1])

    def test_readDataFromEmptyFile(self):
        main = Main(DataInputFile(), self.user_input, self.user_output)
        file_path = "../../resources/emptyTestFile.csv"
        main.setDataFilePath(file_path)
        main.setGameDataAndHeader()
        output_message = "An error occurred. Switching to stub data."
        self.assertEqual(output_message, self.user_output.getOutputList()[-1])

    def test_readDataFromStub(self):
        main = Main(DataInputStub(), self.user_input, self.user_output)
        main.setDataFilePath("")
        main.setGameDataAndHeader()
        game_name = main.getGameData()[0].getGameName()
        self.assertEqual("Xbox Video Game", game_name)


if __name__ == '__main__':
    unittest.main()
