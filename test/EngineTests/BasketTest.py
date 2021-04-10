import unittest

from src.Display.ConsoleInput import ConsoleInput
from src.Display.TestOutput import TestOutput
from src.Engine.Basket import Basket
from src.Engine.Game import Game
from src.Engine.GameData import GameData


class BasketTest(unittest.TestCase):
    user_input = ConsoleInput(False)
    user_output = TestOutput()

    game = Game("1", "Anno 1701", 8.99, 4)
    game2 = Game("2", "Metro 2033", 9.99, 5)
    game3 = Game("3", "Assassin's Creed Brotherhood", 26.99, 7)

    game_data = GameData(user_input, user_output)
    game_data.gameDataList = [game, game2, game3]

    # updateBasket

    def test_addGameToEmptyBasket(self):
        basket = Basket(self.user_input, self.user_output, self.game_data)
        basket.updateBasket(self.game, "add")
        self.assertEqual(self.game, basket.basket_list[0])

    def test_addGameToBasket(self):
        basket = Basket(self.user_input, self.user_output, self.game_data)
        basket_size = len(basket.basket_list)
        basket.updateBasket(self.game, "add")
        self.assertEqual(basket_size + 1, len(basket.basket_list))

    def test_addGameToBasketOutput(self):
        basket = Basket(self.user_input, self.user_output, self.game_data)
        basket.updateBasket(self.game, "add")
        self.assertEqual("Game added successfully.", self.user_output.getOutputList()[-1])

    def test_addOutOfStockGameToBasket(self):
        basket = Basket(self.user_input, self.user_output, self.game_data)
        out_of_stock_game = Game("1", "Anno 1701", 8.99, 0)
        basket_size = len(basket.basket_list)
        basket.updateBasket(out_of_stock_game, "add")
        self.assertEqual(basket_size, len(basket.basket_list))

    def test_addOutOfStockGameToBasketOutput(self):
        basket = Basket(self.user_input, self.user_output, self.game_data)
        out_of_stock_game = Game("1", "Anno 1701", 8.99, 0)
        basket.updateBasket(out_of_stock_game, "add")
        output_message = "Game not added; game may already be in basket."
        self.assertEqual(output_message, self.user_output.output_list[-1])

    def test_addExistingGameToBasketOutput(self):
        basket = Basket(self.user_input, self.user_output, self.game_data)
        basket.updateBasket(self.game, "add")
        basket.updateBasket(self.game, "add")
        output_message = "Game not added; game may already be in basket."
        self.assertEqual(output_message, self.user_output.output_list[-1])

    def test_addMultipleGamesToBasket(self):
        basket = Basket(self.user_input, self.user_output, self.game_data)
        basket.updateBasket(self.game, "add")
        basket.updateBasket(self.game2, "add")
        basket.updateBasket(self.game3, "add")
        self.assertEqual(3, len(basket.basket_list))

    def test_removeExistingGameFromBasket(self):
        basket = Basket(self.user_input, self.user_output, self.game_data)
        basket.updateBasket(self.game, "add")
        basket_size = len(basket.basket_list)
        basket.updateBasket(self.game, "remove")
        self.assertEqual(basket_size - 1, len(basket.basket_list))

    def test_removeExistingGameFromBasketOutput(self):
        basket = Basket(self.user_input, self.user_output, self.game_data)
        basket.updateBasket(self.game, "add")
        basket.updateBasket(self.game, "remove")
        self.assertEqual("Game removed successfully.", self.user_output.output_list[-1])

    def test_removeGameFromEmptyBasket(self):
        basket = Basket(self.user_input, self.user_output, self.game_data)
        basket.updateBasket(self.game, "remove")
        self.assertEqual("Game not in basket.", self.user_output.output_list[-1])

    def test_removeMissingGameFromBasket(self):
        basket = Basket(self.user_input, self.user_output, self.game_data)
        basket.updateBasket(self.game, "add")
        basket_size = len(basket.basket_list)
        basket.updateBasket(self.game2, "remove")
        self.assertEqual(basket_size, len(basket.basket_list))

    def test_removeMissingGameFromBasketOutput(self):
        basket = Basket(self.user_input, self.user_output, self.game_data)
        basket.updateBasket(self.game2, "remove")
        self.assertEqual("Game not in basket.", self.user_output.output_list[-1])

    def test_removeMultipleGamesFromBasket(self):
        basket = Basket(self.user_input, self.user_output, self.game_data)
        basket.updateBasket(self.game, "add")
        basket.updateBasket(self.game2, "add")
        basket.updateBasket(self.game3, "add")

        basket.updateBasket(self.game, "remove")
        basket.updateBasket(self.game2, "remove")
        basket.updateBasket(self.game3, "remove")
        self.assertEqual(0, len(basket.basket_list))

    # calculateBasketTotal

    def test_CalculateBasketTotal(self):
        basket = Basket(self.user_input, self.user_output, self.game_data)
        basket.updateBasket(self.game, "add")
        basket.updateBasket(self.game2, "add")
        basket.calcualateBasketTotal()
        self.assertEqual(18.98, basket.basket_total)

    def test_CalculateEmptyBasketTotal(self):
        basket = Basket(self.user_input, self.user_output, self.game_data)
        basket.calcualateBasketTotal()
        self.assertEqual(0, basket.basket_total)

    def test_CalculateUpdatedBasketTotal(self):
        basket = Basket(self.user_input, self.user_output, self.game_data)
        basket.updateBasket(self.game, "add")
        basket.calcualateBasketTotal()
        basket_total = basket.basket_total
        basket.updateBasket(self.game2, "add")
        basket.calcualateBasketTotal()
        self.assertNotEqual(basket_total, basket.basket_total)

    # displayBasket

    def test_displayBasketOutput(self):
        basket = Basket(self.user_input, self.user_output, self.game_data)
        basket.updateBasket(self.game, "add")
        basket.updateBasket(self.game2, "add")
        basket.displayBasket()
        self.assertEqual("Basket total: £18.98", self.user_output.output_list[-1])

    def test_displayEmptyBasketOutput(self):
        basket = Basket(self.user_input, self.user_output, self.game_data)
        basket.displayBasket()
        self.assertEqual("Basket total: £0.0", self.user_output.output_list[-1])

    # purchaseBasket

    def test_purchaseBasket(self):
        basket = Basket(self.user_input, self.user_output, self.game_data)
        basket.updateBasket(self.game, "add")
        basket.updateBasket(self.game2, "add")
        basket.purchaseBasket()
        self.assertEqual(0, len(basket.basket_list))

    def test_purchaseBasketOutput(self):
        basket = Basket(self.user_input, self.user_output, self.game_data)
        basket.updateBasket(self.game, "add")
        basket.updateBasket(self.game2, "add")
        basket.purchaseBasket()
        self.assertEqual("Your order:", self.user_output.output_list[-3])

    def test_purchaseEmptyBasketOutput(self):
        basket = Basket(self.user_input, self.user_output, self.game_data)
        basket.purchaseBasket()
        self.assertEqual("Your basket is emtpy.", self.user_output.output_list[-1])


if __name__ == '__main__':
    unittest.main()