import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, "../src"))

from bowling_game import Game

import pytest


@pytest.mark.parametrize(
    "roll_sequence, expected_score",
    [
        ("0,1,2,3,4,5,0,1,2,3,4,5,0,1,2,3,4,5,0,1", 46),
        ("0,1,2,3,4,5,0,1,2,3,4,5,0,1,2,3,5,5,9,1,2", 67),
        ("0,1,2,3,4,5,0,1,2,3,4,5,0,1,2,3,X,X,1,0", 68),
        ("X,X,X,X,X,X,X,X,X,X,X,X", 300),
        ("6,3,9,0,0,3,8,2,7,3,X,9,1,8,0,X,6,4,5", 139),
        ("6,3,9,0,0,3,8,2,7,3,X,9,1,8,0,X,X,X,X", 164),
        ("0,10,1,5,0,0,0,0,X,X,X,5,1,8,1,0,4", 107),
        ("6,3,9,0,0,3,8,2,7,3,X,9,1,8,0,X,X,0,0", 134),
        ("6,3,9,0,0,3,8,2,7,3,X,9,1,8,0,X,X,1,8", 144),
        ("X,X,X,X,X,X,X,X,X,X,X,2", 292),
        ("X,0,0,X,0,0,X,0,0,X,0,0,X,0,0", 50),
    ],
)
def test_bowling_game(roll_sequence, expected_score):
    assert Game(roll_sequence).calc_score() == expected_score
