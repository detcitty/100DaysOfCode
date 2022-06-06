# https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python

def is_isogram(string):
    #your code here
    letters = list(string.lower())
    letters.remove
    not_unique = True
    
    for count, l in enumerate(letters):
        if (letters[count-1]):
            not_unique = False
            break
        else:
            continue
        
    return(True if len(string) == 0 else not_unique)
    
    