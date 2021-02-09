import unittest

def divisors(n):
    divisiors = []

    for i in range(1, min(n , 500000)):
        remainder = n % i

        if(remainder == 0):
            divisiors.append(remainder)

    return(len(divisiors)+1)

print(divisors(3))
