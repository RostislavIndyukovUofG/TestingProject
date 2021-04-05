from src.Data.IDataInput import IDataInput


class DataInputStub(IDataInput):

    def readRawData(self, file_path):
        header = ["GameID", "Game Name", "Price", "Stock"]
        game1 = ["1", "Xbox Video Game", 4.99, 3]
        game2 = ["2", "Playstation Video Game", 5.99, 3]
        game3 = ["3", "PC Video Game", 7.99, 3]

        file_data = [header, game1, game2, game3]
        return file_data

    def getFileData(self, file_path, user_output):
        file_data = self.readRawData(file_path)
        return file_data