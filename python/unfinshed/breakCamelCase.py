# https://www.codewars.com/kata/5208f99aee097e6552000148/train/python

def solution(s):
    array_letters = list(s)
    
    index = 0
    found_end = False
    while not found_end:
        if array_letters[index].isupper():
            array_letters.insert(index, " ")
            index += 2
        elif index == len(array_letters):
            found_end = True
        else:
            index += 1
            
    return ''.join(array_letters)

test1 = solution("helloWorld")