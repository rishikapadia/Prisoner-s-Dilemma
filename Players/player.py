import Game
STAY_SILENT = Game.STAY_SILENT
RAT_OUT = Game.RAT_OUT

class Player():
    def __init__(self, _scoreboard, _ID):
        self.scoreboard = _scoreboard
        self.ID = _ID
        self.lawyerdiff = 0
        self.myresults = []
        if self.ID == 0:
            self.opponent = 1
        if self.ID == 1:
            self.opponent = 0

    
    def differences(self):
        num_round = self.scoreboard.get_round_number()
        if self.scoreboard.get_round_number():
            res = self.scoreboard.get_result(num_round - 1)[1]
            if self.myresults[num_round] == STAY_SILENT and (res == 0 or res == 2):
                self.lawyerdiff = self.lawyerdiff + 1
            if self.myresults[num_round] == RAT_OUT and (res == 1 or res == 3):
                self.lawyerdiff = self.lawyerdiff + 1
    
    def runs(x):
        silent_runs = 0;
        rat_runs = 0;
        number_silent = 0;
        number_rat = 0;
        max_silent_run = 0;
        max_rat_run = 0;
        silent_run_length = 0;
        rat_run_length = 0;
        rat_out = 0; 
        prev = 2;
        for i in x:
            if(i(self.opponent) == prev):
                if(i(self.opponent) == 1 or i(self.opponent) == 3):
                    silent_run_length+=1;
                    number_silent+=1;
                    if(silent_run_length == 2):
                        silent_runs+=1;
                if(i(self.opponent) == 0 or i(self.opponent) == 2):
                    number_rat+=1;
                    rat_run_length+=1;
                    if(rat_run_length == 2):
                        rat_runs+=1;
            else:
                if(i(self.opponent) == 1 or i(self.opponent) == 3):
                    max_rat_run = max(max_rat_run, rat_run);
                    rat_run_length = 0;
                    number_silent+=1;
                    silent_run_length+=1;
                else:
                    max_silent_run = max(max_silent_run, silent_run);
                    silent_run_length = 0;
                    number_rat+=1;
                    rat_run_length+=1;
            prev = i(self.opponent);
        max_rat_run = max(max_rat_run, rat_run);
        max_silent_run = max(max_silent_run, silent_run);
        return [number_silent,number_rat, silent_runs,rat_runs,max_silent_run,max_rat_run]
    
    def get_move(self):
        scores = []
        for i in range(self.scoreboard.get_round_number()):
            scores[i] = self.scoreboard.get_result(i)
        differences()
        stats = runs(scores)
        if self.scoreboard.get_result(self.scoreboard.get_round_number()-1):
            return Game.RAT_OUT
        
        return 0
        #return Game.STAY_SILENT
