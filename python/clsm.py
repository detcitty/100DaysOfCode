# https://www.codewars.com/kata/5868b2de442e3fb2bb000119/train/python

def closest(string):
    # your code
    values = string.split(" ")
    values.sort()
    combo = list(map(lambda x, y: [x, y], values, values))
    clean_val = list(map(lambda x: x.strip(), combo))