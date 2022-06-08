# https://www.codewars.com/kata/5769b3802ae6f8e4890009d2/train/python

def remove_every_other(my_list):
    # Your code here!
    new_list = []

    for i, e in enumerate(my_list):
        new_list.append(e if i % 2 == 0 else "")
    new_list = [i for i in new_list if i]

    return(new_list)