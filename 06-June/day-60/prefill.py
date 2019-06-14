# https://www.codewars.com/kata/54129112fb7c188740000162/train/python

def prefill(n, v):
    #your code here

    value = map(v, v*range(n))
    return value

print(prefill(3,1))
