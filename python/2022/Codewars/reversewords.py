# https://www.codewars.com/kata/5259b20d6021e9e14c0010d4/train/python

def reverse_words(text):
    #go for it
    new_str = ''
    words = text.split(" ")

    for w in words:
            
        list_text = list(w)

        while len(list_text) > 0:
            new_str += list_text.pop(-1)
        
        new_str += " "

    return(new_str.strip())
