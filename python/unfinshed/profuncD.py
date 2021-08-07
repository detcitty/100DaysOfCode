# https://www.codewars.com/kata/55b7bb74a0256d4467000070/train/python
import math
def proper_fractions(n):
    #your code here
    value = str(n)
    numerator, denominator = value.split('/')
    num = math.gcd(numerator, denominator)

