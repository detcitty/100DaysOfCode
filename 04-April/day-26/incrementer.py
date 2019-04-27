# https://www.codewars.com/kata/string-incrementer/train/python
import re

def increment_string(strng):
    test = re.search('[0-9]', strng)
    return test

print(increment_string("foobar001"))
