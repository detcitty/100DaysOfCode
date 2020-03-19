# https://www.codewars.com/kata/585d7d5adb20cf33cb000235/train/python

def find_uniq(arr):
    # your code here
    unique = list(set(arr))

    first = unique[0]
    second = unique[1]
    #print(first, second)
    count = [0,0]

    value = 0
    for e in arr:
        #print(e)
        if(e == first):
            count[0] += 1
        elif(e == second):
            count[1] += 1

    value = unique[count.index(max(count))]
            


    return value   # n: unique integer in the array

print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))
print(find_uniq([ 0, 0, 0.55, 0, 0 ]))