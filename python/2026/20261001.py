def gimme(input_array):
    # Implement this function
    '''
    As a part of this Kata, you need to create a function that when provided with a triplet, returns the index of the numerical element that lies between the other two elements.

The input to the function will be an array of three distinct numbers (Haskell: a tuple).

For example:

gimme([2, 3, 1]) => 0
2 is the number that fits between 1 and 3 and the index of 2 in the input array is 0.

Another example (just to make sure it is clear):

gimme([5, 10, 14]) => 1
10 is the number that fits between 5 and 14 and the index of 10 in the input array is 1.
    '''
    max_num = max(input_array)
    min_num = min(input_array)
    max_index = input_array.index(max_num)
    min_index = input_array.index(min_num)
    diff_index = max_index - min_index
    final_index = None
    if len(input_array) != 3:
        raise ValueError("Input array must contain exactly three distinct numbers.")

    if max_index == 1 and min_index == 2:
        final_index = 0
    elif max_index == 1 and min_index == 0:
        final_index = 2
    elif max_index == 0 and min_index == 1:
        final_index = 2
    elif max_index == 0 and min_index == 2:
        final_index = 1
    elif max_index == 2 and min_index == 0:
        final_index =  1
    elif max_index == 2 and min_index == 1:
        final_index =  0
        
    return final_index
