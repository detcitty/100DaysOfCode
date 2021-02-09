# https://www.codewars.com/kata/56cac350145912e68b0006f0/train/python

def arrange(strng):
    # your code

    string_list = strng.split(' ')

    size = lambda x : len(x)

    sizes = list(map( size, string_list))
    current = ""
    past = ""

    for num, size in enumerate(sizes, start=1):
        print(num, size)
        current = size
        past = size if past == "" else past 

        if num % 2 == 1:
            past if past <= current else current
        else:
            current if past <= current else past

        past = size
            

    return(sizes)

print(arrange("who hit retaining The That a we taken"))
arrange("on I came up were so grandmothers")
arrange("way the my wall them him")
arrange("turn know great-aunts aunt look A to back")