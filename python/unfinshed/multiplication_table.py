# https://www.codewars.com/kata/534d2f5b5371ecf8d2000a08/train/python
'''
Your task, is to create NxN multiplication table, of size provided in parameter.

for example, when given size is 3:

1 2 3
2 4 6
3 6 9
for given example, the return value should be: [[1,2,3],[2,4,6],[3,6,9]]


'''
def multiplication_table(size):
    indices = [x for x in range(1, size+1)]
    return(list(map(lambda x: x * indices, indices)))
    #return # good luck