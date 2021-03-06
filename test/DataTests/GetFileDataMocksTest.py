import unittest
from unittest.mock import MagicMock

from src.Data.DataInputFile import DataInputFile
from src.Display.TestOutput import TestOutput


class GetFileDataMocksTest(unittest.TestCase):
    file_path = "../../resources/gameData.csv"
    input_type = DataInputFile()
    user_output = TestOutput()

    data_list = [["GameID", "Game Name", "Price", "Stock"],
                 ["1", "City Builder", "8.99", "4"],
                 ["2", "Survivalist", "9.99", "5"]]

    data_list2 = [["GameID", "Game Name", "Price", "Stock"],
                  ["3", "Secret Treasure", "26.99", "7"]]

    data_list3 = [["GameID", "Game Name", "Price", "Stock"],
                  ["4", "Arena Battler", "14.99", "8"]]

    def test_getDataFromFoundFileMock(self):
        DataInputFile.readRawData = MagicMock(return_value=self.data_list)
        getFileData = self.input_type.getFileData
        file_data = getFileData(self.file_path, self.user_output)
        self.assertEqual(['1', 'City Builder', '8.99', '4'], file_data[1])

    def test_getGameDataFromMissingFileMock(self):
        DataInputFile.readRawData = MagicMock(side_effect=FileNotFoundError)
        getFileData = self.input_type.getFileData
        file_data = getFileData(self.file_path, self.user_output)
        self.assertEqual(['3', 'PC Video Game', '7.99', '3'], file_data[-1])

    def test_getGameDataFromMultipleFoundFilesMock(self):
        DataInputFile.readRawData = MagicMock(side_effect=[self.data_list, self.data_list2, self.data_list3])
        getFileData = self.input_type.getFileData
        file_data = getFileData(self.file_path, self.user_output)
        file_data2 = getFileData(self.file_path, self.user_output)
        file_data3 = getFileData(self.file_path, self.user_output)
        self.assertEqual(['4', 'Arena Battler', '14.99', '8'], file_data3[-1])


if __name__ == '__main__':
    unittest.main()
