# https://www.codewars.com/kata/54eb33e5bc1a25440d000891/train/python
import queue

def decompose(n):
    # your code
    values = queue.Queue()
    for i in range(n):
        values.put(i**2)
    
    return values

    last = values.get()

    diff = 1
    while diff > 0:
        output = values.get()
        stage_diff = last - output
        


print(decompose(30))