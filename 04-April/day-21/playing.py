# https://www.codewars.com/kata/55ab4f980f2d576c070000f4/train/python

def game(n):

    property = [[] for x in range(n)]

    for i in range(2, n):
        for j in range(n):
            property[i].append(i/(j+1))

    return property

print(game(8))
