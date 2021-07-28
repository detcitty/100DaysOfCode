# https://www.codewars.com/kata/52ec24228a515e620b0005ef/train/python
import math

def exp_sum(n):
    # your code here
    perm = math.perm(n)
    comb = math.comb(n, 1)
    return(perm, comb)

test1 = exp_sum(10)

print(test1)
