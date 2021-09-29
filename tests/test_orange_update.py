from app import *


def test_orange_league():
    score1 = 10
    score2 = 20
    orange_league.winner_score = []
    orange_league.loser_score = []

    if score1 < score2:
        orange_league.winner_score.append(score2)
        orange_league.loser_score.append(score1)
    else:
        orange_league.winner_score.append(score1)
        orange_league.loser_score.append(score2)


    assert orange_league.winner_score == [score2]
    assert orange_league.loser_score == [score1]
