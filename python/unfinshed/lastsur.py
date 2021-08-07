# https://www.codewars.com/kata/609eee71109f860006c377d1/train/python

def last_survivor(letters, coords): 
    # your code here
    values = list(map(lambda x, y: list(x).pop(y), letters, coords))
    return(''.join(values))