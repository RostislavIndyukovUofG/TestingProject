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


    def displayGameDetails(self):
        main_line = self.getGameID() + ":\t" + self.getGameName()
        details_line = "Price: £" + self.getPrice() + "\tstock: " + self.getStock()
        game_details = [main_line, details_line]
        return game_details
