# https://www.codewars.com/kata/639dd2efd424cc0016e7a611/train/python

'''
Description
You will need to write a function that takes sum as an argument, and returns a list. 
In this list there should be one or more nested lists; in each of them - three natural numbers, 
so that the sum of this three numbers equals sum, and the product of this numbers is ending with 
us much zeroes as possible. You will need to find all solutions. The sum will be from 1 to 500, 
so you can use bruteforce. Feel free to create programm that can work not only for 3, but for any 
amount of numbers! Note that you will need to output only unique sets of numbers in ascending order.

Examples
zero_count(407) = [[32, 125, 250]] # 32, 125 and 250 is the only three numbers with sum of 407, 
that after multiplication have 6 zeroes. Other numbers have less
zero_count(199) = [[10, 64, 125], [24, 25, 150], [24, 50, 125], [24, 75, 100], [34, 40, 125]] 
# there is 5 possible solutions
zero_count(3) = [[0, 0, 3], [0, 1, 2]] # 2 solutions, each of them give 1 trailing zero

'''


def zero_count(sum):

    # How would I write this function?

    equal_thirds = sum / 3.0

    # if even, all 3 numbers need to be even?
    # ending in 1-9:
    # 1, 1, 1
    # 3, 3, 3
    # 5, 5, 5
    # 7, 7, 7
    # 9, 9, 9
    #values = []
    odd_values = []
    for i in range(1, 10, 2):
        for j in range(1, 10, 2):
            for k in range(1, 10, 2):
                test_sum = i + j + k
                odd_values.append(test_sum)

    even_values = []
    for i in range(2, 10, 2):
        for j in range(2, 10, 2):
            for k in range(2, 10, 2):
                test_sum = i + j + k
                even_values.append(test_sum)

    odd_odd_even_values = []
    for i in range(1, 10, 2):
        for j in range(1, 10, 2):
            for k in range(2, 10, 2):
                test_sum = i + j + k
                odd_odd_even_values.append(test_sum)
    
    odd_even_even_values = []
    for i in range(1, 10, 2):
        for j in range(2, 10, 2):
            for k in range(2, 10, 2):
                test_sum = i + j + k
                odd_even_even_values.append(test_sum)
    return(set(odd_odd_even_values))


    # pass # write your code here
print(zero_count(1))
