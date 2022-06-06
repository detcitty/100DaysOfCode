# https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python

def is_isogram(string):
    #your code here
    letters = list(string.lower())
    letters.sort()
    not_unique = True
    
    for count, l in enumerate(letters):
        if (letters[count-1] == l):
            not_unique = False
            break
        else:
            continue
    
    return(not_unique)
    
    