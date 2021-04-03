from src.Display.IOuput import IOutput


class ConsoleOutput(IOutput):

    def __init__(self, write_to_file):
        self.write_to_file = write_to_file
        self.file_path = ""

    def setLogFilePath(self, file_path):
        self.file_path = file_path

    def initialiseLogFile(self):
        if self.write_to_file:
            with open(self.file_path, "w") as log:
                log.write("")

    def displayOutput(self, output_message):
        if self.write_to_file:
            with open(self.file_path, "a") as log:
                log.write(output_message + "\n")

        print(output_message)