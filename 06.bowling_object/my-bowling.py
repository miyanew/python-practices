#! /usr/bin/env python3

import argparse
from src.bowling_game import Game


def main(roll_sequence):
    bowling_game = Game(roll_sequence)
    print(bowling_game.calc_score())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("roll_sequence", help="ボウリングの投球結果")
    args = parser.parse_args()

    main(args.roll_sequence)
