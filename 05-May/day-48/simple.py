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

    text1 = ""
    text2 = ""

    for i in range(size):
        text1 += first_row[i]
        text2 += second_row[i]

    final_text = text1 + text2
    return final_text.strip()

simple_transposition("Simple transposition1")