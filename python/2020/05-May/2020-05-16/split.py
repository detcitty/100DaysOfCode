#https://www.codewars.com/kata/5946a0a64a2c5b596500019a/train/python

import math

def split_and_add(numbers, n):
    values = list(map(lambda x: math.ceil(x/(len(numbers)/3)), numbers))
    
    where_2 = [{'list:':math.floor(i/(len(numbers)/(n+1))), 'value':x } for i,x in enumerate(numbers)]
    data = {k: [] for k in where_2.keys()}

    test_2 = map(lambda x, y: y[x['list']].append(x['value']),where_2, data)
    print(where_2)

split_and_add([1,2,3,2,23,34, 34], 2)