class Basket:

    def __init__(self, user_input, user_output, game_data):
        self.user_input = user_input
        self.user_output = user_output
        self.basket_list = []
        self.basket_total = 0.00
        self.game_data = game_data

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

    def findGameInBasket(self, target_game):
        target_game_id = target_game.getGameId()
        game_position = -1

        for i, basket_game in enumerate(self.basket_list):
            basket_game_id = basket_game.getGameId()

            if basket_game_id == target_game_id:
                game_position = i

        return game_position

    def addToBasket(self, game_position, game_to_add):
        if game_position < 0 and game_to_add.getStock() > 0:
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

        for game in self.basket_list:
            game.displayGameDetails(self.user_output)

        self.user_output.displayOutput("Basket total: £" + str(self.basket_total))

    def purchaseBasket(self):
        if len(self.basket_list) > 0:
            self.user_output.displayOutput("Your order:")
            print()

            for basket_game in self.basket_list:
                basket_game.displayGame(self.user_output)
                basket_game.reduceStock()

            self.basket_list = []
            self.calcualateBasketTotal()

        else:
            self.user_output.displayOutput("Your basket is emtpy.")
