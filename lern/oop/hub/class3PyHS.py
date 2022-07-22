from datetime import datetime as dt


class Player:
    __LEVEL, __HEALTH = 1, 10
    __slots__ = ['__level', '__health', '__born']

    def __init__(self):
        self.__level = Player.__LEVEL
        self.__health = Player.__HEALTH
        self.__born = dt.now()

    def level(self):
        return self.__level

    def level(self, numeric):
        self.__level += numeric
