from abc import ABC, abstractmethod


class IDataInput(ABC):
    
    @abstractmethod
    def readRawData(self, file_path):
        pass

    @abstractmethod
    def getFileData(self, file_path, user_output):
        pass