# https://www.codewars.com/kata/string-incrementer/train/python
import re

def increment_string(strng):
    re.search('.*[0-9])', strng)
    return strng

print(increment_string("foobar001"))
