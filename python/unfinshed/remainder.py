# https://www.codewars.com/kata/524f5125ad9c12894e00003f

def remainder(a,b):
    #your code here
    return(max(a, b)%min(b, a) if min(b,a) != 0 else None)