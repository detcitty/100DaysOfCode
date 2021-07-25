# https://www.codewars.com/kata/5629db57620258aa9d000014/train/python
import re
def mix(s1, s2):
    # your code
    char_regex = re.compile(r"[^a-z]")
    list_str = list(map(lambda x, y: re.split(x, y), [s1, s2], char_regex))
    return(list_str)

test1 = mix("Are they here", "yes, they are here")
print(test1)
