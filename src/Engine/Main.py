from src.Data.DataInputFile import DataInputFile
from src.Data.DataInputStub import DataInputStub
from src.Display.ConsoleInput import ConsoleInput
from src.Display.ConsoleOutput import ConsoleOutput
from src.Engine.Basket import Basket
from src.Engine.CommandHandler import CommandHandler
from src.Engine.Game import Game


class Main:

    def __init__(self, input_type=None, user_input=None, user_output=None):
        if input_type == None:
            self.input_type = DataInputFile()
        else:
            self.input_type = input_type
        if user_input == None:
            self.user_input = ConsoleInput(True)
        else:
            self.user_input = user_input
        if user_output == None:
            self.user_output = ConsoleOutput(True)
        else:
            self.user_output = user_output

        self.file_path = "resources/gameData.csv"
        self.basket = Basket(self.user_input, self.user_output)
        self.command_handler = CommandHandler(self.user_input, self.user_output, self.basket, self)
        self.game_data = []
        self.header = []

    def setDataFilePath(self, file_path):
        self.file_path = file_path

    def setDataInputType(self, input_type):
        self.input_type = input_type

    def setUserInput(self, user_input):
        self.user_input = user_input

    def setUserOutput(self, user_output):
        self.user_output = user_output

    def getGameData(self):
        return self.game_data

    def getGameFromGameId(self, game_id):
        for game in self.game_data:
            if game_id == game.getGameID():
                return game

    def getGameDetails(self, game_id):
        game = self.getGameFromGameId(game_id)
        return game.getGameDetails()

    def setGameDataAndHeader(self):
        file_data = self.input_type.getFileData(self.file_path, self.user_output)
        game_data = []
        self.header = file_data[0]

        for row in file_data[1:]:
            game_id = row[0]
            game_name = row[1]
            price = float(row[2])
            stock = int(row[3])
            temp_game = Game(game_id, game_name, price, stock)
            game_data.append(temp_game)
        self.game_data = game_data

    def displayInitialMessage(self):
        self.user_output.displayOutput("Welcome to the Game Store.")

    def displayStock(self):
        self.user_output.displayOutput("The current games in stock are:")
        for game in self.game_data:
            game.displayGameDetails(self.user_output)
        print()


def main():
    main = Main()
    main.setGameDataAndHeader()
    main.displayInitialMessage()
    close = main.command_handler.handleUserCommands()

    if close:
        exit()


if __name__ == "__main__":
    main()