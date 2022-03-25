# https://www.codewars.com/kata/580878d5d27b84b64c000b51/train/python

def sum_triangular_numbers(n):
    #your code here
    list(map(lambda x: sum(x), n, range(len(n))))
    return sum_