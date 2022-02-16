# https://www.codewars.com/kata/55b7bb74a0256d4467000070/train/python
import math
def proper_fractions(n):
    #your code here
    # What does this even do again?
    value = str(n)
    numerator, denominator = value.split('/')
    num = math.gcd(numerator, denominator)

