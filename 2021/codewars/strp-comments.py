# https://www.codewars.com/kata/51c8e37cee245da6b40000bd/train/python
import re

def solution(string,markers):
    #your code here
    remove_regex = r'[\#\!](.*)([\n$])'
    final = re.sub(remove_regex, "\2", string, flags=re.M)
    return(final)

te = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
print(te)