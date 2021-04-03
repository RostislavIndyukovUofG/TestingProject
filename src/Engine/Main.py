from src.Data.DataInputFile import DataInputFile
from src.Data.DataInputStub import DataInputStub
from src.Display.ConsoleOutputs import ConsoleOutput
from src.Engine.Basket import Basket
from src.Data.FileDataMapper import FileDataMapper
from src.Engine.UserCommands import UserCommands
from src.Display.ConsoleInputs import ConsoleInputs
from src.Engine.BasketControls import BasketControls


class Main:
    data_file_path = "resources/gameData.csv"
    input_type = None
    game_data = []
    header = []
    user_basket = Basket()

    def __init__(self, input_type):
        self.input_type = input_type

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

    def handleUserCommands(self):
        UserCommands.displayCommands()
        active = True
        game_id = ""
        while active:

            user_command = ConsoleInputs.getUserCommand()
            operation = user_command[0]
            if len(user_command) > 1:
                game_id = user_command[1]

            if operation == "list":
                ConsoleOutput.displayStock(self.header, self.game_data)

            elif operation == "view":
                ConsoleOutput.displayGameDetails(self.getGameFromGameId(game_id))

            elif operation == "add":
                BasketControls.addToUserBasket(game_id, self, self.user_basket)

            elif operation == "basket":
                ConsoleOutput.displayUserBasket(self.user_basket)

            elif operation == "remove":
                BasketControls.removeFromUserBasket(game_id, self, self.user_basket)

            elif operation == "buy":
                BasketControls.purchaseUserBasket(self.user_basket, self.game_data)

            elif operation == "help":
                UserCommands.displayCommands()

            elif operation == "exit":
                exit()

def main():
    main = Main(DataInputFile())
    header_row, game_data = FileDataMapper.mapFileDataToGameData(main.input_type, main.data_file_path)
    main.setHeader(header_row)
    main.setGameData(game_data)
    ConsoleOutput.displayInitialMessage()
    ConsoleOutput.displayStock(main.getHeader(), main.getGameData())
    main.handleUserCommands()


if __name__ == "__main__":
    main()