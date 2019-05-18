# https://www.codewars.com/kata/554e52e7232cdd05650000a0/train/python
from collections import deque

def lowest_product(input):
    ls = [int(s) for s in input]
    deq = deque(ls)
    values = deque()

    while (len(deq) is not 0):
        if (len(values) != 4):
            values.append(deq.popleft())
        else:
            sum = 0
            for i in values:
                sum += i
            print(sum)


lowest_product("123456789")
