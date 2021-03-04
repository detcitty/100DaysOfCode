# https://www.codewars.com/kata/5168bb5dfe9a00b126000018/train/python

def solution(string):
    x = ''
    for i in range(len(string)):
        x += string[len(string)-i-1]
    return x
