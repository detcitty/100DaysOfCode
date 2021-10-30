# https://www.codewars.com/kata/5cd5ba1ce4471a00256930c0/train/python

def solution(n,d):
    #print(list(str(n)))
    digits = list(map(lambda x: int(x), list(str(n))))
    return(digits[-d+1:])

test1 = solution(123,4)
print(test1)