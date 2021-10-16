# https://www.codewars.com/kata/55e0467217adf9c3690000f9/train/python
import re

def my_very_own_split(string, delimiter = None):
    found = re.match(delimiter, string)
    yield found;
