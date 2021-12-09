# https://www.codewars.com/kata/566b490c8b164e03f8000002/train/python
from collections import OrderedDict

def fight(robot_1, robot_2, tactics):
    # your code
    list_of_speeds = list(map(lambda x: x['speed'], [robot_1, robot_2]))
    if list_of_speeds[0] > list_of_speeds[1]:
        pass
    elif list_of_speeds[0] < list_of_speeds[1]:
        pass
    else:
        pass