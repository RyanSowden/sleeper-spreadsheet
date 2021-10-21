import gspread
import time
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from sleeper_wrapper import League
from sleeper_wrapper import Players


scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('/volumes/alpha/programming/apikeys/creds.json', scope)
client = gspread.authorize(creds)

sheet = client.open('RUFFL 2021 Season Sheet - Testing')
sh  = sheet.worksheet('Week 4')
week = 4

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
        self.winner_cell = sh.range('U70:U75')
        self.loser_cell = sh.range('W70:W75')
        self.winner_score_cell = sh.range('V70:V75')
        self.loser_score_cell = sh.range('X70:X75')
       
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
        self.winner_cell = sh.range('U34:U39')
        self.loser_cell = sh.range('W34:W39')
        self.winner_score_cell = sh.range('V34:V39')
        self.loser_score_cell = sh.range('X34:X39')
       

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
        time.sleep(60)

class black_league:

    def __init__(self,*args):
        self.args = args

    def black_update(self,*args):
        self.black_league = League(728298233297797120)
        self.black_rosters = self.black_league.get_rosters()
        self.black_users = self.black_league.get_users()
        self.black_standings = self.black_league.get_standings(self.black_rosters,self.black_users)
        self.black_matchups = self.black_league.get_matchups(week)
        self.black_lineups = self.black_league.get_lineups(self.black_rosters,self.black_matchups,self.black_users,week)
        self.black_scoreboards = self.black_league.get_scoreboards(self.black_rosters,self.black_matchups,self.black_users,week)

        self.score1 = self.black_scoreboards[1][0]
        self.score2 = self.black_scoreboards[1][1]
        self.score3 = self.black_scoreboards[2][0]
        self.score4 = self.black_scoreboards[2][1]
        self.score5 = self.black_scoreboards[3][0]
        self.score6 = self.black_scoreboards[3][1]
        self.score7 = self.black_scoreboards[4][0]
        self.score8 = self.black_scoreboards[4][1]
        self.score9 = self.black_scoreboards[5][0]
        self.score10 = self.black_scoreboards[5][1]
        self.score11 = self.black_scoreboards[6][0]
        self.score12 = self.black_scoreboards[6][1]

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
        self.winner_cell = sh.range('U4:U9')
        self.loser_cell = sh.range('W4:W9')
        self.winner_score_cell = sh.range('V4:V9')
        self.loser_score_cell = sh.range('X4:X9')
       

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

class blue_league:

    def __init__(self,*args):
        self.args = args

    def blue_update(self,*args):
        self.blue_league = League(728131727024865280)
        self.blue_rosters = self.blue_league.get_rosters()
        self.blue_users = self.blue_league.get_users()
        self.blue_standings = self.blue_league.get_standings(self.blue_rosters,self.blue_users)
        self.blue_matchups = self.blue_league.get_matchups(week)
        self.blue_lineups = self.blue_league.get_lineups(self.blue_rosters,self.blue_matchups,self.blue_users,week)
        self.blue_scoreboards = self.blue_league.get_scoreboards(self.blue_rosters,self.blue_matchups,self.blue_users,week)

        self.score1 = self.blue_scoreboards[1][0]
        self.score2 = self.blue_scoreboards[1][1]
        self.score3 = self.blue_scoreboards[2][0]
        self.score4 = self.blue_scoreboards[2][1]
        self.score5 = self.blue_scoreboards[3][0]
        self.score6 = self.blue_scoreboards[3][1]
        self.score7 = self.blue_scoreboards[4][0]
        self.score8 = self.blue_scoreboards[4][1]
        self.score9 = self.blue_scoreboards[5][0]
        self.score10 = self.blue_scoreboards[5][1]
        self.score11 = self.blue_scoreboards[6][0]
        self.score12 = self.blue_scoreboards[6][1]


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
        self.winner_cell = sh.range('U10:U15')
        self.loser_cell = sh.range('W10:W15')
        self.winner_score_cell = sh.range('V10:V15')
        self.loser_score_cell = sh.range('X10:X15')
       

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
        time.sleep(60)

