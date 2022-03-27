# https://www.codewars.com/kata/5809c661f15835266900010a/train/python

## COMPLETED!

import numpy as np

def double_every_other(lst):
    values = list(map(lambda x: lst[x]*2, range(1, len(lst), 2)))

    for count, value in enumerate(range(1, len(lst), 2)):
        lst[value] = values[count]
    return(lst)

test1 = [1,19,6,2,12,-3]
print(double_every_other(test1))