# https://www.codewars.com/kata/561e9c843a2ef5a40c0000a4/train/python

def gap(g, m, n):
    found_remainders = []
    for i in range(g+1):
        if g % i != 0:
            found_remainders.append(i)
    return(found_remainders)
