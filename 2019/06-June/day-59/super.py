# https://www.codewars.com/kata/57b06f90e298a7b53d000a86/train/python
import Queue

def queue_time(customers, n):
    # TODO
    q = Queue.queue()
    for i in range(len(customers)):
        q.put(i)
queue_time([2,2,3,3,4,4], 2)
