# https://www.codewars.com/kata/5865918c6b569962950002a1/train/python
'''
All Star Code Challenge #18

Create a function that accepts 2 string arguments and returns an integer of the count of occurrences the 2nd argument is found in the first one.

If no occurrences can be found, a count of 0 should be returned.
Notes:

    The first argument can be an empty string
    The second string argument will always be of length 1

'''
def str_count(strng, letter):
    # Your code here ;)
    found_letters = list(filter(lambda x: (x == letter), list(strng)))
    return(len(found_letters))