from src.Data.DataInputFile import DataInputFile
from src.Data.DataInputStub import DataInputStub
from src.Engine.Game import Game


class Main:
    product_file_path = "../../resources/gameData.csv"
    input_type = None
    game_data = []

    def __init__(self, input_type):
        self.input_type = input_type

    def setProductFilePath(self, productFilePath):
        self.product_file_path = productFilePath

    def setGameData(self, game_data):
        self.game_data = game_data

    def getFileData(self):
        file_data = self.input_type.getFileData(self.product_file_path)
        return file_data

    def mapFileDataToGameData(self, file_data):
        for row in file_data[1:]:
            game_id = row[0]
            game_name = row[1]
            price = row[2]
            age_rating = row[3]
            platform = row[4]
            temp_game = Game(game_id, game_name, price, age_rating, platform)
            self.game_data.append(temp_game)


def main():
    main = Main(DataInputFile())
    file_data = main.getFileData()
    main.mapFileDataToGameData(file_data)

    displayWelcomeMessage()
    displayGameData()
    user_command_string = getUserCommands()
    handleCommand()



if __name__ == "__main__":
    main()