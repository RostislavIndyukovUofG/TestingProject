from src.Data.DataInputFile import DataInputFile
from src.Data.DataInputStub import DataInputStub
from src.Display.ConsoleOutputs import ConsoleOutput
from src.Engine.Basket import Basket
from src.Data.FileDataMapper import FileDataMapper
from src.Engine.UserCommands import UserCommands
from src.Display.ConsoleInputs import ConsoleInputs


class Main:
    data_file_path = "resources/gameData.csv"
    input_type = None
    game_data = []
    header = []
    user_basket = Basket()

    def __init__(self, input_type):
        self.input_type = input_type

    def setProductFilePath(self, product_file_path):
        self.product_file_path = product_file_path

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

    def addToUserBasket(self, game_id):
        game = self.getGameFromGameId(game_id)
        if self.user_basket.addToBasket(game):
            print("Game added successfully.")
        else:
            print("Game not added; game may already be in basket.")

    def removeFromUserBasket(self, game_id):
        game = self.getGameFromGameId(game_id)
        if self.user_basket.removeFromBasket(game):
            print("Game removed successfully.")
        else:
            print("Game not in basket.")

    def purchaseUserBasket(self):
        print("Your order: ")
        print()
        for game in self.user_basket.getBasketList():
            game_id = game.getGameID()
            for i, game_in_stock in enumerate(self.game_data):
                if game_in_stock.getGameID() == game_id:
                    game_stock = game_in_stock.getStock()
                    print("before:", game_in_stock.getStock())
                    self.game_data[i].setStock(game_stock-1)
                    print("after:", game_in_stock.getStock())
            print(game.getGameName() + "\t\t£" + str(game.getPrice()))

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
                self.addToUserBasket(game_id)
            elif operation == "basket":
                ConsoleOutput.displayUserBasket(self.user_basket)
            elif operation == "remove":
                self.removeFromUserBasket(game_id)
            elif operation == "buy":
                self.purchaseUserBasket()
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