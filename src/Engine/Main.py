from src.Data.DataInputFile import DataInputFile
from src.Data.DataInputStub import DataInputStub
from src.Display.ConsoleOutput import ConsoleOutput
from src.Engine.Basket import Basket
from src.Data.FileDataMapper import FileDataMapper
from src.Engine.CommandHandler import CommandHandler


class Main:
    data_file_path = "resources/gameData.csv"
    input_type = None
    command_handler = None
    user_basket = Basket()
    game_data = []
    header = []

    def __init__(self, input_type):
        self.input_type = input_type
        self.command_handler = CommandHandler(self)

    def setProductFilePath(self, data_file_path):
        self.data_file_path = data_file_path

    def setGameData(self, game_data):
        self.game_data = game_data

    def setHeader(self, header):
        self.header = header

    def getHeader(self):
        return self.header

    def getGameData(self):
        return self.game_data

    def getUserBasket(self):
        return self.user_basket

    def getGameFromGameId(self, game_id):
        for game in self.game_data:
            if game_id == game.getGameID():
                return game

    def getGameDetails(self, game_id):
        game = self.getGameFromGameId(game_id)
        return game.getGameDetails()


def main():
    main = Main(DataInputFile())
    header_row, game_data = FileDataMapper.mapFileDataToGameData(main.input_type, main.data_file_path)
    main.setHeader(header_row)
    main.setGameData(game_data)
    ConsoleOutput.displayInitialMessage()
    ConsoleOutput.displayStock(main.getHeader(), main.getGameData())
    main.command_handler.handleUserCommands()


if __name__ == "__main__":
    main()