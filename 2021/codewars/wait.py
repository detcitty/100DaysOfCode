# https://www.codewars.com/kata/5875b200d520904a04000003/train/python

def enough(cap, on, wait):
    left_over = on - cap

    diff = left_over - wait

    return(0 if diff > 0 else abs(diff))
