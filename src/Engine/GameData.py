class GameData:

    def __init__(self, user_input, user_output):
        self.user_input = user_input
        self.user_output = user_output
        self.game_data_list = []

    def setGameDataList(self, game_data_list):
        self.game_data_list = game_data_list

    def getGameDataList(self):
        return self.game_data_list

    def getGameFromGameId(self, game_id):
        for game in self.game_data_list:
            if game_id == game.getGameId():
                return game

        return None

    def displayGameData(self):
        self.user_output.displayOutput("\nThe current games in stock are:\n")

        for game in self.game_data_list:
            game.displayGameDetails(self.user_output)

        print()

