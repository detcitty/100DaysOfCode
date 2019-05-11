# https://www.codewars.com/kata/54eb33e5bc1a25440d000891/train/python

def decompose(n):
    # your code
    values = []
    for i in range(n):
        values.append(i**2)
    
    return values


print(decompose(30))