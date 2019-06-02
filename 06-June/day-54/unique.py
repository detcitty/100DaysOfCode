# https://www.codewars.com/kata/585d7d5adb20cf33cb000235/train/python

def find_uniq(arr):
    # your code here
    unique = list(set(arr))

    first = unique[0]
    second = unique[1]
    #print(first, second)
    count_first = 0
    count_second = 0

    value = 0
    for e in arr:
        print(e)
        if(e == first):
            count_first += 1
        elif(e == second):
            count_second += 1

    
    if(count_first > 2):
        value = first
    elif(count_second > 2):
        value = second
            


    return value   # n: unique integer in the array

print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))
print(find_uniq([ 0, 0, 0.55, 0, 0 ]))