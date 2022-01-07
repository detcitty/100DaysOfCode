# https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python
import numpy as np
import re

def get_count(sentence):
    s = re.sub(r'[^a-zA-Z0-9]', '', sentence)
    np_array = np.array(list(s))