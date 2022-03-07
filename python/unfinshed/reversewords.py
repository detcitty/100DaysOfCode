# https://www.codewars.com/kata/5259b20d6021e9e14c0010d4/train/python

def reverse_words(text):
    #go for it
    new_str = ''
    list_text = list(text)

    while len(list_text) > 0:
        new_str += list_text.pop(-1)

    return(new_str)
