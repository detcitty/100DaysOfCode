# https://www.codewars.com/kata/57a1fd2ce298a731b20006a4/train/python

def move(s_list):
    value = True
    for i in range(0, int(len(s_list)/2)):
        if(s_list[i] != s_list[i-i]):
            value = False
            break
    return(value)


def is_palindrome(s):
    is_pal = False
    lowercase_list = list(s.lower())
    if (len(lowercase_list) % 2 == 0):
        is_pal = move(lowercase_list)
    else:
        is_pal = move(lowercase_list)
    return(is_pal)

test1 = is_palindrome('Kasue')
print(test1)