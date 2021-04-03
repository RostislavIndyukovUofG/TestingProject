import unittest

from src.Data.DataInputFile import DataInputFile
from src.Data.LogFileReader import LogFileReader
from src.Display.TestInput import TestInput
from src.Display.TestOutput import TestOutput
from src.Engine.Main import Main


class ConsoleInputTest(unittest.TestCase):

    def test_UserInputFaking(self):
        main = Main(DataInputFile(), TestInput(), TestOutput())
        main.user_input.setInputList = LogFileReader.readFromLogFile("../../resources/IOLogs/InputLog.txt")
        main.user_input.setOutputList = LogFileReader.readFromLogFile("../../resources/IOLogs/OutputLog.txt")
        main.setGameDataAndHeader()
        main.displayInitialMessage()
        main.command_handler.handleUserCommands()

        self.assertEqual(True, False)



if __name__ == '__main__':
    unittest.main()
