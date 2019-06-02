# https://www.codewars.com/kata/5389864ec72ce03383000484/train/python

import re

def autocomplete(input_, dictionary):
    #your code here
    found = []
    for e in dictionary:
        z = re.match(input_+ ".+", e, re.IGNORECASE)

        if z:
            found.append(z.group())

    print(found)

    if (len(found)> 5):
        return found[:5]
    else:
        return found

dictionary=[ 'abnormal',
  'arm-wrestling',
  'absolute',
  'airplane',
  'airport',
  'amazing',
  'apple',
  'ball' ]

autocomplete('ai', dictionary), ['airplane','airport']
autocomplete('a', dictionary), ['abnormal','arm-wrestling','absolute','airplane','airport']