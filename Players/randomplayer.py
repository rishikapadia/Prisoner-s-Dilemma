import Game
from random import random

class Player():
    def __init__(self, _scoreboard, _ID):
        self.scoreboard = _scoreboard
        self.ID = _ID
        self.lawyerdiff = 0
        self.myresults = []


    def get_move(self):
        return int(random() + 1)