class brown_league:

    def __init__(self,*args):
        self.args = args

    def brown_update(self,*args):
        self.brown_league = League(728298916340187136)
        self.brown_rosters = self.brown_league.get_rosters()
        self.brown_users = self.brown_league.get_users()
        self.brown_standings = self.brown_league.get_standings(self.brown_rosters,self.brown_users)
        self.brown_matchups = self.brown_league.get_matchups(week)
        self.brown_lineups = self.brown_league.get_lineups(self.brown_rosters,self.brown_matchups,self.brown_users,week)
        self.brown_scoreboards = self.brown_league.get_scoreboards(self.brown_rosters,self.brown_matchups,self.brown_users,week)

        self.score1 = self.brown_scoreboards[1][0]
        self.score2 = self.brown_scoreboards[1][1]
        self.score3 = self.brown_scoreboards[2][0]
        self.score4 = self.brown_scoreboards[2][1]
        self.score5 = self.brown_scoreboards[3][0]
        self.score6 = self.brown_scoreboards[3][1]
        self.score7 = self.brown_scoreboards[4][0]
        self.score8 = self.brown_scoreboards[4][1]
        self.score9 = self.brown_scoreboards[5][0]
        self.score10 = self.brown_scoreboards[5][1]
        self.score11 = self.brown_scoreboards[6][0]
        self.score12 = self.brown_scoreboards[6][1]


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
        self.winner_cell = sh.range('U16:U21')
        self.loser_cell = sh.range('W16:W21')
        self.winner_score_cell = sh.range('V16:V21')
        self.loser_score_cell = sh.range('X16:X21')
       

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

class forest_league:

    def __init__(self,*args):
        self.args = args

    def forest_update(self,*args):
        self.forest_league = League(728299677849600000)
        self.forest_rosters = self.forest_league.get_rosters()
        self.forest_users = self.forest_league.get_users()
        self.forest_standings = self.forest_league.get_standings(self.forest_rosters,self.forest_users)
        self.forest_matchups = self.forest_league.get_matchups(week)
        self.forest_lineups = self.forest_league.get_lineups(self.forest_rosters,self.forest_matchups,self.forest_users,week)
        self.forest_scoreboards = self.forest_league.get_scoreboards(self.forest_rosters,self.forest_matchups,self.forest_users,week)

        self.score1 = self.forest_scoreboards[1][0]
        self.score2 = self.forest_scoreboards[1][1]
        self.score3 = self.forest_scoreboards[2][0]
        self.score4 = self.forest_scoreboards[2][1]
        self.score5 = self.forest_scoreboards[3][0]
        self.score6 = self.forest_scoreboards[3][1]
        self.score7 = self.forest_scoreboards[4][0]
        self.score8 = self.forest_scoreboards[4][1]
        self.score9 = self.forest_scoreboards[5][0]
        self.score10 = self.forest_scoreboards[5][1]
        self.score11 = self.forest_scoreboards[6][0]
        self.score12 = self.forest_scoreboards[6][1]


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
        self.winner_cell = sh.range('U22:U27')
        self.loser_cell = sh.range('W22:W27')
        self.winner_score_cell = sh.range('V22:V27')
        self.loser_score_cell = sh.range('X22:X27')
       

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
        time.sleep(60)

