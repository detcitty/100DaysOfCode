# https://www.codewars.com/kata/570409d3d80ec699af001bf9/train/python

def fusc(n):
    assert type(n) == int and n >= 0
    #Your code here
    '''
    help i need to pratic
    '''
    if (n == 0):
        return(0)
    elif(n == 1):
        return(1)
    elif(n % 2 == 0):
        return(fusc(n))
    else:
        return(fusc(n-1) + fusc(n))

test1 = fusc(3)