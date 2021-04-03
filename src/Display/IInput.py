from abc import ABC, abstractmethod


class IInput(ABC):

    @abstractmethod
    def getInput(self, input_message):
        pass