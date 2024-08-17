import argparse
from datetime import datetime


def main(options):
    print(options)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Process data for a specific year and month"
    )
    parser.add_argument(
        "year",
        type=int,
        nargs="?",
        default=datetime.now().year,
        help="Year (optional, defaults to current year)",
    )
    parser.add_argument(
        "-m",
        "--month",
        type=int,
        default=datetime.now().month,
        help="Month (1-12, optional, defaults to current month)",
    )

    args = parser.parse_args()

    main(args)
