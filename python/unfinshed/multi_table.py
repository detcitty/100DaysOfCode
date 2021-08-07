# https://www.codewars.com/kata/5a2fd38b55519ed98f0000ce/train/python

def multi_table(number):
    num_dic = {}

    for value, i in enumerate(range(number))):
        num_dic[value] = i * number
        
    return(num_dic)
