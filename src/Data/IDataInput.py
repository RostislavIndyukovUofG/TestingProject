from abc import ABC, abstractmethod


class IDataInput(ABC):
    
    @abstractmethod
    def getData(self, file_path):
        pass