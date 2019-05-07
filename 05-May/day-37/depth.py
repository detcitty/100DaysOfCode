# https://www.codewars.com/kata/59b401e24f98a813f9000026/train/python

def compute_depth(n):
    values = []

    for i in range(1,10):
        multiple = i * n
        values.append(multiple)
    return values
print(compute_depth(42))
