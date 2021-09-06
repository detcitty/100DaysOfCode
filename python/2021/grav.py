# https://www.codewars.com/kata/5f70c883e10f9e0001c89673/train/python

def flip(d, a):
    '''
    Aligning squares to either left or right wall,
    in descending or ascending order.
    '''
    # Do some magic
    sort_left = True if d == "L" else False
    a.sort(reverse=sort_left)
    return(a)
