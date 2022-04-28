# https://www.codewars.com/kata/54dc6f5a224c26032800005c/train/python

def split_and_change_to_num(new_list):
    
    pass

def stock_list(listOfArt, listOfCat):
    '''
    Is this similar to the Dewey Decimal System?
    '''
    # List comprehension:
    # new_list = [expression for member in iterable]
    split_cat_nums = list(map(lambda x: x.split(" "), listOfArt))
    another_split_cat_nums = [x.split(' ') for x in listOfArt]
    return(0)