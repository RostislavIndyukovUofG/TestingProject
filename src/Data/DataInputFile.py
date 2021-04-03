import csv
from src.Data.IDataInput import IDataInput


class DataInputFile(IDataInput):

    def getData(self, file_path):
        file_data = []
        with open(file_path, "r") as file:
            file_reader = csv.reader(file)

            for row in file_reader:
                file_data.append(row)

        return file_data
