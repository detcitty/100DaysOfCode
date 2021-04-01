# https://www.codewars.com/kata/5a057ec846d843c81a0000ad/train/python

def cycle(n):
    values = []
    for i in range(n):
        decimals = 1/float(n+1)
        values.append(decimals)

val = cycle(3)
print(val)
