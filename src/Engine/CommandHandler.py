from src.Engine.UserCommands import UserCommands


class CommandHandler:

    def __init__(self, user_input, user_output, basket, main):
        self.user_input = user_input
        self.user_output = user_output
        self.basket = basket
        self.main = main

    def handleUserCommands(self):
        UserCommands.displayCommands(self.user_output)
        active = True
        close = True
        game_id = ""

        while active:
            user_command = self.getUserCommand()

            operation = user_command[0]
            if len(user_command) > 1:
                game_id = user_command[1]

            if operation in UserCommands.LIST.value[1]:
                self.main.displayStock()

            elif operation in UserCommands.ADD.value[1]:
                game_to_add = self.main.getGameFromGameId(game_id)
                self.basket.addToBasket(game_to_add)

            elif operation in UserCommands.BASKET.value[1]:
                self.basket.displayBasket()

            elif operation in UserCommands.REMOVE.value[1]:
                game_to_remove = self.main.getGameFromGameId(game_id)
                self.basket.removeFromBasket(game_to_remove)

            elif operation in UserCommands.BUY.value[1]:
                self.basket.purchaseBasket(self.main.getGameData())

            elif operation in UserCommands.HELP.value[1]:
                UserCommands.displayCommands(self.user_output)

            elif operation in UserCommands.EXIT.value[1]:
                self.user_output.displayOutput("Closing program.")
                active = False

        return close


    def getUserCommand(self):
        is_valid_command = False
        while not is_valid_command:
            try:
                command_list = []
                command = self.user_input.getInput("Enter a command: ")
                command_list = self.formatCommand(command)
                is_valid_command = self.isValidUserCommand(command_list[0])

                if not is_valid_command:
                    raise ValueError
            except:
                self.user_input.getInput("Invalid command. Type help to see available commands: ")

        return command_list

    def formatCommand(self, command):
        command.strip()
        command_list = command.split(" ")
        return command_list

    def isValidUserCommand(self, command_operation):
        for command in UserCommands:
            if command_operation in command.value[1]:
                return True
        return False