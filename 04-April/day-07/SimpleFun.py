def reverse_letter(string):
    #do your magic here
    text = ""
    list_name = range(len(string))
    len_str = len(string)
    for i in list_name:
        print(i)
        text += string[len_str - (i + 1)]

    return(text)

print(reverse_letter("krishan"))
