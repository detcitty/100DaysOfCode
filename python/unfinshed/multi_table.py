# https://www.codewars.com/kata/5a2fd38b55519ed98f0000ce/train/python
'''
What does this do? 
How do I try this value?
What about multiplying and thinking of the fuctions in general?
'''
def multi_table(number):
    num_dic = {}

    for value, i in enumerate(range(number))):
        num_dic[value] = i * number
        
    return(num_dic)
