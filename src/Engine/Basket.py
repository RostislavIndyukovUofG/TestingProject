class Basket:

    def __init__(self, user_input, user_output):
        self.user_input = user_input
        self.user_output = user_output
        self.basket_list = []
        self.basket_total = 0.00

    def getBasketList(self):
        return self.basket_list

    def setBasketList(self, basket_list):
        self.basket_list = basket_list
        self.calculateBasketTotal()

    def updateBasket(self, game, operation):
        game_position = self.findGameInBasket(game)

        if operation == "add":
            self.addToBasket(game_position, game)
        else:
            self.removeFromBasket(game_position, game)

        self.calculateBasketTotal()

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
            self.user_output.displayOutput("Game added successfully.")
        else:
            self.user_output.displayOutput("Game not added; game may already be in basket.")

    def removeFromBasket(self, game_position, game_to_remove):
        if game_position >= 0:
            self.basket_list.remove(game_to_remove)
            self.user_output.displayOutput("Game removed successfully.")
        else:
            self.user_output.displayOutput("Game not in basket.")

    def calculateBasketTotal(self):
        basket_total = 0.00

        for basket_game in self.basket_list:
            basket_total += basket_game.getPrice()
        self.basket_total = round(basket_total, 2)

    def displayBasket(self):
        for game in self.basket_list:
            game.displayGame(self.user_output)

        self.user_output.displayOutput("\nTotal: £" + str(self.basket_total))

    def purchaseBasket(self):
        if len(self.basket_list) > 0:
            self.user_output.displayOutput("\nYour order:\n")
            self.displayBasket()

            for basket_game in self.basket_list:
                basket_game.reduceStock()

            self.user_output.displayOutput("\nThank you for your purchase!\n")
            self.setBasketList([])
        else:
            self.user_output.displayOutput("Your basket is emtpy.")
