# https://www.codewars.com/kata/57fafd0ed80daac48800019f/train/python
import re

def remove(s):
    ex = re.compile('\!')
    str_found = re.findall(ex, s)
    flat_list = [item for sublist in str_found for item in sublist]
    no_ex = re.sub(ex, '', s)
    return(no_ex + ''.join(flat_list))