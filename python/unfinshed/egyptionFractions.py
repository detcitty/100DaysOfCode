# https://www.codewars.com/kata/54f8693ea58bce689100065f/train/python
from sympy.ntheory import factorint

def decompose(n):
    # your 
    numer, denom = n.split("/")
    numer_int = int(numer)
    denom_int = int(denom)
    top_primeFactors = factorint(numer_int, multiple=True)
    bottom_primeFactors = factorint(denom_int, multiple=True)
    return [top_primeFactors, bottom_primeFactors]

test1 = decompose("21/23")
print(test1)