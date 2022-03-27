# https://www.codewars.com/kata/5d49c93d089c6e000ff8428c/train/python

def save(sizes, hd): 
    # your code here
    total = len(sizes)
    start = 0
    end = total
    for i in range(0, total):
        for j in range(i, total-i):
            all_sum = sum(hd[start:end])
    return None