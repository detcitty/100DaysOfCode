# https://www.codewars.com/kata/5544c7a5cb454edb3c000047/train/python

'''

How many times will the mother see the ball pass in front of her window (including when it's falling and bouncing?
Three conditions must be met for a valid experiment:

    Float parameter "h" in meters must be greater than 0
    Float parameter "bounce" must be greater than 0 and less than 1
    Float parameter "window" must be less than h.

If all three conditions above are fulfilled, return a positive integer, otherwise return -1.
Note:

The ball can only be seen if the height of the rebounding ball is strictly greater than the window parameter.
Examples:

- h = 3, bounce = 0.66, window = 1.5, result is 3

- h = 3, bounce = 1, window = 1.5, result is -1 

(Condition 2) not fulfilled).

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