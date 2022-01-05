# https://www.codewars.com/kata/583ebb9328a0c034490001ba/train/python

def duplicate_elements(m, n):
    # Write your solution here.
    mset = set(m)
    nset = set(n)
    intersect = mset.intersection(nset)
    
    size_list = len(list(intersect))

    return(True if size_list >= 1 else False)