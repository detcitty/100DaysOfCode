# https://www.codewars.com/kata/57faece99610ced690000165/train/python
'''
Description:

Remove all exclamation marks from the end of sentence.
Examples

remove("Hi!") === "Hi"
remove("Hi!!!") === "Hi"
remove("!Hi") === "!Hi"
remove("!Hi!") === "!Hi"
remove("Hi! Hi!") === "Hi! Hi"
remove("Hi") === "Hi"


'''
import regex as re

def remove(s):
    return(re.sub('\!+$', '', s))
    