# https://www.codewars.com/kata/55f89832ac9a66518f000118/train/python
import re

def simplify(poly):
    split_regex = r"[\+\-]"
    values = re.split(split_regex, poly)
