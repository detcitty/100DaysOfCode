# https://www.codewars.com/kata/5541f58a944b85ce6d00006a/train/python
'''
What is going to go on?
'''

def productFib(prod):
    factors = []
    for i in range(1, prod + 1):
        if prod % i == 0:
            factors.append(i)
    return(factors)
