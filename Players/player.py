import Game
STAY_SILENT = Game.STAY_SILENT
RAT_OUT = Game.RAT_OUT

class Player():
    def __init__(self, _scoreboard, _ID):
        self.scoreboard = _scoreboard
        self.ID = _ID
        self.lawyerdiff = 0
        self.myresults = []


    def differences(self):
        num_round = self.scoreboard.get_round_number()
        if self.scoreboard.get_round_number():
            res = self.scoreboard.get_result(num_round - 1)
            if self.myresults[num_round] == STAY_SILENT and (res == 0 or res == 2):
                self.lawyerdiff = self.lawyerdiff + 1
            if self.myresults[num_round] == RAT_OUT and (res == 1 or res == 3):
                self.lawyerdiff = self.lawyerdiff + 1    



    def get_move(self):
        return Game.RAT_OUT
        #for i in range(self.scoreboard.get_round_number()):
        differences()
        from random import random
        return int(random() + 1)
        #return Game.STAY_SILENT