class gray_league:

    def __init__(self,*args):
        self.args = args

    def gray_update(self,*args):
        self.gray_league = League(728300277744140288)
        self.gray_rosters = self.gray_league.get_rosters()
        self.gray_users = self.gray_league.get_users()
        self.gray_standings = self.gray_league.get_standings(self.gray_rosters,self.gray_users)
        self.gray_matchups = self.gray_league.get_matchups(week)
        self.gray_lineups = self.gray_league.get_lineups(self.gray_rosters,self.gray_matchups,self.gray_users,week)
        self.gray_scoreboards = self.gray_league.get_scoreboards(self.gray_rosters,self.gray_matchups,self.gray_users,week)

        self.score1 = self.gray_scoreboards[1][0]
        self.score2 = self.gray_scoreboards[1][1]
        self.score3 = self.gray_scoreboards[2][0]
        self.score4 = self.gray_scoreboards[2][1]
        self.score5 = self.gray_scoreboards[3][0]
        self.score6 = self.gray_scoreboards[3][1]
        self.score7 = self.gray_scoreboards[4][0]
        self.score8 = self.gray_scoreboards[4][1]
        self.score9 = self.gray_scoreboards[5][0]
        self.score10 = self.gray_scoreboards[5][1]
        self.score11 = self.gray_scoreboards[6][0]
        self.score12 = self.gray_scoreboards[6][1]


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
        self.winner_cell = sh.range('U28:U33')
        self.loser_cell = sh.range('W28:W33')
        self.winner_score_cell = sh.range('V28:V33')
        self.loser_score_cell = sh.range('X28:X33')
       

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


class lime_league:

    def __init__(self,*args):
        self.args = args

    def lime_update(self,*args):
        self.lime_league = League(728301690490585088)
        self.lime_rosters = self.lime_league.get_rosters()
        self.lime_users = self.lime_league.get_users()
        self.lime_standings = self.lime_league.get_standings(self.lime_rosters,self.lime_users)
        self.lime_matchups = self.lime_league.get_matchups(week)
        self.lime_lineups = self.lime_league.get_lineups(self.lime_rosters,self.lime_matchups,self.lime_users,week)
        self.lime_scoreboards = self.lime_league.get_scoreboards(self.lime_rosters,self.lime_matchups,self.lime_users,week)

        self.score1 = self.lime_scoreboards[1][0]
        self.score2 = self.lime_scoreboards[1][1]
        self.score3 = self.lime_scoreboards[2][0]
        self.score4 = self.lime_scoreboards[2][1]
        self.score5 = self.lime_scoreboards[3][0]
        self.score6 = self.lime_scoreboards[3][1]
        self.score7 = self.lime_scoreboards[4][0]
        self.score8 = self.lime_scoreboards[4][1]
        self.score9 = self.lime_scoreboards[5][0]
        self.score10 = self.lime_scoreboards[5][1]
        self.score11 = self.lime_scoreboards[6][0]
        self.score12 = self.lime_scoreboards[6][1]


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
        self.winner_cell = sh.range('U40:U45')
        self.loser_cell = sh.range('W40:W45')
        self.winner_score_cell = sh.range('V40:V45')
        self.loser_score_cell = sh.range('X40:X45')
       

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
        time.sleep(60)

class maroon_league:

    def __init__(self,*args):
        self.args = args

    def maroon_update(self,*args):
        self.maroon_league = League(728302070943322112)
        self.maroon_rosters = self.maroon_league.get_rosters()
        self.maroon_users = self.maroon_league.get_users()
        self.maroon_standings = self.maroon_league.get_standings(self.maroon_rosters,self.maroon_users)
        self.maroon_matchups = self.maroon_league.get_matchups(week)
        self.maroon_lineups = self.maroon_league.get_lineups(self.maroon_rosters,self.maroon_matchups,self.maroon_users,week)
        self.maroon_scoreboards = self.maroon_league.get_scoreboards(self.maroon_rosters,self.maroon_matchups,self.maroon_users,week)

        self.score1 = self.maroon_scoreboards[1][0]
        self.score2 = self.maroon_scoreboards[1][1]
        self.score3 = self.maroon_scoreboards[2][0]
        self.score4 = self.maroon_scoreboards[2][1]
        self.score5 = self.maroon_scoreboards[3][0]
        self.score6 = self.maroon_scoreboards[3][1]
        self.score7 = self.maroon_scoreboards[4][0]
        self.score8 = self.maroon_scoreboards[4][1]
        self.score9 = self.maroon_scoreboards[5][0]
        self.score10 = self.maroon_scoreboards[5][1]
        self.score11 = self.maroon_scoreboards[6][0]
        self.score12 = self.maroon_scoreboards[6][1]

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
        self.winner_cell = sh.range('U46:U51')
        self.loser_cell = sh.range('W46:W51')
        self.winner_score_cell = sh.range('V46:V51')
        self.loser_score_cell = sh.range('X46:X51')
       

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

