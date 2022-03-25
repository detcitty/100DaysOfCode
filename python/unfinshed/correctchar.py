# https://www.codewars.com/kata/577bd026df78c19bca0002c0/train/python

def correct(s):
    dict_correct = {
        '5' : 'S',
        '0' : 'O',
        '1' : 'I'
    }

    for word, initial in dict_correct.items():
        s = s.replace(word, initial)
    return(s)
