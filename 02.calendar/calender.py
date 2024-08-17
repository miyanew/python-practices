import argparse
import calendar
import re
from datetime import datetime


def main(opts):
    cal = calendar.LocaleTextCalendar(
        firstweekday=calendar.SUNDAY,
        locale="ja_JP.UTF-8",
    )
    cal_str = cal.formatmonth(opts.year, opts.month)
    cal_formatted = format_weeday_line(cal_str)
    print(cal_formatted)


def format_weeday_line(calendar_str):
    weekday_pattern = r"^.*日.*月.*火.*水.*木.*金.*土.*$"
    weekday_line = re.search(weekday_pattern, calendar_str, re.MULTILINE).group()
    new_weekday_line = "日 月 火 水 木 金 土"
    return calendar_str.replace(weekday_line, new_weekday_line)


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
