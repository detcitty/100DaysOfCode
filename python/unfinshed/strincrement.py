# https://www.codewars.com/kata/54a91a4883a7de5d7800009c/train/python

import re

def increment_string(strng):
    final_value = ''
    match_bool = re.search(r'\d+', strng)
    if match_bool:
        str_index = match_bool.span()
        #print(str_index)
        num = int(match_bool.group()) + 1
        num_str = str(num)
        num_lead = num_str.zfill(len(match_bool.group())-len(num_str))

        final_value = strng[:str_index[0]] + num_lead

    else:
        final_value = strng + '1'
    return(final_value)

test1 = increment_string('foo0003')
print(test1)