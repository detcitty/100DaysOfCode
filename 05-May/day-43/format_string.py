# https://www.codewars.com/kata/53368a47e38700bd8300030d/train/python

def namelist(names):
    #your code here
    left = len(names)
    final_str = ""

    while(left > 0):
        index = len(names) - left
        dict_name = names[index]
        first_name = dict_name['name']

        if(left == 2):
            final_str += first_name + " "
        elif(left == 1):
            final_str += "& " + first_name
        else:
            final_str += ", " + first_name

        left -= 1
    return final_str


print(namelist([{'name': 'Bart'},{'name': 'Lisa'}]))
