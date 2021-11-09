# https://www.codewars.com/kata/59c5f4e9d751df43cf000035/train/python
import re

def solve(s):
    '''
    How do we solve these regular expressions?
    What about coding?
    '''
    regex1 = r'a|e|i|o|u'
    return(re.match(regex1, s))