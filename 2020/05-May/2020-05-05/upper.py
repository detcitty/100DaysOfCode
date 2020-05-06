# https://www.codewars.com/kata/56cd44e1aa4ac7879200010b/train/python

def isUpper(maybe):
    values = list(maybe)

    is_true = map(lambda x: x.isupper(), values)
    return (all(is_true))


def is_uppercase(inp):
    splits = inp.split(" ")
    values = map(isUpper, splits)

    return (all(values))

print(isUpper("MAYBE"))