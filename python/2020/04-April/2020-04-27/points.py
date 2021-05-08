# https://www.codewars.com/kata/5bb904724c47249b10000131/train/python

def points(games):
    split = lambda x: x.split(":")
    values = list(map(split, games))
    return(values)

test = ['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']

print(points(test))