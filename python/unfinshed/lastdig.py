# https://www.codewars.com/kata/5cd5ba1ce4471a00256930c0/train/python

def solution(n,d):
    digits = list(map(lambda x: int(n), list(str(n))))
    return(digits[:d])