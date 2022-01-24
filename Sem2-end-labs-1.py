# Author: IBN (AMDG) 1/24/2022
def count_sheeps(sheep):
    total = 0
    for i,v in enumerate(sheep):
        if v == True:
            total += 1
            i += 1
        else:
            i += 1
    return total

print(count_sheeps([True, True, True, False, True, False, True]) == 5)
print(count_sheeps([False, True, False, True, False, True]) == 3)
print(count_sheeps([True, True, True, False, True, False, True, True, False, False, True]) == 7)