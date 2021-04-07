import unittest

from src.Data.DataInputFile import DataInputFile
from src.Data.LogFileReader import LogFileReader
from src.Display.TestInput import TestInput
from src.Display.TestOutput import TestOutput
from src.Engine.Main import Main


class ConsoleInputTest(unittest.TestCase):

    def test_UserInputFaking(self):
        main = Main(DataInputFile(), TestInput(), TestOutput())
        input_list = LogFileReader.readFromLogFile("../../resources/IOLogs/InputLog.txt")
        main.user_input.setInputList(input_list)
        output_list = LogFileReader.readFromLogFile("../../resources/IOLogs/OutputLog.txt")
        main.user_output.setOutputList(output_list)
        main.setGameDataAndHeader()
        main.displayInitialMessage()
        close = main.command_handler.handleUserCommands()
        self.assertEqual(output_list, main.user_output.getOutputList())


if __name__ == '__main__':
    unittest.main()
