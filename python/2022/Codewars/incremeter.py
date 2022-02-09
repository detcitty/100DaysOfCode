# https://www.codewars.com/kata/590e03aef55cab099a0002e8/train/python

def incrementer(nums):
    # your code here
    new_sum = []
    for index, value in enumerate(nums):
        digit = index+1+value
        digit_str = str(digit)
        last_digit = digit_str[-1]
        new_sum.append(int(last_digit))
    return(new_sum)