class GameData:

    def __init__(self, user_input, user_output):
        self.user_input = user_input
        self.user_output = user_output
        self.game_data_list = []

    def setGameDataList(self, game_data_list):
        self.game_data_list = game_data_list

    def displayGameData(self):
        self.user_output.displayOutput("The current games in stock are:")
        for game in self.game_data_list:
            game.displayGameDetails(self.user_output)
        print()

    def getGameFromGameId(self, game_id):
        for game in self.game_data_list:
            if game_id == game.game_id:
                return game

    def reduceGameStock(self, target_game_id):
        for i, game in enumerate(self.game_data_list):
            if game.game_id == target_game_id:
                game_stock = game.stock
                self.game_data_list[i].setStock(game_stock - 1)
