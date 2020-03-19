# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/train/python

def persistence(n):
    # your code

    new_num = n
    count = 0

    while(len(str(new_num)) > 1):

        multiply = 1
        for i in str(new_num):
            #print(i)
            multiply = multiply * int(i)

        new_num = multiply
        count += 1
    return count

print(persistence(999))
