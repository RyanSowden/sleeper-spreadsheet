import pytest
from app import *


def test_red_update():
    score1 = 10
    score2 = 20
    red_league.winner_score = []
    red_league.loser_score = []

    if score1 < score2:
        red_league.winner_score.append(score2)
        red_league.loser_score.append(score1)
    else:
        red_league.winner_score.append(score1)
        red_league.loser_score.append(score2)


    red_league.winner_score = {score2} 
    assert red_league.winner_score == {score2}
