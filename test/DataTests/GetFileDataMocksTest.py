import unittest
from unittest.mock import MagicMock

from src.Data.DataInputFile import DataInputFile
from src.Display.TestOutput import TestOutput


class GetFileDataMocksTest(unittest.TestCase):
    data_list = []
    data_list.append(["GameID", "Game Name", "Price", "Stock"])
    data_list.append(["1", "Anno 1701", "8.99", "4"])
    data_list.append(["2", "Metro 2033", "9.99", "5"])

    data_list2 = []
    data_list2.append(["GameID", "Game Name", "Price", "Stock"])
    data_list2.append(["3", "Assassin's Creed Brotherhood", "26.99", "7"])

    data_list3 = []
    data_list3.append(["GameID", "Game Name", "Price", "Stock"])
    data_list3.append(["4", "Killer Instinct", "14.99", "8"])

    user_output = TestOutput()

    def test_getHeaderFromFoundFileMock(self):
        file_path = "../../resources/gameData.csv"
        data_file = DataInputFile()
        DataInputFile.readRawData = MagicMock(return_value=self.data_list)
        header, game_data = data_file.getGameDataAndHeader(file_path, self.user_output)
        self.assertEqual(["GameID", "Game Name", "Price", "Stock"], header)

    def test_getGameDataFromFoundFileMock(self):
        file_path = "../../resources/gameData.csv"
        data_file = DataInputFile()
        DataInputFile.readRawData = MagicMock(return_value=self.data_list)
        header, game_data = data_file.getGameDataAndHeader(file_path, self.user_output)
        self.assertEqual("Metro 2033", game_data[-1].getGameName())

    def test_getGameDataFromMissingFileMock(self):
        file_path = "../../resources/gameData.csv"
        data_file = DataInputFile()
        DataInputFile.readRawData = MagicMock(side_effect=FileNotFoundError)
        header, game_data = data_file.getGameDataAndHeader(file_path, self.user_output)
        self.assertEqual("PC Video Game", game_data[-1].getGameName())

    def test_getGameDataFromMultipleFoundFilesMock(self):
        file_path = "../../resources/gameData.csv"
        data_file = DataInputFile()
        DataInputFile.readRawData = MagicMock(side_effect=[self.data_list, self.data_list2, self.data_list3])
        header, game_data = data_file.getGameDataAndHeader(file_path, self.user_output)
        header, game_data = data_file.getGameDataAndHeader(file_path, self.user_output)
        header, game_data = data_file.getGameDataAndHeader(file_path, self.user_output)
        self.assertEqual("Killer Instinct", game_data[-1].getGameName())


if __name__ == '__main__':
    unittest.main()
