# https://www.codewars.com/kata/58856a06760b85c4e6000055/train/python

def bits_battle(numbers):
    num_range = [2**x for x in range(0, max(numbers)/2)]

    for num in numbers:
        total = 0
        for i in num_range:
            if total < num:
                total += 1

test1([5, 3, 14])