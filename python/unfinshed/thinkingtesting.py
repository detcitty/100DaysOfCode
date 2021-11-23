# https://www.codewars.com/kata/56d904db9963e9cf5000037d/train/python

def testit (a, b):
    # Good Luck
    sum_ = a + b
    prod_ = a * b
    diff_ = abs(b - a)
    if diff_ in [1,10]:
        return(sum_)
    else:
        return(prod_)
    return ("{} {}".format(a, b), sum_, prod_, diff_) # Hmm is that right?