from app import *


def test_lime_league():
    score1 = 10
    score2 = 20
    lime_league.winner_score = []
    lime_league.loser_score = []

    if score1 < score2:
        lime_league.winner_score.append(score2)
        lime_league.loser_score.append(score1)
    else:
        lime_league.winner_score.append(score1)
        lime_league.loser_score.append(score2)


    assert lime_league.winner_score == [score2]
    assert lime_league.loser_score == [score1]
