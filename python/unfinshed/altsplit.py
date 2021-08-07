# https://www.codewars.com/kata/55dd5386575839a74f0000a9/train/python

class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    # Your code goes here.
    # Remember to return the context.
    for head is Node:
        try:
            head.first
        except:
            print("Unexpected error:")
