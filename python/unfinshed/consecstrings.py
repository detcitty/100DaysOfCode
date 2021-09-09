# https://www.codewars.com/kata/56a5d994ac971f1ac500003e/train/python

from itertools import combinations

def longest_consec(strarr, k):
    # your code
    combos = list(combinations(strarr, k))
    str_joined = map(lambda x: x.join(''), combos)
    str_lengeth = map(lambda x: str(x), str_joined)
    res = dict(zip(str_joined, str_lengeth))
    max_value = max(res.values())
    str_longest = ''

    for k, v in enumerate(res.items()):
        if v == max_value:
            str_longest = k
            break

    return(str_longest)
