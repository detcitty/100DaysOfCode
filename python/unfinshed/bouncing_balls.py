# https://www.codewars.com/kata/5544c7a5cb454edb3c000047/train/python

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