# https://www.codewars.com/kata/54d4c8b08776e4ad92000835/train/python

def isPP(n):
    #your code here
    found = []
    for i in range(n):
        for j in range(n):
            if j**i == n:
                found.append([i,j])
    
    return(found[0] if len(found) != 0 else None)