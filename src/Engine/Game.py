class Game:

    def __init__(self, game_id, game_name, price, stock):
        self.game_id = game_id
        self.game_name = game_name
        self.price = price
        self.stock = stock

    def __str__(self):
        return self.game_id + "\t\t" + self.game_name

    def setStock(self, stock):
        if stock > 0:
            self.stock -= 1
        else:
            self.stock = 0

    def getGameID(self):
        return self.game_id

    def getGameName(self):
        return self.game_name

    def getPrice(self):
        return self.price

    def getStock(self):
        return self.stock

    def getGameDetails(self):
        game_id = self.getGameID()
        game_name = self.getGameName()
        price = self.getPrice()
        stock = self.getStock()
        game_details = [game_id, game_name, price, stock]
        return game_details

    def displayGameDetails(self, user_output):
        if len(self.getGameName()) > 0:
            if self.getStock() > 0:
                user_output.displayOutput("Game Id:\t" + self.getGameID())
                user_output.displayOutput("Game Name:\t" + self.getGameName())
                user_output.displayOutput("Price:\t£" + str(self.getPrice()))
                user_output.displayOutput("Stock:\t" + str(self.getStock()))
        else:
            user_output.displayOutput("Game not found.")
        print()

    def displayGameData(self, game_data, user_output):
        for game in game_data:
            user_output.displayOutput(game)
