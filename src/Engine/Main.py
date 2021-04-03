from src.Data.DataInputFile import DataInputFile
from src.Data.DataInputStub import DataInputStub
from src.Display.DisplayOutputs import DisplayOutputs
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

    def setDataFilePath(self, data_file_path):
        self.data_file_path = data_file_path

    def getHeader(self):
        return self.header

    def getGameData(self):
        return self.game_data

    def getGameFromGameId(self, game_id):
        for game in self.game_data:
            if game_id == game.getGameID():
                return game

    def getGameDetails(self, game_id):
        game = self.getGameFromGameId(game_id)
        return game.getGameDetails()

    def getGameDataAndHeader(self):
        file_data = self.input_type.getFileData(self.data_file_path)
        self.header, self.game_data = FileDataMapper.mapFileDataToGameData(file_data)


def main():
    game_store_main = Main(DataInputFile())
    game_store_main.getGameDataAndHeader()
    DisplayOutputs.displayInitialMessage()
    DisplayOutputs.displayStock(game_store_main.getHeader(), game_store_main.getGameData())
    game_store_main.command_handler.handleUserCommands()


if __name__ == "__main__":
    main()