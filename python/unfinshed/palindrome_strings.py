# https://www.codewars.com/kata/57a5015d72292ddeb8000b31/train/python
'''
Palindrome strings

A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward or forward. This includes capital letters, punctuation, and word dividers.

Implement a function that checks if something is a palindrome. If the input is a number, convert it to string first.
Examples(Input ==> Output)

"anna"   ==> true
"walter" ==> false
12321    ==> true
123456   ==> false


'''
import math
from re import I

def is_palindrome(string):
    new_string = string if isinstance(string, str) else str(string)
    is_even = True if len(new_string) % 2 == 0 else False
    middle_value = math.floor(len(new_string) / 2)
    found_palindrome = True
    new_string_list = list(new_string)
    
    for i in range(0, middle_value):
        first_index = i 
        last_index = len(new_string) - i
        if (new_string[first_index] == new_string[last_index]):
            continue
        else:
            found_palindrome = False
            break
    
    return(found_palindrome)