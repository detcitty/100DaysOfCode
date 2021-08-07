# https://www.codewars.com/kata/58817056e7a31c2ceb000052/train/python

def interpreter(tape):
    # Your code here
    file_map = {}

    for x in list(tape):
        if x not in file_map.keys():
            pass
        else:
            file_map[x] += 1
            
    return(file_map)