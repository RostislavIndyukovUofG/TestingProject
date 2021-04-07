import unittest

from src.Display.ConsoleInput import ConsoleInput
from src.Display.TestOutput import TestOutput
from src.Engine.Basket import Basket
from src.Engine.Game import Game
from src.Engine.GameData import GameData


class PurchaseBasketTest(unittest.TestCase):
    user_input = ConsoleInput(False)
    user_output = TestOutput()

    game = Game("1", "Anno 1701", 8.99, 4)
    game2 = Game("2", "Metro 2033", 9.99, 5)
    game3 = Game("3", "Assassin's Creed Brotherhood", 26.99, 7)

    game_data = GameData(user_input, user_output)
    game_data.game_data_list = [game, game2, game3]

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
        self.assertEqual("Basket total: £18.98", self.user_output.getOutputList()[-1])

    def test_displayEmptyBasketOutput(self):
        basket = Basket(self.user_input, self.user_output, self.game_data)
        basket.displayBasket()
        self.assertEqual("Basket total: £0.0", self.user_output.getOutputList()[-1])

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
        self.assertEqual("Your order:", self.user_output.getOutputList()[-3])

    def test_purchaseEmptyBasketOutput(self):
        basket = Basket(self.user_input, self.user_output, self.game_data)
        basket.purchaseBasket()
        self.assertEqual("Your basket is emtpy.", self.user_output.getOutputList()[-1])


if __name__ == '__main__':
    unittest.main()
