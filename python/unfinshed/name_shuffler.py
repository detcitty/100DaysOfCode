# https://www.codewars.com/kata/559ac78160f0be07c200005a/train/python

def name_shuffler(str_):
    #your code here
    first_name, last_name = str_.split(" ")
    return(last_name + " " + first_name)