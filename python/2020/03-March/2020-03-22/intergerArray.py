# https://www.codewars.com/kata/52a112d9488f506ae7000b95/train/python

import re

def is_int_array(arr):
    # your code here
    end_value = None
    if not arr:
        end_value = True
    else:
        for e in arr:

            regex_exp = "(\.)(\d*$)"
            test = re.search(regex_exp, str(e))
            if(type(e) is not float or type(e) is not int or test.groups()[] is None):
                end_value = False
                break
        end_value = True
    return(end_value)

is_int_array([1,2,3])