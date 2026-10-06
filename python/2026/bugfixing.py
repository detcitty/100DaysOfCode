# https://www.codewars.com/kata/55cd4ce59382498cbd000080/train/python
'''
Class conundrum - Bug Fixing #7
Oh no! Timmy's List class has broken! Can you help Timmy and fix his class? Timmy has a List class he has created, this is used for type strict arrays (which Timmy calls Lists).

When Timmy calls the count property of the list it still remains at 0 when adding items.

Also it fails when Timmy tries to chain the adds e.g.

my_list.add(0).add(1)
'''

class List:
    def __init__(self,type):
        self.type=type
        self.items=[]
        self.count=0
    
    def add(self,item):
        if type(item)!=self.type:
            item_type="str" if self.type==str else "int" if self.type==int else "float"
            return "This item is not of type: %s" %(item_type)
        self.items.append(item)
        self.count+=1
        return self