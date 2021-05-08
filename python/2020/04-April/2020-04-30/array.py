# https://www.codewars.com/kata/5a2be17aee1aaefe2a000151/train/python

def addition(a, b):
    return(a + b)

def array_plus_array(arr1, arr2):
    x = list(map(addition, arr1, arr2))
    return(sum(x))