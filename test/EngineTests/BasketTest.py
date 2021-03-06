import unittest

from src.Display.ConsoleInput import ConsoleInput
from src.Display.TestOutput import TestOutput
from src.Engine.Basket import Basket
from src.Engine.Game import Game
from src.Engine.GameData import GameData


class BasketTest(unittest.TestCase):
    user_input = ConsoleInput(False)
    user_output = TestOutput()

    game = Game({"Game Id": "1", "Game Name": "City Builder", "Price": 8.99, "Stock": 4})
    game2 = Game({"Game Id": "2", "Game Name": "Survivalist", "Price": 9.99, "Stock": 5})
    game3 = Game({"Game Id": "3", "Game Name": "Secret Treasure", "Price": 26.99, "Stock": 7})

    game_data = GameData(user_input, user_output)
    game_data.gameDataList = [game, game2, game3]

    # updateBasket

    def test_addGameToEmptyBasket(self):
        basket = Basket(self.user_input, self.user_output)
        basket.updateBasket(self.game, "add")
        self.assertEqual(self.game, basket.getBasketList()[0])

    def test_addGameToBasket(self):
        basket = Basket(self.user_input, self.user_output)
        basket_size = len(basket.getBasketList())
        basket.updateBasket(self.game, "add")
        self.assertEqual(basket_size + 1, len(basket.getBasketList()))

    def test_addGameToBasketOutput(self):
        basket = Basket(self.user_input, self.user_output)
        basket.updateBasket(self.game, "add")
        self.assertEqual("Game added successfully.", self.user_output.getOutputList()[-1])

    def test_addOutOfStockGameToBasket(self):
        basket = Basket(self.user_input, self.user_output)
        out_of_stock_game = Game({"Game Id": "1", "Game Name": "City Builder", "Price": 8.99, "Stock": 0})
        basket_size = len(basket.getBasketList())
        basket.updateBasket(out_of_stock_game, "add")
        self.assertEqual(basket_size, len(basket.getBasketList()))

    def test_addOutOfStockGameToBasketOutput(self):
        basket = Basket(self.user_input, self.user_output)
        out_of_stock_game = Game({"Game Id": "1", "Game Name": "City Builder", "Price": 8.99, "Stock": 0})
        basket.updateBasket(out_of_stock_game, "add")
        output_message = "Game is out of stock."
        self.assertEqual(output_message, self.user_output.getOutputList()[-1])

    def test_addExistingGameToBasketOutput(self):
        basket = Basket(self.user_input, self.user_output)
        basket.updateBasket(self.game, "add")
        basket.updateBasket(self.game, "add")
        self.assertEqual("Game is already in basket.", self.user_output.getOutputList()[-1])

    def test_addMultipleGamesToBasket(self):
        basket = Basket(self.user_input, self.user_output)
        basket.updateBasket(self.game, "add")
        basket.updateBasket(self.game2, "add")
        basket.updateBasket(self.game3, "add")
        self.assertEqual(3, len(basket.getBasketList()))

    def test_removeExistingGameFromBasket(self):
        basket = Basket(self.user_input, self.user_output)
        basket.updateBasket(self.game, "add")
        basket_size = len(basket.getBasketList())
        basket.updateBasket(self.game, "remove")
        self.assertEqual(basket_size - 1, len(basket.getBasketList()))

    def test_removeExistingGameFromBasketOutput(self):
        basket = Basket(self.user_input, self.user_output)
        basket.updateBasket(self.game, "add")
        basket.updateBasket(self.game, "remove")
        self.assertEqual("Game removed successfully.", self.user_output.getOutputList()[-1])

    def test_removeGameFromEmptyBasket(self):
        basket = Basket(self.user_input, self.user_output)
        basket.updateBasket(self.game, "remove")
        self.assertEqual("Game not in basket.", self.user_output.getOutputList()[-1])

    def test_removeMissingGameFromBasket(self):
        basket = Basket(self.user_input, self.user_output)
        basket.updateBasket(self.game, "add")
        basket_size = len(basket.getBasketList())
        basket.updateBasket(self.game2, "remove")
        self.assertEqual(basket_size, len(basket.getBasketList()))

    def test_removeMissingGameFromBasketOutput(self):
        basket = Basket(self.user_input, self.user_output)
        basket.updateBasket(self.game2, "remove")
        self.assertEqual("Game not in basket.", self.user_output.getOutputList()[-1])

    def test_removeMultipleGamesFromBasket(self):
        basket = Basket(self.user_input, self.user_output)
        basket.updateBasket(self.game, "add")
        basket.updateBasket(self.game2, "add")
        basket.updateBasket(self.game3, "add")

        basket.updateBasket(self.game, "remove")
        basket.updateBasket(self.game2, "remove")
        basket.updateBasket(self.game3, "remove")
        self.assertEqual(0, len(basket.getBasketList()))

    # calculateBasketTotal

    def test_calculateBasketTotal(self):
        basket = Basket(self.user_input, self.user_output)
        basket.updateBasket(self.game, "add")
        basket.updateBasket(self.game2, "add")
        basket.calculateBasketTotal()
        self.assertEqual(18.98, basket.basket_total)

    def test_calculateEmptyBasketTotal(self):
        basket = Basket(self.user_input, self.user_output)
        basket.calculateBasketTotal()
        self.assertEqual(0, basket.basket_total)

    def test_calculateUpdatedBasketTotal(self):
        basket = Basket(self.user_input, self.user_output)
        basket.updateBasket(self.game, "add")
        basket.calculateBasketTotal()
        basket_total = basket.basket_total
        basket.updateBasket(self.game2, "add")
        basket.calculateBasketTotal()
        self.assertNotEqual(basket_total, basket.basket_total)

    # displayBasket

    def test_displayBasketOutput(self):
        basket = Basket(self.user_input, self.user_output)
        basket.updateBasket(self.game, "add")
        basket.updateBasket(self.game2, "add")
        basket.displayBasket()
        self.assertEqual("\nTotal: ??18.98", self.user_output.output_list[-1])

    def test_displayEmptyBasketOutput(self):
        basket = Basket(self.user_input, self.user_output)
        basket.displayBasket()
        self.assertEqual("\nTotal: ??0.0", self.user_output.output_list[-1])

    # purchaseBasket

    def test_purchaseBasket(self):
        basket = Basket(self.user_input, self.user_output)
        basket.updateBasket(self.game, "add")
        basket.updateBasket(self.game2, "add")
        basket.purchaseBasket()
        self.assertEqual(0, len(basket.basket_list))

    def test_purchaseBasketOutput(self):
        basket = Basket(self.user_input, self.user_output)
        basket.updateBasket(self.game, "add")
        basket.updateBasket(self.game2, "add")
        basket.purchaseBasket()
        output_message = "\nThank you for your purchase!\n"
        self.assertEqual(output_message, self.user_output.output_list[-1])

    def test_purchaseEmptyBasketOutput(self):
        basket = Basket(self.user_input, self.user_output)
        basket.purchaseBasket()
        self.assertEqual("Your basket is emtpy.", self.user_output.output_list[-1])


if __name__ == '__main__':
    unittest.main()
