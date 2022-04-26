# https://www.codewars.com/kata/5208f99aee097e6552000148/train/python

def solution(s):
    array_letters = list(s)
    i = 0

    found_end = False
    while not found_end:
        letter = array_letters[i]
        if letter.isupper():
            array_letters.insert(i, " ")
            i += 2
        elif i == len(array_letters)-1:
            found_end = True
        else:
            i += 1
            
    return ''.join(array_letters)

test1 = solution("helloWorld")
print(test1)