import unittest

from src.Data.DataInputFile import DataInputFile
from src.Data.LogFileReader import LogFileReader
from src.Display.TestInput import TestInput
from src.Display.TestOutput import TestOutput
from src.Engine.Main import Main


class ConsoleInputTest(unittest.TestCase):
    input_list = LogFileReader.readFromLogFile("../../resources/IOLogs/InputLog.txt")
    output_list = LogFileReader.readFromLogFile("../../resources/IOLogs/OutputLog.txt")

    main = Main(DataInputFile(), TestInput(), TestOutput())
    main.user_input.setInputList(input_list)
    main.user_output.setOutputList(output_list)

    def test_userInputFaking(self):
        self.main.initialiseHelperClasses()
        self.main.displayInitialMessage()
        close = self.main.command_handler.handleUserCommands()
        self.assertEqual(self.output_list, self.main.user_output.output_list)


if __name__ == '__main__':
    unittest.main()
