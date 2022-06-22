# https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0/train/python

def remove_char(s):
    #your code here
    list_s = list(s)
    list_s.pop(0)
    list_s.pop(-1)
    return(''.join(list_s))

test1 = remove_char('eloquent')
print(test1)