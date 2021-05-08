# https://www.codewars.com/kata/diophantine-equation/train/python

def sol_equa(n):
    # your code
    values = []
    for i in range(n):

        x1 = n - 2*i
        x2 = n + 2*i

        total = x2 * x1
        print(x1, x2, total)
        if(x1 == x2):
            values.append((x1, i))
    return values

print(sol_equa(12))
