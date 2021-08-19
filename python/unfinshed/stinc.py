# https://www.codewars.com/kata/54a91a4883a7de5d7800009c/train/python
import re

def increment_string(strng):
    re_text = '([^\d]*)(\d+)?'
    # How do we use regex? What about lookahead and lookbehinds?
    return strng.match(re_text)

