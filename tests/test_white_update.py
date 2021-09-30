from app import *


def test_white_league():
    score1 = 10
    score2 = 20
    white_league.winner_score = []
    white_league.loser_score = []

    if score1 < score2:
        white_league.winner_score.append(score2)
        white_league.loser_score.append(score1)
    else:
        white_league.winner_score.append(score1)
        white_league.loser_score.append(score2)


    assert white_league.winner_score == [score2]
    assert white_league.loser_score == [score1]
