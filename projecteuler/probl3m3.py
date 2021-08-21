'''
What is this code going to do?
I am trying to figure out how prime numbers work.

Directions: 
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

import numpy as np

def start(number):
    half_way = (number + 1) / 2.0
    list_values = np.arange(half_way, dtype='i2')
    odds = list_values[(list_values % 2 == 1) | (list_values == 2)]
    odds_sans_threes = odds[(odds % 3 != 0) | (odds == 3)] 
    odds_sans_fives = odds_sans_threes[(odds_sans_threes % 5 != 0) | (odds_sans_threes == 5)]
    count_files = len(odds_sans_fives)
    return(count_files)

    #map(lambda x, y: x(y), half_way, prime)

test1 = start(600851475143)
print(test1)
