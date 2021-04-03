from src.Display.DisplayInputs import ConsoleInput
from src.Display.DisplayOutputs import DisplayOutputs
from src.Engine.BasketControls import BasketControls
from src.Engine.UserCommands import UserCommands


class CommandHandler:
    game_store_main = None

    def __init__(self, game_store_main):
        self.game_store_main = game_store_main

    def handleUserCommands(self):
        UserCommands.displayCommands()
        active = True
        game_id = ""

        while active:
            user_command = ConsoleInput.getUserCommand()

            operation = user_command[0]
            if len(user_command) > 1:
                game_id = user_command[1]

            if operation in UserCommands.LIST.value[1]:
                DisplayOutputs.displayStock(self.game_store_main.header, self.game_store_main.game_data)

            elif operation in UserCommands.VIEW.value[1]:
                DisplayOutputs.displayGameDetails(self.game_store_main.getGameFromGameId(game_id))

            elif operation in UserCommands.ADD.value[1]:
                BasketControls.addToUserBasket(game_id, self.game_store_main, self.game_store_main.user_basket)

            elif operation in UserCommands.BASKET.value[1]:
                DisplayOutputs.displayUserBasket(self.game_store_main.user_basket)

            elif operation in UserCommands.REMOVE.value[1]:
                BasketControls.removeFromUserBasket(game_id, self.game_store_main, self.game_store_main.user_basket)

            elif operation in UserCommands.BUY.value[1]:
                BasketControls.purchaseUserBasket(self.game_store_main.user_basket, self.game_store_main.game_data)

            elif operation in UserCommands.HELP.value[1]:
                UserCommands.displayCommands()

            elif operation in UserCommands.EXIT.value[1]:
                exit()