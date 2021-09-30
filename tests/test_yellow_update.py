from app import *


def test_yellow_league():
    score1 = 10
    score2 = 20
    yellow_league.winner_score = []
    yellow_league.loser_score = []

    if score1 < score2:
        yellow_league.winner_score.append(score2)
        yellow_league.loser_score.append(score1)
    else:
        yellow_league.winner_score.append(score1)
        yellow_league.loser_score.append(score2)


    assert yellow_league.winner_score == [score2]
    assert yellow_league.loser_score == [score1]
