import pytest
from app import *


def test_black_league ():
    score1 = 10
    score2 = 20
    black_league.winner_score = []
    black_league.loser_score = []

    if score1 < score2:
        black_league.winner_score.append(score2)
        black_league.loser_score.append(score1)
    else:
        black_league.winner_score.append(score1)
        black_league.loser_score.append(score2)


    assert black_league.winner_score == [score2]    
    assert black_league.loser_score == [score1]
