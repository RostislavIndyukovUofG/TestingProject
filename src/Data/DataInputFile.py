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

    def getGameDataAndHeader(self, file_path, user_output):
        try:
            file_data = self.readRawData(file_path)

            if len(file_data) == 0:
                raise Exception
        except:
            user_output.displayOutput("An error occurred. Switching to stub data.")
            stub = DataInputStub()
            file_data = stub.readRawData(file_path)
        finally:
            header, game_data = self.mapDataToGameData(file_data, user_output)
            return header, game_data