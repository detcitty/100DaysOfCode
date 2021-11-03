# https://www.codewars.com/kata/5541f58a944b85ce6d00006a/train/python

def fib_gen(n):
    if n == 0 or n == 1:
        yield 1
    else:
        yield fib_gen(n-1) + fib_gen(n-2)

def productFib(prod):
    # your code
    
    return 