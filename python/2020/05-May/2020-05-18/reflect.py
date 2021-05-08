# https://www.codewars.com/kata/5eaf88f92b679f001423cc66/train/python

def reflections(max_x, max_y):
    slopes = [1/2, -1/2]
    intercepts = [0, 0]
    get_past = map(lambda x: slopes*x + intercepts, [max_x, max_y])
    