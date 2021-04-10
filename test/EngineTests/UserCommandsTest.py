import unittest

from src.Display.TestOutput import TestOutput
from src.Engine.UserCommands import UserCommands


class UserCommandsTest(unittest.TestCase):
    user_output = TestOutput()

    def test_displayCommands(self):
        command_count = len(UserCommands)
        UserCommands.displayCommands(self.user_output)
        self.assertEqual(command_count + 1, len(self.user_output.getOutputList()))


if __name__ == '__main__':
    unittest.main()
