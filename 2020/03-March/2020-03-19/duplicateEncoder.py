# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python

def duplicate_encode(word):
    #your code here

    unique = ''
    value = ""
    for ch in word:
        if (ch in unique):
            value += "("
        else:
            unique += ch
            value += ")"
    return(value)

print(duplicate_encode("Success"))