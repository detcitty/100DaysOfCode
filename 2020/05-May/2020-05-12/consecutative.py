# https://www.codewars.com/kata/58f8a3a27a5c28d92e000144/train/python

def first_non_consecutive(arr):
    #your code here
    first = arr[0]
    found = None
    while len(arr) != 0:
        value = arr.pop(0)

        diff = abs(first - value)

        if (diff > 1):
            found = value
            break
        else:
            first = value

    return(found)