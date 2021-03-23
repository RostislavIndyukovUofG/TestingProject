class Main:
    product_file_path = "../resources/gameData.csv"
    input_type = None

    def __init__(self, input_type):
        self.input_type = input_type

    def setProductFilePath(self, productFilePath):
        self.product_file_path = productFilePath

    def getFileData(self):
        file_data = self.input_type(self.product_file_path)
        return file_data


    def main(self):

        raw_data = getFileData()
        game_data = mapRawDataToGameData(raw_data)
        displayWelcomeMessage()
        displayGameData()
        user_command_string = getUserCommands()
        handleCommand()



if __name__ == "__main__":
    Main(InputFileData())