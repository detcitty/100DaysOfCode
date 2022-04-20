# https://www.codewars.com/kata/54edbc7200b811e956000556/train/python

def count_sheeps(sheep):
    # TODO May the force be with you
    x = sum(map(lambda w: 1 if w == True else 0, sheep))
    return(x)
