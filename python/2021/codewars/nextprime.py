# https://www.codewars.com/kata/58e230e5e24dde0996000070/train/python
import functools
'''
What was the name of the website to test math problems.

Project Euler
'''

def next_prime(n):
    # have fun ^.^
    potential_prime = n+1
    found_prime = False
    while (found_prime == False):
        all_indices = []
        for i in range(1, potential_prime+1):
            if n % i == 0:
                all_indices.append(i)
        if functools.reduce(lambda x, y : x and y, map(lambda p, q: p == q, all_indices,[1, potential_prime]), True):
            found_prime = True
        else:
            found_prime = False
            potential_prime += 1
    return(potential_prime)

test1 = next_prime(14)
print(test1)