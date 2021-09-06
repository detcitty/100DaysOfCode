# https://www.codewars.com/kata/5f70c883e10f9e0001c89673/train/python

def flip(d, a):
    '''
    What does this even do?
    '''
    # Do some magic
    sort_left = True if d == "L" else False
    a.sort(reverse=sort_left)
    return(a)
