class Game:
    game_id = None
    game_name = None
    price = None
    platform = None
    stock = None

    def __init__(self, game_id, game_name, price, platform, stock):
        self.game_id = game_id
        self.game_name = game_name
        self.price = price
        self.platform = platform
        self.stock = stock

    def __str__(self):
        return self.game_id + "\t\t" + self.game_name

    def getGameID(self):
        return self.game_id

    def getGameName(self):
        return self.game_name

    def getPrice(self):
        return self.price

    def getPlatform(self):
        return self.platform

    def getStock(self):
        return self.stock
