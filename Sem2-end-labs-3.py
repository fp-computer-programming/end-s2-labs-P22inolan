# Author: IBN (AMDG) 1/24/2022
import math


def make_negative(number):
    if number >= 1:
        neg = number * -1
        return neg
    elif number <= -1:
        return number
    else:
        return number

print(make_negative(15) == -15)
print(make_negative(-15) == -15)
print(make_negative(0) == 0)