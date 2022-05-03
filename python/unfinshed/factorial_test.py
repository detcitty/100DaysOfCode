# https://www.codewars.com/kata/54ff0d1f355cfd20e60001fc/train/python

def factorial(n):
    try:
        fac = 1
        for i in range(n):
            fac *= i
    except ValueError as err:
        print(err.args)
    
    return(fac)
