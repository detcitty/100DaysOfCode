# https://www.codewars.com/kata/57ee31c5e77282c24d000024/train/python

def paul(x):
    # your code here
    dict_values = { 'kata' : 5, 
    'Petes kata' : 10,
    'life': 0,
    'eating' : 1 }

    scores = 0

    for i in x:
        scores += (dict_values[i])

    if scores < 40:
        return("Super happy!")
    elif scores < 70 and scores >= 40:
        return("Happy!")
    elif scores < 100 and scores >= 70:
        return("Sad!")
    else:
        return("Miserable!")
    