# https://www.codewars.com/kata/554e52e7232cdd05650000a0/train/python
from collections import deque

def consecutive(value):
    ls = [int(s) for s in value]
    output = True

    for i in range(len(value)-1):
        if (ls[i+1] != ls[i]+1 ):
            output = False
    return output

def lowest_product(input):
    ls = [int(s) for s in input]
    deq = deque(ls)
    values = deque()
    sums = []
    min = 0
    while (len(deq) is not 0):
        if (len(values) != 4):
            values.append(deq.popleft())
        else:
            sum = 0
            str_sum = ""
            for i in values:
                sum += i
                str_sum += str(i)
            print(consecutive(str_sum))
            sums.append(sum)
            print(str_sum, sum)
            values.popleft()
            values.append(deq.popleft())


#lowest_product("123456789")
lowest_product("2345611117899")
