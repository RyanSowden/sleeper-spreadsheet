from app import *


def test_maroon_league():
    score1 = 10
    score2 = 20
    maroon_league.winner_score = []
    maroon_league.loser_score = []

    if score1 < score2:
        maroon_league.winner_score.append(score2)
        maroon_league.loser_score.append(score1)
    else:
        maroon_league.winner_score.append(score1)
        maroon_league.loser_score.append(score2)


    assert maroon_league.winner_score == [score2]
    assert maroon_league.loser_score == [score1]
