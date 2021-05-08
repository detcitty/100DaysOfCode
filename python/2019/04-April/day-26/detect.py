# https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python
import string

def is_pangram(s):
    charcters = s.split(' ')
    names = set(s.lower())
    found = []
    for i in names:
        if (i.isalpha()):
            found.append(i)

    #print(charcters)
    return (len(found) == 26)


pangram = "The quick, brown fox jumps over the lazy dog!"
print(is_pangram(pangram))
