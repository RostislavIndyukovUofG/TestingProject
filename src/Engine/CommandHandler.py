from src.Engine.Basket import Basket
from src.Engine.UserCommands import UserCommands


class CommandHandler:

    def __init__(self, user_input, user_output, game_data):
        self.user_input = user_input
        self.user_output = user_output
        self.game_data = game_data
        self.basket = Basket(self.user_input, self.user_output)

    def handleUserCommands(self):
        close = False
        game_id = ""
        UserCommands.displayCommands(self.user_output)

        while not close:

            # set up user command

            user_command = self.getUserCommand()
            operation = user_command[0]

            if len(user_command) > 1:
                game_id = user_command[1]

            # handle user command

            if operation in UserCommands.LIST.value[1]:
                self.game_data.displayGameData()

            elif operation in UserCommands.ADD.value[1]:
                game_to_add = self.game_data.getGameFromGameId(game_id)
                self.basket.updateBasket(game_to_add, "add")

            elif operation in UserCommands.REMOVE.value[1]:
                game_to_remove = self.game_data.getGameFromGameId(game_id)
                self.basket.updateBasket(game_to_remove, "remove")

            elif operation in UserCommands.BASKET.value[1]:
                self.user_output.displayOutput("\nYour basket:\n")
                self.basket.displayBasket()

            elif operation in UserCommands.PURCHASE.value[1]:
                self.basket.purchaseBasket()

            elif operation in UserCommands.HELP.value[1]:
                UserCommands.displayCommands(self.user_output)

            elif operation in UserCommands.EXIT.value[1]:
                self.user_output.displayOutput("Closing program.")
                close = True

        return close

    def getUserCommand(self):
        command_list = []
        is_valid_command = False

        while not is_valid_command:
            command = self.user_input.getInput("Enter a command: ")
            command_list = self.formatCommand(command)
            is_valid_command = self.isValidCommand(command_list)

            if not is_valid_command:
                self.user_output.displayOutput("Invalid command. Type help to see available commands.")

            if is_valid_command:
                is_valid_command = self.isValidGameId(command_list)

        return command_list

    def formatCommand(self, command):
        while command[0] == " " or command[-1] == " ":
            command = command.strip()

        command_list = command.split(" ")
        return command_list

    def isValidCommand(self, user_command_list):
        for command in UserCommands:
            valid_options = command.value[1]
            command_size = command.value[2]

            user_command_exists = user_command_list[0] in valid_options
            correct_size = len(user_command_list) == command_size

            if user_command_exists and correct_size:
                return True

        return False

    def isValidGameId(self, command_list):
        if len(command_list) > 1:
            game_id = command_list[1]

            if self.game_data.getGameFromGameId(game_id) is None:
                self.user_output.displayOutput("Invalid game id. Type list to view the available games.")
                return False

        return True
