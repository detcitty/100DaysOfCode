# https://www.codewars.com/kata/56e3cbb5a28956899400073f/train/python

def find_subarr_maxsum(arr):
    #your code Here
    max_num = max(arr)
    max_indices = list(filter(None, [x if y == max_num else None for x, y in enumerate(arr)]))
    print(max_indices)
    final_return = []

    if max_num < 0:
        final_return = [[], 0]
    else:
        
    #return [[], x] # or [[[]], x]

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
test1 = find_subarr_maxsum(arr)