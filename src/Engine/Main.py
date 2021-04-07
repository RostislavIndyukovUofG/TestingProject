from src.Data.DataInputFile import DataInputFile
from src.Display.ConsoleInput import ConsoleInput
from src.Display.ConsoleOutput import ConsoleOutput
from src.Engine.Basket import Basket
from src.Engine.CommandHandler import CommandHandler
from src.Engine.Game import Game
from src.Engine.GameData import GameData


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
        self.header = []
        self.game_data = None
        self.basket = None
        self.command_handler = None

    def initialiseHelperClasses(self):
        self.setGameDataAndHeader()
        self.basket = Basket(self.user_input, self.user_output, self.game_data)
        self.command_handler = CommandHandler(self.user_input, self.user_output, self.basket, self.game_data)

    def setGameDataAndHeader(self):
        file_data = self.input_type.getFileData(self.file_path, self.user_output)
        game_data_list = []
        self.header = file_data[0]

        for row in file_data[1:]:
            game_id = row[0]
            game_name = row[1]
            price = float(row[2])
            stock = int(row[3])
            temp_game = Game(game_id, game_name, price, stock)
            game_data_list.append(temp_game)
        self.game_data = GameData(self.user_input, self.user_output)
        self.game_data.game_data_list = game_data_list

    def displayInitialMessage(self):
        self.user_output.displayOutput("Welcome to the Game Store.")


def main():
    main = Main()
    main.initialiseHelperClasses()
    main.displayInitialMessage()
    close = main.command_handler.handleUserCommands()

    if close:
        exit()


if __name__ == "__main__":
    main()
