# https://www.codewars.com/kata/5c4cb8fc3cf185147a5bdd02/train/python
import numpy as np

def sum_or_product(array, n):
    a = np.array(array)
    a_sorted = np.argsort(a)
    potential_prod = a[a_sorted][:n]
    potenial_sum = a[a_sorted][-n:]

    prod = np.prod(potential_prod)
    sums = np.sum(potenial_sum)

    value = ''
    if prod > sums:
        value = 'product'
    elif prod < sums:
        value = 'sum'
    else:
        value = 'same'

    return(value)
