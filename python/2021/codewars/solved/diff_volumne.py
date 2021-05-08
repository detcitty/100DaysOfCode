# https://www.codewars.com/kata/58cb43f4256836ed95000f97/train/python

def find_difference(a, b):
    # Your code here!
    total_a = 1
    total_b = 1
    for i in range(3):
        total_a *= a[i]
        total_b *= b[i]

    return(abs(total_a - total_b))
