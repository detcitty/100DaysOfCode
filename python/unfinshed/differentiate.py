# https://www.codewars.com/kata/566584e3309db1b17d000027/train/python

def differentiate(equation, point):
    '''
    What is calculus differentiation?
    '''
    values = equation.split("+")
    exponent = list(map(lambda x: x.split("x^")), values)
    final = exponent.join(' ')
    return exponent**2

