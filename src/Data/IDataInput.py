from abc import ABC, abstractmethod

from src.Engine.Game import Game


class IDataInput(ABC):
    
    @abstractmethod
    def readRawData(self, file_path):
        pass

    @abstractmethod
    def getGameDataAndHeader(self, file_path, user_output):
        pass

    def mapDataToGameData(self, file_data, user_output):
        game_data = []
        header_row = file_data[0]

        for row in file_data[1:]:
            game_id = row[0]
            game_name = row[1]
            price = float(row[2])
            stock = int(row[3])
            temp_game = Game(game_id, game_name, price, stock)
            game_data.append(temp_game)
        return header_row, game_data