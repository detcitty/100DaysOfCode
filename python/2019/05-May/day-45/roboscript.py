# https://www.codewars.com/kata/58708934a44cfccca60000c4/train/python

import re

def highlight(code):
    # Implement your syntax highlighter here
    math = re.findall("F", code)
