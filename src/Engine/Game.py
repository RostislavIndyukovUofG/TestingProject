class Game:
    game_id = None
    game_name = None
    price = None
    age_rating = None
    platform = None

    def __init__(self, game_id, game_name, price, age_rating, platform):
        self.game_id = game_id
        self.game_name = game_name
        self.price = price
        self.age_rating = age_rating
        self.platform = platform

    def getGameID(self):
        return self.game_id

    def getGameName(self):
        return self.game_name

    def getPrice(self):
        return self.price

    def getAgeRating(self):
        return self.age_rating

    def getPlatform(self):
        return self.platform
