# https://www.codewars.com/kata/525a566985a9a47bc8000670/train/python

def rotate(matrix, direction): 
    # your code here
    coodinates = []
    for x in range(len(matrix)):
        for y in range(len(matrix)):
            coodinates.append((x,y))

    ## case for even-even rows


    ## case for odd-odd rows