from app import *


def test_teal_league():
    score1 = 10
    score2 = 20
    teal_league.winner_score = []
    teal_league.loser_score = []

    if score1 < score2:
        teal_league.winner_score.append(score2)
        teal_league.loser_score.append(score1)
    else:
        teal_league.winner_score.append(score1)
        teal_league.loser_score.append(score2)


    assert teal_league.winner_score == [score2]
    assert teal_league.loser_score == [score1]
