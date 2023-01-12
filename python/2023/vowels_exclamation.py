# https://www.codewars.com/kata/57fb09ef2b5314a8a90001ed/train/python
'''
Description:
Replace all vowel to exclamation mark in the sentence. aeiouAEIOU is vowel.

Examples
replace("Hi!") === "H!!"
replace("!Hi! Hi!") === "!H!! H!!"
replace("aeiou") === "!!!!!"
replace("ABCDE") === "!BCD!"
'''
import regex as re

def replace_exclamation(s):
    pattern = re.compile(r'[aeiou]', re.IGNORECASE)
    return(re.sub(pattern, '!', s))
