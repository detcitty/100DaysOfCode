# https://www.codewars.com/kata/566fc12495810954b1000030/train/python
'''
Take an integer n (n >= 0) and a digit d (0 <= d <= 9) as an integer.

Square all numbers k (0 <= k <= n) between 0 and n.

Count the numbers of digits d used in the writing of all the k**2.

Call nb_dig (or nbDig or ...) the function taking n and d as parameters and returning this count.
'''
import numpy as np


def nb_dig(n, d):
    # your code
    values = np.arange(0, n+1)
    k_squared = np.square(values)
    #print(k_squared)
    # I just need to check if there is at least one digit d in the k**2 list
    # How do I convert an array to string
    str_k = np.char.mod('%d', k_squared)
    #(str_k)
    #str_k = np.array(map(str, k_squared))
    count_d = np.char.count(str_k, str(d))
    #print(count_d)
    return(np.sum(count_d))


# Something is not working right.
# How can I do an apply on all of the numbers?
test1 = nb_dig(5750, 0)
test2 = nb_dig(10, 0)

print(test2)