class navy_league:

    def __init__(self,*args):
        self.args = args

    def navy_update(self,*args):
        self.navy_league = League(728302444005695488)
        self.navy_rosters = self.navy_league.get_rosters()
        self.navy_users = self.navy_league.get_users()
        self.navy_standings = self.navy_league.get_standings(self.navy_rosters,self.navy_users)
        self.navy_matchups = self.navy_league.get_matchups(week)
        self.navy_lineups = self.navy_league.get_lineups(self.navy_rosters,self.navy_matchups,self.navy_users,week)
        self.navy_scoreboards = self.navy_league.get_scoreboards(self.navy_rosters,self.navy_matchups,self.navy_users,week)

        self.score1 = self.navy_scoreboards[1][0]
        self.score2 = self.navy_scoreboards[1][1]
        self.score3 = self.navy_scoreboards[2][0]
        self.score4 = self.navy_scoreboards[2][1]
        self.score5 = self.navy_scoreboards[3][0]
        self.score6 = self.navy_scoreboards[3][1]
        self.score7 = self.navy_scoreboards[4][0]
        self.score8 = self.navy_scoreboards[4][1]
        self.score9 = self.navy_scoreboards[5][0]
        self.score10 = self.navy_scoreboards[5][1]
        self.score11 = self.navy_scoreboards[6][0]
        self.score12 = self.navy_scoreboards[6][1]

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
        self.winner_cell = sh.range('U52:U57')
        self.loser_cell = sh.range('W52:W57')
        self.winner_score_cell = sh.range('V52:V57')
        self.loser_score_cell = sh.range('X52:X57')
       

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
        time.sleep(60)
class orange_league:

    def __init__(self,*args):
        self.args = args

    def orange_update(self,*args):
        self.orange_league = League(728302805219143680)
        self.orange_rosters = self.orange_league.get_rosters()
        self.orange_users = self.orange_league.get_users()
        self.orange_standings = self.orange_league.get_standings(self.orange_rosters,self.orange_users)
        self.orange_matchups = self.orange_league.get_matchups(week)
        self.orange_lineups = self.orange_league.get_lineups(self.orange_rosters,self.orange_matchups,self.orange_users,week)
        self.orange_scoreboards = self.orange_league.get_scoreboards(self.orange_rosters,self.orange_matchups,self.orange_users,week)

        self.score1 = self.orange_scoreboards[1][0]
        self.score2 = self.orange_scoreboards[1][1]
        self.score3 = self.orange_scoreboards[2][0]
        self.score4 = self.orange_scoreboards[2][1]
        self.score5 = self.orange_scoreboards[3][0]
        self.score6 = self.orange_scoreboards[3][1]
        self.score7 = self.orange_scoreboards[4][0]
        self.score8 = self.orange_scoreboards[4][1]
        self.score9 = self.orange_scoreboards[5][0]
        self.score10 = self.orange_scoreboards[5][1]
        self.score11 = self.orange_scoreboards[6][0]
        self.score12 = self.orange_scoreboards[6][1]

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
        self.winner_cell = sh.range('U58:U63')
        self.loser_cell = sh.range('W58:W63')
        self.winner_score_cell = sh.range('V58:V63')
        self.loser_score_cell = sh.range('X58:X63')
       

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

