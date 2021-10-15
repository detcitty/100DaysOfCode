# https://www.codewars.com/kata/5ab6538b379d20ad880000ab/train/python

def area_or_perimeter(l , w):
    # return your answer
    final_value = 0
    if (l == w):
        final_value = l*w
    else:
        final_value = 2*(l+w)
    return(final_value)
