# https://www.codewars.com/kata/56f1c6034d0c330e4a001059/train/python

import random
def generate_color_rgb():
    #here is the code go
    #Go go go go
    rgb = list(map(lambda x: random.randint(0, x), [256] * 3))
    return rgb

print(generate_color_rgb())
