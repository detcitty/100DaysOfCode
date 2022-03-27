# https://www.codewars.com/kata/537529f42993de0e0b00181f/train/python
from itertools import combinations

def count_inversions(array):
    locations = []
    for count, value in enumerate(array):
        idx = value - 1
        diff = idx - count
        locations.append(diff)

    list_combos = list(combinations(array, 2))
    
    # Find the adjacent 
    # Try to sort the list and count the number of times it was sorted
    for i in range(len(list_combos)):
        pass

    return(list_combos)


test1 = [1, 2, 3, 4]  # =>  0 inversions
test2 = [1, 3, 2, 4]  # =>  1 inversion: 2 and 3
test3 = [4, 1, 2, 3]  # =>  3 inversions: 4 and 1, 4 and 2, 4 and 3
test4 = [4, 3, 2, 1]  # =>  6 inversions: 4 and 3, 4 and 2, 4 and 1, 3 and 2, 3 and 1, 2 and 1
test5 = [5, 4, 3, 2, 1]  # =>  6 inversions: 4 and 3, 4 and 2, 4 and 1, 3 and 2, 3 and 1, 2 and 1

print(count_inversions(test1))