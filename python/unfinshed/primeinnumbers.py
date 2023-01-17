# https://www.codewars.com/kata/54d512e62a5e54c96200019e/train/python
'''
Given a positive number n > 1 find the prime factor decomposition of n. The result will be a string with the following form :

 "(p1**n1)(p2**n2)...(pk**nk)"
with the p(i) in increasing order and n(i) empty if n(i) is 1.

Example: n = 86240 should return "(2**5)(5)(7**2)(11)"
'''

def find_next_prime(n):

    return()


def prime_factors(n):
    list_of_primes = []

    found_prime = find_next_prime(n)



def prime_factors(n):
    start = 2
    reduced_value = n:
    values = []
    repeat = True
    while(reduced_value != 1):
        if reduced_value % start == 0 and repeat == True:
            reduced_value = reduced_value / float(start)
            values.append(values)
            repeat = True
        elif repeat == False:
            if reduced_value % start == 0:
                pass
            else:
                pass
        elif repeat == True and reduced_value % start != 0:
            pass
        else:
            pass
