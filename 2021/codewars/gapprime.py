# https://www.codewars.com/kata/561e9c843a2ef5a40c0000a4/train/python

def gap(g, m, n):
    is_prime = []
    # I don't know how to find prime numbers efficently
    for i in range(1, n):
        if n % 2 == 0:
            is_prime.append(i)
    return(is_prime)

print(gap(1, 3, 14))
