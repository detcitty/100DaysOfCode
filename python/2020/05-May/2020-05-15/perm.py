import itertools
# https://www.codewars.com/kata/5254ca2719453dcc0b00027d/train/python
def permutations(string):

    #your code here
    array_name = []

    for x in range(len(string)):
        number = x + 1

        values = list(itertools.permutations(string, number))
        combinded = list(map(lambda x : ''.join(x), values))
        array_name.append(combinded)
        #print(combinded)
    return(list(set(array_name[-1])))

print(permutations('ABCD'))