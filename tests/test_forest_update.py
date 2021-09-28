import pytest
from app import *


def test_forest_league():
    score1 = 10
    score2 = 20
    forest_league.winner_score = []
    forest_league.loser_score = []

    if score1 < score2:
        forest_league.winner_score.append(score2)
        forest_league.loser_score.append(score1)
    else:
        forest_league.winner_score.append(score1)
        forest_league.loser_score.append(score2)


    assert forest_league.winner_score == [score2]
    assert forest_league.loser_score == [score1]
