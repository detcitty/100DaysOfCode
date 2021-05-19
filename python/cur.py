# https://www.codewars.com/kata/53cf7e37e9876c35a60002c9/train/python

def curry_partial(f,*initial_args):
  "Curries and partially applies the initial arguments to the function"

  test = map(lambda x: x.sum(), initial_args)