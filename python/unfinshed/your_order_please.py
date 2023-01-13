# https://www.codewars.com/kata/55c45be3b2079eccff00010f/train/python

'''
Your task is to sort a given string. Each word in the string will contain a 
single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. The words in the input 
String will only contain valid consecutive numbers.

Examples
"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  ""
'''
#import numpy as np
import regex as re


def order(sentence):
    # code here

    if sentence:
        words = sentence.split(" ")
        pattern = re.compile(r'[1-9]')
        order = list(map(lambda x: pattern.search(x).group(), words))
        word_order_dict = dict(zip(order, words))

        string_final = ''
        for i in range(1, len(words) + 1):
            x_word = word_order_dict[f'{i}']
            string_final += f'{x_word} '

        return(string_final.strip())
    else:
        return("")
