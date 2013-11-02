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
            if(i == prev):
                if(i == STAY_SILENT):
                    silent_run_length+=1;
                    number_silent+=1;
                    if(silent_run_length == 2):
                        silent_runs+=1;
                if(i == RAT_OUT):
                    number_rat+=1;
                    rat_run_length+=1;
                    if(rat_run_length == 2):
                        rat_runs+=1;
            else:
                if(i == STAY_SILENT):
                    max_rat_run = max(max_rat_run, rat_run);
                    rat_run_length = 0;
                    number_silent+=1;
                    silent_run_length+=1;
                else:
                    max_silent_run = max(max_silent_run, silent_run);
                    silent_run_length = 0;
                    number_rat+=1;
                    rat_run_length+=1;
            prev = i;
        max_rat_run = max(max_rat_run, rat_run);
        max_silent_run = max(max_silent_run, silent_run);
        return [number_silent,number_rat, silent_runs,rat_runs,max_silent_run,max_rat_run]
    
    def get_move(self):
        #for i in range(self.scoreboard.get_round_number()):
        differences()
        if 
        return 0
        #return Game.STAY_SILENT
