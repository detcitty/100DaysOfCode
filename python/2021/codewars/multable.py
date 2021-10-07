# https://www.codewars.com/kata/5a2fd38b55519ed98f0000ce/train/python

def multi_table(number):
    final_string = ''
    for i in range(1, 11):
        final_string += "{} * {} = {}".format(i, number, i*number) + '\n'
    return(final_string.strip())

