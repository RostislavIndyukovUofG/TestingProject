import unittest

from src.Display.ConsoleInput import ConsoleInput
from src.Display.TestOutput import TestOutput
from src.Engine.Basket import Basket
from src.Engine.Game import Game


class BasketTest(unittest.TestCase):
    user_input = ConsoleInput(False)
    user_output = TestOutput()

    game = Game("1", "Anno 1701", 8.99, 4)
    game2 = Game("2", "Metro 2033", 9.99, 5)
    game3 = Game("3", "Assassin's Creed Brotherhood", 26.99, 7)

    game_data = [game, game2, game3]

    # updateBasket

    def test_addGameToEmptyBasket(self):
        user_input = ConsoleInput(False)
        user_output = TestOutput()
        basket = Basket(user_input, user_output)
        basket.updateBasket(self.game, "add")
        self.assertEqual(self.game, basket.getBasketList()[0])

    def test_addGameToBasket(self):
        user_input = ConsoleInput(False)
        user_output = TestOutput()
        basket = Basket(user_input, user_output)
        basket_size = len(basket.getBasketList())
        basket.updateBasket(self.game, "add")
        self.assertEqual(basket_size + 1, len(basket.getBasketList()))

    def test_addGameToBasketOutput(self):
        user_input = ConsoleInput(False)
        user_output = TestOutput()
        basket = Basket(user_input, user_output)
        basket.updateBasket(self.game, "add")
        self.assertEqual("Game added successfully.", user_output.getOutputList()[-1])

    def test_addExistingGameToBasketOutput(self):
        user_input = ConsoleInput(False)
        user_output = TestOutput()
        basket = Basket(user_input, user_output)
        basket.updateBasket(self.game, "add")
        basket.updateBasket(self.game, "add")
        output_message = "Game not added; game may already be in basket."
        self.assertEqual(output_message, user_output.getOutputList()[-1])

    def test_addMultipleGamesToBasket(self):
        user_input = ConsoleInput(False)
        user_output = TestOutput()
        basket = Basket(user_input, user_output)
        basket.updateBasket(self.game, "add")
        basket.updateBasket(self.game2, "add")
        basket.updateBasket(self.game3, "add")
        self.assertEqual(3, len(basket.getBasketList()))

    def test_removeExistingGameFromBasket(self):
        user_input = ConsoleInput(False)
        user_output = TestOutput()
        basket = Basket(user_input, user_output)
        basket.updateBasket(self.game, "add")
        basket_size = len(basket.getBasketList())
        basket.updateBasket(self.game, "remove")
        self.assertEqual(basket_size - 1, len(basket.getBasketList()))

    def test_removeExistingGameFromBasketOutput(self):
        user_input = ConsoleInput(False)
        user_output = TestOutput()
        basket = Basket(user_input, user_output)
        basket.updateBasket(self.game, "add")
        basket.updateBasket(self.game, "remove")
        self.assertEqual("Game removed successfully.", user_output.getOutputList()[-1])

    def test_removeGameFromEmptyBasket(self):
        user_input = ConsoleInput(False)
        user_output = TestOutput()
        basket = Basket(user_input, user_output)
        basket.updateBasket(self.game, "remove")
        self.assertEqual("Game not in basket.", user_output.getOutputList()[-1])

    def test_removeMissingGameFromBasket(self):
        user_input = ConsoleInput(False)
        user_output = TestOutput()
        basket = Basket(user_input, user_output)
        basket.updateBasket(self.game, "add")
        basket_size = len(basket.getBasketList())
        basket.updateBasket(self.game2, "remove")
        self.assertEqual(basket_size, len(basket.getBasketList()))

    def test_removeMissingGameFromBasketOutput(self):
        user_input = ConsoleInput(False)
        user_output = TestOutput()
        basket = Basket(user_input, user_output)
        basket.updateBasket(self.game2, "remove")
        self.assertEqual("Game not in basket.", user_output.getOutputList()[-1])

    def test_removeMultipleGamesFromBasket(self):
        user_input = ConsoleInput(False)
        user_output = TestOutput()
        basket = Basket(user_input, user_output)
        basket.updateBasket(self.game, "add")
        basket.updateBasket(self.game2, "add")
        basket.updateBasket(self.game3, "add")
        basket.updateBasket(self.game, "remove")
        basket.updateBasket(self.game2, "remove")
        basket.updateBasket(self.game3, "remove")
        self.assertEqual(0, len(basket.getBasketList()))

    # addToBasket

    def test_AddNewGameToBasket(self):
        basket = Basket(self.user_input, self.user_output)
        basket.addToBasket(-1, self.game)
        self.assertEqual(1, len(basket.getBasketList()))

    def test_AddNewGameToBasketOutput(self):
        basket = Basket(self.user_input, self.user_output)
        basket.addToBasket(-1, self.game)
        self.assertEqual(1, len(basket.getBasketList()))

    def test_AddMultipleGamesToBasket(self):
        basket = Basket(self.user_input, self.user_output)
        basket.addToBasket(-1, self.game)
        basket.addToBasket(-1, self.game2)
        basket.addToBasket(-1, self.game3)
        self.assertEqual(3, len(basket.getBasketList()))

    def test_AddExistingGameToBasket(self):
        basket = Basket(self.user_input, self.user_output)
        basket.updateBasket(self.game, "add")
        basket.addToBasket(0, self.game)
        self.assertEqual(1, len(basket.getBasketList()))

    def test_AddExistingGameToBasketOutput(self):
        basket = Basket(self.user_input, self.user_output)
        basket.updateBasket(self.game, "add")
        basket.addToBasket(0, self.game)
        output_message = "Game not added; game may already be in basket."
        self.assertEqual(output_message, self.user_output.getOutputList()[-1])

    # removeFromBasket

    def test_RemoveExistingGameFromBasket(self):
        basket = Basket(self.user_input, self.user_output)
        basket.updateBasket(self.game, "add")
        basket.removeFromBasket(0, self.game)
        self.assertEqual(0, len(basket.getBasketList()))

    def test_RemoveExistingGameFromBasketOutput(self):
        basket = Basket(self.user_input, self.user_output)
        basket.updateBasket(self.game, "add")
        basket.removeFromBasket(0, self.game)
        output_message = "Game removed successfully."
        self.assertEqual(output_message, self.user_output.getOutputList()[-1])

    def test_RemoveMultipleGamesFromBasket(self):
        basket = Basket(self.user_input, self.user_output)
        basket.updateBasket(self.game, "add")
        basket.updateBasket(self.game2, "add")
        basket.updateBasket(self.game3, "add")
        basket.removeFromBasket(0, self.game)
        basket.removeFromBasket(0, self.game2)
        basket.removeFromBasket(0, self.game3)
        self.assertEqual(0, len(basket.getBasketList()))

    def test_RemoveMissingGameFromBasket(self):
        basket = Basket(self.user_input, self.user_output)
        basket.updateBasket(self.game, "add")
        basket.removeFromBasket(-1, self.game2)
        self.assertEqual(1, len(basket.getBasketList()))

    def test_RemoveMissingGameFromBasketOutput(self):
        basket = Basket(self.user_input, self.user_output)
        basket.updateBasket(self.game, "add")
        basket.removeFromBasket(-1, self.game2)
        output_message = "Game not in basket."
        self.assertEqual(output_message, self.user_output.getOutputList()[-1])

    # findGameInBasket

    def test_FindExistingGame(self):
        basket = Basket(self.user_input, self.user_output)
        basket.updateBasket(self.game, "add")
        basket.updateBasket(self.game2, "add")
        basket.updateBasket(self.game3, "add")
        self.assertEqual(1, basket.findGameInBasket(self.game2))

    def test_FindMissingGame(self):
        basket = Basket(self.user_input, self.user_output)
        basket.updateBasket(self.game, "add")
        basket.updateBasket(self.game2, "add")
        self.assertEqual(-1, basket.findGameInBasket(self.game3))

    def test_FindGameInEmptyBasket(self):
        basket = Basket(self.user_input, self.user_output)
        self.assertEqual(-1, basket.findGameInBasket(self.game))

    # calculateBasketTotal

    def test_CalculateBasketTotal(self):
        basket = Basket(self.user_input, self.user_output)
        basket.updateBasket(self.game, "add")
        basket.updateBasket(self.game2, "add")
        basket.calcualateBasketTotal()
        self.assertEqual(18.98, basket.getBasketTotal())

    def test_CalculateEmptyBasketTotal(self):
        basket = Basket(self.user_input, self.user_output)
        basket.calcualateBasketTotal()
        self.assertEqual(0, basket.getBasketTotal())

    def test_CalculateUpdatedBasketTotal(self):
        basket = Basket(self.user_input, self.user_output)
        basket.updateBasket(self.game, "add")
        basket.calcualateBasketTotal()
        basket_total = basket.getBasketTotal()
        basket.updateBasket(self.game2, "add")
        basket.calcualateBasketTotal()
        self.assertNotEqual(basket_total, basket.getBasketTotal())

    # displayBasket

    def test_displayBasketOutput(self):
        basket = Basket(self.user_input, self.user_output)
        basket.updateBasket(self.game, "add")
        basket.updateBasket(self.game2, "add")
        basket.displayBasket()
        self.assertEqual("Basket total: £18.98", self.user_output.getOutputList()[-1])

    def test_displayEmptyBasketOutput(self):
        basket = Basket(self.user_input, self.user_output)
        basket.displayBasket()
        self.assertEqual("Basket total: £0.0", self.user_output.getOutputList()[-1])

    # purchaseBasket

    def test_purchaseBasket(self):
        basket = Basket(self.user_input, self.user_output)
        basket.updateBasket(self.game, "add")
        basket.updateBasket(self.game2, "add")
        basket.purchaseBasket(self.game_data)
        self.assertEqual(0, len(basket.getBasketList()))

    def test_purchaseBasketOutput(self):
        basket = Basket(self.user_input, self.user_output)
        basket.updateBasket(self.game, "add")
        basket.updateBasket(self.game2, "add")
        basket.purchaseBasket(self.game_data)
        self.assertEqual("Your order:", self.user_output.getOutputList()[-3])

    def test_purchaseEmptyBasketOutput(self):
        basket = Basket(self.user_input, self.user_output)
        basket.purchaseBasket(self.game_data)
        self.assertEqual("Your basket is emtpy.", self.user_output.getOutputList()[-1])




if __name__ == '__main__':
    unittest.main()
