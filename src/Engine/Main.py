from src.Data.DataInputFile import DataInputFile
from src.Data.DataInputStub import DataInputStub
from src.Engine.Game import Game


class Main:
    product_file_path = "../../resources/gameData.csv"
    input_type = None
    game_data = []
    header = []
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

    def readFileData(self):
        file_data = self.input_type.getFileData(self.product_file_path)
        return file_data

    def mapFileDataToGameData(self, file_data):
        for row in file_data[1:]:
            game_id = row[0]
            game_name = row[1]
            price = row[2]
            platform = row[3]
            stock = row[4]
            temp_game = Game(game_id, game_name, price, platform, stock)
            self.game_data.append(temp_game)

    def displayGameData(self):
        for game in self.game_data:
            print(game)
            
    def displayStock(self):
        print("The current games in stock are:")
        print()
        print(self.header[0] + "\t" + self.header[1])
        self.displayGameData()
        print()

    def displayInitialMessage(self):
        print("Welcome to the Game Store.")
        self.displayStock()

    def getLongestKeyLength(self):
        longest_length = 0
        for command_key in self.commands.keys():
            key_length = len(command_key)

            if key_length > longest_length:
                longest_length = key_length
        return longest_length


    def displayCommandRow(self, key, value, command_key_length):
        spacing_length = command_key_length - len(key)
        spacing = " " * spacing_length
        print(key + ": " + spacing + value)


    def displayCommands(self):
        print("The commands are:")
        command_key_length = self.getLongestKeyLength()

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

    def handleUserCommands(self):
        self.displayCommands()
        active = True
        while active:
            user_command = self.getUserCommand()




def main():
    main = Main(DataInputFile())
    file_data = main.readFileData()
    main.setHeader(file_data[0])
    main.mapFileDataToGameData(file_data)
    main.displayInitialMessage()
    main.handleUserCommands()



if __name__ == "__main__":
    main()