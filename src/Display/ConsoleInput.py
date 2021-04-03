from src.Display.IInput import IInput


class ConsoleInput(IInput):

    def __init__(self, write_to_file):
        self.write_to_file = write_to_file
        self.file_path = ""

    def setLogFilePath(self, file_path):
        self.file_path = file_path

    def initialiseLogFile(self):
        if self.write_to_file:
            with open(self.file_path, "w") as log:
                log.write("")

    def getInput(self, input_message):
        user_input = input(input_message)

        if self.write_to_file:
            with open(self.file_path, "a") as log:
                log.write(input_message + "\n")

        return user_input