class purple_league:

    def __init__(self,*args):
        self.args = args

    def purple_update(self,*args):
        self.purple_league = League(728303464031076352)
        self.purple_rosters = self.purple_league.get_rosters()
        self.purple_users = self.purple_league.get_users()
        self.purple_standings = self.purple_league.get_standings(self.purple_rosters,self.purple_users)
        self.purple_matchups = self.purple_league.get_matchups(week)
        self.purple_lineups = self.purple_league.get_lineups(self.purple_rosters,self.purple_matchups,self.purple_users,week)
        self.purple_scoreboards = self.purple_league.get_scoreboards(self.purple_rosters,self.purple_matchups,self.purple_users,week)

        self.score1 = self.purple_scoreboards[1][0]
        self.score2 = self.purple_scoreboards[1][1]
        self.score3 = self.purple_scoreboards[2][0]
        self.score4 = self.purple_scoreboards[2][1]
        self.score5 = self.purple_scoreboards[3][0]
        self.score6 = self.purple_scoreboards[3][1]
        self.score7 = self.purple_scoreboards[4][0]
        self.score8 = self.purple_scoreboards[4][1]
        self.score9 = self.purple_scoreboards[5][0]
        self.score10 = self.purple_scoreboards[5][1]
        self.score11 = self.purple_scoreboards[6][0]
        self.score12 = self.purple_scoreboards[6][1]

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
        self.winner_cell = sh.range('U64:U69')
        self.loser_cell = sh.range('W64:W69')
        self.winner_score_cell = sh.range('V64:V69')
        self.loser_score_cell = sh.range('X64:X69')
       

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
        time.sleep(60)


class sky_league:

    def __init__(self,*args):
        self.args = args

    def sky_update(self,*args):
        self.sky_league = League(728304973456216064)
        self.sky_rosters = self.sky_league.get_rosters()
        self.sky_users = self.sky_league.get_users()
        self.sky_standings = self.sky_league.get_standings(self.sky_rosters,self.sky_users)
        self.sky_matchups = self.sky_league.get_matchups(week)
        self.sky_lineups = self.sky_league.get_lineups(self.sky_rosters,self.sky_matchups,self.sky_users,week)
        self.sky_scoreboards = self.sky_league.get_scoreboards(self.sky_rosters,self.sky_matchups,self.sky_users,week)

        self.score1 = self.sky_scoreboards[1][0]
        self.score2 = self.sky_scoreboards[1][1]
        self.score3 = self.sky_scoreboards[2][0]
        self.score4 = self.sky_scoreboards[2][1]
        self.score5 = self.sky_scoreboards[3][0]
        self.score6 = self.sky_scoreboards[3][1]
        self.score7 = self.sky_scoreboards[4][0]
        self.score8 = self.sky_scoreboards[4][1]
        self.score9 = self.sky_scoreboards[5][0]
        self.score10 = self.sky_scoreboards[5][1]
        self.score11 = self.sky_scoreboards[6][0]
        self.score12 = self.sky_scoreboards[6][1]

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
        self.winner_cell = sh.range('U76:U81')
        self.loser_cell = sh.range('W76:W81')
        self.winner_score_cell = sh.range('V76:V81')
        self.loser_score_cell = sh.range('X76:X81')
       

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

class teal_league:

    def __init__(self,*args):
        self.args = args

    def teal_update(self,*args):
        self.teal_league = League(728305668985085952)
        self.teal_rosters = self.teal_league.get_rosters()
        self.teal_users = self.teal_league.get_users()
        self.teal_standings = self.teal_league.get_standings(self.teal_rosters,self.teal_users)
        self.teal_matchups = self.teal_league.get_matchups(week)
        self.teal_lineups = self.teal_league.get_lineups(self.teal_rosters,self.teal_matchups,self.teal_users,week)
        self.teal_scoreboards = self.teal_league.get_scoreboards(self.teal_rosters,self.teal_matchups,self.teal_users,week)

        self.score1 = self.teal_scoreboards[1][0]
        self.score2 = self.teal_scoreboards[1][1]
        self.score3 = self.teal_scoreboards[2][0]
        self.score4 = self.teal_scoreboards[2][1]
        self.score5 = self.teal_scoreboards[3][0]
        self.score6 = self.teal_scoreboards[3][1]
        self.score7 = self.teal_scoreboards[4][0]
        self.score8 = self.teal_scoreboards[4][1]
        self.score9 = self.teal_scoreboards[5][0]
        self.score10 = self.teal_scoreboards[5][1]
        self.score11 = self.teal_scoreboards[6][0]
        self.score12 = self.teal_scoreboards[6][1]

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
        self.winner_cell = sh.range('U82:U87')
        self.loser_cell = sh.range('W82:W87')
        self.winner_score_cell = sh.range('V82:V87')
        self.loser_score_cell = sh.range('X82:X87')
       

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
        time.sleep(60)

