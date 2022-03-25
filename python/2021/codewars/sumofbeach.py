# https://www.codewars.com/kata/5b37a50642b27ebf2e000010/train/python
import re
from itertools import chain
def sum_of_a_beach(beach):
    # your code
    sand = re.compile('sand', re.I)
    water = re.compile('water', re.I)
    fish = re.compile('fish', re.I)
    sun = re.compile('sun', re.I)

    found = list(map(lambda x: re.findall(x, beach), [sand, water, fish, sun]))
    return(len(list(chain(*found))))

test1 = sum_of_a_beach("GolDeNSanDyWateRyBeaChSuNN")
print(test1)