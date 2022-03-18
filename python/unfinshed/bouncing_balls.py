# https://www.codewars.com/kata/5544c7a5cb454edb3c000047/train/python

'''
  // your code here
  // How would I make this an object-oreinted?

  /*
  drop() -> calculateHeight
  drop() -> calculateHeight
  
  think about the direction too.

  Drops 1 foot
  Bounces 0.66 foot
  drops 0.66 foot
  bounces 0.44 foot
  drops 0.44 foot
  bounces 0.2962 foot

  */
'''

class NumList:
    def __init__(self):
        self.__list = [] 
    
    def add_value(self, val):
        self.__list.append(val)
    
    def remove_value(self):
        rv = self.__list[-1]
        del self.__list[-1]
        return rv
    
    def print_list(self):
        return self.__list


def bouncing_ball(h, bounce, window):
    # your code
    return -1