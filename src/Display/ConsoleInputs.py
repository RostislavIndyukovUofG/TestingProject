from src.Engine.UserCommands import UserCommands

class ConsoleInputs:

    @classmethod
    def getUserCommand(cls):
        is_valid_command = False
        while not is_valid_command:
            try:
                user_command_list = []
                raw_command = input("Enter a command: ")
                raw_command.strip()
                user_command_list = raw_command.split(" ")
                is_valid_command = cls.isValidUserCommand(user_command_list)

                if not is_valid_command:
                    raise ValueError
            except:
                print("Invalid command. Type help to see available commands: ")
        return user_command_list

    @classmethod
    def isValidUserCommand(cls, user_command_list):
        for command in UserCommands:
            if user_command_list[0] in command.value[1]:
                return True
        return False