# https://www.codewars.com/kata/51e056fe544cf36c410000fb/train/python
import re

def top_3_words(text):
    lowercase = text.lower()
    cleaned = re.sub(r'[^A-Za-z\r\n\s]', '', lowercase)
    cleaned_now = re.sub(r'[\r\n]', " ", cleaned)
    all_words = cleaned_now.split(" ")
    return(all_words)

test_ = """In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income."""

print(top_3_words(test_))
