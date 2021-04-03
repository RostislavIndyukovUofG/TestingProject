from src.Display.IInput import IInput


class TestInput(IInput):

    def __init__(self):
        self.input_list = []

    def setInputList(self, input_list):
        self.input_list = input_list

    def getInputList(self):
        return self.input_list

    def getInput(self, input_message):
        user_input = self.input_list.pop(0)
        return user_input