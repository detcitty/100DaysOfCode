#https://www.codewars.com/kata/5946a0a64a2c5b596500019a/train/python

import math

def split_and_add(numbers, n):
    length_numbers = len(numbers)
    test = list(range(1, 10))
    values = list(map(lambda x: math.ceil(x/(len(test)/3)), test))
    print(values)

split_and_add([1,2,3], 3)