# https://www.codewars.com/kata/563f879ecbb8fcab31000041/train/python
'''
Write a function, factory, that takes a number as its parameter and returns another function.

The returned function should take an array of numbers as its parameter, and return an array of those numbers multiplied by the number that was passed into the first function.

In the example below, 5 is the number passed into the first function. So it returns a function that takes an array and multiplies all elements in it by five.

Translations and comments (and upvotes) welcome!

Example
'''

def factory(x):
    
    values = [item * factor for item in x]
    return values