# https://www.codewars.com/kata/51e056fe544cf36c410000fb/train/python
import re

def top_3_words(text):
    lowercase = text.lower()
    cleaned = re.sub(r'[^A-Za-z\r\n]', '', lowercase)
    cleaned_now = re.sub(r'[\r\n]', " ", cleaned)
    all_words = cleaned_now.split(" ")
    return(all_words)


