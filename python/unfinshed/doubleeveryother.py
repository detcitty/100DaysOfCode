# https://www.codewars.com/kata/5809c661f15835266900010a/train/python
import numpy as np

def double_every_other(lst):
    values = list(map(lambda x, y: x[y]*2 , lst, range(1, len(lst), 2)))

test1 = [1,19,6,2,12,-3]
print(double_every_other(test1))