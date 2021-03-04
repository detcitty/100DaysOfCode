# https://www.codewars.com/kata/51c8991dee245d7ddf00000e/train/python

def reverse_words(s):
    words = s.split(" ")
    print(words)
    flipped_s = ""
    for i in range(len(words)):
        print(i)
        index_opp = len(words) - i - 1
        print(index_opp)
        flipped_s += words[index_opp] + " "
    return flipped_s

print(reverse_words("Devin is a cunt!"))