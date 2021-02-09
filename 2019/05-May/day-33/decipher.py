# https://www.codewars.com/kata/581e014b55f2c52bb00000f8/train/python

import re

def decipher_this(string):
    #your code here
    words = string.split(" ")
    for w in words:
        first = re.match('\d+', w).group(0)
        second = re.search('\D+', w)
        second.groups()
        print(first, "This is work", second)

    return words

print(decipher_this("65 119esi 111dl 111lw 108dvei 105n 97n 111ka"))
