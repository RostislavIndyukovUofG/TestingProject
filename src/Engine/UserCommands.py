from enum import Enum


class UserCommands(Enum):
    LIST = [["list", "view stock"],
            ["list", "l"]]

    ADD = [["add [game ID]", "add selected game to basket"],
           ["add", "a"]]

    BASKET = [["basket", "view basket"],
              ["basket", "b"]]

    REMOVE = [["remove [game ID]", "remove selected game from basket"],
              ["remove", "r"]]

    BUY = [["purchase", "purchase items in basket"],
           ["purchase", "p"]]

    HELP = [["help", "show available commands"],
            ["help", "h"]]

    EXIT = [["exit", "leave program"],
            ["exit", "e"]]

    @classmethod
    def displayCommandRow(cls, command_details, keyword_length, user_output):
        keyword = command_details[0][0]
        description = command_details[0][1]

        spacing_length = keyword_length - len(keyword)
        spacing = " " * spacing_length
        user_output.displayOutput(keyword + ": " + spacing + description)

    @classmethod
    def displayCommands(cls, user_output):
        user_output.displayOutput("The commands are:")
        keyword_length = cls.getLongestWordLength()

        for command in UserCommands:
            cls.displayCommandRow(command.value, keyword_length, user_output)
        print()

    @classmethod
    def getLongestWordLength(cls):
        longest_word = 0
        for command in UserCommands:
            command_keyword = command.value[0][0]
            keyword_length = len(command_keyword)

            if keyword_length > longest_word:
                longest_word = keyword_length
        return longest_word