from src.Display.IInput import IInput


class ConsoleOutput(IInput):

    def __init__(self):
        self.output_list = []

    def setInputList(self, output_list):
        self.output_list = output_list

    def getInput(self, input_message):
        user_output = self.output_list.pop(0)

        return user_output