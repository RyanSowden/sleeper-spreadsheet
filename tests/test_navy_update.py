from app import *


def test_navy_league():
    score1 = 10
    score2 = 20
    navy_league.winner_score = []
    navy_league.loser_score = []

    if score1 < score2:
        navy_league.winner_score.append(score2)
        navy_league.loser_score.append(score1)
    else:
        navy_league.winner_score.append(score1)
        navy_league.loser_score.append(score2)


    assert navy_league.winner_score == [score2]
    assert navy_league.loser_score == [score1]
