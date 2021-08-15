'''
What is this code going to do?
I am trying to figure out how prime numbers work.
'''

import numpy as np

def start(number):
    half_way = (number + 1) / 2.0
    list_values = np.arange(half_way, dtype='i2')
    odds = list_values[(list_values % 2 == 1) | (list_values == 2)]
    odds_sans_fives = odds[(odds % 5 != 0) | (odds == 5)]
    return(odds_sans_fives)
    #map(lambda x, y: x(y), half_way, prime)

test1 = start(1000)
print(test1)