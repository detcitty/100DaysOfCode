# https://www.codewars.com/kata/570409d3d80ec699af001bf9/train/python

def fusc(n):
    assert type(n) == int and n >= 0
    #Your code here

    if (n == 0):
        return(0)
    elif(n == 1):
        return(1)
    elif(n % 2 == 0):
        return(fusc(n))
    else:
        return(fusc(n) + fusc(n+1))