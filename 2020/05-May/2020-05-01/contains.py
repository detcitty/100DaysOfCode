# https://www.codewars.com/kata/5e4eb72bb95d28002dbbecde/train/python

import re

def regex_contains_all(st): 
    # your code here
    char = list(st)
    between = list(map(lambda x: f"(?=.*{x})", char))
    final = "".join(between)
    return final

print(regex_contains_all("sst"))