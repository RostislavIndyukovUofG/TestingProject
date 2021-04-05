class Basket:

    def __init__(self, user_input, user_output):
        self.basket_list = []
        self.basket_total = 0.00
        self.user_input = user_input
        self.user_output = user_output

    def getBasketTotal(self):
        return self.basket_total

    def getBasketList(self):
        return self.basket_list

    def setBasketList(self, basket_list):
        self.basket_list = basket_list

    def updateBasket(self, game, operation):
        game_position = self.findGameInBasket(game)

        if operation == "add":
            self.addToBasket(game_position, game)
        else:
            self.removeFromBasket(game_position, game)

    def findGameInBasket(self, game):
        game_id = game.getGameID()
        game_position = -1

        for i, basket_game in enumerate(self.getBasketList()):
            basket_game_id = basket_game.getGameID()

            if basket_game_id == game_id:
                game_position = i

        return game_position

    def addToBasket(self, game_position, game_to_add):
        if game_position < 0:
            self.basket_list.append(game_to_add)
            self.calcualateBasketTotal()
            self.user_output.displayOutput("Game added successfully.")
        else:
            self.user_output.displayOutput("Game not added; game may already be in basket.")

    def removeFromBasket(self, game_position, game_to_remove):
        if game_position >= 0:
            self.basket_list.remove(game_to_remove)
            self.calcualateBasketTotal()
            self.user_output.displayOutput("Game removed successfully.")
        else:
            self.user_output.displayOutput("Game not in basket.")

    def calcualateBasketTotal(self):
        self.basket_total = 0.00

        for game in self.basket_list:
            self.basket_total += game.getPrice()

    def displayBasket(self):
        self.user_output.displayOutput("Your basket:")

        for game in self.getBasketList():
            game.displayGameDetails(self.user_output)

        self.user_output.displayOutput("Basket total: £" + str(self.getBasketTotal()))

    def purchaseBasket(self, game_data):
        if len(self.getBasketList()) > 0:
            self.user_output.displayOutput("Your order:")
            print()

            for basket_game in self.getBasketList():
                basket_game.displayGame(self.user_output)
                self.reduceGameStock(game_data, basket_game.getGameID())
            self.setBasketList([])
            self.calcualateBasketTotal()
        else:
            self.user_output.displayOutput("Your basket is emtpy.")

    def reduceGameStock(self, game_data, basket_game_id):
        for i, game in enumerate(game_data):
            if game.getGameID() == basket_game_id:
                game_stock = game.getStock()
                game_data[i].setStock(game_stock - 1)

