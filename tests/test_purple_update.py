from app import *


def test_purple_league():
    score1 = 10
    score2 = 20
    purple_league.winner_score = []
    purple_league.loser_score = []

    if score1 < score2:
        purple_league.winner_score.append(score2)
        purple_league.loser_score.append(score1)
    else:
        purple_league.winner_score.append(score1)
        purple_league.loser_score.append(score2)


    assert purple_league.winner_score == [score2]
    assert purple_league.loser_score == [score1]
