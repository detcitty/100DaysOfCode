# https://www.codewars.com/kata/61a8c3a9e5a7b9004a48ccc2/train/python

def direction(facing, turn):
    # your smart code here
    direction = turn % 45
    cardinal_facings = {
        'N' : 0,
        'NE' : 1,
        'E' : 2,
        'SE' : 3,
        'S' : 4,
        'SW' : 5,
        'W' : 6,
        'NW' : 7
    }
    return "S"