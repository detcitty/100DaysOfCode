# https://www.codewars.com/kata/55aa075506463dac6600010d/train/python

def list_squared(m, n):
    # your code
    return list(map(lambda x: x*2, [m, n]))

test1 = list_squared(1, 250)
print(test1)