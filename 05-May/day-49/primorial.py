# https://www.codewars.com/kata/5a99a03e4a6b34bb3c000124/train/python
from itertools import permutations 

def prime_num(n):
    values = []
    for i in range(1,n): 
        if (n % i != 0):
            values.append(i)

    return values

def num_primorial(n):
    #your code here

    prime = prime_num(n)
    perm = permutations(prime)
    for i in perm:
        print(i)

num_primorial(9)