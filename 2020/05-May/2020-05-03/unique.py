# https://www.codewars.com/kata/585d7d5adb20cf33cb000235/train/python

def find_uniq(arr):
    # your code here

    items = {}
    for e in arr:
        if e not in items.keys():
            items[e] = 1
        else:
            items[e] += 1
    #key_max = max(items.keys(), key=(lambda k: items[k]))
    key_min = min(items.keys(), key=(lambda k: items[k]))

    return key_min   # n: unique integer in the array

test = find_uniq([ 1, 1, 1, 2, 1, 1 ])
print(test)