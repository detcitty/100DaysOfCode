# https://www.codewars.com/kata/554f76dca89983cc400000bb/train/python

def sol_equa(n):
    # your code
    items = range(0, n)
    array_all = []
    for i in items:
        for j in items:
            left = i - 2*j
            right = i + 2*j
            total = left * right

            if(total == n):
                array_all.append([i,j])
            else:
                pass
    return array_all

print(sol_equa(5))