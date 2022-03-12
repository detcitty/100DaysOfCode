# https://www.codewars.com/kata/55c45be3b2079eccff00010f/train/python
'''
Your task is to sort a given string. Each word in the string will contain a single number. 
This number is the position the word should have in the result.
Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
If the input string is empty, return an empty string. 
The words in the input String will only contain valid consecutive numbers.
'''
import re
def order(sentence):
    # code here
    list_sentence = sentence.split(" ")
    help_ = list(map(lambda x: (re.search(r'[0-9]+', x).group(0), x), list_sentence))
    #help_.sort()
    final_str = ""
    print(help_)
    for i in sorted(help_):
        final_str += str(i)
        
    return(test1)

test1 = "4of Fo1r pe6ople g3ood th5e the2"
print(order(test1))