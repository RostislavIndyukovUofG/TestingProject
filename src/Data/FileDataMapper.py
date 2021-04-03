from src.Engine.Game import Game


class FileDataMapper:

    @classmethod
    def mapFileDataToGameData(cls, file_data):
        game_data = []
        header_row = file_data[0]

        for row in file_data[1:]:
            game_id = row[0]
            game_name = row[1]
            price = float(row[2])
            stock = int(row[3])
            temp_game = Game(game_id, game_name, price, stock)
            game_data.append(temp_game)

        return header_row, game_data