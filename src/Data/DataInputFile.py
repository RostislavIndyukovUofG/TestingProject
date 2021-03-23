import csv
from IDataInput import IDataInput

class DataInputFile(IDataInput):

    def getFileData(self, file_path):
        file_data = []
        with open(file_path, "r") as file:
            file_reader = csv.reader(file)
            for row in file_reader:
                file_data.append(row)
        return file_data
