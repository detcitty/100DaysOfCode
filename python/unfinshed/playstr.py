# https://www.codewars.com/kata/56c30ad8585d9ab99b000c54/train/python

def work_on_strings(a, b):
    '''
    How does this work and what do we do for this issues? 
    '''
    a_list = list(a)
    b_list = list(b)

    return list(map(lambda x, y: x == y, a_list, b_list))
