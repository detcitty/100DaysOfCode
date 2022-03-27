# https://www.codewars.com/kata/566b490c8b164e03f8000002/train/python
from collections import OrderedDict
import operator
from functools import reduce
  
def countList(lst1, lst2):
    return reduce(operator.add, zip(lst1, lst2))

def fight(robot_1, robot_2, tactics):
    # your code
    values = []
    list_of_speeds = list(map(lambda x: x['speed'], [robot_1, robot_2]))
    if list_of_speeds[0] > list_of_speeds[1]:
        tactics1 = countList(robot_1['tactics'], robot_2['tactics'])
    elif list_of_speeds[0] < list_of_speeds[1]:
        tactics2 = countList(robot_2['tactics'], robot_1['tactics'])
    else:
        pass