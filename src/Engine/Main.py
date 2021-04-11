from src.Data.DataInputFile import DataInputFile
from src.Display.ConsoleInput import ConsoleInput
from src.Display.ConsoleOutput import ConsoleOutput
from src.Engine.CommandHandler import CommandHandler
from src.Engine.Game import Game
from src.Engine.GameData import GameData


class Main:

    def __init__(self, input_type=None, user_input=None, user_output=None):
        if input_type is None:
            self.input_type = DataInputFile()
        else:
            self.input_type = input_type
        if user_input is None:
            self.user_input = ConsoleInput(True)
        else:
            self.user_input = user_input
        if user_output is None:
            self.user_output = ConsoleOutput(True)
        else:
            self.user_output = user_output

        self.file_path = "resources/gameData.csv"
        self.game_data = None
        self.command_handler = None

    def initialiseHelperClasses(self):
        self.setGameData()
        self.command_handler = CommandHandler(self.user_input, self.user_output, self.game_data)

    def setFilePath(self, file_path):
        self.file_path = file_path

    def setGameData(self):
        file_data = self.input_type.getFileData(self.file_path, self.user_output)
        game_data_list = []

        for row in file_data[1:]:
            game_details = {}
            game_details["Game Id"] = row[0]
            game_details["Game Name"] = row[1]
            game_details["Price"] = float(row[2])
            game_details["Stock"] = int(row[3])
            temp_game = Game(game_details)
            game_data_list.append(temp_game)

        self.game_data = GameData(self.user_input, self.user_output)
        self.game_data.setGameDataList(game_data_list)

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
