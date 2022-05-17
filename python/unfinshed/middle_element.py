# https://www.codewars.com/kata/545a4c5a61aa4c6916000755/train/python

def gimme(input_array):
    # Implement this function
    max_value, min_value = max(input_array), min(input_array)
    max_index = 0
    min_index = 0

    for i in range(len(input_array)):
        if input_array[i] == max_value:
            max_index = i
        
        if input_array[i] == min_value:
            min_index = i

    return()