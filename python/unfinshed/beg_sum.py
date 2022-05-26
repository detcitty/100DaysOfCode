# https://www.codewars.com/kata/55f2b110f61eb01779000053/train/python

def get_sum(a,b):
    #good luck!
    min_num = min([a, b])
    max_num = max([a, b])
    return(sum(range(min_num, max_num+1, 1)))