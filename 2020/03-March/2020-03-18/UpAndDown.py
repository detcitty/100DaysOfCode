# https://www.codewars.com/kata/56cac350145912e68b0006f0/train/python

def arrange(strng):
    # your code

    string_list = strng.split(' ')
    
    size = lambda x : len(x)

    sizes = list(map( size, string_list))
    return(sizes)

print(arrange("who hit retaining The That a we taken"))
arrange("on I came up were so grandmothers")
arrange("way the my wall them him")
arrange("turn know great-aunts aunt look A to back")