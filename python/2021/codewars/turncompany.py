# https://www.codewars.com/kata/61a8c3a9e5a7b9004a48ccc2/train/python

def method1(dict, search_direction):
    for name, age in dict.items():
        if age == search_direction:
            return name

def direction(facing, turn):
    # your smart code here
    direction = turn % 45 
    cardinal_facings = {
        'N' : 1,
        'NE' : 2,
        'E' : 3,
        'SE' : 4,
        'S' : 5,
        'SW' : 6,
        'W' : 7,
        'NW' : 8
    }
    current_facing = cardinal_facings[facing]
    new_facing = (current_facing + (direction % 8 )) 
    new_direction = method1(cardinal_facings, new_facing)
    return(new_direction)