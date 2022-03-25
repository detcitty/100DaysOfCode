# https://www.codewars.com/kata/54d4c8b08776e4ad92000835/train/python
'''
Returns a list of prime numbers up to the first one
'''
def find_prime_numbers(first_number):
    find_prime_numbers = [2]
    start = 3
    while (start < first_number / 2):
        values = list(map(lambda x, y: x % y, start, find_prime_numbers))
        if 0 in values:
            continue
        else:
            start += 1

def isPP(n):
    #your code here
    return()