from abc import ABC, abstractmethod


class IDataInput(ABC):
    
    @abstractmethod
    def getFileData(self, file_path):
        pass