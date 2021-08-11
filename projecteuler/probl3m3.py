'''
What is this code going to do?
I am trying to figure out how prime numbers work.
'''

import numpy as np

def start(number):
    half_way = number / 2.0
    list_values = np.arange(half_way)
    map(lambda x, y: x(y), half_way, prime)
