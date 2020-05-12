# https://www.codewars.com/kata/5635e7cb49adc7b54500001c/train/python

import math

def solve(n):

    amounts = [10, 20, 50, 100, 200, 500]
    if (n % 5 != 0):
        return -1
    else:
        test = list(map(lambda x: math.floor(n/x), amounts))
        print(test)
        return(sum(test))

print(solve(770))