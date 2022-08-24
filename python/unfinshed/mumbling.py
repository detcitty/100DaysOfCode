# https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python

'''
This time no story, no theory. The examples below show you how to write function accum:
Examples:

accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"

The parameter of accum is a string which includes only letters from a..z and A..Z.

'''
# What does this do?
def accum(s):
    # your code
    letters = list(s)
    test1 = map(lambda x, y: x.lower() * y, letters, range(1, len(letters) + 1))
    test2 = map(lambda x: x[0])
    return("-".join(test1))
    