# Author: IBN (AMDG) 1/24/2022
from webbrowser import get


def get_count(sentence):
    total = 0
    for letter in sentence:
        if letter in "aeiou":
            total += 1
    return total

print(get_count("banana") == 3)
print(get_count("ouija") == 4)
print(get_count("quarter") == 3)