import numpy as np

test_array = np.arange(1, 1000)

def values(x_):
    sum_ = 0
    found = []
    for item in x_: 
        if item % 3 == 0 or item % 5 == 0:
            found.append(item)
            sum_ += item
    print(found)
    return(sum_)

print(values(test_array))