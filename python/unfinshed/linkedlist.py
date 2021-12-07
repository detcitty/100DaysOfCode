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

    current_node = head
    
    while current_node is not None:
        values.append(current_node)
        next_node = current_node.next
        current_node = next_node