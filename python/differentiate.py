# https://www.codewars.com/kata/566584e3309db1b17d000027/train/python

def differentiate(equation, point):
    values = equation.split("+")
    exponent = list(map(lambda x: x.split("x^")), values)
    return exponent
