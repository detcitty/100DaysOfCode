# https://www.codewars.com/kata/57a1fd2ce298a731b20006a4/train/python

def move(s_list):
    value = True
    for i in range(0, len(s_list)/2):
        if(s_list[i] != s_list[i-i]):
            value = False
            break
    return(value)


def is_palindrome(s):
    is_pal = False
    lowercase = s.lower()
    if (s % 2 == 0):
        is_pal = move(list(lowercase))
    else:
        is_pal = move(list(lowercase)) 
    return(is_pal)