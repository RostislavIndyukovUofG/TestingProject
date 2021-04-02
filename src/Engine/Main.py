from src.Data.DataInputFile import DataInputFile
from src.Data.DataInputStub import DataInputStub
from src.Engine.Basket import Basket
from src.Engine.Game import Game


class Main:
    product_file_path = "resources/gameData.csv"
    input_type = None
    game_data = []
    header = []
    user_basket = Basket()
    commands = {"list": "view stock",
                "view [game ID]": "view the selected game details",
                "add [game ID]": "add selected game to basket",
                "basket": "view basket",
                "remove [game ID]": "remove selected game from basket",
                "buy": "purchase items in basket",
                "help": "show available commands",
                "exit": "leave program"}

    def __init__(self, input_type):
        self.input_type = input_type

    def setProductFilePath(self, product_file_path):
        self.product_file_path = product_file_path

    def setGameData(self, game_data):
        self.game_data = game_data

    def setHeader(self, header):
        self.header = header

    def getUserBasket(self):
        return self.user_basket

    def readFileData(self):
        file_data = self.input_type.getFileData(self.product_file_path)
        return file_data

    def mapFileDataToGameData(self, file_data):
        for row in file_data[1:]:
            game_id = row[0]
            game_name = row[1]
            price = float(row[2])
            stock = int(row[4])
            temp_game = Game(game_id, game_name, price, stock)
            self.game_data.append(temp_game)

    def displayGameData(self):
        for game in self.game_data:
            print(game)

    def getGameFromGameId(self, game_id):
        for game in self.game_data:
            if game_id == game.getGameID():
                return game

    def getGameDetails(self, game_id):
        game = self.getGameFromGameId(game_id)
        return game.getGameDetails()

    def displayGameDetails(self, game_id):
        game_details = self.getGameDetails(game_id)
        if len(game_details) > 0:
            if game_details[3] > 0:
                print()
                print("Game Id:\t" + game_details[0])
                print("Game Name:\t" + game_details[1])
                print("Price:\t£" + str(game_details[2]))
                print("Stock:\t" + str(game_details[3]))
        else:
            print("Game not found.")
        print()

    def displayStock(self):
        print("The current games in stock are:")
        print(self.header[0] + "\t" + self.header[1])
        for game in self.game_data:
            self.displayGameDetails(game.getGameID())
        print()

    def displayInitialMessage(self):
        print("Welcome to the Game Store.")
        self.displayStock()

    def getLongestKeyLength(self, data_structure):
        longest_length = 0
        for key in data_structure:
            key_length = len(key)

            if key_length > longest_length:
                longest_length = key_length
        return longest_length

    def displayCommandRow(self, key, value, command_key_length):
        spacing_length = command_key_length - len(key)
        spacing = " " * spacing_length
        print(key + ": " + spacing + value)

    def displayCommands(self):
        print("The commands are:")
        command_key_length = self.getLongestKeyLength(self.commands.keys())

        for command_row in self.commands.items():
            self.displayCommandRow(command_row[0], command_row[1], command_key_length)
        print()

    def getUserCommand(self):
        is_valid = False
        while not is_valid:
            try:
                user_command = []
                raw_command = input("Enter a command: ")
                raw_command.strip()
                user_command = raw_command.split(" ")
                is_valid = True
            except:
                print("Invalid command, type help to see available commands: ")
        return user_command

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

    def viewUserBasket(self):
        print("Your basket:")
        for game in self.user_basket.getBasketList():
            game_id = game.getGameID()
            self.displayGameDetails(game_id)
        print("Basket total: £" + str(self.user_basket.getBasketTotal()))

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
        self.displayCommands()
        active = True
        game_id = ""
        while active:

            user_command = self.getUserCommand()
            operation = user_command[0]
            if len(user_command) > 1:
                game_id = user_command[1]

            if operation == "list":
                self.displayStock()
            elif operation == "view":
                self.displayGameDetails(game_id)
            elif operation == "add":
                self.addToUserBasket(game_id)
            elif operation == "basket":
                self.viewUserBasket()
            elif operation == "remove":
                self.removeFromUserBasket(game_id)
            elif operation == "buy":
                self.purchaseUserBasket()
            elif operation == "help":
                self.displayCommands()
            elif operation == "exit":
                exit()

def main():
    main = Main(DataInputFile())
    file_data = main.readFileData()
    main.setHeader(file_data[0])
    main.mapFileDataToGameData(file_data)
    main.displayInitialMessage()
    main.handleUserCommands()


if __name__ == "__main__":
    main()