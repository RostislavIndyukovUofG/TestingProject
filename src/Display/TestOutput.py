from src.Display.IOuput import IOutput


class TestOutput(IOutput):

    def __init__(self):
        self.output_list = []

    def setOutputList(self, output_list):
        self.output_list = output_list

    def getOutputList(self):
        return self.output_list

    def displayOutput(self, output_message):
        user_output = self.output_list.append(output_message)
        return user_output