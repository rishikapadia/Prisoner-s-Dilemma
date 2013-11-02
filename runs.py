#x is an input of loses and wins.

RAT_OUT = 0
STAY_SILENT = 1

#returns number of 1 runs, 0 runs.
#Returns a list with 
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
