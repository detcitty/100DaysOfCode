# https://www.codewars.com/kata/525a566985a9a47bc8000670/train/python
from statistics import median
import math

def rotate(matrix, direction): 
    # your code here
    coorindates = []

    size = len(matrix)
    halfway = median(range(len(matrix)))
    ## case for even-even rows
    for x in range(len(matrix)):
        row_ = []
        for y in range(len(matrix)):
            x_coord = float(x-halfway)
            y_coord = float(y-halfway)
            sign_x = math.copysign(1, y_coord)
            sign_y = math.copysign(1, y_coord)

            if (x_coord.is_integer() and y_coord.is_integer()):
                row_.append([x_coord, y_coord])
                #print('PART!')
            else:
                x_ciel_abs = math.ceil(abs(x_coord))
                y_ciel_abs = math.ceil(abs(y_coord))
                row_.append([sign_x * (x_ciel_abs), sign_y * (y_ciel_abs)])
        coorindates.append(row_)
    print(coorindates)

    if (direction == 'left'):
        for i in range(len(matrix)):
            first_ = coorindates[i]
            x_changed = map(lambda x: [-1*x[0], x[1]], first_)
