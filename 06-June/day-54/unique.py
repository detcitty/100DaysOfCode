# https://www.codewars.com/kata/585d7d5adb20cf33cb000235/train/python

def find_uniq(arr):
    # your code here
    unique = list(set(arr))

    first = unique[0]
    second = unique[1]

    count_first = 0
    count_second = 0

    value = 0
    for e in unique:
        if(e == first):
            count_first += 1
        elif(e == second):
            count_second += 1

        elif(count_first > 1):
            value = first
            break
        elif(count_second > 1):
            value = second
            break


    return value   # n: unique integer in the array

print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))