import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from sleeper_wrapper import League
from sleeper_wrapper import Players


scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('/volumes/alpha/programming/apikeys/creds.json', scope)
client = gspread.authorize(creds)

sheet = client.open('RUFFL 2021 Season Sheet - Testing')
sh  = sheet.worksheet('Week 2')
week = 2

class red_league:

    def __init__(self,*args):
        self.args = args

    def red_update(self,*args):
        self.red_league = League(728304037711237120)
        self.red_rosters = self.red_league.get_rosters()
        self.red_users = self.red_league.get_users()
        self.red_standings = self.red_league.get_standings(self.red_rosters,self.red_users)
        self.red_matchups = self.red_league.get_matchups(week)
        self.red_lineups = self.red_league.get_lineups(self.red_rosters,self.red_matchups,self.red_users,week)
        self.red_scoreboards = self.red_league.get_scoreboards(self.red_rosters,self.red_matchups,self.red_users,week)

        self.score1 = self.red_scoreboards[1][0]
        self.score2 = self.red_scoreboards[1][1]
        self.score3 = self.red_scoreboards[2][0]
        self.score4 = self.red_scoreboards[2][1]
        self.score5 = self.red_scoreboards[3][0]
        self.score6 = self.red_scoreboards[3][1]
        self.score7 = self.red_scoreboards[4][0]
        self.score8 = self.red_scoreboards[4][1]
        self.score9 = self.red_scoreboards[5][0]
        self.score10 = self.red_scoreboards[5][1]
        self.score11 = self.red_scoreboards[6][0]
        self.score12 = self.red_scoreboards[6][1]

        #self.results = {score1,score2,score3,score4,score5,score6}

        self.winner_name = []
        self.loser_name = []
        self.winner_score =[]
        self.loser_score = []
       
       #comparing each of the matchups to decide a winner and loser, then appending them to the correct lists. 
        if self.score1[1] > self.score2[1]:
           self.winner_name.append(self.score1[0])
           self.winner_score.append(self.score1[1])
           self.loser_name.append(self.score2[0])
           self.loser_score.append(self.score2[1])
        else: 
            self.winner_name.append(self.score2[0])
            self.winner_score.append(self.score2[1])
            self.loser_name.append(self.score1[0])
            self.loser_score.append(self.score1[1])

        if self.score3[1] > self.score4[1]:
           self.winner_name.append(self.score3[0])
           self.winner_score.append(self.score3[1])
           self.loser_name.append(self.score4[0])
           self.loser_score.append(self.score4[1])
        else: 
            self.winner_name.append(self.score4[0])
            self.winner_score.append(self.score4[1])
            self.loser_name.append(self.score3[0])
            self.loser_score.append(self.score3[1])
        
        if self.score5[1] > self.score6[1]:
           self.winner_name.append(self.score5[0])
           self.winner_score.append(self.score5[1])
           self.loser_name.append(self.score6[0])
           self.loser_score.append(self.score6[1])
        else: 
            self.winner_name.append(self.score6[0])
            self.winner_score.append(self.score6[1])
            self.loser_name.append(self.score5[0])
            self.loser_score.append(self.score5[1])

        if self.score7[1] > self.score8[1]:
           self.winner_name.append(self.score7[0])
           self.winner_score.append(self.score7[1])
           self.loser_name.append(self.score8[0])
           self.loser_score.append(self.score8[1])
        else: 
            self.winner_name.append(self.score8[0])
            self.winner_score.append(self.score8[1])
            self.loser_name.append(self.score7[0])
            self.loser_score.append(self.score7[1])
        
        if self.score9[1] > self.score10[1]:
           self.winner_name.append(self.score9[0])
           self.winner_score.append(self.score9[1])
           self.loser_name.append(self.score10[0])
           self.loser_score.append(self.score10[1])
        else: 
            self.winner_name.append(self.score10[0])
            self.winner_score.append(self.score10[1])
            self.loser_name.append(self.score9[0])
            self.loser_score.append(self.score9[1])

        if self.score11[1] > self.score12[1]:
           self.winner_name.append(self.score11[0])
           self.winner_score.append(self.score11[1])
           self.loser_name.append(self.score12[0])
           self.loser_score.append(self.score12[1])
        else: 
            self.winner_name.append(self.score12[0])
            self.winner_score.append(self.score12[1])
            self.loser_name.append(self.score11[0])
            self.loser_score.append(self.score11[1])

       #Delcaring the cells for the list to be committed too 
        self.winner_cell = sh.range('U74:U79')
        self.loser_cell = sh.range('W74:W79')
        self.winner_score_cell = sh.range('V74:V79')
        self.loser_score_cell = sh.range('X74:X79')
       
        for i, val in enumerate(self.winner_name):
            self.winner_cell[i].value = val
            sh.update_cells(self.winner_cell)
        
        for i, val in enumerate(self.loser_name):
            self.loser_cell[i].value = val
            sh.update_cells(self.loser_cell)

        for i, val in enumerate(self.winner_score):
            self.winner_score_cell[i].value = val
            sh.update_cells(self.winner_score_cell)

        for i, val in enumerate(self.loser_score):
            self.loser_score_cell[i].value = val
            sh.update_cells(self.loser_score_cell)

