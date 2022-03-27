# https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python
import numpy as np
import re

from numpy.lib import s_

def get_count(sentence):
    s = re.sub(r'[^a-zA-Z0-9]', '', lower(sentence))
    s_unique = np.unique(s, return_inverse = True)
    print(s_unique)
    np_array = np.array(list(s))