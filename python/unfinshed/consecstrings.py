# https://www.codewars.com/kata/56a5d994ac971f1ac500003e/train/javascript

from itertools import combinations

def longest_consec(strarr, k):
    # your code
    combos = list(combinations(strarr, k))
    str_joined = map(lambda x: x.join(''), combos)