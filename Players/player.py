import Game

class Player():
    def __init__(self, _scoreboard, _ID):
        self.scoreboard = _scoreboard
        self.ID = _ID
        self.lawyerdiff = 0
        self.myresults = []


    def get_move(self):
        return Game.RAT_OUT
        #for i in range(self.scoreboard.get_round_number()):
        num_round = self.scoreboard.get_round_number()
        if self.scoreboard.get_round_number():
            res = self.scoreboard.get_result(num_round)
            #if self.myresults != res:
                
        from random import random
        return int(random() + 1)
        #return Game.STAY_SILENT
