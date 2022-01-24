# Author: IBN (AMDG) 1/24/2022
def get_count(sentence):
    total = 0
    for letter in sentence:
        if letter in "aeiou":
            total += 1
    return total