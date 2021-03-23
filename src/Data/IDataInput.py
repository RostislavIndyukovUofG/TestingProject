from abc import ABC, abstractmethod

class IDataInput(ABC):
    
    @abstractmethod
    def getFileData(self):
        pass