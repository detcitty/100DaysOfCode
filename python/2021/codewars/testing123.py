# https://www.codewars.com/kata/54bf85e3d5b56c7a05000cf9/train/python

def number(lines):
    #your code here
    return( list(map(lambda x, y: "{}: {}".format(x, y), range(1, len(lines)+1), lines)))

test1 = number(["a", "b", "c"])
print(test1)