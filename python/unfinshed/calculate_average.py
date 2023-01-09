# https://www.codewars.com/kata/57a2013acf1fa5bfc4000921/train/python
'''
Write a function which calculates the average of the numbers in a given list.

Note: Empty arrays should return 0.
'''

def find_average(numbers):
    # your code here
    return(sum(numbers)/len(numbers) if len(numbers) != 0 else 0)