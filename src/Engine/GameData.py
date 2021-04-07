class GameData:

    def __init__(self, user_input, user_output):
        self.user_input = user_input
        self.user_output = user_output
        self.game_data_list = []

    def displayGameData(self):
        self.user_output.displayOutput("The current games in stock are:")
        for game in self.game_data_list:
            game.displayGameDetails(self.user_output)
        print()

    def getGameFromGameId(self, game_id):
        for game in self.game_data_list:
            if game_id == game.game_id:
                return game
        return None
