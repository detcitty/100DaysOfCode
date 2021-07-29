# https://www.codewars.com/kata/55aa075506463dac6600010d/train/python

def list_squared(m, n):
    # your code
    squared = list(map(lambda x: x*2, range(m, n+1)))
    filter(lambda x, y: x == y,squared)

test1 = list_squared(1, 250)
print(test1)