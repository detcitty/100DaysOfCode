# https://www.codewars.com/kata/56efc695740d30f963000557/train/python

def to_alternating_case(string):
    #your code here
    all_letters = list(string)
    values = list(map(lambda x: x.isupper(), all_letters))

    letters_key_pair = zip(all_letters, values)