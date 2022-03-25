# https://www.codewars.com/kata/57cff961eca260b71900008f/train/python

import re

def is_vow(inp):
    vowel_regex = re.compile('a|e|i|o|u', re.I)

    for count, vow in enumerate(inp):
        #print(vow)
        if vowel_regex.match(str(vow)):
            #print("FOUND")
            inp[count] = ord(vow)
        else:
            continue
    return(inp)

test1 = [118, "u",120,121,"u",98,122,"a",120,106,104,116,113,114,113,120,106 ]
print(is_vow(test1))