# https://www.codewars.com/kata/57cfdf34902f6ba3d300001e/train/python

'''
You will be given a list of strings. You must sort it alphabetically (case-sensitive, and based on the ASCII values of the chars) and then return the first value.

The returned value must be a string, and have "***" between each of its letters.

You should not remove or add elements from/to the array.


'''
def two_sort(array):
    # your code here
    sorted_array = sorted(array)
    first_string_list = list(sorted_array.pop(0))
    values = [f"{item}***" for item in first_string_list]
    return "***".join(first_string_list)