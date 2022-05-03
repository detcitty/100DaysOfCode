# https://www.codewars.com/kata/54ff0d1f355cfd20e60001fc/train/python

def factorial(n):
    try:
        some_code_that_may_raise_our_value_error()

    except ValueError as err:
        print(err.args)
