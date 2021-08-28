# https://www.codewars.com/kata/5865a407b359c45982000036/train/python
from itertools import combinations

'''
What about having good code and commits?

'''
def slogan_maker(array):
    #your code here
    first = list(set(array[0]))
    # second = array[1]
    all_comb = list(combinations(first, len(first)))
    concat_str = list(map(lambda x: " ".join(x), all_comb))
    together = '\r\n'.join(concat_str)
    return(together)


