# https://www.codewars.com/kata/567fe8b50c201947bc000056/train/python
import re

def ipv4_address(address):
    #your code here

    results = re.match('^\d+.\d+.\d+.\d+$')
    return results

ipv4_address("255.255.255.255")
