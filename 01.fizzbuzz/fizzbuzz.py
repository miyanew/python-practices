#!/usr/bin/env python3


def fizz_buzz(number):
    """
    FizzBuzz問題の解を返す関数
    3の倍数の場合は'Fizz'、5の倍数の場合は'Buzz'、
    3と5の両方の倍数の場合は'FizzBuzz'を返す。
    それ以外の場合は数字をそのまま文字列として返す。
    """
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 5 == 0:
        return "Buzz"
    elif number % 3 == 0:
        return "Fizz"
    else:
        return str(i)


start = 1
max_count = 20

for i in range(start, start + max_count):
    print(fizz_buzz(i))
