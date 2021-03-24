class Game:
    game_id = None
    game_name = None
    price = None
    platform = None
    stock = None

    def __init__(self, game_id, game_name, price, stock):
        self.game_id = game_id
        self.game_name = game_name
        self.price = price
        self.stock = stock

    def __str__(self):
        return self.game_id + "\t\t" + self.game_name

    def getGameID(self):
        return self.game_id

    def getGameName(self):
        return self.game_name

    def getPrice(self):
        return self.price

    def getStock(self):
        return self.stock

    def displayGameDetails(self):
        main_line = self.getGameID() + ":\t" + self.getGameName()
        details_line = "Price: £" + self.getPrice() + "\tstock: " + self.getStock()
        game_details = [main_line, details_line]
        return game_details
