# https://www.codewars.com/kata/57ea5b0b75ae11d1e800006c/train/python

'''
Write a function that takes an array of strings as an argument and returns a sorted array containing the same strings, ordered from shortest to longest.

For example, if this array were passed as an argument:

["Telescopes", "Glasses", "Eyes", "Monocles"]

Your function would return the following array:

["Eyes", "Glasses", "Monocles", "Telescopes"]

All of the strings in the array passed to your function will be different lengths, so you will not have to decide how to order multiple strings of the same length.


'''
def sort_by_length(arr):
    #dict_order = {}
    nested_list = []
    for index, ele in enumerate(arr):
        size = len(ele)
        #dict_order[index] = size
        #nested_list.append([index, size])
        nested_list.append([size, index])
    nested_list.sort()

    final_array = list(map(lambda x: arr[x[-1]], nested_list))
    return(final_array)
