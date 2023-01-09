# https://www.codewars.com/kata/52efefcbcdf57161d4000091/train/python
'''
The main idea is to count all the occurring characters in a string. If you
have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object 
literal, {}.
'''
from collections import defaultdict


def count(string):
    # The function code should be here
    #all_chars = string.split("")
    if len(string) != 0:
        all_chars = list(string)

        unique_chars = set(all_chars)
        intial_dict = dict.fromkeys(unique_chars, 0)
        counts_char = defaultdict(lambda: 0, intial_dict)

        for x in all_chars:
            key = x
            value = counts_char[x]

            counts_char[key] = value + 1

        return(counts_char)

    else:
        return({})
