# https://www.codewars.com/kata/59c287b16bddd291c700009a/train/python
import math

def ice_brick_volume(radius, bottle_length, rim_length):
    cube_height = bottle_length- rim_length
    cube_side = radius * math.sqrt(2)
    return(radius**2.0 * 2 * cube_height)