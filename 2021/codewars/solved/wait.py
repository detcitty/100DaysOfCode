# https://www.codewars.com/kata/5875b200d520904a04000003/train/python

def enough(cap, on, wait):
    left_over = cap - on

    diff = wait - left_over

    return(0 if diff < 0 else abs(diff))
