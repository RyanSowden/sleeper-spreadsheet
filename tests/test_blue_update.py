import pytest
from app import *


def test_blue_league():
    score1 = 10
    score2 = 20
    blue_league.winner_score = []
    blue_league.loser_score = []

    if score1 < score2:
        blue_league.winner_score.append(score2)
        blue_league.loser_score.append(score1)
    else:
        blue_league.winner_score.append(score1)
        blue_league.loser_score.append(score2)


    assert blue_league.winner_score == [score2]
    assert blue_league.loser_score == [score1]