class white_league:

    def __init__(self,*args):
        self.args = args

    def white_update(self,*args):
        self.white_league = League(728306032106962944)
        self.white_rosters = self.white_league.get_rosters()
        self.white_users = self.white_league.get_users()
        self.white_standings = self.white_league.get_standings(self.white_rosters,self.white_users)
        self.white_matchups = self.white_league.get_matchups(week)
        self.white_lineups = self.white_league.get_lineups(self.white_rosters,self.white_matchups,self.white_users,week)
        self.white_scoreboards = self.white_league.get_scoreboards(self.white_rosters,self.white_matchups,self.white_users,week)

        self.score1 = self.white_scoreboards[1][0]
        self.score2 = self.white_scoreboards[1][1]
        self.score3 = self.white_scoreboards[2][0]
        self.score4 = self.white_scoreboards[2][1]
        self.score5 = self.white_scoreboards[3][0]
        self.score6 = self.white_scoreboards[3][1]
        self.score7 = self.white_scoreboards[4][0]
        self.score8 = self.white_scoreboards[4][1]
        self.score9 = self.white_scoreboards[5][0]
        self.score10 = self.white_scoreboards[5][1]
        self.score11 = self.white_scoreboards[6][0]
        self.score12 = self.white_scoreboards[6][1]

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
        self.winner_cell = sh.range('U88:U93')
        self.loser_cell = sh.range('W88:W93')
        self.winner_score_cell = sh.range('V88:V93')
        self.loser_score_cell = sh.range('X88:X93')
       

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
        

class yellow_league:

    def __init__(self,*args):
        self.args = args

    def yellow_update(self,*args):
        self.yellow_league = League(728306466766839808)
        self.yellow_rosters = self.yellow_league.get_rosters()
        self.yellow_users = self.yellow_league.get_users()
        self.yellow_standings = self.yellow_league.get_standings(self.yellow_rosters,self.yellow_users)
        self.yellow_matchups = self.yellow_league.get_matchups(week)
        self.yellow_lineups = self.yellow_league.get_lineups(self.yellow_rosters,self.yellow_matchups,self.yellow_users,week)
        self.yellow_scoreboards = self.yellow_league.get_scoreboards(self.yellow_rosters,self.yellow_matchups,self.yellow_users,week)

        self.score1 = self.yellow_scoreboards[1][0]
        self.score2 = self.yellow_scoreboards[1][1]
        self.score3 = self.yellow_scoreboards[2][0]
        self.score4 = self.yellow_scoreboards[2][1]
        self.score5 = self.yellow_scoreboards[3][0]
        self.score6 = self.yellow_scoreboards[3][1]
        self.score7 = self.yellow_scoreboards[4][0]
        self.score8 = self.yellow_scoreboards[4][1]
        self.score9 = self.yellow_scoreboards[5][0]
        self.score10 = self.yellow_scoreboards[5][1]
        self.score11 = self.yellow_scoreboards[6][0]
        self.score12 = self.yellow_scoreboards[6][1]

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
        self.winner_cell = sh.range('U94:U99')
        self.loser_cell = sh.range('W94:W99')
        self.winner_score_cell = sh.range('V94:V99')
        self.loser_score_cell = sh.range('X94:X99')
       

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
        print("Successfully completed.")
if __name__ == "__main__":
    #red_league().red_update()
    #green_league().green_update()
    #black_league().black_update()
    #blue_league().blue_update()
    #brown_league().brown_update()
    #forest_league().forest_update()
    #gray_league().gray_update()
    #lime_league().lime_update()
    #maroon_league().maroon_update()
    #navy_league().navy_update()
    #orange_league().orange_update()
    #purple_league().purple_update()
    sky_league().sky_update()
    teal_league().teal_update()
    white_league().white_update()
    yellow_league().yellow_update()
