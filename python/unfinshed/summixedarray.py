# https://www.codewars.com/kata/57eaeb9578748ff92a000009/train/python

def sum_mix(arr):
    #your code here
    # turn all values into numbers
    numbers = list(map(lambda x: int(x) if x == type(str) else x, arr))
    return(sum(numbers))

test1 = sum_mix(['3', 6, 6, 0, '5', 8, 5, '6', 2,'0'])
print(test1)