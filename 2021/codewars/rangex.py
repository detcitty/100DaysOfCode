# https://www.codewars.com/kata/51ba717bb08c1cd60f00002f/train/python

def solution(args):

    # i = 0
    # end_i = len(args)
    new_array = []

    for i in range(len(args)-1):
        print(i)
        if (args[i]+1 == args[i+1]):
            continue
        else:
            new_array.append(args[i])
    return(new_array)

values = solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
print(values)
