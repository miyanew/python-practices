#! /usr/bin/env python3

import argparse
import src.bowling_game as bowling_game


def main(all_roll_result):
    game = bowling_game.Game()
    print(game.score(all_roll_result))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("all_roll_result",help="ボウリングの投球結果")
    args = parser.parse_args()

    main(args.all_roll_result)
