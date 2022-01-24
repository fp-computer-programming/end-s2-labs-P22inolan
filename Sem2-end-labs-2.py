# Author: IBN (AMDG) 1/24/2022
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(even_or_odd(5) == "Odd")
print(even_or_odd(12412) == "Even")
print(even_or_odd(7) == "Odd")