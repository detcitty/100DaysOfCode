# https://www.codewars.com/kata/57a1fd2ce298a731b20006a4/train/python

def move(s_list, end):
    value = True
    #print(end)
    for i in range(0, end):
        #print(i)
        if(s_list[i] == s_list[i-i]):
            continue
        else:
            value = False
            #print('here')
            break
    return(value)


def is_palindrome(s):
    is_pal = False
    lowercase_list = list(s.lower())
    #print(lowercase_list)
    if (len(lowercase_list) % 2 == 0):
        is_pal = move(lowercase_list, int(len(lowercase_list)/2)-1)
    else:
        is_pal = move(lowercase_list, int(len(lowercase_list)/2)+1)
        #print(is_pal)
    return(is_pal)

test1 = is_palindrome('Kasue')
print(test1)