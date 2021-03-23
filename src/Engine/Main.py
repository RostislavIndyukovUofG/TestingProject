from src.Data.DataInputFile import DataInputFile
from src.Data.DataInputStub import DataInputStub
from src.Engine.Game import Game


class Main:
    product_file_path = "../../resources/gameData.csv"
    input_type = None
    game_data = []
    header = []

    def __init__(self, input_type):
        self.input_type = input_type

    def setProductFilePath(self, productFilePath):
        self.product_file_path = productFilePath

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


def main():
    main = Main(DataInputFile())
    file_data = main.readFileData()
    main.setHeader(file_data[0])
    main.mapFileDataToGameData(file_data)
    main.displayInitialMessage()
    user_command_string = getUserCommands()
    handleCommand()



if __name__ == "__main__":
    main()