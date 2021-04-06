# https://www.codewars.com/kata/57ebdf1c2d45a0ecd7002cd5/train/python

def inside_out(st):
    values = list(st)
    end = ''
    while len(values) != 0:
        end += values.pop(-1)

    return(end)

test = "Devin"
print(inside_out(test))
