# https://www.codewars.com/kata/57cc981a58da9e302a000214/train/python

def small_enough(array, limit):
    compare = list(map(lambda x: x <= limit, array))
    print(compare)
    is_small = max(all(compare))
    print(is_small)
    return(is_small)

values = small_enough([1,2,3,5,6,7,10], 6)
print(values)
