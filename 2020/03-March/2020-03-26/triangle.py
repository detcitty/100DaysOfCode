# https://www.codewars.com/kata/58e3e62f20617b6d7700120a/train/python
from itertools import combinations

class Point:
    def __init__(self, x_cord, y_cord):
        self.x = x_cord
        self.y = y_cord


class Triangle(Point):
    def __init__(self, first, second, third):
        self.a = first
        self.b = second
        self.c = third

def triangle_perimeter(triangle):
    # your solution here
    sets = list(combinations(triangle, 2))


triangle_perimeter(Triangle(Point(10, 10), Point(40, 10), Point(10, 50)))