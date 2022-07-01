# https://www.codewars.com/kata/576b93db1129fcf2200001e6/train/python
'''
Task

Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element ( by value, not by index! ).

The highest or lowest element respectively is a single element at each edge, even if there are more than one with the same value.

Mind the input validation.
'''
def sum_array(arr):
    #your code here
    if arr is None or len(arr) <= 1:
        return 0
    else:
        return(sum(arr) - min(arr) - max(arr))
    