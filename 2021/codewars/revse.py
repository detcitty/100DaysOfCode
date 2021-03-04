# https://www.codewars.com/kata/51c8991dee245d7ddf00000e/train/python

def reverse_words(s):
    words = s.split(" ")
    flipped_s = ""
    for i in range(len(s)):
        flipped_s += words[len(s)-i-1]
    return flipped_s