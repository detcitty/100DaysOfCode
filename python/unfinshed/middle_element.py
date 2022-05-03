# https://www.codewars.com/kata/545a4c5a61aa4c6916000755/train/python

def gimme(input_array):
    # Implement this function
    max_i, min_i = max(input_array), min(input_array)

    for i in range(len(input_array)):
        