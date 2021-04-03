class ConsoleOutput:

    @classmethod
    def displayGameDetails(cls, game):
        if len(game.getGameName()) > 0:
            if game.getStock() > 0:
                print()
                print("Game Id:\t" + game.getGameID())
                print("Game Name:\t" + game.getGameName())
                print("Price:\t£" + str(game.getPrice()))
                print("Stock:\t" + str(game.getStock()))
        else:
            print("Game not found.")
        print()

    @classmethod
    def displayGameData(cls, game_data):
        for game in game_data:
            print(game)

    @classmethod
    def displayStock(cls, header, game_data):
        print("The current games in stock are:")
        print(header[0] + "\t" + header[1])
        for game in game_data:
            cls.displayGameDetails(game)
        print()

    @classmethod
    def displayInitialMessage(cls):
        print("Welcome to the Game Store.")

    @classmethod
    def displayUserBasket(cls, basket):
        print("Your basket:")
        for game in basket.getBasketList():
            cls.displayGameDetails(game)
        print("Basket total: £" + str(basket.getBasketTotal()))

    @classmethod
    def displayAddToBasketMessage(cls, is_game_added):
        if is_game_added:
            print("Game added successfully.")
        else:
            print("Game not added; game may already be in basket.")

    @classmethod
    def displayRemoveFromBasketMessage(cls, is_game_removed):
        if is_game_removed:
            print("Game removed successfully.")
        else:
            print("Game not in basket.")