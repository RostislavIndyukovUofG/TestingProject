from abc import ABC, abstractmethod


class IOutput(ABC):

    @abstractmethod
    def displayOutput(self, output_message):
        pass
