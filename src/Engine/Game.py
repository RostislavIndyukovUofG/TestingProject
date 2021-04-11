class Game:

    def __init__(self, game_details):
        self.game_details = game_details

    def getGameId(self):
        return self.game_details["Game Id"]

    def getGameName(self):
        return self.game_details["Game Name"]

    def getPrice(self):
        return self.game_details["Price"]

    def getStock(self):
        return self.game_details["Stock"]

    def reduceStock(self):
        if self.game_details["Stock"] > 0:
            self.game_details["Stock"] -= 1

    def displayGameDetails(self, user_output):
        if len(self.getGameId()) > 0:
            if self.getStock() > 0:
                for attribute in self.game_details.items():
                    attribute_name = attribute[0]
                    attribute_value = attribute[1]

                    string_connector = ":\t"
                    if attribute_name == "Price":
                        string_connector += "£"

                    user_output.displayOutput(attribute_name + string_connector + str(attribute_value))
        else:
            user_output.displayOutput("Game not found.")
        print()

    def displayGame(self, user_output):
        user_output.displayOutput(self.getGameName() + "\t£" + str(self.getPrice()))
