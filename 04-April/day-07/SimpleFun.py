# https://www.codewars.com/kata/58b8c94b7df3f116eb00005b/train/python

def reverse_letter(string):
    #do your magic here
    text = ""
    list_name = range(len(string))
    len_str = len(string)
    for i in list_name:
        # print(i)
        text += string[len_str - (i + 1)]

    final = ''.join(filter(str.isalpha, text))
    return(final)

print(reverse_letter("krishan"))
