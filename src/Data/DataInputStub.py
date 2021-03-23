from IDataInput import IDataInput

class DataInputStub(IDataInput):

    def getFileData(self):
        file_data = []
        header = ["GameID", "Game Name", "Price", "Age Rating", "Platform"]
        game1 = ["1", "Xbox Video Game", 4.99, 3, "Xbox"]
        game2 = ["2", "Playstation Video Game", 5.99, 7, "Playstation"]
        game3 = ["3", "PC Video Game", 7.99, 12, "PC"]
        file_data.append(header, game1, game2, game3)
        return file_data