# https://www.codewars.com/kata/51fd6bc82bc150b28e0000ce/train/python
'''
Write a small function that returns the values of an array that are not odd.

All values in the array will be integers. Return the good values in the order they are given.

'''
def no_odds(values):
    # Return list of only even values
    return(list(filter(lambda x: x % 2 == 0, values)))
