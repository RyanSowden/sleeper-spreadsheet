import pytest
from app import *


def test_green_league ():
    score1 = 10
    score2 = 20
    green_league.winner_score = []
    green_league.loser_score = []

    if score1 < score2:
        green_league.winner_score.append(score2)
        green_league.loser_score.append(score1)
    else:
        green_league.winner_score.append(score1)
        green_league.loser_score.append(score2)


    assert green_league.winner_score == [score2]
    assert green_league.loser_score == [score1]
