from src.Data.IDataInput import IDataInput
from src.Engine.Game import Game


class DataInputStub(IDataInput):

    def readRawData(self, file_path):
        file_data = []
        header = ["GameID", "Game Name", "Price", "Stock"]
        game1 = ["1", "Xbox Video Game", 4.99, 3]
        game2 = ["2", "Playstation Video Game", 5.99, 3]
        game3 = ["3", "PC Video Game", 7.99, 3]

        file_data.append(header)
        file_data.append(game1)
        file_data.append(game2)
        file_data.append(game3)
        return file_data

    def getGameDataAndHeader(self, file_path, user_output):
        file_data = self.readRawData(file_path)
        header, game_data = self.mapDataToGameData(file_data, user_output)
        return header, game_data