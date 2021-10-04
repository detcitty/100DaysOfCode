# https://www.codewars.com/kata/5ef0456fcd067000321baffa/train/python

def connotation(strng):
    #have fun!
    names_list = strng.split(" ")
    first_values = list(map(lambda x: ord(x.lower()[0])- 97, names_list))
    split_values = first_values >= 13
    return(split_values)

test1 = 'Help me have fun'
print(connotation(test1))