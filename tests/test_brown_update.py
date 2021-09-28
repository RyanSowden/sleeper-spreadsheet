import pytest
from app import *


def test_brown_league():
    score1 = 10
    score2 = 20
    brown_league.winner_score = []
    brown_league.loser_score = []

    if score1 < score2:
        brown_league.winner_score.append(score2)
        brown_league.loser_score.append(score1)
    else:
        brown_league.winner_score.append(score1)
        brown_league.loser_score.append(score2)


    assert brown_league.winner_score == [score2]
    assert brown_league.loser_score == [score1]
