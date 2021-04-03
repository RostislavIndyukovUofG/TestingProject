class Basket:

    def __init__(self):
        self.basket_list = []
        self.basket_total = 0.00

    def addToBasket(self, game_to_add):
        found = False

        for game in self.basket_list:
            game_id = game.getGameID()
            if game_id == game_to_add.getGameID():
                found = True

        if not found:
            self.basket_list.append(game_to_add)
            self.calcualateBasketTotal()
            return True
        return False

    def removeFromBasket(self, game_to_remove):
        for game in self.basket_list:
            game_id = game.getGameID()
            if game_id == game_to_remove.getGameID():
                self.basket_list.remove(game_to_remove)
                self.calcualateBasketTotal()
                return True
        return False

    def calcualateBasketTotal(self):
        self.basket_total = 0
        for game in self.basket_list:
            self.basket_total += game.getPrice()

    def getBasketTotal(self):
        return self.basket_total

    def getBasketList(self):
        return self.basket_list