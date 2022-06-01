# https://www.codewars.com/kata/53da6d8d112bd1a0dc00008b/train/python

def reverse_list(l):
    'return a list with the reverse order of l'
    
    new_list = []
    
    for index, value in enumerate(l):
        new_list.insert(0, value)
    
    return(new_list)