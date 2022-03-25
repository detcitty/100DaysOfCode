# https://www.codewars.com/kata/5629db57620258aa9d000014/train/python
import re

def mix(s1, s2):
    # your code
    repl_regex = r'[^a-z]'
    all_string = map(lambda x: re.sub(repl_regex, ' ', x), [s1, s2])
    return(list(all_string))

test1 = mix("Are they here", "yes, they are here")
print(test1)