# https://www.codewars.com/kata/57a153e872292d7c030009d4/train/python

def simple_transposition(text):
    # your code here

    size = int((len(text) / 2) + 0.5)

    if(len(text) % 2 != 0):
        text += " "

    first_row = []
    second_row = []

    for i in range(size):
        first_row.append(text[i*2])
        second_row.append(text[i*2+1])
    print(size)
    print(first_row)
    print(second_row)
    #return

simple_transposition("Simple transposition1")