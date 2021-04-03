from enum import Enum


class UserCommands(Enum):
    LIST = [["list", "view stock"],
            ["list"]]

    VIEW = [["view [game ID]", "view the selected game details"],
            ["view"]]

    ADD = [["add [game ID]", "add selected game to basket"],
           ["add"]]

    BASKET = [["basket", "view basket"],
              ["basket"]]

    REMOVE = [["remove [game ID]", "remove selected game from basket"],
              ["remove"]]

    BUY = [["buy", "purchase items in basket"],
           ["buy"]]

    HELP = [["help", "show available commands"],
            ["help"]]

    EXIT = [["exit", "leave program"],
            ["exit"]]

    @classmethod
    def displayCommandRow(cls, command_details, keyword_length):
        keyword = command_details[0][0]
        description = command_details[0][1]

        spacing_length = keyword_length - len(keyword)
        spacing = " " * spacing_length
        print(keyword + ": " + spacing + description)

    @classmethod
    def displayCommands(cls):
        print("The commands are:")
        keyword_length = cls.getLongestKeywordLength()

        for command in UserCommands:
            cls.displayCommandRow(command.value, keyword_length)
        print()

    @classmethod
    def getLongestKeywordLength(cls):
        longest_keyword = 0
        for command in UserCommands:
            command_keyword = command.value[0][0]
            keyword_length = len(command_keyword)

            if keyword_length > longest_keyword:
                longest_keyword = keyword_length
        return longest_keyword