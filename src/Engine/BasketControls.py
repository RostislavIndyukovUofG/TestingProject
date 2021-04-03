from src.Display.DisplayOutputs import ConsoleOutput


class BasketControls:

    @classmethod
    def addToUserBasket(cls, game_id, game_store_main, user_basket):
        game = game_store_main.getGameFromGameId(game_id)
        is_game_added = user_basket.addToBasket(game)
        ConsoleOutput.displayAddToBasketMessage(is_game_added)

    @classmethod
    def removeFromUserBasket(cls, game_id, game_store_main, user_basket):
        game = game_store_main.getGameFromGameId(game_id)
        is_game_removed = user_basket.removeFromBasket(game)
        ConsoleOutput.displayRemoveFromBasketMessage(is_game_removed)

    @classmethod
    def purchaseUserBasket(cls, user_basket, game_data):
        if len(user_basket.getBasketList()) > 0:
            print("Your order: ")
            print()

            for basket_game in user_basket.getBasketList():
                basket_game_id = basket_game.getGameID()

                for i, game in enumerate(game_data):

                    if game.getGameID() == basket_game_id:
                        game_stock = game.getStock()
                        game_data[i].setStock(game_stock - 1)

                print(basket_game.getGameName() + "\t\t£" + str(basket_game.getPrice()))
        else:
            print("Your basket is emtpy.")