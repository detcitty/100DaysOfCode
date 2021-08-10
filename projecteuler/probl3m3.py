'''
What is this code going to do?
I am trying to figure out how prime numbers work.
'''
def start(number):

    half_way = number / 2.0
    map(lambda x, y: x(y), half_way, prime)
