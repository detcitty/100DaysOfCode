# https://www.codewars.com/kata/54da539698b8a2ad76000228/train/python

def is_valid_walk(walk):
    #determine if walk is valid
    '''
    What will the new coordinate be?
    '''
    position = [0, 0]
    # x +- 1: East and West
    # y +- 1: North and South
    walk_dict = {
        'e' : 1,
        'w' : -1,
        'n' : 1,
        's' : -1
    }
    
    return(help)