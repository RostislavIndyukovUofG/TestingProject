class Game:

    def __init__(self, game_id, game_name, price, stock):
        self.game_id = game_id
        self.game_name = game_name
        self.price = price
        self.stock = stock

    def setStock(self, stock):
        if stock > 0:
            self.stock -= 1
        else:
            self.stock = 0

    def getGameDetails(self):
        game_id = self.game_id
        game_name = self.game_name
        price = self.price
        stock = self.stock
        game_details = [game_id, game_name, price, stock]
        return game_details

    def displayGameDetails(self, user_output):
        if len(self.game_name) > 0:
            if self.stock > 0:
                user_output.displayOutput("Game Id:\t" + self.game_id)
                user_output.displayOutput("Game Name:\t" + self.game_name)
                user_output.displayOutput("Price:\t£" + str(self.price))
                user_output.displayOutput("Stock:\t" + str(self.stock))
        else:
            user_output.displayOutput("Game not found.")
        print()

    def displayGame(self, user_output):
        user_output.displayOutput(self.game_name + "\t\t£" + str(self.price))
