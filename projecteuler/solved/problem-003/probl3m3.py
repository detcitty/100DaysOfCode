'''
What is this code going to do?
I am trying to figure out how prime numbers work.

Directions: 
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

I think I can solve this problem if I understand what prime numbers are
'''

import numpy as np
import math

# https://stackoverflow.com/questions/36095518/get-prime-numbers-from-numpy-array/36095942

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def factorize_number(num):
    half_sqrt = math.sqrt(num)
    test_num = num
    diversor = 2
    found_numbers = []
    while (test_num > 1 ):
        if (test_num % diversor == 0):
            found_numbers.append(diversor)
            test_num = test_num  / diversor
        if(test_num % diversor != 0):
            diversor += 1
    print(found_numbers)
    print(np.prod(found_numbers))
    return(found_numbers[-1])

test2 = factorize_number(600851475143)
print(test2)

def start(number):    
    '''
    The code fails when making large computations. 
    I need to figure out a way how to not use an array.

    What about finding all of the prime numbers and checking to see if it's a multiple of X.
    '''
    half_way = (number + 1) / 2.0
    list_values = np.arange(half_way, dtype='i2')
    odds = list_values[(list_values % 2 == 1) | (list_values == 2)]
    odds_sans_threes = odds[(odds % 3 != 0) | (odds == 3)] 
    odds_sans_fives = odds_sans_threes[(odds_sans_threes % 5 != 0) | (odds_sans_threes == 5)]
    count_files = len(odds_sans_fives)
    return(count_files[-1])

    #map(lambda x, y: x(y), half_way, prime)

#test1 = start(600851475143)
#print(test1)
