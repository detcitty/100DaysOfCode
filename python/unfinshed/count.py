# https://www.codewars.com/kata/5513795bd3fafb56c200049e/train/python

def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    HELP
    """
    gen_ = map(lambda x: x.upper(), n)
    return(list(range(x, x*n+1, x)))