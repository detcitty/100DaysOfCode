# https://www.codewars.com/kata/53cf7e37e9876c35a60002c9/train/python
"""
Also view this website: https://betterprogramming.pub/functional-programming-currying-vs-partial-application-53b8b05c73e3
It shows good examples: curry vs partial application
All of this is related to functional programming
"""

def curry_partial(f,*initial_args):
    "Curries and partially applies the initial arguments to the function"
    return_func = lambda x, y: x + y

    for arg in initial_args:
        recursive_func = lambda x, y: x + y

        return_func = return_func(f(arg), recursive_func)
    return(return_func)