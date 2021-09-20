# https://www.codewars.com/kata/570e8ec4127ad143660001fd/train/python

def billboard(name, price=30):
    letters = list(name)
    return(sum(list(map(lambda x: price, name))))