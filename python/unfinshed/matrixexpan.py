# https://www.codewars.com/kata/614adaedbfd3cf00076d47de/train/python

def expansion(matrix, n):
    test1 = matrix
    for i in range(len(matrix)):
        for j in range(n):
            test1[i].append(sum(test1[:i]))
    return test1