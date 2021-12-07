# https://github.com/detcitty/100DaysOfCode/tree/master/python/2021/codewars

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
    values = []
    first_list = []
    second_list = []

    current_node = head
    
    while current_node is not None:
        values.append(current_node)
        next_node = current_node.next
        current_node = next_node
    
    for i, e in enumerate(values):
        if i % 2:
            second_list.append(e)
        else:
            first_list.append(e)
    
    for i in range(len(first_list)-1):
        first_list[i].next = first_list[i+1]
    
    for i in range(len(second_list)-1):
        second_list[i].next = second_list[i+1]

    first_list[-1].next = None
    second_list[-1].next = None

    return(Context(first_list[0], second_list[0]))