class green_league:

    def __init__(self,*args):
        self.args = args

    def green_update(self,*args):
        self.green_league = League(728300963290517504)
        self.green_rosters = self.green_league.get_rosters()
        self.green_users = self.green_league.get_users()
        self.green_standings = self.green_league.get_standings(self.green_rosters,self.green_users)
        self.green_matchups = self.green_league.get_matchups(week)
        self.green_lineups = self.green_league.get_lineups(self.green_rosters,self.green_matchups,self.green_users,week)
        self.green_scoreboards = self.green_league.get_scoreboards(self.green_rosters,self.green_matchups,self.green_users,week)

        self.score1 = self.green_scoreboards[1][0]
        self.score2 = self.green_scoreboards[1][1]
        self.score3 = self.green_scoreboards[2][0]
        self.score4 = self.green_scoreboards[2][1]
        self.score5 = self.green_scoreboards[3][0]
        self.score6 = self.green_scoreboards[3][1]
        self.score7 = self.green_scoreboards[4][0]
        self.score8 = self.green_scoreboards[4][1]
        self.score9 = self.green_scoreboards[5][0]
        self.score10 = self.green_scoreboards[5][1]
        self.score11 = self.green_scoreboards[6][0]
        self.score12 = self.green_scoreboards[6][1]

        #self.results = {score1,score2,score3,score4,score5,score6}

        self.winner_name = []
        self.loser_name = []
        self.winner_score =[]
        self.loser_score = []
       
       #comparing each of the matchups to decide a winner and loser, then appending them to the correct lists. 
        if self.score1[1] > self.score2[1]:
           self.winner_name.append(self.score1[0])
           self.winner_score.append(self.score1[1])
           self.loser_name.append(self.score2[0])
           self.loser_score.append(self.score2[1])
        else: 
            self.winner_name.append(self.score2[0])
            self.winner_score.append(self.score2[1])
            self.loser_name.append(self.score1[0])
            self.loser_score.append(self.score1[1])

        if self.score3[1] > self.score4[1]:
           self.winner_name.append(self.score3[0])
           self.winner_score.append(self.score3[1])
           self.loser_name.append(self.score4[0])
           self.loser_score.append(self.score4[1])
        else: 
            self.winner_name.append(self.score4[0])
            self.winner_score.append(self.score4[1])
            self.loser_name.append(self.score3[0])
            self.loser_score.append(self.score3[1])
        
        if self.score5[1] > self.score6[1]:
           self.winner_name.append(self.score5[0])
           self.winner_score.append(self.score5[1])
           self.loser_name.append(self.score6[0])
           self.loser_score.append(self.score6[1])
        else: 
            self.winner_name.append(self.score6[0])
            self.winner_score.append(self.score6[1])
            self.loser_name.append(self.score5[0])
            self.loser_score.append(self.score5[1])

        if self.score7[1] > self.score8[1]:
           self.winner_name.append(self.score7[0])
           self.winner_score.append(self.score7[1])
           self.loser_name.append(self.score8[0])
           self.loser_score.append(self.score8[1])
        else: 
            self.winner_name.append(self.score8[0])
            self.winner_score.append(self.score8[1])
            self.loser_name.append(self.score7[0])
            self.loser_score.append(self.score7[1])
        
        if self.score9[1] > self.score10[1]:
           self.winner_name.append(self.score9[0])
           self.winner_score.append(self.score9[1])
           self.loser_name.append(self.score10[0])
           self.loser_score.append(self.score10[1])
        else: 
            self.winner_name.append(self.score10[0])
            self.winner_score.append(self.score10[1])
            self.loser_name.append(self.score9[0])
            self.loser_score.append(self.score9[1])

        if self.score11[1] > self.score12[1]:
           self.winner_name.append(self.score11[0])
           self.winner_score.append(self.score11[1])
           self.loser_name.append(self.score12[0])
           self.loser_score.append(self.score12[1])
        else: 
            self.winner_name.append(self.score12[0])
            self.winner_score.append(self.score12[1])
            self.loser_name.append(self.score11[0])
            self.loser_score.append(self.score11[1])

       #Delcaring the cells for the list to be committed too 
        self.winner_cell = sh.range('U38:U43')
        self.loser_cell = sh.range('W38:W43')
        self.winner_score_cell = sh.range('V38:V43')
        self.loser_score_cell = sh.range('X38:X43')
       
        print(self.winner_name)

        for i, val in enumerate(self.winner_name):
            self.winner_cell[i].value = val
            sh.update_cells(self.winner_cell)
        
        for i, val in enumerate(self.loser_name):
            self.loser_cell[i].value = val
            sh.update_cells(self.loser_cell)

        for i, val in enumerate(self.winner_score):
            self.winner_score_cell[i].value = val
            sh.update_cells(self.winner_score_cell)

        for i, val in enumerate(self.loser_score):
            self.loser_score_cell[i].value = val
            sh.update_cells(self.loser_score_cell)
if __name__ == "__main__":
    red_league().red_update()
    green_league().green_update()
