import pytest
from app import *


def test_gray_league():
    score1 = 10
    score2 = 20
    gray_league.winner_score = []
    gray_league.loser_score = []

    if score1 < score2:
        gray_league.winner_score.append(score2)
        gray_league.loser_score.append(score1)
    else:
        gray_league.winner_score.append(score1)
        gray_league.loser_score.append(score2)


    assert gray_league.winner_score == [score2]
    assert gray_league.loser_score == [score1]
