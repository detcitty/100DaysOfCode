# https://www.codewars.com/kata/530e15517bc88ac656000716/train/python

def rot13(message):
    values = list(map(lambda x: chr(ord(x) + 13) + (chr(x) + 93) % 13, list(message)))
    values
    return(values)