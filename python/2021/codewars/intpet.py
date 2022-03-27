#!/usr/bin/python
# -*- coding: utf-8 -*-

# https://www.codewars.com/kata/55cf3b567fc0e02b0b00000b/train/python
from itertools import combinations

def part(n):
    # write your code here
    test = combinations(range(1,n+1), n)
    yield test
    return(test)

test1 = part(3)
print(test1)