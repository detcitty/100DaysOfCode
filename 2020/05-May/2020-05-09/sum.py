# https://www.codewars.com/kata/55fd2d567d94ac3bc9000064/train/python

def row_sum_odd_numbers(n):
    #your code here)
    triangle = []
    values = []
    for x in range(1, n+1):
        triangle.append(x)
        print(x)
    total = sum(triangle*2)
    #print(total)
    odd_numbers = list(range(1, total, 2))
    #print(odd_numbers)
    for i, elem in enumerate(triangle):
        test = []
        for x in range(0, i+1):
            test.append(odd_numbers.pop(0))
        values.append(test)
    #print(values[n-1])
    return(sum(values[n-1]))


row_sum_odd_numbers(5)