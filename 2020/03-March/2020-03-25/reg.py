# https://www.codewars.com/kata/567fe8b50c201947bc000056/train/python

import re
def ipv4_address(address):
    #your code here

    values = re.findall(r"[0-2]?[0-9]?[0-9]", address)
    return(values)

print(ipv4_address("127.0.0.1"))