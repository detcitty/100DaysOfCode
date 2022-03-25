# https://www.codewars.com/kata/5648b12ce68d9daa6b000099/train/python

def number(bus_stops):
    # Good Luck!
    return(sum(list(map(lambda x: x[0]-x[1], bus_stops))))

test1 = number([[10,0],[3,5],[5,8]])
print(test1)