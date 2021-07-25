# https://www.codewars.com/kata/5629db57620258aa9d000014/train/python
import re
def mix(s1, s2):
    # your code
    char_regex = r"[^a-z]"
    list_str = list(map(lambda x, y: re.split(x, y), [s1, s2], char_regex))
