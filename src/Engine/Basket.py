class Basket:

    def __init__(self, user_input, user_output):
        self.basket_list = []
        self.basket_total = 0.00
        self.user_input = user_input
        self.user_output = user_output

    def addToBasket(self, game_to_add):
        found = False

        for game in self.basket_list:
            game_id = game.getGameID()
            if game_id == game_to_add.getGameID():
                found = True

        if not found:
            self.basket_list.append(game_to_add)
            self.calcualateBasketTotal()
            self.user_output.displayOutput("Game added successfully.")
        else:
            self.user_output.displayOutput("Game not added; game may already be in basket.")

    def removeFromBasket(self, game_to_remove):
        for game in self.basket_list:
            game_id = game.getGameID()
            if game_id == game_to_remove.getGameID():
                self.basket_list.remove(game)
                self.calcualateBasketTotal()
                self.user_output.displayOutput("Game removed successfully.")
            else:
                self.user_output.displayOutput("Game not in basket.")

    def calcualateBasketTotal(self):
        self.basket_total = 0
        for game in self.basket_list:
            self.basket_total += game.getPrice()

    def getBasketTotal(self):
        return self.basket_total

    def getBasketList(self):
        return self.basket_list

    def displayBasket(self):
        self.user_output.displayOutput("Your basket:")
        for game in self.getBasketList():
            game.displayGameDetails(self.user_output)
        self.user_output.displayOutput("Basket total: £" + str(self.getBasketTotal()))

    def purchaseBasket(self, game_data):
        if len(self.getBasketList()) > 0:
            self.user_output.displayOutput("Your order: ")
            print()

            for basket_game in self.getBasketList():
                self.user_output.displayOutput(basket_game.getGameName() + "\t\t£" + str(basket_game.getPrice()))
                basket_game_id = basket_game.getGameID()

                for i, game in enumerate(game_data):
                    if game.getGameID() == basket_game_id:
                        game_stock = game.getStock()
                        game_data[i].setStock(game_stock - 1)

        else:
            self.user_output.displayOutput("Your basket is emtpy.")
