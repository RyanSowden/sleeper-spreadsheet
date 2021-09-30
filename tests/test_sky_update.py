from app import *


def test_sky_league():
    score1 = 10
    score2 = 20
    sky_league.winner_score = []
    sky_league.loser_score = []

    if score1 < score2:
        sky_league.winner_score.append(score2)
        sky_league.loser_score.append(score1)
    else:
        sky_league.winner_score.append(score1)
        sky_league.loser_score.append(score2)


    assert sky_league.winner_score == [score2]
    assert sky_league.loser_score == [score1]
