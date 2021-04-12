import unittest

from src.Data.DataInputFile import DataInputFile
from src.Data.LogFileReader import LogFileReader
from src.Display.TestInput import TestInput
from src.Display.TestOutput import TestOutput
from src.Engine.Main import Main


class ConsoleInputTest(unittest.TestCase):
    input_list = LogFileReader.readFromLogFile("../../resources/IOLogs/InputLog.txt")
    output_list = LogFileReader.readFromLogFile("../../resources/IOLogs/OutputLog.txt")

    def test_userInputFaking(self):
        main = Main(DataInputFile(), TestInput(), TestOutput())
        main.user_input.setInputList(self.input_list)
        main.user_output.setOutputList(self.output_list)
        main.initialiseHelperClasses()
        main.displayInitialMessage()
        close = main.command_handler.handleUserCommands()
        self.assertEqual(self.output_list, main.user_output.output_list)


if __name__ == '__main__':
    unittest.main()
