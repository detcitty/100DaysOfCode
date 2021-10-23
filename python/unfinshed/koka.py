# https://www.codewars.com/kata/58e8cad9fd89ea0c6c000258/train/python
import re

def kooka_counter(laughing):
    #your code here
    male_regex = r'HaHaHa'
    female_regex = r'hahaha'

    males = re.findall(male_regex, laughing)
    females = re.findall(female_regex, laughing)

    size_males = len(males)
    size_females = len(females)
    #print(size_males, size_females)

    return(sum([size_females, size_males]))

test1 = kooka_counter("hahaha")
print(test1)