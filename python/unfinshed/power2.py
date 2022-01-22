# https://www.codewars.com/kata/57a083a57cb1f31db7000028/train/python

'''
I don't know what this does but I need to do it.
Maybe do more practicing on Leetcode
'''

def powers_of_two(n):
    return list(map(lambda x: x^2, list(range(n))))

print(powers_of_two(5))
