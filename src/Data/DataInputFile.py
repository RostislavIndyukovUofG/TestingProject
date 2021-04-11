import csv

from src.Data.DataInputStub import DataInputStub
from src.Data.IDataInput import IDataInput


class DataInputFile(IDataInput):

    def readRawData(self, file_path):
        file_data = []

        with open(file_path, "r") as file:
            file_reader = csv.reader(file)

            for row in file_reader:
                file_data.append(row)

        return file_data

    def getFileData(self, file_path, user_output):
        file_data = []

        try:
            file_data = self.readRawData(file_path)

            if len(file_data) == 0:
                raise Exception

        except (FileNotFoundError, Exception):
            user_output.displayOutput("An error occurred. Switching to stub data.")
            stub = DataInputStub()
            file_data = stub.readRawData(file_path)
        finally:
            return file_data
