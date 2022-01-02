# https://www.codewars.com/kata/5656b6906de340bd1b0000ac/train/python

def longest(a1, a2):
    # your code
    a1_l = list(set(list(a1)))
    a2_l = list(set(list(a2)))

    a1_l.sort(reverse=False)
    a2_l.sort(reverse=False)
    #print(a2_l)

    list3 = list(set(a1_l + a2_l))
    list3.sort(reverse=False)
    return(''.join(list3))

test1 = longest("aretheyhere", "yestheyarehere")
print(test1)