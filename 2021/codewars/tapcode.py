# https://www.codewars.com/kata/605f5d33f38ca800322cb18f/train/python

def tap_code_translation(text):
    split = text.split(r'\s')
    for i in split:
        print(i)

test = "Devin is practicing"

tap_code_translation(test)
