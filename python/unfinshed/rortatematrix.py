# https://www.codewars.com/kata/525a566985a9a47bc8000670/train/python
from statistics import median

def rotate(matrix, direction): 
    # your code here
    coorindates = []

    size = len(matrix)
    halfway = median(range(len(matrix)))
    ## case for even-even rows
    for x in range(len(matrix)):
        for y in range(len(matrix)):
            coorindates.append([x-halfway, y-halfway])
    print(coorindates)
