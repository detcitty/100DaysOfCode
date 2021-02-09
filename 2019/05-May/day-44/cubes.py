# https://www.codewars.com/kata/5592e3bd57b64d00f3000047/train/python

def find_nb(m):
    # your code

    index = 1
    sum = 0

    while (sum < m):
        cube = index**3
        sum += cube
        index += 1

    value = 0
    if(sum == m):
        value = index - 1
    else:
        value = -1
    return value
