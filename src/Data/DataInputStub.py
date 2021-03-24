from src.Data.IDataInput import IDataInput

class DataInputStub(IDataInput):

    def getFileData(self):
        file_data = []
        header = ["GameID", "Game Name", "Price", "Stock"]
        game1 = ["1", "Xbox Video Game", 4.99, 3]
        game2 = ["2", "Playstation Video Game", 5.99, 3]
        game3 = ["3", "PC Video Game", 7.99, 3]
        file_data.append(header, game1, game2, game3)
        return file_data