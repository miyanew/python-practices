import os
import sys
import unittest

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, "../src"))

from bowling_game import Game


class TestBowlingGame(unittest.TestCase):
    def test_no_bonus(self):
        roll_sequence = "0,1,2,3,4,5,0,1,2,3,4,5,0,1,2,3,4,5,0,1"
        self.assertEqual(46, Game(roll_sequence).calc_score())

    def test_spare_bonus(self):
        roll_sequence = "0,1,2,3,4,5,0,1,2,3,4,5,0,1,2,3,5,5,9,1,2"
        self.assertEqual(67, Game(roll_sequence).calc_score())

    def test_strike_bonus(self):
        roll_sequence = "0,1,2,3,4,5,0,1,2,3,4,5,0,1,2,3,X,X,1,0"
        self.assertEqual(68, Game(roll_sequence).calc_score())

    def test_all_strikes(self):
        roll_sequence = "X,X,X,X,X,X,X,X,X,X,X,X"
        self.assertEqual(300, Game(roll_sequence).calc_score())

    def test_last_frame_is_spare(self):
        roll_sequence = "6,3,9,0,0,3,8,2,7,3,X,9,1,8,0,X,6,4,5"
        self.assertEqual(139, Game(roll_sequence).calc_score())

    def test_last_frame_is_perfect(self):
        roll_sequence = "6,3,9,0,0,3,8,2,7,3,X,9,1,8,0,X,X,X,X"
        self.assertEqual(164, Game(roll_sequence).calc_score())

    def test_last_frame_took_2pitches(self):
        roll_sequence = "0,10,1,5,0,0,0,0,X,X,X,5,1,8,1,0,4"
        self.assertEqual(107, Game(roll_sequence).calc_score())

    def test_last_frame_is_scoreless_after_strikes(self):
        roll_sequence = "6,3,9,0,0,3,8,2,7,3,X,9,1,8,0,X,X,0,0"
        self.assertEqual(134, Game(roll_sequence).calc_score())

    def test_last_frame_is_bonusless_scored_after_strike(self):
        roll_sequence = "6,3,9,0,0,3,8,2,7,3,X,9,1,8,0,X,X,1,8"
        self.assertEqual(144, Game(roll_sequence).calc_score())

    def test_all_strikes_except_the_last(self):
        roll_sequence = "X,X,X,X,X,X,X,X,X,X,X,2"
        self.assertEqual(292, Game(roll_sequence).calc_score())

    def test_strike_but_no_bonus(self):
        roll_sequence = "X,0,0,X,0,0,X,0,0,X,0,0,X,0,0"
        self.assertEqual(50, Game(roll_sequence).calc_score())


if __name__ == "__main__":
    unittest.main()
