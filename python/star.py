# https://www.codewars.com/kata/5865a407b359c45982000036/train/python
from itertools import combinations

def slogan_maker(array):
    #your code here
    first = list(set(array[0]))
    # second = array[1]
    all_comb = list(combintations(first, len(first)))
    concat_str = list(map(lambda x: " ".join(x), all_comb))
    return(concat_str)


