# https://www.codewars.com/kata/5672682212c8ecf83e000050/train/python

def dbl_linear(n):
    values = [1]
    start = 0

    while(len(values) < n):
        values.sort()
        y = 2 * values[start] + 1
        z = 3 * values[start] + 1 
        values.append(y)
        values.append(z)
        start += 1
        values.sort()
    return(values)

test = dbl_linear(20)
print(test)